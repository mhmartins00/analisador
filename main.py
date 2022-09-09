from functions import *

line_count = 0 # Numerador da linhas
arquivo = open("./texTo.txt", 'r', encoding='utf-8')
dados = arquivo.read()
linhas = dados.splitlines()
identified = 0

file_token = open("./token.txt", "w", encoding='utf-8')
file_error = open("./error.txt", "w", encoding='utf-8')
file_symbol = open("./symbol.txt", "w", encoding='utf-8')

token_list = []
for word in linhas:
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
    else:
        message = (f"[{line_count}] ({word})")
        print(message)
        file_error.write(message + "\n")