export const bootstrap = (): void => {
    // falsy
    console.log(false ? 'truthy' : 'falsy');
    console.log(0 ? 'truthy' : 'falsy');
   // console.log('' ? 'truthy' : 'falsy');
   // console.log(null ? 'truthy' : 'falsy');
   // console.log(undefined ? 'truthy' : 'falsy');
    //console.log(NaN ? 'truthy' : 'falsy');

    // truthy
    console.log(true ? 'truthy' : 'falsy');
    console.log(-1 ? 'truthy' : 'falsy');
    //console.log(' ' ? 'truthy' : 'falsy');
    //console.log([] ? 'truthy' : 'falsy');
    //console.log({} ? 'truthy' : 'falsy');

    const moveis = ['Duna: Parte 2', 'Interestelar', 'Matrix'];

    const movie = moveis.find(item => item.includes('Matrix'));

    // type guard
    if(movie) {
        // string
        console.log(movie);
    } else {
        // undefined
        console.warn('Filme não localizado!');
    }

}