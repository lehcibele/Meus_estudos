export const bootstrap = (): void => {
    // o "as" indica o tipo que é o body
    const body = document.querySelector('body') as HTMLBodyElement;
    const video = document.querySelector('#promo') as HTMLVideoElement;
    const input = document.querySelector('.inputText') as HTMLInputElement;

    video.volume;
    input.addEventListener('blur', (event: FocusEvent) => {alert('teste')})
    
};