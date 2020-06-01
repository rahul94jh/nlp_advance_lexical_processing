# import library
from nltk.metrics.distance import edit_distance
import pandas as pd

""" The levenshtein distance calculates the number of steps (insertions, deletions or substitutions) 
required to go from source string to target string. """

# http://www.let.rug.nl/~kleiweg/lev/


def lev_distance(source: str = "", target: str = "") -> (int, pd.DataFrame):
    """[summary]
        Make a Levenshtein Distances Matrix
    Keyword Arguments:
        source {str} -- source string (default: {""})
        target {str} -- target string (default: {""})

    Returns:
        (int,pd.DataFrame) -- tuple containing edit distance and the edit matrix
    """
    # get length of both strings
    n1, n2 = len(source), len(target)

    # create matrix using length of both strings - source string sits on columns, target string sits on rows
    matrix = [[0 for i in range(n1 + 1)] for j in range(n2 + 1)]

    # fill the first row - (0 to n1-1)
    for i in range(1, n1 + 1):
        matrix[0][i] = i

    # fill the first column - (0 to n2-1)
    for j in range(1, n2 + 1):
        matrix[j][0] = j

    # fill the matrix
    for j in range(1, n2 + 1):
        for i in range(1, n1 + 1):

            # check whether letters being compared are same
            if source[i - 1] == target[j - 1]:
                value = matrix[j - 1][i - 1]  # top-left cell value
            else:
                value = min(
                    matrix[j - 1][i] + 1,  # left cell value     + 1
                    matrix[j][i - 1] + 1,  # top cell  value     + 1
                    matrix[j - 1][i - 1] + 1,
                )  # top-left cell value + 1

            matrix[j][i] = value

    # return bottom-right cell value
    return matrix[-1][-1], pd.DataFrame(matrix)


def nltk_edit_distance(
    source: str = "", target: str = "", transpose: bool = False
) -> int:

    """[summary]
        Levenshtein & Damerau-Levenshtein Distancein using nltk library
    Keyword Arguments:
        source {str} -- source string to ba analysed (default: {""})
        target {str} -- target string to ba analysed  (default: {""})
        transpose {bool} -- Whether to allow transposition edits (default: {False})

    Returns:
        [int] -- edit distance between target and source string
    """
    return edit_distance(source, target, transpositions=transpose)
