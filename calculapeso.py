# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 20:52:27 2019

@author: Tainara
"""
import math 
import json

#from dicionario import Dicionario 

class Peso:
    
    def calcularpeso(self, lista_palavras, lista_aparicoes):
        
        lista_final = []      
        numero_usuarios = json.load(open("numeroperfis.json", 'r', encoding="utf8"))
        dicionario = json.load(open("dicionarios/dicionario.json"))
        #dicionario = json.load(open("dicionarios/dicionarioSujo.json"))
                
        for palavra in lista_palavras:
            
            freq_parcial = 0
            freq_total = 0
            peso_usuarios = 0
            peso_ln = 0
            peso = 0
            
            indice_aparicao = [lista_aparicoes.index(x) for x in lista_aparicoes if palavra in x]
            
            for ia in indice_aparicao:
                #numerador = calcula  termo x aparicao + termo x aparicao x 0,5
                if lista_aparicoes[ia][2] == 0:
                    freq_parcial += lista_aparicoes[ia][1]
                else: 
                    freq_parcial += lista_aparicoes[ia][1]*0.5
                
                #denominador = frequencia total da palavra
                freq_total += lista_aparicoes[ia][1]
            
            peso_usuarios = freq_parcial/freq_total
            
            # procura palavra no dicionario
            #serve para verificar quantos usuarios tem a palavra
            usuarios_com_palavra = dicionario.get(palavra)
    
            peso_ln = math.log(numero_usuarios/usuarios_com_palavra + 1) 
            
            peso = peso_usuarios * peso_ln
            
            lista_final.append((palavra, peso))
                
        return lista_final
        
            