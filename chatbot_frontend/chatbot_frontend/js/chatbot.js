function carregarPrincipal(){
    var url = "http://127.0.0.1:8000/chatbot_api/principal";

    fetch(url)
        .then(res => res.json())
        .then(res => carregarMenuChatBot(res))
        .catch(err => {
            alert("Algo deu errado, contate o administrador.");
        });
}

function carregarMenuChatBot(menu){
    sessionStorage.clear();

    var titulo = menu.titulo;
    var listaOpcoes = menu.respostas;

    var tituloHtml = "<h3>" + titulo + "</h3>";
    var listaOpcoesHtml = "";
    
    for(i = 0; i < listaOpcoes.length; i++){
        var valor = listaOpcoes[i].valor;
        var descricao = listaOpcoes[i].descricao;
        var acao = listaOpcoes[i].acao

        sessionStorage.setItem(valor, acao);

        listaOpcoesHtml = listaOpcoesHtml + "<p>" + valor + ". " + descricao + "</p>" 
        
    }

    document.getElementById("divDados").innerHTML = tituloHtml + listaOpcoesHtml;
}

function confirmarOpcao(){
    var opcao = document.getElementById("txtOpcao").value;
    if(opcao != ''){
        var acao = sessionStorage.getItem(opcao);
        
        if(acao == null){
            alert('Selecione uma opção válida ;)');
            return;
        }

        var url = acao;

        fetch(url)
            .then(res => res.json())
            .then(res => carregarMenuChatBot(res))
            .catch(err => {
                alert("Erro ao listar usuario");
        });
        txtOpcao.value = '';
    }
}

