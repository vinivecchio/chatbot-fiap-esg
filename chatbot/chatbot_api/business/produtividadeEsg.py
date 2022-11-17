from ..models import Pergunta, Resposta
def produtividadeEsg():
    pergunta = Pergunta()
    pergunta.codigo = 7
    pergunta.titulo = "Documentar e definir processos, incentivar desenvolvimento de novas tecnologias, agir de maneira preventiva e liderar pessoas levando em conta suas diferenças."
    pergunta.acao_anterior=""

    resposta1 = Resposta()
    resposta1.codigo = 72
    resposta1.valor = '1'
    resposta1.descricao = "Voltar para o menu anterior."
    resposta1.acao = "http://127.0.0.1:8000/chatbot_api/duvidas-esg"

    resposta2 = Resposta()
    resposta2.codigo = 73
    resposta2.valor = '2'
    resposta2.descricao = "Voltar para o menu inicial."
    resposta2.acao = "http://127.0.0.1:8000/chatbot_api/principal"

    pergunta.save()
    resposta1.save()
    resposta2.save()

    pergunta.respostas.add(resposta1)
    pergunta.respostas.add(resposta2)

    return pergunta