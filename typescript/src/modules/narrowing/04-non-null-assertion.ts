export const bootstrap = (): void => {
    // esse elemento title não existe no HTML, logo ao usar o ! eu indico que existe esse elemento e pode ocorrer um erro em produção
    const title = document.getElementById('title')!;
    // o ! indica que o elemento é um HTMLElement e não recebe mais o null
    const subtitle = document.getElementById('subtitle')!;
    subtitle.style.color = 'green';

    // Ao usar a ! não precisa mais do if para verificar se o elemento é um HTMLElement
    // if(subtitle) {
    //     subtitle.style.color = 'green';
    // }

    const getProducts = (): string[] | null => {
        return ['Smartphone', 'Headset'];
    }

    // define que a atribuição não será de um valor null ou undefined
    const products = getProducts()!;
    products.map((item) => console.log(item));
    
};