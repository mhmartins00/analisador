def VerifySpace(word):
    if ' ' in word:
        print("A palavra possui espaco")
    else:
        print("A palavra não tem espaço")


def VerifyComment(word):
    first = word[0]
    if first == '/':
        if first == word[1]:
            print("Este trecho é um comentário")
        else:
            print("Este trecho possui apenas uma '/' ou possuí espaco entre as '/' ")
    else:
        print("Este trecho não é um comentario")


def VerifyReservedWord(word):
    reservedWords = ['int', 'double', 'float', 'real', 'break', 'case','char', 'const', 'continue']
    if word in reservedWords:
        print("Essa é uma palavra reservada")
    else:
        print("Essa não é uma palavra reservada")

def VerifyNumFloat(word):
    limit = 99.99
    size = len(word)
    if size < 6:
        position = word.find('.') # Funcao find retorna a posicao de um caracter na string
        # print(f"Esta é a posição do ponto: {position}")
        tmp = len(word[position:position+3])
        if tmp < 3:
            print("Este número real não possui duas casas decimais")
           
        else:
            word = float(word)
            if word <= limit:
                print("Este número real é aceito")
            else:
                print("Este número real não é aceito")
    else: 
        print("Este número possuí mais que duas casas decimais")












nome = 'char'
num = '99.4'
# VerifySpace(nome)
# VerifyComment(nome)
# VerifyReservedWord(nome)
VerifyNumFloat(num)

   