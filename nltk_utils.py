import numpy as np
import nltk
# nltk.download('punkt')
from nltk.stem.snowball import SwahiliStemmer
stemmer = SwahiliStemmer()


def tokenize(sentence):
    """
    split sentence into array of words/tokens
    a token can be a word or punctuation character, or number
    """
    return nltk.word_tokenize(sentence, language='sw')


def stem(word):
    """
    stemming = find the root form of the word
    examples:
    words = ["kuandaa", "kuanda", "kuandika"]
    words = [stem(w) for w in words]
    -> ["andaa", "anda", "andik"]
    """
    return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence, words):
    """
    return bag of words array:
    1 for each known word that exists in the sentence, 0 otherwise
    example:
    sentence = ["habari", "za", "jioni"]
    words = ["salamu", "habari", "mimi", "wewe", "kwaheri", "asante", "safi"]
    bog   = [  0 ,    1 ,    0 ,   0 ,      0 ,    0 ,      0]
    """
    # stem each word
    sentence_words = [stem(word) for word in tokenized_sentence]
    # initialize bag with 0 for each word
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words: 
            bag[idx] = 1

    return bag