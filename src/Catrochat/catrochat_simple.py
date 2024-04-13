import json
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


class CatrochatSimple:

    def __init__(self):
        self.nlp = spacy.load("en_core_web_md")
        with open('scraper-data/wiki_data.json') as f:
            self.data = json.load(f)
        # Extract text from data for TF-IDF vectorization
        self.document_texts = self.extract_text(self.data)
        # Preprocessing
        self.preprocessed_texts = [self.preprocess_text(text) for key, text in self.document_texts]
        # Initializing TF-IDF vectorizer
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = self.vectorizer.fit_transform(self.preprocessed_texts)

    def extract_text(self, data, parent_key=None):
        texts = []
        for key, value in data.items():
            current_key = parent_key + '/' + key if parent_key else key
            if isinstance(value, dict):
                texts.extend(self.extract_text(value, key))
            elif key == 'text':
                texts.append(("https://wiki.catrobat.org" + current_key.rsplit('/', 1)[0], value))
        return texts

    # Function to preprocess text data
    def preprocess_text(self, text):
        doc = self.nlp(text)
        tokens = [token.text.lower() for token in doc if
                  token.text.lower() not in self.nlp.Defaults.stop_words and token.text.isalpha()]
        return ' '.join(tokens)

    # TF-IDF
    def calculate_similarity(self, query):
        query = self.preprocess_text(query)
        query_tfidf = self.vectorizer.transform([query])
        similarity_scores = cosine_similarity(query_tfidf, self.tfidf_matrix)
        return similarity_scores.flatten()

    def find_most_similar_entry(self, query):
        similarity_scores = self.calculate_similarity(query)
        max_similarity_index = similarity_scores.argmax()
        if max_similarity_index < 0.15:
            return "Could not find any result for \"" + query + "\", please try again.", False
        return self.document_texts[max_similarity_index], True

    def find_multiple_similar_entries(self, query):
        similarity_scores = self.calculate_similarity(query)
        similarity_score_indices = np.argpartition(similarity_scores, -4)[-4:]
        top_four_similarities = dict()
        for index in similarity_score_indices:
            top_four_similarities[index] = similarity_scores[index]

        top_four_similarities = dict(sorted(top_four_similarities.items(), key=lambda x: x[1], reverse=True))

        top_four_texts = []
        for index in top_four_similarities.keys():
            top_four_texts.append(self.document_texts[index])

        return (top_four_texts)

    def recognize_intent(self, query):
        greetings_keywords = ["hello", "hi", "hey", "ola", "hola", "bonjour", "hallo"]
        help_keywords = ["help", "assist"]
        farewell_keywords = ["goodbye", "bye", "see you later", "baba"]

        if any(keyword in query.lower() for keyword in greetings_keywords):
            return "Hello! How can I help you today?"
        elif any(keyword in query.lower() for keyword in help_keywords):
            return "I'm here to help! What do you need help with?"
        elif any(keyword in query.lower() for keyword in farewell_keywords):
            return "Goodbye! See you soon!"
        else:
            return None

    def answer_user(self, user_query):
        most_similar_entries = []
        intent_response = self.recognize_intent(user_query)
        if intent_response:
            return intent_response
        else:
            most_similar_entry, found = self.find_most_similar_entry(user_query)
            if not found:
                return str(most_similar_entry) + "<br>"

            response = str(most_similar_entry[1]) + "<br>"
            response = response + "You can find additional info <a href = ' + str(most_similar_entry[0]) + '> here </a> <br>"

            most_similar_entries = self.find_multiple_similar_entries(user_query)
            if most_similar_entries:
                response = response + "__________________________________________________________________________________________________<br>"
                response = response + "Here are additional relevant search results for your question:<br>"
                counter = 0
                response = response + "<ul>"
                for similar_entry in most_similar_entries:
                    if counter > 0:
                        response = response + "<li>"
                        response = response + str(similar_entry[1]) + "<br>"
                        response = response + "<a href= ' + str(similar_entry[0]) + '> Details </a>"
                        response = response + "</li>"
                    counter = counter + 1
                    response = response + "</ul>"
                response = response + "__________________________________________________________________________________________________<br>"


            return response
