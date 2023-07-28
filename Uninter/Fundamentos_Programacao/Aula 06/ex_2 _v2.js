let v1 = document.querySelector("#vlr_1");
let v2 = document.querySelector("#vlr_2");
let btns = document.querySelectorAll("button");
let btn = document.querySelector(".btn")
let btnSoma = document.querySelector('#soma');
let btnSub = document.querySelector("#sub");
let btnDivi = document.querySelector("#dividir");
let btnMult = document.querySelector("#mult");

let btn_soma = false
let btn_sub = false
let btn_mult = false
let btn_divi = false

v1.addEventListener("mouseout", consumir1);
v2.addEventListener("mouseout", consumir2);
btn.addEventListener("click", act_btn);

function consumir1() {
    vlr1 = v1.value;
};

function consumir2() {
    vlr2 = v2.value;
};

function act_btn(){
    for (let i of btns){
        let id_btn = '#'+i.id;
        btn_act = document.querySelector(id_btn);
        btn_act.addEventListener("click", acao);
    };
};

function acao(evt){
    console.log("Meu operador é = "+evt.target.id);
    if(evt.target.id === "soma")
        
        console.log("Acertei o +");
    if(evt.target.id === "sub")
        console.log("Acertei o -");
    if(evt.target.id === "dividir")
        console.log("Acertei o /");
    if(evt.target.id === "mult")
        console.log("Acertei o X");
};


