function cal_porcento() {
    //calcula a qtd de homens e mulheres
    var qtd_H = parseInt(document.getElementById("QTD - Homens").value);
    var qtd_M = parseInt(document.getElementById("QTD - Mulheres").value);
    //pega a qtd total
    var qtd_tot = qtd_H + qtd_M;

    //pega o percentual de cada sexo
    var qtd_perc_H = (qtd_H / qtd_tot) * 100;
    var qtd_perc_M = (qtd_M / qtd_tot) * 100;

    //Cria uma tabela com percentuais
    //tr é para inserir linha e th para colocar vazio
    var tabela = "<table>";
    tabela += "<tr><th></th><th>Quantidade</th><th>Percentual</th></tr>";
    tabela += "<tr><td>Homens</td><td>" + qtd_H + "</td><td>" + qtd_perc_H.toFixed(2) + "%</td></tr>";
    tabela += "<tr><td>Mulheres</td><td>" + qtd_M + "</td><td>" + qtd_perc_M.toFixed(2) + "%</td></tr>";
    tabela += "</table>";

    //injeta no html a funcao acima
    document.getElementById("tabela-porcento").innerHTML = tabela;

}