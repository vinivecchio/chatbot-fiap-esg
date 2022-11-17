from ..models import Pergunta, Resposta
def esqueciSenha():
    pergunta = Pergunta()
    pergunta.codigo = 120
    pergunta.titulo = "No login aperte no botão (esqueci minha senha), depois informe seu email ou telefone utilizado no cadastro."
    pergunta.acao_anterior=""

    resposta1 = Resposta()
    resposta1.codigo = 122
    resposta1.valor = '1'
    resposta1.descricao = "Voltar para o menu anterior."
    resposta1.acao = "http://127.0.0.1:8000/chatbot_api/duvidas-dados-cadastro"

    resposta2 = Resposta()
    resposta2.codigo = 123
    resposta2.valor = '2'
    resposta2.descricao = "Voltar para o menu inicial."
    resposta2.acao = "http://127.0.0.1:8000/chatbot_api/principal"


    pergunta.save()
    resposta1.save()
    resposta2.save()

    pergunta.respostas.add(resposta1)
    pergunta.respostas.add(resposta2)

    return pergunta