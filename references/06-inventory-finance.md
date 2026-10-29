# Estoque, saldo e financeiro

## Estoque
Defina unidade, local, lote/série quando aplicável, quantidade física, reservada, disponível e comprometida. Modele recebimentos, transferências, reservas, consumo, devoluções, perdas, ajustes e inventário com lançamentos rastreáveis.

Saldo disponível não é sinônimo de saldo físico. Regras de reserva e baixa dependem de confirmação com a empresa. Previna concorrência que permita consumir o mesmo recurso duas vezes.

## Financeiro
Separe orçamento, pedido, título, pagamento, recebimento, reembolso, estorno, despesa e conciliação. Use valores monetários decimais ou inteiros em unidade mínima, com regras claras de arredondamento e moeda.

Defina vencimento, parcelas, descontos, taxas, inadimplência, pagamento parcial e cancelamento. Nunca substitua histórico de eventos financeiros apenas sobrescrevendo um total.

Para ambos: idempotência, trilha de auditoria, testes de reversão, permissões e consistência transacional.
