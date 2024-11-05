
function carregarImagem() {
    const imagem = document.getElementById('imagemTema');
    const agenda = document.getElementById('agendamentoico');
    const cadastro = document.getElementById('cadastroico');
    const estoque = document.getElementById('estoqueico');
    const temaEscuro = window.matchMedia('(prefers-color-scheme: dark)').matches;

    if (temaEscuro) {
        imagem.src = '../../imagens/logo (1).png';
        agenda.src = '../../imagens/agendamento (1).png';
        cadastro.src = '../../imagens/cadastro (1).png';
        estoque.src = '../../imagens/estoque (1).png';

    } else {
        imagem.src = '../../imagens/logo.png';
        agenda.src = '../../imagens/agendamento.png';
        cadastro.src = '../../imagens/cadastro.png';
        estoque.src = '../../imagens/estoque.png';
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
