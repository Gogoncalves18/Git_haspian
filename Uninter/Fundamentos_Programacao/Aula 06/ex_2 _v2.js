let v1 = document.querySelector("#vlr_1");
let v2 = document.querySelector("#vlr_2");
let btns = document.querySelectorAll("button");
let btn = document.querySelector(".btn")
let btnSoma = document.querySelector('#soma');
let btnSub = document.querySelector("#sub");
let btnDivi = document.querySelector("#dividir");
let btnMult = document.querySelector("#mult");
let resp = document.querySelector("#res")


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
    if(evt.target.id === "soma"){
        vlrF = parseInt(vlr1)+parseInt(vlr2);
        resp.innerHTML = `${vlrF}`;
        btnSoma.style.backgroundColor ="red"
        setTimeout(() => {btnSoma.style.backgroundColor =""
        }, 3000);
        console.log(`Acertei o + deu ${vlrF}`);
    };
        
    if(evt.target.id === "sub"){
        vlrF = parseInt(vlr1)-parseInt(vlr2);
        resp.innerHTML = `${vlrF}`;
        btnSub.style.backgroundColor ="red"
        setTimeout(() => {btnSub.style.backgroundColor =""
        }, 3000);
        console.log("Acertei o -");
    };

    if(evt.target.id === "dividir"){
        vlrF = parseInt(vlr1)/parseInt(vlr2);
        resp.innerHTML = `${vlrF}`;
        btnDivi.style.backgroundColor ="red"
        setTimeout(() => {btnDivi.style.backgroundColor =""
        }, 3000);
        console.log("Acertei o /");
    };

    if(evt.target.id === "mult"){
        vlrF = parseInt(vlr1)*parseInt(vlr2);
        resp.innerHTML = `${vlrF}`;
        btnMult.style.backgroundColor ="red"
        setTimeout(() => {btnMult.style.backgroundColor =""
        }, 3000);
        console.log("Acertei o X");
    };
};


