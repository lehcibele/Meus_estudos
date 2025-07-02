type Movie = {
    readonly title: string; // ao colocar o readonly o atributo title é só para leitura, não pode alterar o seu valor
    year: number;
    [key: string | number] : string | number | boolean;
}

type Movies = {
    [key: string]: Movie
}

// Fetch endpoint / movies
let movies = {
    movie1: {
        title: 'A origem',
        year: 2010,
        isFavorite: true,
        genre: 'Ficção cientifica',
        director: 'Cristopher Nolan',
    },
    movie2: {
        title: 'Um sonho de liberdade',
        year: 1994,
        isFavorite: true,
        genre: 'Drama',
        runtime: 142,
    },
    movie3: {
        title: 'The Godfather',
        year: 1972,
        isFavorite: false,
        genre: 'Crime', 
    },
}

export function showMovies(movies: Movies) {
    // movies.movie1.title = 'Teste'; erro por conta do readonly
    console.log(movies);
}

// aqui o readonly não funciona, pois é feito a inferencia de tipos, já na função acima o type é definido por Moveis 
movies.movie1.title = 'teste'; 
showMovies(movies);