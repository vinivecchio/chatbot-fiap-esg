from ..models import Pergunta, Resposta
def atividadeExterna():
    pergunta = Pergunta()
    pergunta.codigo = 160
    pergunta.titulo = "Não há problema algum em cadastrar uma atividade feita fora do horário de trabalho, o ESG engloba muitas ações e elas são extremamente importantes, inclusive incentivamos que você aplique na sua vida pessoal."
    pergunta.acao_anterior=""

    resposta1 = Resposta()
    resposta1.codigo = 162
    resposta1.valor = '1'
    resposta1.descricao = "Voltar para o menu anterior."
    resposta1.acao = "http://127.0.0.1:8000/chatbot_api/duvidas-plataforma-pontos"

    resposta2 = Resposta()
    resposta2.codigo = 163
    resposta2.valor = '2'
    resposta2.descricao = "Voltar para o menu inicial."
    resposta2.acao = "http://127.0.0.1:8000/chatbot_api/principal"


    pergunta.save()
    resposta1.save()
    resposta2.save()

    pergunta.respostas.add(resposta1)
    pergunta.respostas.add(resposta2)

    return pergunta