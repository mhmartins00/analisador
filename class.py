#encoding: utf-8


from asyncio.windows_events import NULL
from contextlib import nullcontext


def VerifyHaveSpace(word): 
    if ' ' in word:
        # print("A palavra possui espaco")
        return bool(1)
    else:
        # print("A palavra não tem espaço")
        return bool(0)


def VerifyComment(word): #Corrigir: Se o primeiro caracter da string for um espaço em branco e os próximos forem // considera-se não comentario
    if word == '':
        return bool(0)
    first = word[0]
    if first == '/':
        if word[1] == first:
            # print("Este trecho é um comentário")
            return bool(1)
        else:
            # print("Este trecho possui apenas uma '/' ou possui espaco entre as '/' ")
            return bool(0)
    else:
        # print("Este trecho não é um comentario")
        return bool(0)


def VerifyReservedWord(word): #Corrigir: Se houver espaço no inicio ou no fim da palavra considera-se não reservada
    reservedWords = ['int', 'double', 'float', 'real', 'break', 'case','char', 'const', 'continue']
    if word in reservedWords:
        # print("Essa é uma palavra reservada")
        return bool(1)
    else:
        # print("Essa não é uma palavra reservada")
        return bool(0)


def VerifyNumFloat(word):
    limit = 99.99
    size = len(word)
    if size <= 5:
        position = word.find('.') # Funcao find retorna a posicao de um caracter na string
        # print(f"Esta é a posição do ponto: {position}")
        tmp = len(word[position:position+3])
        if tmp < 3:
            # print("Este número real não possui duas casas decimais")
            return bool(0)
        else:
            if VerifyIsNumOrStr(word) == float:
                word = float(word)
                if word <= limit:
                    # print("Este número real é aceito")
                    return bool(1)
                else:
                    # print("Este número real não é aceito")
                    return bool(0)
            else:
                # print("Este número real não é aceito")
                return bool(0)
    else:
        # print("Este número possui mais que duas casas decimais")
        return bool(0)
 

def VerifyIdentifier(word):
    if word == '':
        return bool(0)
    first = word[0]
    numbers = ['0','1','2','3','4','5','6','7','8','9'] 
    # special_characters = [".",'"',"'",'!','@', '#', '$', '%', '¨', '&', '*', "(", ')', '[', ']', '{','}', '+', '-', '=','´', '`', ',','<', '>', ';', ':','/','?', '^', '~', "|", ]
    accepted_characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
    for i in word:
        if i not in accepted_characters:
            return bool(0)
    if first in numbers:
        # print(f"{word} não é um identificador valido 88")
        return bool(0)
    # elif word.__contains__(".", "L"):
    #     return bool(0)
    else:
        if VerifyReservedWord(word) == False and VerifyHaveSpace(word) == False:
            # print(f"{word} é um identificador válido")
            return bool(1)
        else:
            # print(f"{word} não é um identificador valido 99")
            return bool(0)


def VerifyIsNumInt(word):
    limit=99
    size = len(word)
    if VerifyIsNumOrStr(word) == int:
        word = int(word)
        if size <= 2:
            if word <= limit:
                # print("Este número inteiro é aceito")
                return bool(1)
            else:
                # print("Este número inteiro não é aceito")
                return bool(0)
        else:
            return bool(0)
    else:
        return bool(0)


def VerifyIsNumOrStr(word):
    if word.isdigit() == True:
        wordt=int(word)
        # print(f"{word} é um número inteiro")
        return type(wordt)
    else:
        try:
            wordt=float(word)
            # print(f"{word} é um numero float")
            return type(wordt)
        except ValueError:
            # print(f"{word} é uma string")
            return type(word)


def MainFunctionVerify(word):
    if VerifyComment(word):
        tkn = ("comment")
        return tkn
    elif VerifyReservedWord(word):
        tkn = ("reserved")
        return tkn
    elif VerifyIdentifier(word):
        tkn = ("identify")
        return tkn
    elif VerifyNumFloat(word):
        tkn = ("real")
        return tkn
    elif VerifyIsNumInt(word):
        tkn = ("int")
        return tkn
    else:
        tkn = ("error")
        return tkn
        


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

# VerifyHaveSpace(palavra)
# VerifyComment(palavra)
# VerifyReservedWord(palavra)
# VerifyNumFloat(palavra)
# VerifyIdentifier(palavra)
# VerifyIsNumInt(palavra)
# VerifyIsNumOrStr(palavra)
