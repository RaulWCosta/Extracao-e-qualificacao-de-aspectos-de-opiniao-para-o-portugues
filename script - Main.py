# -*- coding: utf-8 -*-

import os
import fnmatch
from enelvo import normaliser
import re
import numpy as np
import pickle
import sys
import gensim
import nltk

# Dicionario que mapeia os termos-pista para aspectos explicitos
dict_implicit2explicit = {
    # implicit: explicit
    "trava": "velocidade",
    "lento": "velocidade",
    "compacto": "design",
    "intuitiva": "usabilidade",
    "confianca na marca": "confiabilidade",
    "filma em hd": "video",
    "nigth shot": "foto",
    "facilidade de uso": "usabilidade",
    "bonita": "design",
    "compacta": "design",
    "congela": "velocidade",
    "funciona em qualquer lugar": "sinal",
    "descarrega": "bateria",
    "elegante": "design",
    "facil de mexer": "usabilidade",
    "grande": "tamanho",
    "tempo de resposta": "velocidade",
    "pequeno": "tamanho",
    "robusto": "design",
    "leve": "peso",
    "falta de compatibilidade": "sistema operacional",
    "linguagem": "escrita",
    "material": "design",
    "fina": "design",
    "barato": "valor",
    "facil de utilizar": "usabilidade",
    "leveza": "peso",
    "bugs": "velocidade",
    "facilidade de mexer": "usabilidade",
    "pesado": "peso",
    "demora a responder": "velocidade",
    "rapido": "velocidade",
    "facil de manusear": "usabilidade",
    "restarta": "velocidade",
    "chique": "design",
    "levinho": "peso",
    "lindo": "design",
    "facil de operar": "usabilidade",
    "auto explicativa": "usabilidade",
    "recebi chamadas até na beira do rio são francisco": "sinal",
    "arrojado": "design",
    "facil de usar": "usabilidade",
    "linda": "design",
    "pratica": "usabilidade",
    "deora para responder": "velocidade",
    "modulo de filmar": "camera",
    "pequena": "tamanho",
    "sensibilidade": "tela",
    "acessivel": "valor",
    "medidas": "tamanho",
    "versatil": "peso",
    "acesso aos dados": "sincronizacao",
    "facil uso": "usabilidade",
    "modo noite": "imagem",
    "pratico": "usabilidade",
    "operacao": "usabilidade",
    "atual": "design",
    "bonito": "design",
    "volumoso": "tamanho",
    "moderno": "design",
    "porcaria": "smartphone",
    "rapida": "velocidade"
}


def load_lexicon(dir, file):
    """Le arquivos salvos com o Pickle
        Parametros:
            dir (str): Nome da pasta onde o arquivo desejado esta salvo.
            file (str): Nome do arquivo desejado.
        Retorno:
            Variavel que foi salva no arquivo.
    """
    try:
        with open(os.path.join(dir,file), "rb") as f:
            output_file = pickle.load(f)
    except:
        print("the file {0} couldn't be found in {1}".format(file, dir))
    return output_file


def pre_processing_text(text, use_normalizer=False):
    """Pre-processa texto de entreda para garantir que esteja no formato descrito pela monografia
        Parametros:
            text (str): Texto que sera processado.
            use_normalizer (bool): Indica se o normalizador enelvo sera usado, no geral se quer usar
                este normalizador para revisoes inteiras.
        Retorno:
            Texto processado
    """
    if use_normalizer:
        norm = normaliser.Normaliser()
        text = norm.normalise(text)

    text = text.lower()

    input_chars = ["\n", ".", "!", "?", "ç", " / ", " - ", "|", "ã", "õ", "á", "é", "í", "ó", "ú", "â", "ê", "î", "ô", "û", "à", "è", "ì", "ò", "ù"]
    output_chars = [" . ", " . ", " . ", " . ", "c", "/", "-", "", "a", "o", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u"]

    for i in range(len(input_chars)):
        text = text.replace(input_chars[i], output_chars[i])  

    text.strip()

    return text

def load_new_reviews():
    """Carrega revisoes presentes na pasta Nem_reviews que estao no formato .txt, considera-se que cada
        .txt eh uma revisao individual
        Parametros:
            Vazio
        Retorno:
            Lista com as revisoes encontradas carregadas, caso nenhum seja encontrada sera retronada uma lista vazia
    """
    all_reviews = []
    
    for dirpath, _, files in os.walk("./New_reviews"):
        for filename in fnmatch.filter(files, '*.txt'):
            f = open(os.path.join(dirpath, filename), "r", encoding="utf8")
            review = f.read()
            review = pre_processing_text(review, use_normalizer=True)
            all_reviews.append(review)
    return all_reviews

def get_review_key_words(review, words_list):
    """Encontra conjunto de palavras-chave que estao presentes em uma dada revisao.
        Parametros:
            review (str): revisao pre-processada
            words_list (list): lista com as palavras que se deseja buscar dentro da revisao
        Retorno:
            Lista com as palavras encontradas e suas respectivas posicoes na revisao.
                Ex. [[palavra1, posicao1], [palavra2, posicao2]]
    """
    review_key_words = []
    review.replace(","," ")
    review = " "+review+" "
    for word in words_list:
        pattern=re.compile(u" {} ".format(word), re.UNICODE)
        match = re.search(pattern, review)
        if match:
            pos = match.span()[0]
            review_key_words.append([word, pos])
    return review_key_words

def distance_between_words(review, word1, word2):
    """Numero de palavras entre duas palavras dadas em uma revisao
        Parametros:
            review (str): revisao
            word1 (str): palavra 1
            word2 (str): palavra 2
        Retorno:
            Numero de palavras entre as palavras 1 e 2 presentes na revisao. Caso a entrada nao seja valida,
                sera retornado o valor -1.
    
    """
    review.replace(","," ")
    tokenized = nltk.tokenize.word_tokenize(review, language='portuguese')

    if not (word1 in review and word2 in review):
        return -1

    i = 0
    pos1 = 0
    pos2 = 10000000
    for i in range(len(tokenized)):
        if tokenized[i] in word1:
            pos1 = i
        if tokenized[i] in word2:
            pos2 = i
    return abs(pos1 - pos2)

def sent_analisys(review, aspects_list, sent_words, sent_words_polarity, identify_implicity=False):
    """Realiza a analise de sentimentos em uma revisao
        Parametros:
            review (str): revisao de entrada
            aspects_list (list): lexico com os aspectos que serao usados para realizar a extracaao
            sent_words (list): lexico com as palavras de sentimento
            sent_words_polarity (dict): mapeia termos-pista para aspectos explicitos
            identify_implicity (bool): indica se os aspectos implicitos devem ou nao ser identificados
        Retorno:
            Lista com os aspectos identificados e suas respectivas polaridades
    """
    
    opinions = []

    review_sentences = review.split(".")
    for sentence in review_sentences:
        sentence_aspects = get_review_key_words(sentence, aspects_list)
        sentence_sent_words = get_review_key_words(sentence, sent_words)
        

        if len(sentence_aspects) == 0:
            continue
        elif len(sentence_sent_words) == 0:
            for aspect in sentence_aspects:
                if aspect[0] in dict_implicit2explicit:
                    # Mapeia para um aspecto explicito e adiciona na lista de aspectos extraidos, porem sem sentimento atrelado
                    opinions.append([dict_implicit2explicit[aspect[0]], "", "x"])
                else:
                    # Adiciona na lista de aspectos extraidos, porem sem sentimento atrelado
                    opinions.append([aspect[0], "", "x"])
        else:
            # Pegar sentimentos
            for aspect in sentence_aspects:
                min_dist_word=["",0]
                min_dist = 1000
                for sent_word in sentence_sent_words:
                    dist = distance_between_words(sentence, aspect[0], sent_word[0])
                    if min_dist > dist:  
                        min_dist_word = sent_word
                        min_dist = dist
                # Checar se ha mudanca de polaridade na palavra de sentimentos
                polarity = sent_words_polarity[min_dist_word[0]]
                if sentence[sent_word[1]-3:sent_word[1]] == "não" or \
                    sentence[sent_word[1]-5:sent_word[1]] == "não é" or \
                    sentence[sent_word[1]-6:sent_word[1]] == "jamais" or \
                    sentence[sent_word[1]-4:sent_word[1]] == "nada" or \
                    sentence[sent_word[1]-3:sent_word[1]] == "nem" or \
                    sentence[sent_word[1]-6:sent_word[1]] == "nenhum" or \
                    sentence[sent_word[1]-7:sent_word[1]] == "ninguem" or \
                    sentence[sent_word[1]-5:sent_word[1]] == "nunca" or \
                    sentence[sent_word[1]-8:sent_word[1]] == "tampouco":
                    # Mudou orientacao do sentimento
                    if sent_words_polarity[sent_word[0]] == "+":
                        polarity = "-"
                    else:
                        polarity = "+"
                
                if identify_implicity:
                    # Checa se o aspecto identificado eh um termo pista
                    if aspect[0] in dict_implicit2explicit:
                        # Mapeia para um aspecto explicito e adiciona na lista de aspectos+sentimento extraidos
                        opinions.append([dict_implicit2explicit[aspect[0]], min_dist_word[0], polarity])
                    else:
                        # Adiciona na lista de aspectos+sentimento extraidos
                        opinions.append([aspect[0], min_dist_word[0], polarity])
                else:
                    opinions.append([aspect[0], min_dist_word[0], polarity])

    return opinions

def precision_recall_score(y_true, y_pred):
    """Compara os aspectos anotados com os aspectos extraidos para recuperar a precisao, a cobertura e a medida-f
        Parametros:
            y_true (list): Lista com os aspectos que foram anotados presentes na revisao
            y_pred (list): Lista com os aspectos que foram extraidos de uma dada revisao
        Retorno:
            Lista no seguinte formato:
            [precisao otimimsta,
             precisao pessimista,
             cobertura otimista,
             cobertura pessimista,
             presicao de sentimento otimista,
             presicao de sentimento pessimista]
    """

    ot_precision_score = 0
    pe_precision_score = 0
    ot_sent_precision_Score = 0
    pe_sent_precision_Score = 0
    ot_recall_score = 0
    pe_recall_score = 0

    # precisao pessimista
    for i in y_pred:
        for j in y_true:
            if j[2].lower() == i[0].lower():
                pe_precision_score += 1
                if j[3] in i[2]:
                    pe_sent_precision_Score += 1
                break

    # recall pessimista
    for i in y_true:
        for j in y_pred:
            if j[0].lower() == i[2].lower():
                pe_recall_score += 1
                break

    # precisao otimista
    for i in y_pred:
        for j in y_true:
            if j[2].lower() in i[0].lower():
                ot_precision_score += 1
                if j[3] in i[2]:
                    ot_sent_precision_Score += 1
                break

    # recall otimista
    for i in y_true:
        for j in y_pred:
            if j[0].lower() in i[2].lower():
                ot_recall_score += 1
                break

    if len(y_pred) > 0:
        ot_precision_score = ot_precision_score/len(y_pred)
        pe_precision_score = pe_precision_score/len(y_pred)
        ot_sent_precision_Score = ot_sent_precision_Score/len(y_pred)
        pe_sent_precision_Score = pe_sent_precision_Score/len(y_pred)
    else:
        ot_precision_score = 0
        pe_precision_score = 0
        ot_sent_precision_Score = 0
        pe_sent_precision_Score = 0

    ot_recall_score = ot_recall_score/len(y_true)
    pe_recall_score = pe_recall_score/len(y_true)
    
    return [ot_precision_score, pe_precision_score, ot_recall_score, pe_recall_score, ot_sent_precision_Score, pe_sent_precision_Score]

if __name__ == "__main__":

    flag_write_new_review = False
    flag_run_tests = False
    flag_load_new_reviews = False

    for i in range(1, len(sys.argv)):
        if sys.argv[i] == "--wr": # write review in console
            flag_write_new_review = True
        if sys.argv[i] == "--lr": 
            flag_load_new_reviews = True
        else:
            flag_run_tests = True
        
    
    sent_words = load_lexicon("Sentiment_words", "sent_words.p")
    sent_words_polarity = load_lexicon("Sentiment_words", "sent_words_polarity.p")


    if flag_write_new_review:
        
        aspects = load_lexicon("Aspects_lexicon","explicit_aspects.p") + load_lexicon("Aspects_lexicon","implicit_aspects.p")
        print("Digite uma revisao:")
        review = input()
        review = pre_processing_text(review, use_normalizer=True)
        opinions = sent_analisys(review, aspects, sent_words, sent_words_polarity, identify_implicity=True)
        print(opinions)

    elif flag_load_new_reviews:
        
        reviews = load_new_reviews()
        aspects = load_lexicon("Aspects_lexicon", "ontology_explicit_aspects.p") + load_lexicon("Aspects_lexicon", "ontology_implicit_aspects.p")
        
        for r in reviews:
            review = pre_processing_text(r, use_normalizer=True)
            opinions = sent_analisys(review, aspects, sent_words, sent_words_polarity, identify_implicity=True)
            print(str(opinions)+"\n")

    elif flag_run_tests:
            
        try:
            with open(os.path.join("Tagged Corpus", "tagged_reviews.p"), "rb") as f:
                tagged_reviews = pickle.load(f)
        except:
            print("The tagged_reviews.p couldn't be found. Please, run generate_tagged_reviews_pickle.py")


        with open("output_ontology_aspects.txt", "w") as f:
            aspects = load_lexicon("Aspects_lexicon", "ontology_explicit_aspects.p") + load_lexicon("Aspects_lexicon", "ontology_implicit_aspects.p")
            f.write("ot_precision_score, pe_precision_score, ot_recall_score, pe_recall_score, ot_sent_precision_Score, pe_sent_precision_Score\n")
            for idx in tagged_reviews:
                
                review = pre_processing_text(tagged_reviews[idx]["review"], use_normalizer=True)
                opinions = sent_analisys(review, aspects, sent_words, sent_words_polarity, identify_implicity=True)

                print(str(tagged_reviews[idx]["opinions"])+"\n")
                print(str(opinions)+"\n")
                resul = precision_recall_score(tagged_reviews[idx]["opinions"], opinions)
                f.write(str(resul)+"\n")


        with open("output_ontology_embedding_aspects.txt", "w") as f:
            
            aspects = load_lexicon("Aspects_lexicon","ontology_embedding_aspects.p")
            f.write("ot_precision_score, pe_precision_score, ot_recall_score, pe_recall_score, ot_sent_precision_Score, pe_sent_precision_Score\n")
            for idx in tagged_reviews:
                
                review = pre_processing_text(tagged_reviews[idx]["review"], use_normalizer=True)
                opinions = sent_analisys(review, aspects, sent_words, sent_words_polarity, identify_implicity=False)
                print(str(tagged_reviews[idx]["opinions"])+"\n")
                print(str(opinions)+"\n")
                resul = precision_recall_score(tagged_reviews[idx]["opinions"], opinions)
                f.write(str(resul)+"\n")
            
        with open("output_noun_aspects.txt", "w") as f:
            aspects = load_lexicon("Aspects_lexicon", "noun_aspects.p")

            f.write("ot_precision_score, pe_precision_score, ot_recall_score, pe_recall_score, ot_sent_precision_Score, pe_sent_precision_Score\n")
            for idx in tagged_reviews:
                
                review = pre_processing_text(tagged_reviews[idx]["review"], use_normalizer=True)
                opinions = sent_analisys(review, aspects, sent_words, sent_words_polarity, identify_implicity=False)
                print(str(tagged_reviews[idx]["opinions"])+"\n")
                print(str(opinions)+"\n")

                resul = precision_recall_score(tagged_reviews[idx]["opinions"], opinions)
                f.write(str(resul)+"\n")

        with open("output_noun_embedding_aspects.txt", "w") as f:

            aspects = load_lexicon("Aspects_lexicon","noun_embedding_aspects.p")        

            f.write("ot_precision_score, pe_precision_score, ot_recall_score, pe_recall_score, ot_sent_precision_Score, pe_sent_precision_Score\n")
            for idx in tagged_reviews:
                
                review = pre_processing_text(tagged_reviews[idx]["review"], use_normalizer=True)
                opinions = sent_analisys(review, aspects, sent_words, sent_words_polarity, identify_implicity=False)
                print(str(tagged_reviews[idx]["opinions"])+"\n")
                print(str(opinions)+"\n")

                resul = precision_recall_score(tagged_reviews[idx]["opinions"], opinions)
                f.write(str(resul)+"\n")

