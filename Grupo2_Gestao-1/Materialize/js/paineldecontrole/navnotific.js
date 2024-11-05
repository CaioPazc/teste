function abrirNotif() {
    const screenWidth = window.innerWidth; // Pega a largura da tela em pixels
    const navWidth = screenWidth < 720 ? "100%" : "20%"; // Define a largura com base na largura da tela
    document.getElementById("notificaçãoOculto").style.width = navWidth; 
    document.getElementById("notificaçãoOculto").style.transform = "translateX(0)"; // Mostra o painel
}

function fecharnotfic() {
    document.getElementById("notificaçãoOculto").style.width = "0"; 
    document.getElementById("notificaçãoOculto").style.transform = "translateX(100%)"; // Esconde o painel
    setTimeout(function() { 
        document.getElementById("abrirNotif").style.display = "block"; 
        document.getElementById("abrirNotif").style.opacity = "1";
    }, 400); 
}