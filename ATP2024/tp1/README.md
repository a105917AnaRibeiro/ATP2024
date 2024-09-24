# relatório do tp1
## Data: 17/09/2024
## Autor: a105917 Ana Ribeiro 
## Resumo

O tp1 consistiu na realização de dois excercícios:
*resolver o exercício 10 do maze

-Senti algumas dificuldades na realização deste exercício, pelas várias opções de caminhos que existiam, o que tornou o execício bastante complexo. Foi necessário a utilização das ferramentas if, elif e else. Só com várias tentativas e a correr o programa várias vezes, é que consegui resolver o exercício.

*desenhar com o Turtle, a casa, o sol e a árvore

-Não tive dificuldades na realização deste exercício. Primeiramente, fiz a árvore, desenhei um retângulo castanho, utilizando um ciclo 2 vezes e ângulo 90º entre as linhas, e depois um círculo preenchido a cor verde, utilizando um ciclo de 360 vezes com ângulos de 1º entre cada linha desenhada. Seguidamente, fiz o sol, desenhei um círculo preenchido amarelo, do mesmo modo que fiz o círculo da árvore,apenas mudei a cor. De modo a fazer os raios do sol, utilizei o mesmo centro do sol, mas desta vez utilizei um ciclo de 18 vezes com um ângulo de 20º entre cada linha. Por último, desenhei a casa, começando pelo retângulo maior, utilizando um ciclo de 2 vezes, com ângulo de 90º entre as linhas. De seguida, desenhei o telhado, em que as linhas fazem um ângulo de 45º com a linha (imaginária) que passa no centro do retângulo. Na porta e nas janelas da casa, também utilizei ciclos de 2 vezes com ângulos de 90º entre cada linha, uma vez que são retângulos.

Para além disso, todo este processo também exigiu a utilização de outro tipo de ferramentas, de modo achar as coordenadas da árvore, do sol e da casa, tais como "move forward to", "turn left/right by" com rotação de ângulos, e "pen up/down".

# relatório do tp2
## Data: 24/09/2024
## Autor: a105917 Ana Ribeiro 
## Resumo

O tp2 consistiu na realização do seguinte jogo: o computador pensa num número (entre 0 e 100), utilizador tenta adivinhar - opção 1; ou, o utilizador pensa num número (entre 0 e 100) e o computador tenta adivinhar - opção 2.

Na realização da primeira parte do exercício (parte 1), não senti muitas dificuldades. 
Comecei por gerar uma função utilizador_adivinha. Para que o computador gerasse um número aleatóro entre 0 e 100, utilizei as ferramentas import random e random.randint(0, 100). Posteriormente, criei um ciclo while de modo a que o jogo se repetisse até que o utilizador conseguisse advinhar o respetivo número. Criei um input do número de utilizador para que este pudesse escrever o número que pensou até acertar. De seguida, criei if´s que ajudam o utilizador a encontrar o número, dizendo se é mair ou menor... em cada resposta destas, o número de tentativas ia ser acrescentado em 1. Por fim, de modo a iniciar o jogo, interpelei pela função utilizador_adivinha().
Na realização da segunda parte do exercício, senti algumas dificuldades... apesar de ter criado uma função (computador_adivinha), ter utilizado o ciclo while e a ferramenta  if, tal como no primeiro exercício, desta vez tive de criar um input para que o utilizador ajudasse o computador a adivinhar o número, podendo só responder "acertou", "menor" ou "maior". Sendo assim, consoante a resposta dele, as variáveis definidas como maior e menor assumem outros valores, ,e o computador consegue advinhar.
Por fim gerei outra função jogo_adivinha_numero(), para que utilizador escolhesse o jogo que quer jogar.
