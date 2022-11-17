from ..models import Pergunta, Resposta
def grupoAfinidade():
    pergunta = Pergunta()
    pergunta.codigo = 170
    pergunta.titulo = "Sim! Você pode ver na aba grupos, os que já existem e se você se identifica com algum deles, caso contrário você pode criar um grupo convidar seus colegas mais próximos, ou até mesmo deixar público."
    pergunta.acao_anterior=""

    resposta1 = Resposta()
    resposta1.codigo = 172
    resposta1.valor = '1'
    resposta1.descricao = "Voltar para o menu anterior."
    resposta1.acao = "http://127.0.0.1:8000/chatbot_api/duvidas-plataforma-pontos"

    resposta2 = Resposta()
    resposta2.codigo = 173
    resposta2.valor = '2'
    resposta2.descricao = "Voltar para o menu inicial."
    resposta2.acao = "http://127.0.0.1:8000/chatbot_api/principal"


    pergunta.save()
    resposta1.save()
    resposta2.save()

    pergunta.respostas.add(resposta1)
    pergunta.respostas.add(resposta2)

    return pergunta