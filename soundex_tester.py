import soundex_helper as sh

# Let's see the code generation for different versions of Mumbai
# WE see the numeric code is same of all variants
print(sh.get_american_soundex_code("bombay"))
print(sh.get_american_soundex_code("bombai"))
print(sh.get_american_soundex_code("Mumbai"))
print(sh.get_american_soundex_code("Mumbay"))
print(sh.get_american_soundex_code("Mumbaii"))

# All variants got assigned same soundex code
print(sh.get_american_soundex_code("aggrawal"))
print(sh.get_american_soundex_code("agrawal"))
print(sh.get_american_soundex_code("aggrwal"))
print(sh.get_american_soundex_code("aggarwal"))

print(sh.get_american_soundex_code("gud"))
print(sh.get_american_soundex_code("gd"))

# some issues or the false hits with soundex code converter
# both good and god assigned same code though they are not the same in meaning
print(sh.get_american_soundex_code("good"))
print(sh.get_american_soundex_code("god"))

# sun and son get the same code
print(sh.get_american_soundex_code("sun"))
print(sh.get_american_soundex_code("son"))

# here too, Samir & Samira got same code
print(sh.get_american_soundex_code("samir"))
print(sh.get_american_soundex_code("samira"))

""" For such cases we can rely on Beider-Morse Approximate/Exact Phonetic Tokens
 which can differentiate based on phonetic token """
# https://stevemorse.org/census/soundex.html
