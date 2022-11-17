from ..models import Pergunta, Resposta
def duvidasDadosCadastro():
    pergunta = Pergunta()
    pergunta.codigo = 3
    pergunta.titulo = "Qual é a sua dúvida sobre dados e cadastro?"
    pergunta.acao_anterior="http://127.0.0.1:8000/chatbot_api/principal"

    resposta1 = Resposta()
    resposta1.codigo = 31
    resposta1.valor = '1'
    resposta1.descricao = "Quais são os dados necessários para meu cadastro na plataforma?"
    resposta1.acao = "http://127.0.0.1:8000/chatbot_api/dados-necessarios"

    resposta2 = Resposta()
    resposta2.codigo = 32
    resposta2.valor = '2'
    resposta2.descricao = "Não recebi o e-mail de confirmação da criação da conta, o que fazer?"
    resposta2.acao = "http://127.0.0.1:8000/chatbot_api/email-confirmacao"

    resposta3 = Resposta()
    resposta3.codigo = 33
    resposta3.valor = '3'
    resposta3.descricao = "Esqueci minha senha, como prosseguir?"
    resposta3.acao = "http://127.0.0.1:8000/chatbot_api/esqueci-senha"

    resposta4 = Resposta()
    resposta4.codigo = 34
    resposta4.valor = '4'
    resposta4.descricao = "Meus dados que usei na hora do meu cadastro e o registro das atividades são protegidos?"
    resposta4.acao = "http://127.0.0.1:8000/chatbot_api/protecao-dados"

    resposta5 = Resposta()
    resposta5.codigo = 35
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
