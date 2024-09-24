# relatório do tp2
## Data: 24/09/2024
## Autor: a105917 Ana Ribeiro 
## Resumo

O tp2 consistiu na realização do seguinte jogo: o computador pensa num número (entre 0 e 100), utilizador tenta adivinhar - opção 1; ou, o utilizador pensa num número (entre 0 e 100) e o computador tenta adivinhar - opção 2.

Na realização da primeira parte do exercício (parte 1), não senti muitas dificuldades. 
Comecei por gerar uma função utilizador_adivinha. Para que o computador gerasse um número aleatóro entre 0 e 100, utilizei as ferramentas import random e random.randint(0, 100). Posteriormente, criei um ciclo while de modo a que o jogo se repetisse até que o utilizador conseguisse advinhar o respetivo número. Criei um input do número de utilizador para que este pudesse escrever o número que pensou até acertar. De seguida, criei if´s que ajudam o utilizador a encontrar o número, dizendo se é mair ou menor... em cada resposta destas, o número de tentativas ia ser acrescentado em 1. Por fim, de modo a iniciar o jogo, interpelei pela função utilizador_adivinha().
Na realização da segunda parte do exercício, senti algumas dificuldades... apesar de ter criado uma função (computador_adivinha), ter utilizado o ciclo while e a ferramenta  if, tal como no primeiro exercício, desta vez tive de criar um input para que o utilizador ajudasse o computador a adivinhar o número, podendo só responder "acertou", "menor" ou "maior". Sendo assim, consoante a resposta dele, as variáveis definidas como maior e menor assumem outros valores, ,e o computador consegue advinhar.
Por fim gerei outra função jogo_adivinha_numero(), para que utilizador escolhesse o jogo que quer jogar.