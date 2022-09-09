#encoding: utf-8

def VerifyHaveSpace(word): 
    if ' ' in word:
        return bool(1)
    else:
        return bool(0)


def VerifyComment(word): #Corrigir: Se o primeiro caracter da string for um espaço em branco e os próximos forem // considera-se não comentario
    if word == '':
        return bool(0)
    first = word[0]
    if first == '/':
        if word[1] == first:
            return bool(1)
        else:
            return bool(0)
    else:
        return bool(0)


def VerifyReservedWord(word): #Corrigir: Se houver espaço no inicio ou no fim da palavra considera-se não reservada
    reservedWords = ['int', 'double', 'float', 'real', 'break', 'case','char', 'const', 'continue']
    if word in reservedWords:
        return bool(1)
    else:
        return bool(0)


def VerifyNumFloat(word):
    limit = 99.99
    size = len(word)
    if size <= 5:
        position = word.find('.') # Funcao find retorna a posicao de um caracter na string
        tmp = len(word[position:position+3])
        if tmp < 3:
            return bool(0)
        else:
            if VerifyIsNumOrStr(word) == float:
                word = float(word)
                if word <= limit:
                    return bool(1)
                else:
                    return bool(0)
            else:
                return bool(0)
    else:
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
        return bool(0)
    else:
        if VerifyReservedWord(word) == False and VerifyHaveSpace(word) == False:
            return bool(1)
        else:
            return bool(0)


def VerifyIsNumInt(word):
    limit=99
    size = len(word)
    if VerifyIsNumOrStr(word) == int:
        word = int(word)
        if size <= 2:
            if word <= limit:
                return bool(1)
            else:
                return bool(0)
        else:
            return bool(0)
    else:
        return bool(0)


def VerifyIsNumOrStr(word):
    if word.isdigit() == True:
        wordt=int(word)
        return type(wordt)
    else:
        try:
            wordt=float(word)
            return type(wordt)
        except ValueError:
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
        


# line_count = 0 # Numerador da linhas
# arquivo = open("./texTo.txt", 'r', encoding='utf-8')
# dados = arquivo.read()
# linhas = dados.splitlines()
# identified = 0

# file_token = open("./token.txt", "w", encoding='utf-8')
# file_error = open("./error.txt", "w", encoding='utf-8')
# file_symbol = open("./symbol.txt", "w", encoding='utf-8')

# token_list = []
# for word in linhas:
#     line_count = line_count + 1 
#     token = MainFunctionVerify(word)
#     if token == "comment":
#         message = (f"[{line_count}] COMENTARIO")
#         print(message)
#         file_token.write(message + "\n")
#     elif token == "reserved":
#         message = (f"[{line_count}] {word.upper()}")
#         print(message)
#         file_token.write(message + "\n")
#     elif token == "identify":
#         if word in token_list:
#             message = (f"[{line_count}] IDENTIFICADOR {token_list.index(word)+1}")
#             print(message)
#             file_token.write(message + "\n")
#         else:
#             identified+=1
#             message = (f"[{line_count}] IDENTIFICADOR {identified}")
#             print(message)
#             token_list.append(word)
#             file_token.write(message + "\n")
#             symbol_message = (f"{token_list.index(word)+1} - {word}")
#             file_symbol.write(symbol_message + "\n")
#     elif token == "real":
#         if word in token_list:
#             message = (f"[{line_count}] NUMERO REAL {token_list.index(word)+1}")
#             print(message)
#             file_token.write(message + "\n")
#         else:
#             identified+=1
#             message = (f"[{line_count}] NUMERO REAL {identified}")
#             print(message)
#             token_list.append(word)
#             file_token.write(message + "\n")
#             symbol_message = (f"{token_list.index(word)+1} - {word}")
#             file_symbol.write(symbol_message + "\n")
#     elif token == "int":
#         if word in token_list:
#             message = (f"[{line_count}] NUMERO INTEIRO {token_list.index(word)+1}")
#             print(message)
#             file_token.write(message + "\n")
#         else:
#             identified+=1
#             message = (f"[{line_count}] NUMERO INTEIRO {identified}")
#             print(message)
#             token_list.append(word)
#             file_token.write(message + "\n")
#             symbol_message = (f"{token_list.index(word)+1} - {word}")
#             file_symbol.write(symbol_message + "\n")
#     else:
#         message = (f"[{line_count}] ({word})")
#         print(message)
#         file_error.write(message + "\n")

# VerifyHaveSpace(palavra)
# VerifyComment(palavra)
# VerifyReservedWord(palavra)
# VerifyNumFloat(palavra)
# VerifyIdentifier(palavra)
# VerifyIsNumInt(palavra)
# VerifyIsNumOrStr(palavra)
