import gensim
import numpy as np
import os
import pickle
import fnmatch
from enelvo import normaliser

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


all_tokenized_reviews = []

try:
    with(open("Processed_Reviews.p", "rb")) as f:
        all_reviews = pickle.load(f)
except:
    print("Processed_Reviews.p couldn't be found. All reviews will be loaded from txt files, this will take a fell minutes")
    all_reviews = []
    for dirpath, _, files in os.walk("./Reviews_corpus_buscape"):
        for filename in fnmatch.filter(files, '*.txt'):
            f = open(os.path.join(dirpath, filename), "r", encoding="utf8")
            review = f.read()
            review = pre_processing_text(review, use_normalizer=True)
            all_reviews.append(review)
    with open("Processed_Reviews.p", "wb") as f:
        pickle.dump(all_reviews, f)

for review in all_reviews:
	tokenized_review = gensim.utils.simple_preprocess(review)
	all_tokenized_reviews.append(tokenized_review)

model = gensim.models.Word2Vec(all_tokenized_reviews, size=600, window=7, min_count=1, workers=4)
model.train(all_tokenized_reviews, total_examples=len(all_tokenized_reviews), epochs=900)
model.save("word2vec.model")
