// Array vazio que irá armazenar os dados - Array do Javascript são as listas do Python
let dados = [];

// Função que calcular o aumento
function calcularAumento() {
    
}

// Função para inserir os dados em um JSON
function inserirDados() {
    const nome = document.getElementById('nome').value;
    const salario = parseFloat(document.getElementById('salario').value);
    dados.push({ nome, salario });
    localStorage.setItem('dados', JSON.stringify(dados));
    mostrarDados();
}

// Função para mostrar os dados na página html
function mostrarDados() {
    const dadosJSON = localStorage.getItem('dados');
    if (dadosJSON) {
        dados = JSON.parse(dadosJSON);
        let resultado = '';
        dados.forEach(item => {
            resultado += `<p>${item.nome}: R$ ${item.salario.toFixed(2)}</p>`;
        });
        document.getElementById('resultado').innerHTML = resultado;
    }
}

// Carregar os dados do localStorage ao carregar a página
window.onload = mostrarDados;