from ..models import Pergunta, Resposta
def duvidasPlataformaPontos():
    pergunta = Pergunta()
    pergunta.codigo = 4
    pergunta.titulo = "Qual é a sua dúvida sobre a plataforma e pontos?"
    pergunta.acao_anterior="http://127.0.0.1:8000/chatbot_api/principal"

    resposta1 = Resposta()
    resposta1.codigo = 41
    resposta1.valor = '1'
    resposta1.descricao = "Onde posso ver o ranking do meu time e da minha empresa no geral?"
    resposta1.acao = "http://127.0.0.1:8000/chatbot_api/ranking"

    resposta2 = Resposta()
    resposta2.codigo = 42
    resposta2.valor = '2'
    resposta2.descricao = "Eu e um colega de trabalho podemos cadastrar uma atividade que fizemos juntos?"
    resposta2.acao = "http://127.0.0.1:8000/chatbot_api/atividade-conjunta"

    resposta3 = Resposta()
    resposta3.codigo = 43
    resposta3.valor = '3'
    resposta3.descricao = "Posso cadastrar ações ligadas ao ESG que realizei fora do meu horário de trabalho?"
    resposta3.acao = "http://127.0.0.1:8000/chatbot_api/atividade-externa"

    resposta4 = Resposta()
    resposta4.codigo = 44
    resposta4.valor = '4'
    resposta4.descricao = "Dentro da plataforma, existem grupos de afinidade dos quais posso participar?"
    resposta4.acao = "http://127.0.0.1:8000/chatbot_api/grupo-afinidade"

    resposta5 = Resposta()
    resposta5.codigo = 45
    resposta5.valor = '5'
    resposta5.descricao = "Voltar para o menu anterior."
    resposta5.acao = "http://127.0.0.1:8000/chatbot_api/principal"

    pergunta.save()
    resposta1.save()
    resposta2.save()
    resposta3.save()
    resposta4.save()
    resposta5.save()

    pergunta.respostas.add(resposta1)
    pergunta.respostas.add(resposta2)
    pergunta.respostas.add(resposta3)
    pergunta.respostas.add(resposta4)
    pergunta.respostas.add(resposta5)

    return pergunta