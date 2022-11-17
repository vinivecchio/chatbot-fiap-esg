from ..models import Pergunta, Resposta
def duvidasCertificado():
    pergunta = Pergunta()
    pergunta.codigo = 5
    pergunta.titulo = "Qual é a sua dúvida sobre certificados?"
    pergunta.acao_anterior="http://127.0.0.1:8000/chatbot_api/principal"

    resposta1 = Resposta()
    resposta1.codigo = 51
    resposta1.valor = '1'
    resposta1.descricao = "Gosto muito da iniciativa, existe um certificado de participação para postar no meu LinkedIn?"
    resposta1.acao = "http://127.0.0.1:8000/chatbot_api/certificado-participacao"

    resposta2 = Resposta()
    resposta2.codigo = 52
    resposta2.valor = '2'
    resposta2.descricao = "Consigo visualizar o impacto positivos que minhas ações causaram?"
    resposta2.acao = "http://127.0.0.1:8000/chatbot_api/visualizar-impacto"

    resposta3 = Resposta()
    resposta3.codigo = 53
    resposta3.valor = '3'
    resposta3.descricao = "Voltar para o menu anterior."
    resposta3.acao = "http://127.0.0.1:8000/chatbot_api/principal"

    pergunta.save()
    resposta1.save()
    resposta2.save()
    resposta3.save()

    pergunta.respostas.add(resposta1)
    pergunta.respostas.add(resposta2)
    pergunta.respostas.add(resposta3)

    return pergunta
