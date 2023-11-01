let calcScrollValue = () => {
    let scrollProgress = document.getElementById("progress");
    let progressValue = document.getElementById("progress_value");
    let pos = document.documentElement.scrollTop;
    let calcHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    let scrollValue = Math.round((pos * 100) / calcHeight);

    if (pos > 100) {
        scrollProgress.style.display = "flex";
    }
    else {
        scrollProgress.style.display = "none";
    }

    scrollProgress.addEventListener("click", () => {
        document.documentElement.scrollTop = 0;
    });

    scrollProgress.style.background = `conic-gradient(#0F9635 ${scrollValue}%, #d7d7d7 ${scrollValue}%`
};


window.onscroll = calcScrollValue;
window.onload = calcScrollValue;



// Validar se usuário inseriu uma imagem

function validateForm() {
    var x = document.forms["selecionar_imagem"]["imagem"].value;
    if (x == "" || x == null) {
        alert("Você precisa selecionar pelo menos 1 imagem!");
        return false;
    }
    
    if (x > 5) {
        alert("Selecione no máximo 5 imagens!");
        return false;
    }
}

// Botão de Ver Mais //

var posts = document.getElementsByClassName("postContent");
var buttons = document.getElementsByClassName("readMore");

for (let i = 0; i < buttons.length; i++) {
    let button = buttons[i];
    let postId = button.getAttribute("data-post-id");
    let content = document.querySelector(`.postContent[data-post-id="${postId}"]`);
    let originalContent = content.innerHTML;

    if (originalContent.length > 1400) {
        let truncatedContent = originalContent.substring(0, 1400) + "...";
        content.innerHTML = truncatedContent;

        button.onclick = function() {
            if (content.innerHTML === truncatedContent) {
                content.innerHTML = originalContent;
                button.innerHTML = "Ler menos";
            } else {
                content.innerHTML = truncatedContent;
                button.innerHTML = "Ler mais";
            }
        };
    } else {
        button.style.display = "none";
    }
}