# Publicação do conhecimento no GitHub

## Repositório da base
Repositório canônico: `https://github.com/vncs06/3E`.
A instalação pode ter um fork diferente. Não pressupor permissão de escrita no repositório canônico.

## Política de atualização
- Consultar `knowledge/INDEX.md` antes de criar entradas.
- A entrada proposta deve respeitar `assets/templates/knowledge-entry.md`.
- Escrita automática só em `knowledge/` e para conteúdo com revisão de privacidade concluída.
- Nunca fazer `git add .`, `git add -A` nem `git push --force`.
- Usar branch específica `knowledge/<identificador>`, commit limitado aos arquivos de conhecimento e pull request quando o ambiente oferecer essa capacidade.
- Quando houver autorização explícita para publicação direta e o ambiente não oferecer pull request, publicar somente as entradas classificadas como públicas e elegíveis, com diff verificado e push normal. Rejeitar branch divergente.
- Não incluir dados de projetos de clientes em payload de publicação ou mensagens de commit.
- Não editar `SKILL.md` ou scripts automaticamente.
- Em caso de conflito, parar e reconciliar. Nunca forçar histórico.
- Ausência de acesso remoto não interrompe o desenvolvimento; registrar a pendência.

## Comandos locais opcionais
O script `scripts/knowledge_manager.py` aceita `validate` para verificar metadados de uma entrada e `publish` para criar commit restrito a arquivos do diretório `knowledge/`. O envio ao GitHub é uma ação explícita com `--push`, nunca implícita no simples registro.

Antes de publicação, confirmar remotamente o destino e a capacidade de push. Um commit local não constitui publicação.

## Fluxo de trabalho do agente
1. Escrever candidato no projeto.
2. Avaliar e sanitizar.
3. Criar entrada em `knowledge/` e atualizar índice.
4. Rodar validação.
5. Revisar diff.
6. Com permissão adequada, publicar pela integração GitHub ou pelo fluxo Git configurado.
7. Registrar commit/PR e informar usuário.
