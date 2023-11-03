var calcScrollValue = () => {
    let scrollProgress = document.getElementById("progress");
    let progressValue = document.getElementById("progress_value");
    let pos = document.documentElement.scrollTop;
    let calcHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    let scrollValue = Math.round((pos * 100) / calcHeight);

    if (scrollProgress){
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
    }
};


window.onscroll = calcScrollValue;
window.onload = calcScrollValue;

// Modal Selecionar Imagem //

window.onload = function() {
    // Get the modal
    var card_modal = document.getElementById("modal");

    // Get the button that opens the modal
    var botao_modal_1 = document.getElementById("botao_modal_1");

    // Get the <span> element that closes the modal
    var voltar = document.getElementsByClassName("modal_baixo_botao_voltar")[0];

    var sim = document.getElementsByClassName("modal_baixo_botao_sim")[0];

    // When the user clicks the button, open the modal 
    botao_modal_1.onclick = function() {
        card_modal.style.display = "block";
    };

    // When the user clicks on <span> (x), close the modal
    voltar.onclick = function() {
        card_modal.style.display = "none";
    };

    sim.onclick = function() {
        card_modal.style.display = "none";
    };

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
      if (event.target == modal) {
        card_modal.style.display = "none";
      };
    };
};

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