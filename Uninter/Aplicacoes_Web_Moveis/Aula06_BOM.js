//Defino uma instancia para receber a funcao do window, onde defino
//o tamanho para abrir ('url caso queira apontar para um link', '', 'defino tamanho')
var janela_Aberta = window.open('', '', 'width=400, height=600');
//Abro funcao
function validar_janela() {
    //Aqui a instancia que eu tenho é possivel validar se esta aberta ou fechada
    if (janela_Aberta.closed) {
        alert('A janela fechou!');
    }
    else {
        alert('Feche a janela animal!');
    };
} 