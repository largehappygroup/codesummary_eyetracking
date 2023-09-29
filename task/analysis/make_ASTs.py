import os
import re
import copy
import pickle
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup, Tag
from difflib import SequenceMatcher



pointless = {',': 0,   '(': 0,   ')': 0, '()': 0,  '{': 0,   '}': 0, ');': 0,
             '),': 0, '));': 0,  '];': 0,  '[': 0,  ']': 0,  '))': 0, '){': 0,
             ';': 0,  ');': 0, '});': 0, '};': 0, '((': 0, ')){': 0, ')[': 0,
             '))));': 0, ')))': 0,  ')(': 0,  '.': 0,   '[': 0, }


def helper_for_comments(func_name, parent, node, ogtree):
    tokens = function_tokens[func_name]  # list of tokens
    for t in tokens:
        ratio = SequenceMatcher(a=node, b=t).ratio()
        if ratio > 0.6 and t != node:
            try:
                k = ogtree[parent].index(node)
                ogtree[t] = ogtree[node]
                ogtree[parent][k] = t
            except:
                x = 5
            # idx = tokens.index(t)
            # function_tokens[func_name][idx] = node


def node_correction(func_name, parent, subtree, tree, ogtree):
    for node in subtree:
        if parent:
            new_node = node
            if re.search('null', node):
                new_node = re.sub('null', 'nan', node)
            elif re.search('true', node):
                new_node = re.sub('true', 'TRUE', node)
            elif re.search('false', node):
                new_node = re.sub('false', 'FALSE', node)
            if new_node != node and ogtree[parent][0] != new_node:
                k = ogtree[parent].index(node)
                ogtree[new_node] = ogtree[node]
                ogtree[parent][k] = new_node

        if re.search(r"\/\/", node):
            helper_for_comments(func_name, parent, node, ogtree)
        else:
            for child in tree[node]:
                node_correction(func_name, child, tree[child], tree, ogtree)


def tree_walk(root, tag, parent):
    global tree, occurrences, count

    if isinstance(tag, Tag):
        parent = f"{tag.name}.{count-1}"
        if parent not in tree:
            tree[parent] = []
        for child in tag.children:
            if child.name:
                tree[parent].append(f"{child.name}.{count}")
                count += 1
            tree_walk(root, child, parent)

    elif tag:
        tag = tag.strip()
        if tag and tag not in pointless:
            if tag not in occurrences:
                if re.search(r"\/\/", tag):
                    occurrences[tag] = 200
                elif re.search(r"\".+\s+.+\"", tag):
                    occurrences[tag] = 100
                else:
                    occurrences[tag] = 0
            else:
                occurrences[tag] += 1
            leaf = f"{tag}.{occurrences[tag]}"
            tree[parent].append(leaf)
            tree[leaf] = []

function_tokens = {}
annotated_path = "./fully_annotated"
annotated_files = os.listdir(annotated_path)
for file in annotated_files:
    name = re.sub(".csv", "", file)
    annotated = pd.read_csv(f"{annotated_path}/{file}")
    tokens = annotated['word'].astype(
        str)+"."+annotated['occurrence'].astype(str)
    function_tokens[name] = list(tokens)

# with open("midprocessing/function_tokens.pkl", "wb") as f:
#     pickle.dump(function_tokens, f)


filepath = './xml_trees'
tree_files = os.listdir(filepath)
trees = {}
for trunk in tree_files:
    count = 1
    tree = {}
    occurrences = {}
    name = re.sub("_wrapped.xml", "", trunk)

    with open(f'{filepath}/{trunk}', 'r') as f:
        data = f.read()

    soup = BeautifulSoup(data, features="xml")
    soup = soup.find('function')

    tree_walk(root=soup, tag=soup, parent='root')
    trees[name] = tree

for key in trees.keys():
    ogtree = copy.deepcopy(trees[key])
    node_correction(key, None, trees[key], trees[key], ogtree)
    trees[key] = ogtree

# with open(f"midprocessing/ASTs.pkl", "wb") as f:
#     pickle.dump(trees, f)
