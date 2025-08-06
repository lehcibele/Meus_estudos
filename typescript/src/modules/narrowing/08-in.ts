export const bootstrap = (): void => {
    type Item = {
        id: string;
        [key: string]: string | null // index signature
    }

    // fetch para um end-point de uma API
    const response : Item[] = [
        {id: 'fneonvoscvwodcjdjc', movie: 'Cinderella Man'},
        {id: 'djjjjriiwewdf', song: 'Ideologia'},
        {id: 'fferfesdwrfrvr', song: 'Azul da cor do mar'},
    ];

    function showItems(itens: Item[]): void {
        const body = document.querySelector('body');

        if(body instanceof HTMLBodyElement) {
            itens.map(item => {
                const itemElement = document.createElement('div');
                if('song' in item) {
                    itemElement.textContent = item.song;
                    itemElement.style.background = 'seagreen';
                } else if('movie' in item) {
                    itemElement.textContent = item.movie;
                    itemElement.style.background = 'cadetblue';
                }

                body.appendChild(itemElement);

            })
        }
    }

    showItems(response);
};