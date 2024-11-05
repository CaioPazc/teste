function abrirNav() {
    
    const screenWidth = window.innerWidth;
    const navWidth = screenWidth < 720 ? "100%" : "20%"; 

    document.getElementById("menuOculto").style.width = navWidth; 
    document.getElementById("principal").style.marginLeft = navWidth; 
    document.getElementById("abrirMenuBtn").style.opacity = "0"; 
    setTimeout(function() { 
        document.getElementById("abrirMenuBtn").style.display = "none";
    }, 500); 
}

function fecharNav() {
    document.getElementById("menuOculto").style.width = "0"; 
    document.getElementById("principal").style.marginLeft = "0"; 
    setTimeout(function() { 
        document.getElementById("abrirMenuBtn").style.display = "block"; 
        document.getElementById("abrirMenuBtn").style.opacity = "1";
    }, 400); 
}



