import os
import re
import nltk
import copy
import pickle
import numpy as np
import pandas as pd
import seaborn as sns
import networkx as nx
import scipy.stats as stats
from scipy.stats import shapiro
from collections import Counter
from bs4 import BeautifulSoup, Tag
from difflib import SequenceMatcher
from scipy.stats import mannwhitneyu
from matplotlib import pyplot as plt
from nltk.probability import FreqDist
from collections import defaultdict, deque
from statistics import mean, variance, median
from sklearn.cluster import AgglomerativeClustering
from scipy.spatial.distance import pdist, squareform
from nltk.collocations import BigramCollocationFinder
from Levenshtein import distance as levenshtein_distance
from sklearn.feature_extraction.text import CountVectorizer


with open("midprocessing/reading_scanpaths.pkl", "rb") as f:
    rscan_paths = pickle.load(f)
with open("midprocessing/writing_scanpaths.pkl", "rb") as f:
    wscan_paths = pickle.load(f)
with open("midprocessing/participant_scanpaths.pkl", "rb") as f:
    participant_scanpaths = pickle.load(f)
with open("midprocessing/reading_functions.pkl", "rb") as f:
    reading_functions = pickle.load(f)
with open("midprocessing/writing_functions.pkl", "rb") as f:
    writing_functions = pickle.load(f)
# with open("midprocessing/abstract_code_parts.pkl", "rb") as f:
with open("midprocessing/abstract_code_parts_by_precedence.pkl", "rb") as f:
    abstract_code_parts = pickle.load(f)


def filter_duplicates(array):
    if len(set(array)) == len(array):
        return array
    else:
        return -1


def calculate_tuples(func, scan_paths, n):
    code_parts = abstract_code_parts[func]
    ngrams = []  # first calculating ngrams of the raw code, then abstracting later
    for path in scan_paths:  # figuring out if we need to handle bigrams or trigrams
        if n == 2:
            ngrams.extend(list(nltk.bigrams(path)))
        elif n == 3:
            ngrams.extend(list(nltk.trigrams(path)))

    # replace each tuple with a list of its abstract code parts ([variable declaration])
    # input: ['variable_1', 'String']
    # output: [['variable', 'variable declaration'], ['parameter', 'type']]
    abstract_tuples = []
    for i, tupl in enumerate(ngrams):
        abstract_tuple = []
        for token in tupl:
            # print(len(tupl), tupl[0], tupl[1])
            temp = code_parts[token]
            try:
                abstract_tuple = abstract_tuple + temp
            except:
                meaningless = 0

        abstract_tuple = filter_duplicates(abstract_tuple)
        if abstract_tuple != -1:
            abstract_tuple = tuple(abstract_tuple)
            # with the abstracted, nested list, permute to get ngrams again
            # input: [['variable', 'variable_declaration'], ['parameter', 'type']]
            # output: ngrams
            # new_tuples = permute(abstract_tuple)
            # print(tuple(abstract_tuple))
            abstract_tuples.append(abstract_tuple)
            # print("tuples", abstract_tuples)

    return abstract_tuples


# Level 1
# takes in scan paths, formatted as:
# {'function1': [['scan','path', '1'], ['scan', 'path', '2']]}
# {'function2': [['scan','path', '1'], ['scan', 'path', '2']]}
# returns abstract bigrams and trigrams for each function
def calculate_ngrams(scan_paths):
    all_bigrams = []
    all_trigrams = []
    for func in scan_paths.keys():  # iterating through all the keys/functions in the dictionary
        bigrams = calculate_tuples(func, scan_paths[func], 2)
        trigrams = calculate_tuples(func, scan_paths[func], 3)
        all_bigrams.extend(bigrams)
        all_trigrams.extend(trigrams)

    return all_bigrams, all_trigrams


qwer = set()


def format_bigrams(grams):
    replacing = {
        'function call': 'Method Call',
        'loop': 'Loop Body',
        'conditional block': 'Conditional Body',
        'conditional statement': 'Conditional Statement',
        'parameter': 'Parameter',
        'variable': 'Variable',
        'variable declaration': 'Variable Declaration',
        'argument': 'Argument',
        'function declaration': 'Method Declaration'
    }

    label = ''
    for i, g in enumerate(grams):
        new_gram = replacing[g]
        # print(new_gram)
        label += f"{new_gram} \u2192 " if i < len(grams)-1 else new_gram
    return label
    # print(label)

    # input is a tuple
    # function declaration --> method declaration
    # loop --> loop body
    # function call --> method call
    # conditional block --> conditional body
    # externally defined variable or function --> external class
