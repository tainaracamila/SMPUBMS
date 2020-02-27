# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 19:23:54 2019

@author: Tainara 

Criando dicionario LIWC em formato JSON

"""
import json 

if __name__ == '__main__':
    
    f = open("dicionarios/liwc/LIWC2015.txt", "r")
    dados = f.readlines()
    f.close() 
    dict_ = {}
    i = 101
    
    while i < len(dados):
        x = str(dados[i]).split("\t",1)
        y = x[1].rstrip().split("\t")
        dict_[x[0].replace('*', '')] = y
        i+=1
    
    json.dump(dict_, open("dicionarioFormatado.json", 'w', encoding="utf-8"))
    
    file = open('dicionarioFormatado.json', 'r', encoding="utf-8")
    dados = json.load(file)
    file.close()
    
    #print(dados)
    
    #exemplo:
    if 'medo' in dados:
        print(dados['medo'])
        