export const bootstrap = (): void => {
    const input = document.querySelector('.inputText') as Node;

    input.addEventListener('click', (event: Event) => {
        console.log('Input clicado');
    });

    console.log('Filho de: ', input.parentNode);

};