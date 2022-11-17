from ..models import Pergunta, Resposta
def atividadeConjunta():
    pergunta = Pergunta()
    pergunta.codigo = 150
    pergunta.titulo = "Não tem problema algum cadastrar uma atividade em conjunto, no registro da atividade basta marcar seu colega com o email de cadastro dele e vice-versa."
    pergunta.acao_anterior=""

    resposta1 = Resposta()
    resposta1.codigo = 152
    resposta1.valor = '1'
    resposta1.descricao = "Voltar para o menu anterior."
    resposta1.acao = "http://127.0.0.1:8000/chatbot_api/duvidas-plataforma-pontos"

    resposta2 = Resposta()
    resposta2.codigo = 153
    resposta2.valor = '2'
    resposta2.descricao = "Voltar para o menu inicial."
    resposta2.acao = "http://127.0.0.1:8000/chatbot_api/principal"


    pergunta.save()
    resposta1.save()
    resposta2.save()

    pergunta.respostas.add(resposta1)
    pergunta.respostas.add(resposta2)

    return pergunta