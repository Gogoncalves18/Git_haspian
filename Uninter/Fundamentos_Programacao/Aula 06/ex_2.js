const campo1 = document.querySelector("#campo1");
const campo2 = document.querySelector("#campo2");
const selct_op = document.querySelector("#operacao");
const botao = document.querySelector("#igual");
let resp = document.querySelector("#res");

botao.addEventListener("click", calcular);

function calcular(){
    const valor1 = parseInt(campo1.value);
        //PARSEINT() é a maneira de transformar em inteiro
    const valor2 = parseInt(campo2.value);
    const operator = selct_op.value;
    if(operator === "somar")
        resp.innerHTML = valor1+valor2;
    if(operator === "subtrair")
        resp.innerHTML = valor1-valor2;
    if(operator === "dividir")
        resp.innerHTML = valor1/valor2;
    if(operator === "multiplicar")
        resp.innerHTML = valor1*valor2;
};