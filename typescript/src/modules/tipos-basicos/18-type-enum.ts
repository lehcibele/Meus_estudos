export const bootstrap = (): void => {
    // Status do pedido, pendente, entregue e cancelado. Por padrão começa com 0, mas podemos atribuir um valor ou uma string ( se for string, não tem o autocomplete)
    enum OrderStatus {
        PENDING,
        DELIVERED = 'Entregue',
        CANCELED = 'Cancelado',
    }

    // Enum é convertido em objeto
    console.log(OrderStatus);
    console.log(OrderStatus.DELIVERED); // 1
    console.log(OrderStatus[1]);        // DELIVERED

    // Aqui não sobrescreve os itens, mas adiciona
    enum OrderStatus {
        WAITINGFORPAYMENT = 500,
        SENT = 'Enviado',
    }

    function changeOrderStatus(newStatus: OrderStatus): void {
        if(newStatus === OrderStatus.SENT) {
            console.log('Novo Status:', newStatus)
        }
    }

    changeOrderStatus(OrderStatus.SENT);
};