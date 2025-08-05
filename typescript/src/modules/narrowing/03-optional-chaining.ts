export const bootstrap = (): void => {
    const title = document.getElementById('title');
    const subtitle = document.getElementById('subtitle');

    // leitura segura
    console.log('title', title?.innerHTML);
};