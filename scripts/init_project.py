#!/usr/bin/env python3
"""Inicializa documentação de ERP sem sobrescrever arquivos existentes."""
import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_path")
    parser.add_argument("--name", required=True)
    parser.add_argument("--sector", required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    source = Path(__file__).resolve().parent.parent / "assets" / "templates"
    target = Path(args.project_path).expanduser().resolve() / "docs" / "erp"
    for original in sorted(source.rglob("*.md")):
        destination = target / original.relative_to(source)
        if destination.exists():
            print(f"SKIP {destination}")
            continue
        print(f"{'WOULD WRITE' if args.dry_run else 'WRITE'} {destination}")
        if not args.dry_run:
            destination.parent.mkdir(parents=True, exist_ok=True)
            content = original.read_text(encoding="utf-8")
            content = content.replace("{{PROJECT_NAME}}", args.name).replace("{{SECTOR}}", args.sector)
            destination.write_text(content, encoding="utf-8")
    print("Simulação concluída." if args.dry_run else "Concluído.")

if __name__ == "__main__":
    main()
