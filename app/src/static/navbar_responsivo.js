// Pegar o menu de hamburguer e as opções do menu
hamburguer = document.querySelector(".navbar_hamburguer");
menu = document.querySelector(".navbar_menu");

// Quando clicar no menu de hamburguer, ganhará uma classe chamada "showing", 
// e enquanto o menu de hamburguer ter essa classe as opções aparecerão
// Se clicar denovo (para fechar), fecha as opções do menu e tira a classe "showing" do menu de hamburguer.
hamburguer.onclick = function() {
  menu.style.display = 'flex';
  menu.classList.toggle("showing");
  if (menu.classList.contains("showing")) {
    menu.style.display = 'none';
  }
}