import gensim
import numpy as np
import os
import pickle
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


def process_reviews():
	all_reviews = np.load("Nonprocessed_Reviews.npy")

	for i in range(len(all_reviews)):
		all_reviews[i] = pre_processing_text(all_reviews[i], use_normalizer=True)

	with open("Processed_Reviews.p", "wb") as f:
		all_reviews = pickle.dump(f)


all_tokenized_reviews = []
with(open("Processed_Reviews.p", "rb")) as f:
	all_reviews = pickle.load(f)
for review in all_reviews:
	tokenized_review = gensim.utils.simple_preprocess(review)
	all_tokenized_reviews.append(tokenized_review)

model = gensim.models.Word2Vec(all_tokenized_reviews, size=600, window=7, min_count=1, workers=4)
model.train(all_tokenized_reviews, total_examples=len(all_tokenized_reviews), epochs=900)
model.save("word2vec.model")



