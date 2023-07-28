const campo1 = document.querySelector("#campo1");
const campo2 = document.querySelector("#campo2");
const selct_op = document.querySelector("#operacao");
//const botao = document.querySelector("#igual");
let resp = document.querySelector("#res");

//botao.addEventListener("click", calcular);
selct_op.addEventListener("change", calcular);
campo1.addEventListener("keyup", calcular);
campo2.addEventListener("keyup", calcular);

function calcular(){

    const valor1 = parseInt(campo1.value);
    const valor2 = parseInt(campo2.value);
        //PARSEINT() é a maneira de transformar em inteiro;
    const operator = selct_op.value;

    if(campo1.value=='' || campo2.value==''){
        /*neste caso o pipe || é a condicional OR do JS assim
        como && é a condicional AND,
        lembrando que a primeira vez que tendo escrever .VALUE
        ele acaba não carregando
        */
        resp.classList.add("problema");
            /*aqui uso o .CLASSLIST para manipular as classes
            que uso dentro do html. Devemos deixar uma classe
            especial dentro do CSS para ficar alternando de 
            classe no codigo.
            Apos .classlist  eu possuo outros recursos como
            .ADD() e .REMOVE() ao qual devo instruir dentro
            de () o nome da classe que quero direcionar
             */
        resp.innerHTML = "PREENCHA O DOIS CAMPOS";

        setTimeout(()=>{
            resp.classList.remove("problema");
            resp.innerHTML = '';
        }, 3000);
        /*SETTIMEOUT('acao','tempo') é uma funcao reservada do JS
        que executa um contador, dentro do () a primeira instrucao 
        é a acao que pode ser uma funcao escrita em lambda e a segunda
        é o tempo em mili_seg.

        Importante destacar que a escrita acima está em lambda os primeiro
        parenteses é da settimeout. O segundo parenteses é da funcao escrita 
        em lambda, nela não preciso colocar no de funcao pq estou usando somente na 
        linha, nao a chamo de outros lugares. Escrita:
        () => {"escrevo aqui as instrucoes"}
         */
    }
    else{            
        if(operator === "somar")
            resp.innerHTML = valor1+valor2;
        if(operator === "subtrair")
            resp.innerHTML = valor1-valor2;
        if(operator === "dividir")
            resp.innerHTML = valor1/valor2;
        if(operator === "multiplicar")
            resp.innerHTML = valor1*valor2;
    };

}; 


    