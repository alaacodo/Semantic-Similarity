import spacy

nlp = spacy.load('en_core_web_sm')

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

#similar words scored full mark
#banana and apple scored the highest score as they are both fruits
#cat and monkey second highest similarity as the both animals
#monkey and banana scored high similarity the module already aware that monkey eats banana
#cat and apple scored the lowest score 

