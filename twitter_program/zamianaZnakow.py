import string


def odkoduj(tekst):
    polskie = {"Ą": "A", "Ć": "C",
               "Ę": "E", "Ł": "L", "Ń": "N", "Ó": "O",
               "Ś": "S", "Ź": "Z", "Ż": "Z", "ą": "a",
               "ć": "c", "ę": "e", "ł": "l", "ń": "n",
               "ó": "o", "ś": "s", "ż": "z", "ź": "z"}
    for x in polskie.keys():
        tekst = tekst.replace(x, polskie[x])
    return tekst
