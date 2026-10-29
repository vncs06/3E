#!/usr/bin/env python3
"""Validate public knowledge entries and commit explicitly selected Markdown files.

Publishing uses an existing Git checkout with write credentials. Nothing is
pushed unless --push is specified. Never use this tool for client-private data.
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KNOWLEDGE = ROOT / "knowledge"
REQUIRED = ("id", "title", "type", "sectors", "capabilities", "status",
            "confidence", "evidence_level", "transferability", "created",
            "updated", "source", "privacy_review", "score")
SECRET_MARKERS = ("-----BEGIN PRIVATE KEY-----", "ghp_", "github_pat_", "sk_live_", "AKIA")
ALLOWED_TYPES = {"sector", "capability", "pattern", "pitfall", "cross-sector"}
ALLOWED_STATUSES = {"validated", "exploratory", "disputed", "deprecated"}
def run(*args):
    return subprocess.run(args, cwd=ROOT, text=True, capture_output=True, check=True).stdout.strip()

def metadata(body):
    if not body.startswith("---\n"):
        raise ValueError("Missing YAML frontmatter")
    ending = body.find("\n---", 4)
    if ending < 0:
        raise ValueError("Unterminated YAML frontmatter")
    lines = body[4:ending].splitlines()
    result = {}
    current_key = None
    for line in lines:
        if ":" in line and not line.startswith(" "):
            key, val = line.split(":", 1)
            current_key = key.strip()
            result[current_key] = val.strip()
        elif line.lstrip().startswith("- ") and current_key in {"sectors", "capabilities"}:
            result[current_key] += " " + line.strip()
    return result

def validate(path):
    path = path.resolve()
    if path == KNOWLEDGE / "INDEX.md":
        if not path.exists() or not path.read_text(encoding="utf-8").strip():
            raise ValueError("Missing knowledge index")
        return
    if KNOWLEDGE not in path.parents or path.suffix != ".md":
        raise ValueError("Only Markdown knowledge files may be processed")
    body = path.read_text(encoding="utf-8")
    fields = metadata(body)
    missing = [k for k in REQUIRED if not fields.get(k)]
    if missing:
        raise ValueError("Missing metadata: " + ", ".join(missing))
    if fields["type"] not in ALLOWED_TYPES:
        raise ValueError("Invalid type")
    if fields["status"] not in ALLOWED_STATUSES:
        raise ValueError("Invalid status")
    if fields["privacy_review"] != "passed":
        raise ValueError("Privacy review required")
    if any(marker in body for marker in SECRET_MARKERS):
        raise ValueError("Potential secret marker detected")
    if not re.fullmatch(r"\d+", fields["score"]) or int(fields["score"]) > 10:
        raise ValueError("Invalid score")
    if fields["status"] == "validated" and int(fields["score"]) < 8:
        raise ValueError("Validated entries require score >= 8")
    if len(body) < 200:
        raise ValueError("Entry is too short")
    if fields["status"] == "validated" and fields["evidence_level"] == "INFERRED":
        raise ValueError("Inferences cannot be treated as validated")
    return fields

def selected(paths):
    output = []
    for arg in paths:
        target = (ROOT / arg).resolve()
        if target != KNOWLEDGE and KNOWLEDGE not in target.parents:
            raise ValueError("Path outside knowledge/: " + arg)
        if target.is_dir():
            output.extend(sorted(target.rglob("*.md")))
        else:
            output.append(target)
    return list(dict.fromkeys(output))

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["validate", "publish"])
    parser.add_argument("paths", nargs="+", help="Files or directories under knowledge/")
    parser.add_argument("--push", action="store_true", help="Push commit to remote branch")
    parser.add_argument("--remote", default="origin")
    parser.add_argument("--branch", help="Explicit remote branch (required with --push)")
    parser.add_argument("--message", default="docs(knowledge): add validated ERP learning")
    args = parser.parse_args()
    try:
        paths = selected(args.paths)
        if not paths:
            raise ValueError("No Markdown files found")
        for p in paths:
            validate(p)
            print("VALID", p.relative_to(ROOT))
        if args.action == "validate":
            return
        if args.push and not args.branch:
            raise ValueError("--branch required with --push")
        branch = run("git", "branch", "--show-current")
        if not branch or branch in {"main", "master"}:
            raise ValueError("Publish from a dedicated knowledge branch, not main")
        if args.push and branch != args.branch:
            raise ValueError("Current branch does not match --branch")
        if run("git", "diff", "--cached", "--name-only"):
            raise ValueError("Index already has staged changes; unstage before publishing")
        dirty = run("git", "status", "--porcelain", "--untracked-files=normal").splitlines()
        allowed = {str(p.relative_to(ROOT)).replace("\\\\", "/") for p in paths}
        other = [line for line in dirty if line[3:].strip().replace("\\\\", "/") not in allowed]
        if other:
            raise ValueError("Unrelated working-tree changes exist; separate the publish operation")
        if not dirty:
            print("No changes to commit")
            return
        run("git", "add", "--", *sorted(allowed))
        staged = set(run("git", "diff", "--cached", "--name-only").splitlines())
        if not staged or staged - allowed:
            raise ValueError("Unexpected staged files")
        print("Staged:", ", ".join(sorted(staged)))
        run("git", "commit", "-m", args.message)
        print("COMMITTED", run("git", "rev-parse", "--short", "HEAD"))
        if args.push:
            # A normal push is non-forcing and fails on divergence or insufficient permission.
            run("git", "push", args.remote, "HEAD:refs/heads/" + args.branch)
            print("PUSHED", args.remote, args.branch)
    except (ValueError, OSError, subprocess.CalledProcessError) as exc:
        print("ERROR:", exc, file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
