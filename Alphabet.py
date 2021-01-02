alef = u'\u05D0'
bet = u'\u05D1'
gimel = u'\u05D2'
dalet = u'\u05D3'
he = u'\u05D4'
vav = u'\u05D5'
zayin = u'\u05D6'
het = u'\u05D7'
tet = u'\u05D8'
yud = u'\u05D9'
final_kaf = u'\u05DA'
kaf = u'\u05DB'
lamed = u'\u05DC'
final_mem = u'\u05DD'
mem = u'\u05DE'
final_nun = u'\u05DF'
nun = u'\u05E0'
samekh = u'\u05E1'
ayin = u'\u05E2'
final_pe = u'\u05E3'
pe = u'\u05E4'
final_tsadi = u'\u05E5'
tsadi = u'\u05E6'
qof = u'\u05E7'
resh = u'\u05E8'
shin = u'\u05E9'
tav = u'\u05EA'

character_dictionary = {
    'l': lamed,
    'b': bet,
    'v': vav,
    'a': alef,
    'A': ayin,
    'g': gimel,
    'd': dalet,
    'h': he,
    'z': zayin,
    'c': het,
    't': tet,
    'r': resh,
    'y': yud,
    'k': kaf,
    'K': final_kaf,
    'm': mem,
    'M': final_mem,
    'n': nun,
    'N': final_nun,
    'S': samekh,
    'p': pe,
    'P': final_pe,
    'x': tsadi,
    'X': final_tsadi,
    'q': qof,
    's': shin,
    'T': tav,
    ' ': ' '
}

def convert_character_to_hebrew(character):
    if character not in character_dictionary:
        return ''
    return character_dictionary[character]