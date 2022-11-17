from ..models import Pergunta, Resposta
def obterMenuPrincipal():
    pergunta = Pergunta()
    pergunta.codigo = 1
    pergunta.titulo = "Olá, digite o número da opção desejada"

    resposta1 = Resposta()
    resposta1.codigo = 1
    resposta1.valor = '1'
    resposta1.descricao = "Dúvidas sobre o ESG"
    resposta1.acao = "http://127.0.0.1:8000/chatbot_api/duvidas-esg"

    resposta2 = Resposta()
    resposta2.codigo = 2
    resposta2.valor = '2'
    resposta2.descricao = "Dúvidas sobre dados e cadastro"
    resposta2.acao = "http://127.0.0.1:8000/chatbot_api/duvidas-dados-cadastro"

    resposta3 = Resposta()
    resposta3.codigo = 3
    resposta3.valor = '3'
    resposta3.descricao = "Dúvidas sobre a plataforma e pontos"
    resposta3.acao = "http://127.0.0.1:8000/chatbot_api/duvidas-plataforma-pontos"

    resposta4 = Resposta()
    resposta4.codigo = 4
    resposta4.valor = '4'
    resposta4.descricao = "Dúvidas sobre certificado de participação"
    resposta4.acao = "http://127.0.0.1:8000/chatbot_api/duvidas-certificado"

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