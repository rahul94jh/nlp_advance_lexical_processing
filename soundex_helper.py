""" Below links are some good reads on Soundex """
# https://www.archives.gov/research/census/soundex
# https://www.legacyfamilytree.se/WEB_US/american_soundex_system.htm
# https://www.familysearch.org/wiki/en/Soundex
# https://www.avotaynu.com/soundex.htm
# https://stevemorse.org/phonetics/bmpm2.htm
# https://stevemorse.org/phonetics/bmpm.htm

""" Online soundex/bmpm phonetic generator """
# https://stevemorse.org/census/soundex.html
# https://www.ics.uci.edu/~dan/genealogy/Miller/javascrp/soundex.htm


def get_american_soundex_code(token: str) -> str:
    """[summary]
        Get the soundex code for the string
    Arguments:
        token {str} -- word of which the soundex code is required

    Returns:
        str -- soundex code for supplied string word
    """

    # Convert string to upper case
    token = token.upper()

    soundex = ""

    # first letter of input is always the first letter of soundex
    soundex += token[0]

    # create a dictionary which maps letters to respective soundex codes.
    # Vowels and 'H', 'W' and 'Y' will be represented by '.'
    char_code_map = get_soundex_char_map()

    # Generate the soundex code from the string using the char code mapper
    soundex = generate_soundex_code(token, char_code_map, soundex)

    # remove vowels and 'H', 'W' and 'Y' from soundex
    soundex = soundex.replace(".", "")

    # trim or pad to make soundex a 4-character code
    soundex = soundex[:4].ljust(4, "0")

    return soundex


def get_soundex_char_map():
    char_code_map = {
        "BFPV": "1",
        "CGJKQSXZ": "2",
        "DT": "3",
        "L": "4",
        "MN": "5",
        "R": "6",
        "AEIOUHWY": ".",
    }
    return char_code_map


def generate_soundex_code(token, char_code_map, soundex):
    for char in token[1:]:
        for key in char_code_map.keys():
            if char in key:
                code = char_code_map[key]
                if code != soundex[-1]:
                    soundex += code
    return soundex
