sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

kod_soucastky = input("Zadajte kod součástky: ")
pozadovane_mnozstvi = int(input("Zadejte mnozstvi: "))


if kod_soucastky in sklad:
    if sklad[kod_soucastky] < pozadovane_mnozstvi:
        print(f"Součástky {kod_soucastky} lze prodat jen omezené množství {sklad[kod_soucastky]}.")
        sklad.pop(kod_soucastky)
    else:
        print(f"Poptávku lze uspokojit v plné výši.")
        sklad[kod_soucastky] -= pozadovane_mnozstvi
else:
    print(f"Zadaná součástky {kod_soucastky} nejsou skladem.")

# Bonus_01
morse_code = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-",
}

zadany_text = input("Zadejte text: ")

for znak in zadany_text:
    if znak in morse_code:
       print(morse_code[znak], end="")
    if znak == " ":
        print("/", end="")

# se druhym bonusem si vubec nevim rady