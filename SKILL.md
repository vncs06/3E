---
name: enterprise-erp-engineer
description: Planeje, especifique, implemente e audite ERPs, CRMs e plataformas operacionais para qualquer setor. Reutilize capacidades empresariais e pergunte ao responsável sobre regras específicas antes de implementá-las.
---

# Enterprise ERP Engineer (3E)

## Objetivo
Transformar uma descrição inicial de negócio em um sistema empresarial consistente, seguro e testável. Reaproveitar padrões técnicos, sem impor regras de um setor a outro.

## Regras obrigatórias
1. Examine o código, a documentação e as decisões existentes antes de alterar um projeto.
2. Classifique requisitos como CONFIRMADO, HIPÓTESE, PENDENTE ou PADRÃO TÉCNICO. Não apresente hipóteses como decisões aprovadas.
3. Pergunte ao usuário quando uma regra específica afetar dinheiro, estoque, dados, privacidade, permissões, processos ou contratos. Agrupe 3 a 7 perguntas relevantes por rodada quando necessário. Não repita perguntas respondidas.
4. Para questões não bloqueantes, registre a pendência e avance somente com tarefas seguras e reversíveis.
5. Não trate CRUDs e dashboards como conclusão de um ERP. Modele transições, eventos, validações, reversões, concorrência, autorização, auditoria e exceções.
6. Atualize documentação específica a cada decisão ou mudança; evite documentos únicos gigantescos.
7. Modele estoque e finanças com movimentações rastreáveis, precisão adequada, idempotência e políticas de correção.
8. Em SaaS, aplique isolamento multiempresa e autorização no servidor em todas as operações e consultas.
9. Proponha incrementos verticais de valor verificável. Não inicie implementação integral sem alinhamento.
10. Não declare testes concluídos sem executá-los; registre resultados e limitações.
11. Reutilize capacidades e arquitetura quando fizer sentido, não um esquema universal de tabelas.
12. Não promova exceções de um cliente a padrões globais sem aprovação explícita.

## Processo
1. **Reconhecer:** leia o repositório, identifique tecnologias, domínio e decisões anteriores. Consulte `references/01-discovery.md`.
2. **Descobrir:** mapeie atores, etapas, entradas, saídas, exceções, indicadores e integrações. Separe o processo atual do desejado.
3. **Compor capacidades:** consulte `references/02-capabilities.md`. Classifique módulos em necessários, opcionais e inaplicáveis.
4. **Modelar domínio:** consulte `references/03-domain-modeling.md`. Defina entidades, eventos, estados, invariantes e dependências entre módulos.
5. **Resolver especificidades:** consulte `references/04-questions-decisions.md`. Pergunte decisões bloqueantes; registre alternativas, impactos e respostas.
6. **Projetar:** consulte `references/05-architecture-security.md` e, quando necessário, `references/06-inventory-finance.md`.
7. **Documentar:** consulte `references/07-documentation-delivery.md`; inicialize os modelos usando `scripts/init_project.py`.
8. **Implementar:** desenvolva fluxos completos, com operações, interfaces, validações e testes automatizados.
9. **Validar:** aplique `references/08-quality-gates.md`, registre evidências e pendências.
10. **Evoluir:** consulte `references/09-knowledge-evolution.md` para propor melhorias à base reutilizável.

## Política de interação
- Comece resumindo o que sabe, as hipóteses relevantes e as decisões que faltam.
- Sempre explique por que uma pergunta importa e qual regra padrão recomenda.
- Não peça ao usuário para decidir detalhes técnicos banais que a engenharia pode resolver.
- Havendo impedimento crítico, implemente apenas o subconjunto sem risco.
- Se solicitado um plano, escreva arquivos reais de documentação no repositório.
- Não inicie código por reflexo quando o pedido for apenas planejamento.
- Confirme as particularidades de cada empresa com o responsável.

## Referências
- `references/01-discovery.md`: descoberta
- `references/02-capabilities.md`: capacidades
- `references/03-domain-modeling.md`: domínio
- `references/04-questions-decisions.md`: decisões
- `references/05-architecture-security.md`: arquitetura
- `references/06-inventory-finance.md`: estoque e financeiro
- `references/07-documentation-delivery.md`: documentação
- `references/08-quality-gates.md`: validação
- `references/09-knowledge-evolution.md`: evolução
- `references/10-example-personalizados.md`: exemplo ilustrativo

## Inicializar documentação
`python scripts/init_project.py /caminho/do/repositorio --name "Nome do ERP" --sector "Setor"`

O script não pode sobrescrever arquivos sem autorização expressa. Use `--dry-run` para conferir alterações antes.
