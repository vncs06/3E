# Governança do conhecimento

## Qualidade da evidência
- OBSERVED: comportamento observado em um projeto, com referência local e contexto.
- TESTED: comportamento confirmado por teste reproduzível.
- DOCUMENTED: fundamentado em especificação ou documentação autorizada, com fonte identificável.
- INFERRED: hipótese analítica; não apta a publicação automática como fato.

Para promover conhecimento, registre evidências reais. Uma única observação pode justificar um padrão local, mas não uma regra universal. Declare limites, setor e pré-condições.

## Classificação e privacidade
Publicável: padrões genéricos, modelos de estados, mecanismos de segurança, estratégias de testes, comportamentos publicados abertamente e lições abstraídas sem revelar a origem.

Não publicável sem revisão específica: dados de clientes, nomes, contatos, preços negociados, históricos financeiros, esquemas reais de produção, incidentes internos, trechos de código fechado, capturas, tokens e documentos completos. Anonimização superficial de dados sensíveis não basta.

## Fronteiras de decisão
A aprovação automática para publicação é permitida somente se:
1. O responsável pelo repositório habilitou publicação automática neste ambiente.
2. A entrada for escrita de forma genérica, sem dependência de contexto confidencial.
3. Todas as verificações passaram, com escore suficiente.
4. O agente conseguiu verificar o diff e a branch de destino.
5. A publicação não altera diretamente instruções centrais ou código executável.

Arquivos `SKILL.md`, `scripts/`, `references/`, políticas, licença, workflows e configuração são protegidos. Alterações nesses arquivos precisam de revisão humana. O autoaprendizado só pode escrever em `knowledge/` e seu índice.

## Situações contraditórias
Se uma entrada conflitar com outra, marcar `status: disputed`, registrar a divergência e pedir verificação. Não apagar evidências anteriores silenciosamente. Entries obsoletas devem manter ligação com substitutas.

## Prevenção de poluição
Consolidar entradas semelhantes, preferindo uma entrada por conceito em vez de dezenas de registros redundantes. Rejeitar argumentos circulares, dados inventados, medições sem método e boas práticas vagas. Não usar o próprio escore como única evidência.

## Direitos de terceiros
Não reproduzir material protegido de documentos de clientes ou de terceiros. Sintetizar princípios genéricos com proveniência permitida.
