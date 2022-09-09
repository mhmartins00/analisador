from main_functions import *

line_count = 0 # Numerador da linhas
identified = 0 # Identificador dos tokens

file = open("./input/texto.txt", 'r', encoding='utf-8')
data = file.read()
lines = data.splitlines()
token_list = []

file_token = open("./output/token.txt", "w", encoding='utf-8')
file_error = open("./output//error.txt", "w", encoding='utf-8')
file_symbol = open("./output//symbol.txt", "w", encoding='utf-8')


for word in lines:
    line_count = line_count + 1 
    token = MainFunctionVerify(word)
    if token == "comment":
        message = (f"[{line_count}] COMENTARIO")
        print(message)
        file_token.write(message + "\n")
    elif token == "reserved":
        message = (f"[{line_count}] {word.upper()}")
        print(message)
        file_token.write(message + "\n")
    elif token == "identify":
        if word in token_list:
            message = (f"[{line_count}] IDENTIFICADOR {token_list.index(word)+1}")
            print(message)
            file_token.write(message + "\n")
        else:
            identified+=1
            message = (f"[{line_count}] IDENTIFICADOR {identified}")
            print(message)
            token_list.append(word)
            file_token.write(message + "\n")
            symbol_message = (f"{token_list.index(word)+1} - {word}")
            file_symbol.write(symbol_message + "\n")
    elif token == "real":
        if word in token_list:
            message = (f"[{line_count}] NUMERO REAL {token_list.index(word)+1}")
            print(message)
            file_token.write(message + "\n")
        else:
            identified+=1
            message = (f"[{line_count}] NUMERO REAL {identified}")
            print(message)
            token_list.append(word)
            file_token.write(message + "\n")
            symbol_message = (f"{token_list.index(word)+1} - {word}")
            file_symbol.write(symbol_message + "\n")
    elif token == "int":
        if word in token_list:
            message = (f"[{line_count}] NUMERO INTEIRO {token_list.index(word)+1}")
            print(message)
            file_token.write(message + "\n")
        else:
            identified+=1
            message = (f"[{line_count}] NUMERO INTEIRO {identified}")
            print(message)
            token_list.append(word)
            file_token.write(message + "\n")
            symbol_message = (f"{token_list.index(word)+1} - {word}")
            file_symbol.write(symbol_message + "\n")
    elif token == "empty":
        message = (f"[{line_count}] PALAVRA VAZIA")
        print(message)
        file_token.write(message + "\n")
    else:
        message = (f"[{line_count}] ({word})")
        print(message)
        file_error.write(message + "\n")
