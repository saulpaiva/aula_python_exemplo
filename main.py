meme_dict = {
            "CRINGE": "Algo vergonhoso ou constrangedor",
            "STALKEAR": "Investigar a vida de alguém online",
            }

word = input("Digite uma palavra moderna que você não entende (escreva todo a palavra em letras maiúsculas): ")


if word in meme_dict.keys():
    # O que devemos fazer se a palavra for encontrada?
    print("Esta palavra já existe! Tente outra")
else:
    # O que devemos fazer se a palavra não for encontrada?
    significado = input("Digite o significado:")
    meme_dict[word] = significado
    print(meme_dict)
