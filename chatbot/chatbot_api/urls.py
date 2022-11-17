from django.urls import path
from . import views
urlpatterns = [
    path('principal', views.obterPrincipal, name='menu-principal'),
    path('duvidas-esg', views.obterDuvidasEsg, name='duvidas-esg'),
    path('duvidas-dados-cadastro', views.duvidasDadosCadastro, name='duvidas-dados-cadastro'),
    path('duvidas-plataforma-pontos', views.obterDuvidasPlataformaPontos, name='duvidas-plataforma-pontos'),
    path('duvidas-certificado', views.obterDuvidasCertificado, name='duvidas-certificado'),
    path('pilares-esg', views.obterPilaresEsg, name='pilares-esg'),
    path('produtividade-esg', views.obterProdutividadeEsg, name='produtividade-esg'),
    path('conteudo-esg', views.obterConteudoEsg, name='conteudo-esg'),
    path('dados-necessarios', views.obterDadosNecessarios, name='dados-necessarios'),
    path('email-confirmacao', views.obterEmailConfirmacao, name='email-confirmacao'),
    path('esqueci-senha', views.obterEsqueciSenha, name='esqueci-senha'),
    path('protecao-dados', views.obterProtecaoDados, name='protecao-dados'),
    path('ranking', views.obterRanking, name='ranking'),
    path('atividade-conjunta', views.obterAtividadeConjunta, name='atividade-conjunta'),
    path('atividade-externa', views.obterAtividadeExterna, name='atividade-externa'),
    path('grupo-afinidade', views.obterGrupoAfinidade, name='grupo-afinidade'),
    path('certificado-participacao', views.obterCertificadoParticipacao, name='certificado-participacao'),
    path('visualizar-impacto', views.obterVisualizarImpacto, name='visualizar-impacto')
]