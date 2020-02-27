# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 08:56:23 2019

@author: Tainara
"""
#class Higienizacao:
import json
import re
import nltk
sno = nltk.stem.SnowballStemmer('portuguese')
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

class Higienizacao:
       
    def higienizar(self, instagram, twitter):   
        #definindo stop_words
        stop_words0 = stopwords.words('english')
        stop_words1 = stopwords.words('portuguese') 
        stop_words = set(stop_words0+stop_words1) 
        
        twitter_termos = self.higienizacaoTwitter(instagram, twitter, stop_words)
        instagram_termos = self.higienizacaoInstagram(instagram, stop_words)
        
        return twitter_termos+instagram_termos   
    
    def higienizacaoTwitter(self, instagram, twitter, stop_words):
        file = open('perfis/'+instagram+'/twitter_'+twitter+'.json', 
                    'r', encoding="utf8")
        dados = json.load(file)
        file.close() 
        
        #pega o texto do tuite
        #primeiro paramentro é variável, pega de cada tuite
        i = 0
        termos = []
        
        while i < len(dados):
            #le o tweet
            texto = dados[i]['text']
            #print(texto+"\n")
            
            #verifica se e rt ou nao
            e_retweet = dados[i]['is_retweet'] 
            
            #deixa tudo em caixa baixa
            texto = texto.lower()
            #print(texto+"\n")
            
            #remove pontuação
            texto = re.sub(r'[^\w\s]', '', texto)
            #print(texto+"\n")
            
            #realiza a tokenização
            texto = word_tokenize(texto)
            #print(texto)
        
            #retira os stop words           
            texto_filtrado = [w for w in texto if not w in stop_words] 
            #print(texto_filtrado)
            
            for palavra in texto_filtrado:
                palavra = palavra.split("http")[0]
                
                if palavra != "":
                    palavra = palavra.split("pic")[0]
                    
                if palavra != "":
                    if not palavra in stop_words:
                       #termos.append(sno.stem(palavra)) 
                       termos.append([palavra,e_retweet]) 
                                     
            i = i + 1
            
        return termos

    def higienizacaoInstagram(self, instagram, stop_words):
        file = open('perfis/'+instagram+'/'+instagram+'.json', 
                    'r', encoding="utf8")
        dados = json.load(file)
        file.close() 
        
        #pega o legenda da foto
        #primeiro paramentro é variável, pega de cada tuite
        i = 0
        termos = []
        
        while i < len(dados['GraphImages']):
            
            texto = ""
        
            #pegar texto da legenda
            if (dados['GraphImages'][i]['edge_media_to_caption']['edges'] != []):
                texto = dados['GraphImages'][i]['edge_media_to_caption']['edges'][0]['node']['text']
                #print(texto)
                #print("\n")
            
            #variavel fixa para instagram
            e_retweet = 0
            
            #deixa tudo em caixa baixa
            texto = texto.lower()
            #print(texto+"\n")
            
            #remove pontuação
            texto = re.sub(r'[^\w\s]', ' ', texto)
            #print(texto+"\n")
            
            #realiza a tokenização
            texto = word_tokenize(texto)
            #print(texto)
        
            #retira os stop words           
            texto_filtrado = [w for w in texto if not w in stop_words] 
            #print(texto_filtrado)
            
            for palavra in texto_filtrado:
                palavra = palavra.split("http")[0]
                
                if palavra != "":
                    palavra = palavra.split("pic")[0]
                    
                if palavra != "":
                    if not palavra in stop_words:
                       #termos.append(sno.stem(palavra)) 
                       termos.append([palavra,e_retweet])
                                     
            i = i + 1
            
        return termos     

        


