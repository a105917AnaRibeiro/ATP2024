#tpc1
#alínea a)

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]  
ncomuns = [x for x in lista1 if x not in lista2] + [x for x in lista2 if x not in lista1]

#alínea b)

texto = """Vivia há já não poucos anos algures num concelho do Ribatejo 
    um pequeno lavrador e negociante de gado chamado Manuel Peres Vigário"""
lista = [palavra for palavra in texto.split() if len(palavra)>3]
# Resultado esperado: ['Vivia', 'poucos', 'anos', 'algures', 'concelho', ...]

#alínea c)
lista = ['anaconda', 'burro', 'cavalo', 'macaco']
listaRes = [(i+1, valor) for i, valor in enumerate(lista)]
# Resultado esperado: [(1,'anaconda'), (2,'burro'), (3,'cavalo'), (4,'macaco')]

#tpc2
# a)

def strCount(s, subs):
    count=1
    i=0
    while i<=len(s)-len(subs):
        if s[i:i+len(subs)==subs]:
            count+=1
            i+=len(subs)
        else:
            i+=1
    return count

strCount("catcowcat", "cat") # --> 2
strCount("catcowcat", "cow") # --> 1
strCount("catcowcat", "dog") # --> 0

#b)

def produtoM3(lista):
    lista_ordenada=sorted(lista)
    return lista_ordenada[0]*lista_ordenada[1]*lista_ordenada[2]

print(produtoM3([12,3,7,10,12,8,9]))
# Resultado esperado: 168 = 3 * 7 * 8

#c)

# Input: 38
# Output: 2
# Explicação: 3 + 8 = 11, 1 + 1 = 2.

# Input: 777
# Output: 3
# Explicação: 7 + 7 + 7 = 21, 2 + 1 = 3.

def reduxInt(n):
    while n>=10:
        n=sum(int(digito) for digito in str(n))
    return n

#d)

# Invocação: indexOf("Hoje está um belo dia de sol!", "belo")
# Resultado: 13

# Invocação: indexOf("Hoje está um belo dia de sol!", "chuva")
# Resultado: -1

def myIndexOf(s1, s2):
    len1, len2 = len(s1), len(s2)
    for i in range(len1-len2+1):
        if s1[i:i+len2]==s1:
            return i
    return -1

#tpc3
# Chamando a função para obter a lista de autores

#a)

def quantosPost(rede_social):
    return rede_social

#b) 

def postsAutor(rede_social, autor):
    return[post for post in rede_social if post['autor']==autor]

#c)
def autores(rede_social):
    autores_lista=[post['autor'] for post in rede_social]
    return sorted(set(autores_lista))

#d)
def insPost(redeSocial, conteudo, autor, dataCriacao, comentarios):
    id_existe=[int(post['id'][1:]) for post in redeSocial]
    id_novo='p'+str(id_existe+1) if id_existe else 'p1'
    novo_post = {
        'id': id_novo,
        'conteudo': conteudo,
        'autor': autor,
        'dataCriacao': dataCriacao,
        'comentarios': comentarios}
    redeSocial.append(novo_post)
    return redeSocial

#e)
def remPost(redeSocial, id):
    for post in redeSocial:
        if post['id']==id:
            redeSocial.remove(post)
            break
    return redeSocial

#f)
def postsPorAutor(redeSocial):
    distribuicao={}
    for post in redeSocial:
        autor=post['autor']
        if autor in distribuicao:
            distribuicao[autor] += 1
        else:
            distribuicao[autor] -= 1
    return distribuicao

#g)
posts_comentados=[]
def comentadoPor(redeSocial, autor):
    for post in redeSocial:
        for comentario in post['comentários:']:
            if comentario['autor']==autor:
                posts_comentados.append(post)
                break

    return posts_comentados

