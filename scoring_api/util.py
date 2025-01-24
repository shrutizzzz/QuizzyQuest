import pickle
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from rake_nltk import Rake

# Initialize components
lemmatizer = WordNetLemmatizer()
rake = Rake()


# Load model data (only the data, not the functions)
def load_model_data():
    with open("subjective_scoring_model(1).pkl", "rb") as file:
        return pickle.load(file)


# Save model data (keyword_weights and default_weight only)
def save_model_data(keyword_weights, default_weight):
    with open("subjective_scoring_model(1).pkl", "wb") as file:
        pickle.dump({
            "keyword_weights": keyword_weights,
            "default_weight": default_weight
        }, file)


def break_phrases(phrases_list):
    words = []
    for phrase in phrases_list:
        if len(phrase.split()) == 1:
            words.append(phrase)
        else:
            words.extend(phrase.split())
    return words


def lemmatize(words_list):
    return list(map(lemmatizer.lemmatize, words_list))


def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    return synonyms


def score_answer(user_answer, keyword_weights, default_weight):
    max_score = 10

    # Extract keywords from the user answer
    rake.extract_keywords_from_text(user_answer)
    user_keywords = lemmatize(break_phrases(rake.get_ranked_phrases()))

    # Calculate the score
    score = 0
    for word in user_keywords:
        if word in keyword_weights:
            score += (keyword_weights[word] * max_score) / 100
        else:
            found = False
            for correct_word in keyword_weights:
                if word in get_synonyms(correct_word):
                    score += (keyword_weights.get(correct_word, default_weight) * max_score) / 100
                    found = True
                    break
            if not found:
                score += (default_weight * max_score) / 100

    # Cap the score at 10
    score = min(score, 10)
    return round(score, 2)
