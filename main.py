# -*- coding: utf-8 -*-
"""
Main classe tcc 2 - Tainara Camila Zacarias
05/11/2019
"""

import time
import json
from operator import itemgetter
from instagramscraper import DadosInstagram 
from ttscraper import DadosTwitter
from higienizacao import Higienizacao
from calculapeso import Peso
from dicionario import Dicionario
from calculacatpeso import CategoriaPeso
from geraperfil import Perfil
from validacaoclassificadores import FuncoesMetodosMachineLearning

if __name__ == '__main__':
        
    # t1 = time.time()
    # indices = []
    # lista_palavras = []
    # lista_aparicoes = []
    # lista_usuario = []
    #
    # dadosInstagram = DadosInstagram()
    # dadosTwitter = DadosTwitter()
    # higienizacao = Higienizacao()
    # dicionario = Dicionario()
    # peso = Peso()
    # catPeso = CategoriaPeso()
    classificacao = FuncoesMetodosMachineLearning()
    #
    # instagram = input('Entre com o instagram: ')
    # twitter = input('Entre com o twitter: ')
    #
    # # Extração dos dados
    # dadosInstagram.colherdados(instagram)
    # dadosTwitter.colherdados(twitter, instagram)
    #
    # # Hizienização dos dados coletados
    # dados = higienizacao.higienizar(instagram, twitter)
    #
    # # Criação da lista de palavras do usuário
    # for d in dados:
    #     indices.append(dados.index(d))
    #
    # indices_filtrados = set(indices)
    #
    # for ind_f in indices_filtrados:
    #     #cria lista de palavras do usuario
    #     lista_palavras.append(dados[ind_f][0])
    #
    # lista_palavras = set(lista_palavras)
    #
    # # Atualização da lista de palavras globais
    # #dicionario.atualizar(lista_palavras)
    #
    # # Criação da lista de aparicoes de cada uma das palavras do usuário
    # for ind_f in indices_filtrados:
    #     aparicoes = 0
    #     #conta quantas vezes o item aparece
    #     aparicoes = indices.count(ind_f)
    #
    #     #adiciona na lista
    #     lista_aparicoes.append([dados[ind_f][0],aparicoes, dados[ind_f][1]])
    #
    # # Criação da lista de palavra/peso do usuario
    # lista_usuario = peso.calcularpeso(lista_palavras, lista_aparicoes)
    #
    # # Ordenando a lista de palavra/peso pegando os maiores pesos inicialmente
    # lista_usuario.sort(key=itemgetter(1), reverse = True)
    #
    # # Salvando a lista de palavra/peso do usuário
    # json.dump(lista_usuario, open("perfis/"+instagram+"/listaPeso_"+instagram+".json", 'w'))
    #
    # # Criando lista de categoria liwc/peso do usuário
    # listaCatPeso = catPeso.calcularcatpeso(instagram)

    # Imprimindo o perfil do usuário
    #perfil = Perfil(instagram, twitter)
    #perfil.print()

    classificacao.get_teste_correlacao()

    #tempoExec = time.time() - t1
    #print("Tempo de execução: {} segundos".format(tempoExec))
       

