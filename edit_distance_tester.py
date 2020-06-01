import edit_distance_helper as edh
import pandas as pd

# Get the Levenshtein distance for cat and cta
source = "Mountbatten"
target = "Mountain"
dis, matrix = edh.lev_distance(source, target)

# # print the edit distance
print("Levenshtein distance between {0} & {1} : ".format(source, target), dis)
# # print the matrix
print(matrix)


# Levenshtein distance using nltk library edit distance helper function
print(edh.nltk_edit_distance("apple", "appel"))  # 2 edit is required here


# The Damerau-Levenshtein distance allows transpositions (swap of two letters which are adjacent to each other) as well.
print(
    edh.nltk_edit_distance("apple", "appel", transpose=True)
)  # 1 edit is required if transpose is true


print(edh.nltk_edit_distance("Damerau", "Levenshtein", transpose=True))
