export const bootstrap = (): void => {
    // null
    let title = null;
    console.log('Title:', title);
    console.log('Title (if):', title ? 'verdadeiro' : 'falso');
    console.log('Tipo null:', typeof title);

    // undefined
    let subtitle = undefined;
    console.log('Subtitle::', subtitle);
    console.log('Subtitle (if):', subtitle ? 'verdadeiro' : 'falso');
    console.log('Tipo undefined:', typeof subtitle);

    type Page = {
        title: string,
        subtile?: string,
        handlerPage?: () => void
    }

    const page: Page = {
        title: 'Curso de TypeScript'
    }

    console.log('Page subtitle:', page.subtile);
    console.log('Page handlePage:', page.handlerPage);

};

