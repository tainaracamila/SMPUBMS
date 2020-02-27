# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 11:57:06 2019

@author: Tainara
"""
import nltk
sno = nltk.stem.SnowballStemmer('portuguese') 
import json

#from dicionario import Dicionario 

class CategoriaPeso:
    
    def calcularcatpeso(self, instagram):
        
        listaCategoriaPeso = {}
        palavraCategoria = []
        listaCatPesPersona = {'15':0.0, '121': 0.0, '40': 0.0, '41': 0.0, '42': 0.0, 
                              '30': 0.0, '31': 0.0, '32': 0.0, '33': 0.0, '34': 0.0, 
                              '35': 0.0, '50': 0.0, '51': 0.0, '52': 0.0, '53': 0.0, 
                              '54': 0.0, '55': 0.0, '60': 0.0, '61': 0.0, '62': 0.0, 
                              '63': 0.0, '70': 0.0, '71': 0.0, '72': 0.0, '73': 0.0, 
                              '74': 0.0, '100': 0.0, '101': 0.0, '102': 0.0, '103': 0.0, 
                              '110':0.0, '111': 0.0, '112': 0.0, '113': 0.0, '114': 0.0, 
                              '115': 0.0, '123': 0.0, '124': 0.0, '125': 0.0}
        
        listaPeso = json.load(open("perfis/"+instagram+"/listaPeso_"+instagram+".json"))
        dicionario = json.load(open('dicionarios/dicionarioLIWC2015.json', 'r', encoding="utf-8"))
        dicionarioCorrelacao = json.load(open('dicionarios/EACNOLiwcWithAgeGenSemBase.json', 'r', encoding="utf-8"))
        
        for palavra in listaPeso:
            if palavra[0] in dicionario:
                palavraCategoria = dicionario.get(palavra[0])
            else:
                palavra_s = sno.stem(palavra[0])  
                if palavra_s in dicionario:
                    palavraCategoria = dicionario.get(palavra_s)
            
            for categoria in palavraCategoria:
                if categoria in listaCategoriaPeso:
                    # vai somando os pesos de todas as palavras que 
                    #pertencem a aquela categoria
                    listaCategoriaPeso[categoria] = listaCategoriaPeso.get(
                            categoria) + palavra[1]
                else:
                    listaCategoriaPeso[categoria] = palavra[1]
                
        for categoriapeso in listaCategoriaPeso:
            if categoriapeso in dicionarioCorrelacao:
                listaCatPesPersona[categoriapeso] = listaCategoriaPeso.get(categoriapeso)
        
        return listaCatPesPersona
                