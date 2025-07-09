export const bootstrap = (): void => {
    // formata um cep
    const zipCodeMask = (value: string | number): string => {
        // type guard -> caso o value seja um number é convertido para uma string
        if(typeof value === 'number') {
            value = value.toString();
        }
        value = value.replace(/\D/g, '');  // vai substitui qualquer coisa que não seja um digito por um caractere vazio
        value = value.replace(/(\d{5})(\d)/, '$1-$2');  // separar os 5 primeiros digitos

        return value;
    }

    const zipCode = zipCodeMask('59149000'); // 10000-00
    console.log(zipCode);

    const zipCode2 = zipCodeMask('20000000');
    console.log(zipCode2);
};