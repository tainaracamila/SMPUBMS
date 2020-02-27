# -*- coding: utf-8 -*-
import json
from validacaoclassificadores import FuncoesMetodosMachineLearning

class Perfil(object):

    def __init__(self, instagram, twitter):
        self.instagram = instagram
        self.twitter = twitter

    def print(self):
        personalidade = FuncoesMetodosMachineLearning()

        print("\n---------------------------")
        print("\nPerfil analisado: "+self.twitter)
        listaPeso = json.load(open("perfis/"+self.instagram+"/listaPeso_"+self.instagram+".json"))
        infoi = json.load(open('perfis/'+self.instagram+'/'+self.instagram+'.json',
                        'r', encoding="utf8"))
        infott = json.load(open('perfis/'+self.instagram+'/twitter_'+self.twitter+'.json',
                        'r', encoding="utf8"))

        i = 0
        j = 0
        k = 0
        likes = 0
        likest = 0
        comentarios = 0
        replies = 0
        nfotos = len(infoi['GraphImages'])

        while i < len(infoi['GraphImages']):
            likes = likes + (infoi['GraphImages'][i]['edge_media_preview_like']['count'])
            comentarios = comentarios + (infoi['GraphImages'][i]['edge_media_to_comment']['count'])
            i += 1

        print("\n>>>>>>>>>> Informações Instagram <<<<<<<<<<")
        print("Media de likes por foto:" + str((likes/nfotos)))
        print("Media de comentários por foto:" + str((comentarios/nfotos)))

        ntt = len(infott) #numero de tuites

        while j < len(infott):
            likest = likes + infott[j]['likes']
            replies = replies + infott[j]['replies']
            j += 1

        print("\n>>>>>>>>>> Informações Twitter <<<<<<<<<<<")
        print("Media de likes por tuíte:" + str((likest/ntt)))
        print("Media de respostas por tuítes:" + str((replies/ntt)))

        print("\n>>>>>>>>>>> Top 20 termos de maiores pesos <<<<<<<<<<")

        while k < 20:
            aux = k + 1
            print("Termo "+str(aux)+": "+listaPeso[k][0])
            k += 1

        texto = personalidade.resultado(self.instagram)

        print("\n>>>>>>>>>> Personalidade <<<<<<<<<<")
        print(texto)