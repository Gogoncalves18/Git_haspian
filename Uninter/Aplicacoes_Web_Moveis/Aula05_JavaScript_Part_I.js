//Solicitar o raio 
let raio = prompt('Insira vlr de raio: ');
//Convertendo de str em float
raio = parseFloat(raio);
//Calcular area
const area = Math.PI * Math.pow(raio, 2);
//resultado projetado no console do browser
console.log('Area do circulo é = ', area);
//valor mostrado na tela sem console, aparece tela de msg
alert('Valor na tela = ' + area.toFixed(2))
