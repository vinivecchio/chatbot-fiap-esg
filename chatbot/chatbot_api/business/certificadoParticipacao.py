from ..models import Pergunta, Resposta
def certificadoParticipacao():
    pergunta = Pergunta()
    pergunta.codigo = 180
    pergunta.titulo = "Para emitir um certificado de participação, basta ir na aba Certificados, nela você vai encontrar os certificados disponíveis, dependendo do seu número de pontos e posição no ranking, você pode ganhar certificados diferenciados."
    pergunta.acao_anterior=""

    resposta1 = Resposta()
    resposta1.codigo = 182
    resposta1.valor = '1'
    resposta1.descricao = "Voltar para o menu anterior."
    resposta1.acao = "http://127.0.0.1:8000/chatbot_api/duvidas-certificado"

    resposta2 = Resposta()
    resposta2.codigo = 183
    resposta2.valor = '2'
    resposta2.descricao = "Voltar para o menu inicial."
    resposta2.acao = "http://127.0.0.1:8000/chatbot_api/principal"


    pergunta.save()
    resposta1.save()
    resposta2.save()

    pergunta.respostas.add(resposta1)
    pergunta.respostas.add(resposta2)

    return pergunta