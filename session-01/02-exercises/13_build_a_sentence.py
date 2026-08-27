adjective_1 = input("Skriv inn et adjektiv: ")
adjective_2 = input("Skriv inn enda et adjektiv: ")
noun = input("Skriv et substantiv: ")
verb = input("Skriv et verb: ")

sentence = f"""
Å øve på python er så gøy,
sa en {adjective_1} og {adjective_2}
student, som tenkte å kjøpe seg
{noun} når han er ferdig med å {verb}.
"""

print(sentence)