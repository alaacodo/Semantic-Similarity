# import spacy
import spacy
# This will return a Language object containing all components and data needed to process text.
nlp = spacy.load("en_core_web_md")

# movie description to comapare with
movie_x = ('''Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator.''')
movies = []
file = open("movies.txt", "r")
for line in file:
    file_strip = line.strip("\n")
    movies.append(file_strip)

model_sentence = nlp(movie_x)

similarity_list = []
for sentence in movies:
    similarity = nlp(sentence).similarity(model_sentence)
    similarity_list.append(similarity)
    


max_value = (max(similarity_list))
index = similarity_list.index(max_value)


print(f"Next Movie Recommended to Watch: {movies[index]}")