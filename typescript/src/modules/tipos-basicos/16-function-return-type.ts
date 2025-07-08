// TODO CartItem
type CartItem = {
    id: number,
    price: number,
}

type Address = {
    cep: string,
    default: boolean
}

type Customer = {
    addresses: Address[]
}

// TODO ShoppingCart
type ShoppingCart = {
    cartItems: CartItem[],
}
// TODO criar variável do tipo ShoppingCart contendo cartItem
const shoppingCart: ShoppingCart = {
    cartItems: [
        {id: 1000, price: 200},
        {id: 1070, price: 300},
        {id: 3000, price: 500},
    ]
}

const addresses: Address[] = [
    {cep: '000000-000', default: false},
    {cep: '000000-001', default: true},
    {cep: '000000-002', default: false},
]

const customer: Customer = {
    addresses: addresses
}

console.log('Detalhes do customer', customer);

export function calculeTotal(shoppingCart: ShoppingCart): number {
    const total = shoppingCart.cartItems.reduce(
        (acc, item) => acc + item.price, 
        0 
    );
    return total;
} 

const total = calculeTotal(shoppingCart);

console.log(`Total do carrinho: R${total.toFixed(2)}`);

export function getPrincipalAddress(customer: Customer): Address | undefined {
    return customer.addresses.find(address => address.default);
}

const principalAddress = getPrincipalAddress(customer);
console.log(principalAddress);