from django.shortcuts import render
from rest_framework.decorators import api_view
from .business import principal, duvidasEsg, dadosCadastro, plataformaPontos, certificado, pilaresEsg, produtividadeEsg,conteudoEsg, dadosNecessarios, emailConfirmacao, esqueciSenha, protecaoDados, ranking, atividadeConjunta, atividadeExterna, grupoAfinidade, certificadoParticipacao,visualizarImpacto
from .serializers import PerguntaSerializer
from django.http.response import JsonResponse

# Create your views here.
@api_view(['GET'])
def obterPrincipal(request):
    perguntaPrincipal = principal.obterMenuPrincipal()
    perguntaPrincipal_serializer = PerguntaSerializer(perguntaPrincipal)
    resp = JsonResponse(perguntaPrincipal_serializer.data, safe=True)
    resp['Access-Control-Allow-Origin'] = '*'
    return resp

@api_view(['GET'])
def obterDuvidasEsg(request):
    perguntaEsg = duvidasEsg.duvidasEsg()
    perguntaDuvidasEsg_serializer = PerguntaSerializer(perguntaEsg)
    resp = JsonResponse(perguntaDuvidasEsg_serializer.data, safe=True)
    resp['Access-Control-Allow-Origin'] = '*'
    return resp

@api_view(['GET'])
def duvidasDadosCadastro(request):
    perguntaDadosCadastro = dadosCadastro.duvidasDadosCadastro()
    perguntaDadosCadastro_serializer = PerguntaSerializer(perguntaDadosCadastro)
    resp = JsonResponse(perguntaDadosCadastro_serializer.data, safe=True)
    resp['Access-Control-Allow-Origin'] = '*'
    return resp

@api_view(['GET'])
def obterDuvidasPlataformaPontos(request):
    perguntaPlataformaPontos = plataformaPontos.duvidasPlataformaPontos()
    perguntaPlataformaPontos_serializer = PerguntaSerializer(perguntaPlataformaPontos)
    resp = JsonResponse(perguntaPlataformaPontos_serializer.data, safe=True)
    resp['Access-Control-Allow-Origin'] = '*'
    return resp

@api_view(['GET'])
def obterDuvidasCertificado(request):
    perguntaCertificado = certificado.duvidasCertificado()
    perguntaCertificado_serializer = PerguntaSerializer(perguntaCertificado)
    resp = JsonResponse(perguntaCertificado_serializer.data, safe=True)
    resp['Access-Control-Allow-Origin'] = '*'
    return resp

@api_view(['GET'])
def obterPilaresEsg(request):
    perguntaPilaresEsg = pilaresEsg.pilaresEsg()
    perguntaPilaresEsg_serializer = PerguntaSerializer(perguntaPilaresEsg)
    resp = JsonResponse(perguntaPilaresEsg_serializer.data, safe=True)
    resp['Access-Control-Allow-Origin'] = '*'
    return resp

@api_view(['GET'])
def obterProdutividadeEsg(request):
    perguntaProdutividadeEsg = produtividadeEsg.produtividadeEsg()
    perguntaProdutividadeEsg_serializer = PerguntaSerializer(perguntaProdutividadeEsg)
    resp = JsonResponse(perguntaProdutividadeEsg_serializer.data, safe=True)
    resp['Access-Control-Allow-Origin'] = '*'
    return resp

@api_view(['GET'])
def obterConteudoEsg(request):
    perguntaConteudoEsg = conteudoEsg.conteudoEsg()
    perguntaConteudoEsg_serializer = PerguntaSerializer(perguntaConteudoEsg)
    resp = JsonResponse(perguntaConteudoEsg_serializer.data, safe=True)
    resp['Access-Control-Allow-Origin'] = '*'
    return resp

@api_view(['GET'])
def obterDadosNecessarios(request):
    perguntaDadosNecessarios = dadosNecessarios.dadosNecessarios()
    perguntaDadosNecessarios_serializer = PerguntaSerializer(perguntaDadosNecessarios)
    resp = JsonResponse(perguntaDadosNecessarios_serializer.data, safe=True)
    resp['Access-Control-Allow-Origin'] = '*'
    return resp

@api_view(['GET'])
def obterEmailConfirmacao(request):
    perguntaEmailConfirmacao = emailConfirmacao.emailConfirmacao()
    perguntaEmailConfirmacao_serializer = PerguntaSerializer(perguntaEmailConfirmacao)
    resp = JsonResponse(perguntaEmailConfirmacao_serializer.data, safe=True)
    resp['Access-Control-Allow-Origin'] = '*'
    return resp

@api_view(['GET'])
def obterEsqueciSenha(request):
    perguntaEsqueciSenha = esqueciSenha.esqueciSenha()
    perguntaEsqueciSenha_serializer = PerguntaSerializer(perguntaEsqueciSenha)
    resp = JsonResponse(perguntaEsqueciSenha_serializer.data, safe=True)
    resp['Access-Control-Allow-Origin'] = '*'
    return resp

@api_view(['GET'])
def obterProtecaoDados(request):
    perguntaProtecaoDados = protecaoDados.protecaoDados()
    perguntaProtecaoDados_serializer = PerguntaSerializer(perguntaProtecaoDados)
    resp = JsonResponse(perguntaProtecaoDados_serializer.data, safe=True)
    resp['Access-Control-Allow-Origin'] = '*'
    return resp

@api_view(['GET'])
def obterRanking(request):
    perguntaRanking = ranking.ranking()
    perguntaRanking_serializer = PerguntaSerializer(perguntaRanking)
    resp = JsonResponse(perguntaRanking_serializer.data, safe=True)
    resp['Access-Control-Allow-Origin'] = '*'
    return resp

@api_view(['GET'])
def obterAtividadeConjunta(request):
    perguntaAtividadeConjunta = atividadeConjunta.atividadeConjunta()
    perguntaAtividadeConjunta_serializer = PerguntaSerializer(perguntaAtividadeConjunta)
    resp = JsonResponse(perguntaAtividadeConjunta_serializer.data, safe=True)
    resp['Access-Control-Allow-Origin'] = '*'
    return resp

@api_view(['GET'])
def obterAtividadeExterna(request):
    perguntaAtividadeExterna = atividadeExterna.atividadeExterna()
    perguntaAtividadeExterna_serializer = PerguntaSerializer(perguntaAtividadeExterna)
    resp = JsonResponse(perguntaAtividadeExterna_serializer.data, safe=True)
    resp['Access-Control-Allow-Origin'] = '*'
    return resp

@api_view(['GET'])
def obterGrupoAfinidade(request):
    perguntaGrupoAfinidade = grupoAfinidade.grupoAfinidade()
    perguntaGrupoAfinidade_serializer = PerguntaSerializer(perguntaGrupoAfinidade)
    resp = JsonResponse(perguntaGrupoAfinidade_serializer.data, safe=True)
    resp['Access-Control-Allow-Origin'] = '*'
    return resp

@api_view(['GET'])
def obterCertificadoParticipacao(request):
    perguntaCertificadoParticipacao = certificadoParticipacao.certificadoParticipacao()
    perguntaCertificadoParticipacao_serializer = PerguntaSerializer(perguntaCertificadoParticipacao)
    resp = JsonResponse(perguntaCertificadoParticipacao_serializer.data, safe=True)
    resp['Access-Control-Allow-Origin'] = '*'
    return resp

@api_view(['GET'])
def obterVisualizarImpacto(request):
    perguntaVisualizarImpacto = visualizarImpacto.visualizarImpacto()
    perguntaVisualizarImpacto_serializer = PerguntaSerializer(perguntaVisualizarImpacto)
    resp = JsonResponse(perguntaVisualizarImpacto_serializer.data, safe=True)
    resp['Access-Control-Allow-Origin'] = '*'
    return resp

