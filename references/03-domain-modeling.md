# Modelagem do domínio

Defina contextos e vocabulário de negócio. Identifique entidades, agregados, atributos, relacionamentos, identificadores e histórico. Modele estados e eventos explícitos, incluindo transições autorizadas e proibidas.

Para cada fluxo descreva:
1. Evento disparador e ator.
2. Pré-condições, autorização e validações.
3. Alterações persistidas e invariantes.
4. Efeitos em outros módulos.
5. Falhas possíveis, compensações e reversões.
6. Auditabilidade, idempotência e concorrência.
7. Critérios de aceite e testes.

Exemplos de invariantes: um item não pode ser alocado simultaneamente a contratos incompatíveis; um pagamento não deve ser registrado duas vezes; um usuário não pode consultar dados de outro tenant.

Não force um modelo de dados único para todos os setores.
