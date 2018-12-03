import pandas as pd

df_ontology = pd.read_csv("output_ontology_aspects.txt")
df_ontology_embedding = pd.read_csv("output_ontology_embedding_aspects.txt")
df_noun = pd.read_csv("output_noun_aspects.txt")
df_noun_embedding = pd.read_csv("output_noun_embedding_aspects.txt")

print(df_noun_embedding.describe())