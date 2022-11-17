from ..models import Pergunta, Resposta
def duvidasEsg():
    pergunta = Pergunta()
    pergunta.codigo = 2
    pergunta.titulo = "Qual é a sua dúvida sobre ESG?"
    pergunta.acao_anterior="http://127.0.0.1:8000/chatbot_api/principal"

    resposta1 = Resposta()
    resposta1.codigo = 21
    resposta1.valor = '1'
    resposta1.descricao = "Quais são os pilares do ESG?"
    resposta1.acao = "http://127.0.0.1:8000/chatbot_api/pilares-esg"

    resposta2 = Resposta()
    resposta2.codigo = 22
    resposta2.valor = '2'
    resposta2.descricao = "Quais ações do ESG podem me ajudar a aumentar minha produtividade?"
    resposta2.acao = "http://127.0.0.1:8000/chatbot_api/produtividade-esg"

    resposta3 = Resposta()
    resposta3.codigo = 23
    resposta3.valor = '3'
    resposta3.descricao = "Quero saber mais sobre o ESG, onde posso encontrar um conteúdo confiável sobre?"
    resposta3.acao = "http://127.0.0.1:8000/chatbot_api/conteudo-esg"

    resposta4 = Resposta()
    resposta4.codigo = 24
    resposta4.valor = '4'
    resposta4.descricao = "Voltar para o menu anterior."
    resposta4.acao = "http://127.0.0.1:8000/chatbot_api/principal"


    pergunta.save()
    resposta1.save()
    resposta2.save()
    resposta3.save()
    resposta4.save()

    pergunta.respostas.add(resposta1)
    pergunta.respostas.add(resposta2)
    pergunta.respostas.add(resposta3)
    pergunta.respostas.add(resposta4)

    return pergunta