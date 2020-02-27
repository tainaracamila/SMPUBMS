# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 20:29:18 2019

@author: Tainara
"""
import json

class Dicionario:
        
    def atualizar(self, lista_palavras):    
        
        dicionario = json.load(open("dicionarios/dicionario.json"))
        
        for palavra in lista_palavras:
            if palavra in dicionario:
                dicionario[palavra] = dicionario.get(palavra) + 1
            else:
                dicionario[palavra] = 1
        
        json.dump(dicionario, open("dicionarios/dicionario.json", 'w'))
        
    

