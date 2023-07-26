console.log('Ei eu aqui novamente')
var nome = "Gustavo"; //Maneira de guardar variavel
var idade  //Outra maneira de abrir variavel
console.log(nome);
idade = 16
console.log(idade);

let altura = 1.80; 
    //Quando a variavel muda durante o codigo, recomenda-se
    //usar o LET e nao mais o VAR
const time = "gremio"; 
    //Quando a variavel nao sofre alteracao
    //recomendasse usar CONST, nao mais o VAR

console.log("O time do " + nome + ",sem sombra de duvida é o " + time);

console.log(`O ${nome} definitivamente gosta do ${time}!`)
    // Acima duas forma de concatenar mensagens e variaveis

if(idade >= 18){
    console.log('Seja bem vindo!');
}
else{
    console.log('Seu acesso foi bloqueado!');
} 
    //Maneira de criar logica    

console.log(typeof nome); 
    //Forma para descobrir o tipo de informacao

let maior_idade = idade >= 18;
    //Maneira mais facil de determinar de MAIOR_IDADE é
    //vdd ou falso

if(maior_idade){
    console.log('Ele é maior de idade!')
}
else{
    console.log('É de menor!')
}

// Estrutura de dados de lista e dict no JS
let lista = ["Carro Luxo", "Valeria Linda", "Casa grande"];

let cpf = {
        "nome": "Gustavo",
        "cidade": "CWB",
        "idade": 41,
        "lista_desejo": lista
};
// Possibilidade de impressao
console.log(cpf)

console.log(lista)

console.log(cpf.lista_desejo)

console.log(cpf["cidade"])

console.log(lista[2])

let ler_paraf = document.querySelector("#tx");
    /*Maneira para eu puxar uma area do html, estou lendo 
    o ID #TX que está marcado no html.
    O DOCUMENT. me devolve o objeto que é a página que estou
    O QUERYSELECTOR("#id") me traz o que está dentro deste 
    paragrafo
    */
console.log(ler_paraf); //Aqui apresento o resultado de cima

let paraf_maior = document.querySelector("#paraf_substituir2");
    /*jogo um paragrafo todo dentro de uma variavel
    */
paraf_maior.addEventListener("click", troca_texto);
    /*Chamo a variavel e depois uso uma funcao reservada
    ADDEVENTLISTNER("acionamento", chamada de funcao) que
    fica escutando eventos na página. Com ele eu uso o 
    evento monitorado de clique através do "CLICK" que
    acionará a funçao escrita na sequencia como ,TROCA_TEXTO
    Alguns outros eventos além do click:
    MOUSEOVER - passagem do mouse por cima
    MOUSEOUT - saida do mouse que está por cima do texto
    */

function troca_texto(){
    paraf_maior.innerHTML="TROQUEI TUDO MANÉ!"
};
    /*A funcao eu escrevo assim, lembrando do innerhtml que 
    é a troca de texto que está dentro da variavel PARAF_MAIOR
     */