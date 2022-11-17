from ..models import Pergunta, Resposta
def visualizarImpacto():
    pergunta = Pergunta()
    pergunta.codigo = 190
    pergunta.titulo = "Na aba Resultados é possível visualizar o impacto das suas ações e do seu time, quantos pontos vocês acumularam, e quantidade de CO2 que será neutralizada em determinado período de tempo."
    pergunta.acao_anterior=""

    resposta1 = Resposta()
    resposta1.codigo = 192
    resposta1.valor = '1'
    resposta1.descricao = "Voltar para o menu anterior."
    resposta1.acao = "http://127.0.0.1:8000/chatbot_api/duvidas-certificado"

    resposta2 = Resposta()
    resposta2.codigo = 193
    resposta2.valor = '2'
    resposta2.descricao = "Voltar para o menu inicial."
    resposta2.acao = "http://127.0.0.1:8000/chatbot_api/principal"


    pergunta.save()
    resposta1.save()
    resposta2.save()

    pergunta.respostas.add(resposta1)
    pergunta.respostas.add(resposta2)

    return pergunta