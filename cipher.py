cipher_dict = {
    "a": "f",
    "b": "g",
    "c": "h",
    "d": "i",
    "e": "j",
    "f": "k",
    "g": "l",
    "h": "m",
    "i": "n",
    "j": "o",
    "k": "p",
    "l": "q",
    "m": "r",
    "n": "s",
    "o": "t",
    "p": "u",
    "q": "v",
    "r": "w",
    "s": "x",
    "t": "y",
    "u": "z",
    "v": "a",
    "w": "b",
    "x": "c",
    "y": "d",
    "z": "e",
}
              
text = str(input("please enter a sentence:"))
text = text.lower()

cipher_text = ""
for c in text:
    if c in cipher_dict:
        c = cipher_dict[c]
    cipher_text += c

print("the sentence is:", text)
print("the encrypted sentence is:", cipher_text)
