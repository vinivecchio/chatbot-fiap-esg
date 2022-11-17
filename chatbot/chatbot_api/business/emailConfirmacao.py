from ..models import Pergunta, Resposta
def emailConfirmacao():
    pergunta = Pergunta()
    pergunta.codigo = 100
    pergunta.titulo = "Primeiro, olhe sua caixa de spam, se não estiver lá, tente realizar o cadastro novamente e caso nenhum dos anteriores funcione, entre em contato conosco pelo sac@esg.com.br"
    pergunta.acao_anterior=""

    resposta1 = Resposta()
    resposta1.codigo = 102
    resposta1.valor = '1'
    resposta1.descricao = "Voltar para o menu anterior."
    resposta1.acao = "http://127.0.0.1:8000/chatbot_api/duvidas-dados-cadastro"

    resposta2 = Resposta()
    resposta2.codigo = 103
    resposta2.valor = '2'
    resposta2.descricao = "Voltar para o menu inicial."
    resposta2.acao = "http://127.0.0.1:8000/chatbot_api/principal"


    pergunta.save()
    resposta1.save()
    resposta2.save()

    pergunta.respostas.add(resposta1)
    pergunta.respostas.add(resposta2)

    return pergunta