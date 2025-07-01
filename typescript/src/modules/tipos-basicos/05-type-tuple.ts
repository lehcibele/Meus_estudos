let filmeArray: (number | string | boolean)[] = [1, 'Guerra Civil', true]

let filmeTuple: [number, string, boolean] = [2, 'Um Lugar Silencioso: Dia um', false]

// O ? diz que o terceiro parametro é opicional
let filmeTupleOpcionalPosition: [number, string, boolean?] = [2, 'Um Lugar Silencioso: Dia um']

const [idArr, titleArr, availableArr] = filmeTuple
const [id, title, available] = filmeTuple

console.log(id)