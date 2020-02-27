# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 12:21:41 2019

@author: Tainara
"""

from sklearn.naive_bayes import GaussianNB
import json
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report, multilabel_confusion_matrix


class FuncoesMetodosMachineLearning(object):

    def get_treinamento_correlacao(self):

        # carrega perfis para treinamento
        treinamento = ['douglasmanso', 'justinianoadriano', 'gabrsmelo', 'santos_emilii', 'dvailson', 'any_nogueira',
                       'ferferrairo', 'allanlac', 'bahgutierrez', 'alexandretito12m', 'reis_junior1', 'sooltonaki',
                       'ygorfremo', 'junnyorbraga', 'martinonews', 'aalves_arthur', 'nemoooj', 'pqp_pedros',
                       'bbcbrasil', 'gabrielassp', 'messo2301', 'paulofraga', 'duda_alho', 'felps11', 'yfsenna',
                       'graphixodzn','ahickmann', 'lenildo.alves.nildo', 'pivo_tech', 'brksedu', '_machadinho',
                       'luanacrzz', 'thaynarakhalil', 'mateuso_', 'eusouluccabueno', 'kevonymartins', 'rosecaldeira',
                       'carlasilvaesp', 'batistaa_batista','rafaaagonz', 'caioaml', 'carolinelinsph', 'kalielpinheiro',
                       'leoamorim00', 'gabimxrques', 'victoroliveira', 'leonardomsrfps', 'brunozzor', 'rachmuniz',
                       'daicrisstina', 'pqpveroniica', 'marcoscastro', 'felipeevz', 'tonkiel', 'se.bastiao', 'bis_23',
                       'fhcfer', 'etserbu', 'marianapascoalz', 'luscas', 'babigms_', 'humbertobergamini', 'nandosang',
                       'jparaujos', 'tainaracamila', 'osnipaulo', 'roberto.filho.cbr', 'dougraz', 'the_nicks7',
                       '_anacardosos', 'zezelune', 'lwithp', 'guilhermefalcaopelegrino', 'renan.siqueira_93',
                       'ericat_lol', 'bpenilhas', 'nathalythaly', 'oledobrasil', 'marcoantonio_tk', 'silvagm1',
                       'diegosoarxs', 'joaoedu.mendes', 'anny.poly', 'iurymneves', 'said_leonardo', 'guiilhermecota',
                       'paulinhoalfaro', 'matheusfesteves', 'tiagostocco', 'bruna.m.o', 'guilhermeevo', 'isahcoutto',
                       'manumontezano', 'wagner_gurutech', 'marcal_mateus_fotografo', 'mucutinho', 'this_1984',
                       'arinoert', 'chicobarney', 'showdavida', 'gustavopetro', '_toral', 'babimsss', 'caco.bapt',
                       'pedro.baesso', 'nereuzin14', 'instadalarissa', 'reisjhr', '_fernandop', 'prazertom',
                       'camposconti', 'leticinios', 'guliguori', 'pityfi', 'f.morroni', 'samimartinss',
                       'renatamellzinha', 'petrusribeiro', 'mulier_niger', 'cadamuroana']

        i = 0
        x = []
        y = []

        # classificação base de treinamento via correlação
        while i < len(treinamento):
            x_usuario = []
            lista = json.load(open("perfis/" + treinamento[i] + "/listaCatPesPersona_" + treinamento[i] + ".json"))

            for l in lista:
                if l != 'P':
                    x_usuario.append(lista.get(l))
            y_usuario = lista.get('P')

            if y_usuario == 'O':
                y.append(1)
            elif y_usuario == 'C':
                y.append(2)
            elif y_usuario == 'E':
                y.append(3)
            elif y_usuario == 'A':
                y.append(4)
            else:
                y.append(5)

            x.append(x_usuario)

            i = i + 1

        return [x, y]

    def get_teste_correlacao(self):

        #carrega perfis de teste
        teste = ['baebuter', 'cauemoura', 'fourlan_nogueira', 'gabriellyluna_', 'guifcamargo', 'guivissotto',
                 'igorreale3', 'karolteixeiraj', 'luquinha.jpg', 'mateusix', 'pedro_hre', 'pedrohrqq_', 'rafinhabastos',
                 'rikkikitsune', 'rodpocket', 'thamsfigueiredo', 'thayssarepoles', 'tklissa', 'malkkav', 'latino_bigode',
                 'lucasrohan', 'alanzoka', 'beladmenezes', 'berriel', 'carolvistro', 'civort', 'cleytu', 'fla_eikani',
                 'wagner.linhares', 'vitustanguini', 'arielsis', '_amorimrenan_', 'guigustoo', 'pedroamericolopes',
                 'cristaosecreto.ofc', 'rosangelagrimadi', 'llucca97', 'milaxxm', 'vitorxcx', 'potyguarabardo',
                 'comicxwarrior', 'catherine_almeidaf','palomacar74', 'nathaanf', 'leandrommcosta', 'amandinha.lr',
                 'kailanyasm', 'imendesfoto_', 'joaomourav', 'brunolima.0']

        j = 0
        xt = []
        yt = []

        # classificação base de teste via correlação
        while j < len(teste):
            x_teste = []
            lista2 = json.load(open("perfis/" + teste[j] + "/listaCatPesPersona_" + teste[j] + ".json"))

            for l2 in lista2:
                if l2 != 'P':
                    x_teste.append(lista2.get(l2))

            if lista2.get('P') == 'O':
                yt.append(1)
            elif lista2.get('P') == 'C':
                yt.append(2)
            elif lista2.get('P') == 'E':
                yt.append(3)
            elif lista2.get('P') == 'A':
                yt.append(4)
            else:
                yt.append(5)

            xt.append(x_teste)
            j = j + 1

        return [xt, yt]

    def resultado(self, instagram):

        # realiza treinamento
        base_treino = self.get_treinamento_correlacao()

        # dados de treino
        x = base_treino[0]
        y = base_treino[1]

        # k = 3
        knn = KNeighborsClassifier(n_neighbors=3)
        scaler = StandardScaler()

        # Treina o modelo de KNN usando os dados de treino
        scaler.fit(x)
        xknn = scaler.transform(x)
        knn.fit(xknn, y)

        # dados do usuário
        x_teste = []
        lista = json.load(open("perfis/" + instagram + "/listaCatPesPersona_" + instagram + ".json"))

        for l in lista:
            if l != 'P':
                x_teste.append(lista.get(l))

        # Realiza a classificação
        xtknn = scaler.transform([x_teste])
        ytknn = knn.predict(xtknn)

        if ytknn == 1:
            texto = "Classificado para a personalidade de \"Abertura para a experiência\": Abertura é o \n" \
                    "interesse pela arte, emoção, aventura, ideias fora do comum, imaginação, curiosidade, e \n" \
                    "variedade de experiências. Este traço distingue as pessoas imaginativas das “terra-a-terra” e \n" \
                    "convencionais. As pessoas com elevada abertura são intelectualmente curiosas, apreciadoras da \n" \
                    "arte, e sensíveis à beleza. Elas tendem a ser, comparadas com as pessoas “fechadas”, mais \n" \
                    "criativas, a prestar mais atenção aos seus sentimentos e a terem opiniões não convencionais. \n"
        elif ytknn == 2:
            texto = "Classificado para a personalidade de \"Conscienciosidade\": É a tendência para mostrar \n" \
                    "autodisciplina, orientação para os deveres e para atingir os objetivos. Este traço mostra uma \n" \
                    "preferência pelo comportamento planejado em vez do espontâneo. Influencia a maneira como \n" \
                    "controlamos e dirigimos os nossos impulsos. Pessoas com esse traço forte são mais rígidas \n" \
                    "contra qualquer eventual quebra de valores.\n"
        elif ytknn == 3:
            texto = "Classificado para a personalidade de \"Extroversão\": É o traço pessoal caracterizado por \n" \
                    "emoções positivas e pela tendência para procurar estimulações, buscar a companhia das outras \n" \
                    "pessoas e pelo profundo envolvimento com o mundo exterior. Os extrovertidos usualmente são \n" \
                    "vistos como sendo cheios de energia, entusiastas e voltados para a ação. Essas pessoas, \n" \
                    "quando em grupos, tendem a ser falantes, assertivas e a chamar as atenções para elas. Por \n" \
                    "outro lado, os introvertidos não têm a exuberância social e os níveis de atividade dos \n" \
                    "extrovertidos. Eles tendem a parecer calmos, ponderados e menos envolvidos com o mundo social. \n"\
                    "Os introvertidos necessitam de menos estimulação e de mais tempo sozinhos do que os \n" \
                    "extrovertidos, mas isso não deve ser confundido com timidez ou depressão. Eles podem ser \n" \
                    "bastante ativos e enérgicos em outros campos que não o do relacionamento social."
        elif ytknn == 4:
            texto = "Classificado para a personalidade de \"Amabilidade\": Amabilidade é a tendência para ser \n" \
                    "compassivo e cooperante em vez de suspeitoso e antagonista face aos outros. Este traço reflete\n "\
                    "diferenças individuais na preocupação com a harmonia social. Indivíduos “amáveis” valorizam a\n " \
                    "boa relação com os outros. Eles são geralmente respeitosos, amigáveis, generosos, prestáveis e\n "\
                    "dispostos a fazer compromissos. Pessoas “amigáveis” têm também uma visão otimista da natureza \n" \
                    "humana. Elas acreditam que as pessoas são basicamente honestas, decentes e dignas de confiança.\n"\
                    "Indivíduos “não-amigáveis” põem o interesse próprio acima da boa relação com os outros. Eles \n" \
                    "normalmente não se preocupam com o bem-estar dos outros, e por vezes o seu ceticismo acerca \n" \
                    "dos motivos dos outros fá-los ser desconfiados e pouco cooperativos."
        else:
            texto = "Classificado para a personalidade de \"Neuroticismo() \": O Neuroticismo mede a instabilidade\n " \
                    "emocional. Pessoas com pontuações altas nessa escala são ansiosas, inibidas, melancólicas, \n" \
                    "dotadas de baixa autoestima e reactivos e vulneráveis ao stress. Já as que obtém baixa \n" \
                    "pontuação são de fácil trato, otimistas e dotadas de boa estima consigo mesmas. Aqueles com \n" \
                    "um grau elevado de neuroticismo são emocionalmente reactivos e vulneráveis ao stress. Estes \n" \
                    "estão mais predispostos a interpretar situações normais como sendo ameaçadoras, e pequenas \n" \
                    "frustrações como dificuldades sem esperança."

        return texto

    def validacao_modelos(self):

        naive = GaussianNB()
        # k = 3
        knn = KNeighborsClassifier(n_neighbors=3)
        # k = 5
        knn2 = KNeighborsClassifier(n_neighbors=5)
        scaler = StandardScaler()

        base_treino = self.get_treinamento_correlacao()
        x = base_treino[0]
        y = base_treino[1]

        base_teste = self.get_teste_correlacao()
        xt = base_teste[0]
        yt = base_teste[1]

        # Treina o modelo de Naive Bayes usando os dados de treino
        naive.fit(x, y)

        # Treina o modelo de KNN usando os dados de treino
        scaler.fit(x)
        xknn = scaler.transform(x)
        knn.fit(xknn, y) # knn usa uma vizinhança de k = 3
        knn2.fit(xknn, y)  # knn usa uma vizinhança de k = 5

        # Resultado de previsão
        k = 0
        correto_naive_bayes = 0
        errado_naive_bayes = 0
        correto_knn_3 = 0
        errado_knn_3 = 0
        correto_knn_5 = 0
        errado_knn_5 = 0

        ytn = []
        xtknn2 = []
        ytknn2 = []
        ytknn3 = []
        ytknn4 = []

        for t in xt:
            # realiza a classificação via naive bayes
            predicted = naive.predict([t])
            # lembrando que yt é o array que contém a classificação correta
            if predicted == [yt[k]]:
                correto_naive_bayes = correto_naive_bayes + 1
            else:
                errado_naive_bayes = errado_naive_bayes + 1
            # array de classificações feitas pelo naive bayes
            ytn.append(predicted)

            # realiza a classificação via knn, com k = 3
            xtknn = scaler.transform([t])
            xtknn2.append(xtknn)
            ytknn = knn.predict(xtknn)

            if ytknn == [yt[k]]:
                correto_knn_3 = correto_knn_3 + 1
            else:
                errado_knn_3 = errado_knn_3 + 1
            # array de classificacões feitas pelo knn, k = 3
            ytknn2.append(ytknn)

            # realiza a classificação via knn, com k = 5
            ytknn3 = knn2.predict(xtknn)

            if ytknn3 == [yt[k]]:
                correto_knn_5 = correto_knn_5 + 1
            else:
                errado_knn_5 = errado_knn_5 + 1
            # array de classificacões feitas pelo knn, k = 5
            ytknn4.append(ytknn3)

            k = k + 1

        # Validação por matriz de confusão
        print(multilabel_confusion_matrix(yt, ytn))
        print("Classification Report Naive Bayes")
        print(classification_report(yt, ytn))

        # Validação por matriz de confusão
        print(multilabel_confusion_matrix(yt, ytknn2))
        print("Classification Report Knn (k=3)")
        print(classification_report(yt, ytknn2))

        # Validação por matriz de confusão
        print(multilabel_confusion_matrix(yt, ytknn4))
        print("Classification Report Knn (k=5)")
        print(classification_report(yt, ytknn4))

        # validação por cross validation
        medias = cross_val_score(naive, xt, yt, cv=4)
        media = sum(medias) / len(medias)
        print('Naive Bayes Cross Validation: ' + str(media))
        print('\n')

        # validação por cross validation
        medias = cross_val_score(knn, xt, yt, cv=4)
        media = sum(medias) / len(medias)
        print('Knn (k=3) Cross Validation: ' + str(media))
        print('\n')

        # validação por cross validation knn para k = 5
        medias = cross_val_score(knn2, xt, yt, cv=4)
        media = sum(medias) / len(medias)
        print('Knn (k=5) Cross Validation: ' + str(media))
        print('\n')

