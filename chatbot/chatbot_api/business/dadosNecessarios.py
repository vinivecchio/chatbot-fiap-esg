from ..models import Pergunta, Resposta
def dadosNecessarios():
    pergunta = Pergunta()
    pergunta.codigo = 9
    pergunta.titulo = "Seu endereço de email corporativo, número de celular e uma senha."
    pergunta.acao_anterior=""

    resposta1 = Resposta()
    resposta1.codigo = 92
    resposta1.valor = '1'
    resposta1.descricao = "Voltar para o menu anterior."
    resposta1.acao = "http://127.0.0.1:8000/chatbot_api/duvidas-dados-cadastro"

    resposta2 = Resposta()
    resposta2.codigo = 93
    resposta2.valor = '2'
    resposta2.descricao = "Voltar para o menu inicial."
    resposta2.acao = "http://127.0.0.1:8000/chatbot_api/principal"


    pergunta.save()
    resposta1.save()
    resposta2.save()

    pergunta.respostas.add(resposta1)
    pergunta.respostas.add(resposta2)

    return pergunta