---
id: ERP-INV-LEDGER-001
title: Movimentações rastreáveis de estoque
type: pattern
sectors:
  - cross-sector
capabilities:
  - inventory
status: validated
confidence: high
evidence_level: DOCUMENTED
transferability: cross-sector
created: 2026-10-29
updated: 2026-10-29
source: foundational-engineering-principle
privacy_review: passed
score: 9
---

# Movimentações rastreáveis de estoque

## Problema
Atualizar apenas um campo de saldo dificulta auditoria, reconciliação, identificação de perdas e correção de erros.

## Contexto e condições
Aplica-se a sistemas com materiais, produtos ou ativos fungíveis que exigem controle de quantidades e histórico de movimentações.

## Princípio
Registrar entradas, saídas, transferências, reservas, liberações, ajustes e perdas como operações explícitas. Derivar ou reconciliar saldos a partir de movimentações confiáveis. Manter quantidade física separada de quantidade reservada e disponível. Proteger atualizações concorrentes.

## Evidência
Princípio de modelagem derivado de escrituração de movimentos e rastreabilidade de sistemas transacionais. Não representa teste executado em um cliente específico.

## Limites
Ativos seriados ou itens únicos podem exigir estados de alocação individuais, não apenas quantidades agregadas. O momento de reserva e consumo depende de confirmação com a empresa.

## Checklist de aplicação
- [ ] Definir unidade, localização e rastreabilidade necessárias.
- [ ] Definir política de reserva, consumo e reversão.
- [ ] Testar operações concorrentes e reprocessamento.
- [ ] Conciliar movimentações com saldos.
