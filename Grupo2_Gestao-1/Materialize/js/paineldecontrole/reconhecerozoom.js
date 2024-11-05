function checkZoom() {
    const devicePixelRatio = window.devicePixelRatio;
    const screenWidth = window.innerWidth; // Pega a largura da tela em pixels
    const screenHeight = window.innerHeight; // Pega a altura da tela em pixels
    const imagem = document.getElementById('imagemwave');

    // Verifica se o zoom está acima de 110%, se a largura da tela é menor ou igual a 720 pixels, 
    // ou se a altura da tela é menor ou igual a 500 pixels
    if (devicePixelRatio >= 1.1 || screenWidth <= 720 || screenHeight <= 700 || screenWidth >= 1950) {
        imagem.style.display = 'none';
    } else {
        imagem.style.display = 'block';
    }
}

window.addEventListener('resize', checkZoom);
window.addEventListener('load', checkZoom);
