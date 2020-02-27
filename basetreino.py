# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 20:17:29 2019

@author: Tainara

Montagem da Base de Treinamento.
"""
import json
import nltk
sno = nltk.stem.SnowballStemmer('portuguese') 

if __name__ == '__main__':
    
    instagram = ['baebuter', 'cauemoura', 'fourlan_nogueira', 'gabriellyluna_', 'guifcamargo', 'guivissotto', 'igorreale3', 'karolteixeiraj', 'luquinha.jpg', 'mateusix', 'pedro_hre', 'pedrohrqq_', 'rafinhabastos', 'rikkikitsune', 'rodpocket', 'thamsfigueiredo', 'thayssarepoles', 'tklissa', 'malkkav', 'latino_bigode', 'lucasrohan', 'alanzoka', 'beladmenezes', 'berriel', 'carolvistro', 'civort', 'cleytu', 'fla_eikani', 'wagner.linhares', 'vitustanguini', 'arielsis', '_amorimrenan_', 'guigustoo', 'pedroamericolopes', 'cristaosecreto.ofc', 'rosangelagrimadi', 'llucca97', 'milaxxm', 'vitorxcx', 'potyguarabardo', 'comicxwarrior', 'catherine_almeidaf', 'palomacar74', 'nathaanf', 'leandrommcosta', 'amandinha.lr', 'kailanyasm', 'imendesfoto_', 'joaomourav', 'brunolima.0']
    #instagram = ['tainaracamila']
    i = 0
    
    #dicionario liwc
    file = open('dicionarios/dicionarioLIWC2015.json', 'r', encoding="utf-8")
    dicionario = json.load(file)
    file.close()
    
    #dicionario correlacao liwc - big five considerando idade e genero
    file = open('dicionarios/EACNOLiwcWithAgeGenSemBase.json', 'r', encoding="utf-8")
    dicionarioCorrelacao = json.load(file)
    file.close()
        
    arrayN = 0
    arrayE = 0
    arrayO = 0
    arrayA = 0
    arrayC = 0  
    
    while i < len(instagram):
        
        listaCategoriaPeso = {}
        listaCatPesPersona = {'15':0.0, '121': 0.0, '40': 0.0, '41': 0.0, '42': 0.0, 
                              '30': 0.0, '31': 0.0, '32': 0.0, '33': 0.0, '34': 0.0, 
                              '35': 0.0, '50': 0.0, '51': 0.0, '52': 0.0, '53': 0.0, 
                              '54': 0.0, '55': 0.0, '60': 0.0, '61': 0.0, '62': 0.0, 
                              '63': 0.0, '70': 0.0, '71': 0.0, '72': 0.0, '73': 0.0, 
                              '74': 0.0, '100': 0.0, '101': 0.0, '102': 0.0, '103': 0.0, 
                              '110':0.0, '111': 0.0, '112': 0.0, '113': 0.0, '114': 0.0, 
                              '115': 0.0, '123': 0.0, '124': 0.0, '125': 0.0, 'P':'A'}
        #categorias Neuroticism, Extraversion, 
        #Openness, Agreeableness, and Conscientiousness
        persona_n = 0.0
        persona_e = 0.0
        persona_o = 0.0
        persona_a = 0.0 
        persona_c = 0.0
        
        persona_n2 = 0.0
        persona_e2 = 0.0
        persona_o2 = 0.0
        persona_a2 = 0.0 
        persona_c2 = 0.0
        
        N = 0.0
        E = 0.0
        O = 0.0
        A = 0.0
        C = 0.0
        
        palavraCategoria = []
        listaPeso = json.load(open(
                "perfis/"+instagram[i]+"/listaPeso_"+instagram[i]+".json"))
        
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
            peso = 0.0
            if categoriapeso in dicionarioCorrelacao:
                listaCatPesPersona[categoriapeso] = listaCategoriaPeso.get(categoriapeso)
                correlacao = dicionarioCorrelacao.get(categoriapeso)
                peso = listaCategoriaPeso.get(categoriapeso)
                #calculo da personalidade
                persona_e = persona_e + (correlacao[0] * peso)
                persona_a = persona_a + (correlacao[1] * peso)
                persona_c = persona_c + (correlacao[2] * peso)
                persona_n = persona_n + (correlacao[3] * peso)
                persona_o = persona_o + (correlacao[4] * peso)
        
        N = persona_n
        E = persona_e
        O = persona_o
        A = persona_a
        C = persona_c
                
        arrayPersonalidade = [N , E, O, A, C]
        max_imo = max(arrayPersonalidade)
                
        if max_imo == N:
            listaCatPesPersona['P'] = 'N'
            arrayN += 1
        elif max_imo == E:
            listaCatPesPersona['P'] = 'E'
            arrayE += 1
        elif max_imo == O:
            listaCatPesPersona['P'] = 'O'
            arrayO += 1
        elif max_imo == A:
            listaCatPesPersona['P'] = 'A'
            arrayA += 1
        else:
            listaCatPesPersona['P'] = 'C'
            arrayC += 1
        
        #json.dump(listaCatPesPersona, open(
         #       "perfis/"+instagram[i]+"/listaCatPesPersona_"+instagram[i]+".json", 'w'))
        
        i = i + 1
    
    print(arrayO)
    print(arrayC)
    print(arrayE)
    print(arrayA)
    print(arrayN)
    print("Done.")
   
        
