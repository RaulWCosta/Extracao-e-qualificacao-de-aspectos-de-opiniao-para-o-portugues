import pickle
import os
import nltk
import gensim
import numpy as np
from enelvo import normaliser
import fnmatch

def pre_processing_text(text, use_normalizer=False):
    
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

def create_aspects_lexicon_nouns(frequency_cut=0.03, save=False):

    with open("tagger.pkl", "rb") as f:
        tagger = pickle.load(f)

    try:
        with(open("Nonprocessed_Reviews.p", "rb")) as f:
            all_reviews = pickle.load(f)
    except:
        print("Nonprocessed_Reviews.p couldn't be found. All reviews will be loaded from txt files, this will take a fell minutes")
        all_reviews = []
        for dirpath, _, files in os.walk("./Reviews_corpus_buscape"):
            for filename in fnmatch.filter(files, '*.txt'):
                f = open(os.path.join(dirpath, filename), "r", encoding="utf8")
                review = f.read()
                # review = pre_processing_text(review, use_normalizer=True)
                all_reviews.append(review)
        with open("Nonprocessed_Reviews.p", "wb") as f:
            pickle.dump(all_reviews, f)

    portuguese_sent_tokenizer = nltk.data.load("tokenizers/punkt/portuguese.pickle")
    
    noun_words = {}
    aspects =[]

    for review in all_reviews:
        sentences = portuguese_sent_tokenizer.tokenize(review)
        tag_review = [tagger.tag(nltk.word_tokenize(sentence)) for sentence in sentences]
        for tag_sentence in tag_review:
            for tag in tag_sentence:
                if tag[1] == "NOUN":
                    word = pre_processing_text(tag[0])
                    if word in noun_words:
                        noun_words[word] += 1
                    else:
                        noun_words[word] = 1

    noun_words = sorted(noun_words.items(), key=lambda kv: kv[1])
    len_noun_words = len(noun_words)
    for i in range(int(len_noun_words*(1-frequency_cut)), len_noun_words):
        aspects.append(noun_words[i][0])
  
    aspects = list(set(aspects))
    if save:
        with open(os.path.join("Aspects_lexicon","noun_aspects.p"), "wb") as f:
            pickle.dump(aspects, f)
    return aspects



def create_aspects_lexicon_ontologies(save=False):
    """Create a list of the aspects indicated in the groups file"""
    explicit_aspects = []
    implicit_aspects = []
    with open("groups.xml", "r", encoding="utf8") as file:
        text = file.readlines()
        for line in text:
            if "Explicit" in line:
                for word in line.split(">")[1].split("<")[0].split(","):
                    explicit_aspects.append(pre_processing_text(word))
            elif "Implicit" in line:
                for word in line.split(">")[1].split("<")[0].split(","):
                    implicit_aspects.append(pre_processing_text(word))
    # Do some cleaning rules
    _explicit_aspects = []
    _implicit_aspects = []
    for aspect in explicit_aspects:
        if aspect != "s/n" and aspect != " . ":
            _explicit_aspects.append(aspect)
    for aspect in implicit_aspects:
        if aspect != "s/n" and aspect != " . ":
            _implicit_aspects.append(aspect)
    # Remove repetition on aspects list
    _explicit_aspects = list(set(_explicit_aspects))
    _implicit_aspects = list(set(_implicit_aspects))
    if save:
        with open(os.path.join("Aspects_lexicon","ontology_explicit_aspects.p"), "wb") as f:
            pickle.dump(_explicit_aspects, f)
        with open(os.path.join("Aspects_lexicon","ontology_implicit_aspects.p"), "wb") as f:
            pickle.dump(_implicit_aspects, f)

    return [_explicit_aspects, _implicit_aspects]


def create_aspects_lexicon_embeddings(seeds, seeds_type, number_synonym=3,save=False):

    aspects_list = []
    model = gensim.models.Word2Vec.load("word2vec.model")
    for word in seeds:
        aspects_list.append(word)
        if word in model.wv.vocab:
            out = model.wv.most_similar(positive=word, topn=number_synonym)  
            aspects_list.append(out[0][0].lower())
            aspects_list.append(out[1][0].lower())
            aspects_list.append(out[2][0].lower())
    aspects_list = list(set(aspects_list))
    if save:
        with open(os.path.join("Aspects_lexicon",seeds_type+"_embedding_aspects.p"), "wb") as f:
            pickle.dump(aspects_list, f)
    return aspects_list

def create_sentiment_words_lexicon(save=False):
    """Create a sentiment words list using LIWC lexicon"""
    sent_words = []
    sent_words_polarity = {}
    with open("liwc.txt", encoding="utf8") as f:
        text = f.readlines()
        for line in text:
            word = pre_processing_text(line.split()[0])
            if "126" in line:
                # Positive sentiment word
                sent_words.append(word)
                sent_words_polarity[word] = "+"
            elif "127" in line:
                sent_words.append(word)
                sent_words_polarity[word] = "-"
    # Remove duplicated words
    sent_words = list(set(sent_words))
    if save:
        with open(os.path.join("Sentiment_words","sent_words.p"), "wb") as f:
            pickle.dump(sent_words, f)
        with open(os.path.join("Sentiment_words","sent_words_polarity.p"), "wb") as f:
            pickle.dump(sent_words_polarity, f)

    return [sent_words, sent_words_polarity]



