
function carregarImagem() {
    const imagem = document.getElementById('imagemTema');

    const temaEscuro = window.matchMedia('(prefers-color-scheme: dark)').matches;

    if (temaEscuro) {
        imagem.src = '../../imagens/logo (1).png';

    } else {
        imagem.src = '../../imagens/logo.png';
    }
    console.log(window.matchMedia);
}

window.onload = function() {
    carregarImagem();
    setInterval(carregarImagem, 500);
};

window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', event => {
    if (event.matches) {
        document.body.classList.add('light');
        document.body.classList.remove('dark');
    } else {
        document.body.classList.add('dark');
        document.body.classList.remove('light');
    }
    carregarImagem();
});
