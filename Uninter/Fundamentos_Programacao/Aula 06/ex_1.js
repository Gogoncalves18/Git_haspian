let botao = document.querySelector("#btnx");
botao.style.background = "blue"
    /* Usando o ID com # eu consigo acessar a propriedade de STYLE forcadamente
    e atribuir uma cor para ela sobreescrevendo o CSS
     */

let var_clique = false;
    //Variavel para controlar as a mudanca de cor enquanto nao clico no botao

botao.addEventListener("mouseover", troca_cor);

function troca_cor(){
    if (var_clique===false)
        botao.style.background = "red"
};
    // Seto nova cor quando o mouse passa por cima

botao.addEventListener("mouseout", troca_cor_fix);

function troca_cor_fix(){
    if (var_clique===false)
        botao.style.background = "blue"
    }
    // Seto cor quando o mouse sai de cima do botao

botao.addEventListener("click", e => {botao.style.background = "pink";
    botao.innerHTML="Se foi o boi com as cordas";
    var_clique=true;
    // Altero a variavel para verdadeiro para a cor do botao nao mudar mais
});