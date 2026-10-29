# 3E

**Enterprise ERP Engineer** é uma skill para agentes de programação que desenvolvem ERPs, CRMs e sistemas de gestão para diferentes setores.

Ela fornece um processo de descoberta do negócio, modelagem de dados e fluxos, arquitetura, documentação, implementação e testes. O agente reutiliza fundamentos de ERP e consulta o responsável pelo projeto quando encontra regras específicas da empresa.

## Instalação com um agente

Envie esta instrução ao Codex ou a outro agente com acesso ao GitHub e ao sistema de arquivos:

```text
Instale a skill 3E a partir de https://github.com/vncs06/3E.
Clone o repositório e copie todos os arquivos da skill para
~/.agents/skills/enterprise-erp-engineer (ou para a pasta de skills do projeto).
Leia o SKILL.md, preserve a estrutura de diretórios e confirme a instalação.
```

No Windows, o diretório global é `%USERPROFILE%\.agents\skills\enterprise-erp-engineer`.

## Instalação manual

```bash
git clone https://github.com/vncs06/3E.git enterprise-erp-engineer
mkdir -p ~/.agents/skills
cp -R enterprise-erp-engineer ~/.agents/skills/enterprise-erp-engineer
```

## Uso

```text
$enterprise-erp-engineer
Planeje um ERP para uma empresa de produtos personalizados.
Mapeie a operação, identifique as regras que precisam ser definidas
comigo e produza a documentação antes de implementar.
```

## Memória evolutiva

A 3E mantém conhecimento reutilizável em arquivos Markdown por setor, capacidade e padrão técnico. O agente consulta a base antes de cada projeto, analisa evidências durante o desenvolvimento e registra descobertas relevantes em arquivos `knowledge/`.

Entradas passam por avaliação de relevância, evidência, transferência entre setores e privacidade. Conteúdo genérico validado pode ser publicado no GitHub durante a execução do agente, com permissão de escrita e revisão do diff. Dados específicos ou confidenciais de clientes ficam no projeto de origem.

O aprendizado é baseado em memória externa consultada pelo modelo. Não altera os pesos da IA e não roda sozinho quando o agente está inativo.

```text
$enterprise-erp-engineer
Use a base de conhecimento da 3E neste ERP.
Ao concluir cada etapa relevante, avalie novas lições, registre
conhecimento genérico em Markdown e publique entradas elegíveis
no repositório GitHub conforme as políticas da skill.
```

## Validar conhecimento

```bash
python scripts/knowledge_manager.py validate knowledge/
```

Para publicar, o agente deve revisar os arquivos, trabalhar em uma branch dedicada e fazer commit e push com permissões existentes. Consulte [o fluxo de publicação](references/13-github-publication.md).

## Estrutura

| Caminho | Conteúdo |
| --- | --- |
| `SKILL.md` | Instruções e processo de trabalho do agente |
| `references/` | Conhecimento de engenharia e capacidades comuns de ERP |
| `assets/templates/` | Modelos de documentos por projeto |
| `scripts/init_project.py` | Gerador da documentação inicial |
| `knowledge/` | Memória reutilizável organizada por setor e capacidade |
| `scripts/knowledge_manager.py` | Verificador de entradas e publicação controlada |
| `references/11-learning-lifecycle.md` | Ciclo de aprendizado da skill |

## Criar a documentação de um ERP

```bash
python scripts/init_project.py /caminho/do/projeto --name "Nome do ERP" --sector "Setor"
```

A skill organiza especificações e orienta a implementação. Não é um ERP pronto.

## Licença

MIT. Consulte [LICENSE](LICENSE).
