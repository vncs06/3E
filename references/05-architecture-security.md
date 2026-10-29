# Arquitetura e segurança

Preserve stack e convenções do projeto. Prefira fronteiras de domínio claras, interfaces estáveis, contratos versionados, migrações reversíveis e testes de integração.

Para SaaS: defina isolamento de tenants em dados, arquivos, cache, filas e consultas; políticas de autorização executadas no servidor; controle de acesso por papel e escopo; auditoria; limites operacionais; provisionamento e desativação de empresas.

Aplique proteção de segredos, criptografia apropriada, TLS, backups com testes de restauração, políticas de retenção, exclusão e exportação de dados. Evite dados pessoais em logs.

Trate privacidade e exigências regulatórias por setor e jurisdição. Registre avaliações necessárias; não declare conformidade apenas por implementar funcionalidades.
