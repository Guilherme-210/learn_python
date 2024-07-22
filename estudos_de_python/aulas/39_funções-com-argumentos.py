# cria uma função que recebe dois argumentos
def full_name(fname, lname):
    print(f"{fname} {lname}")

# cria uma função que some dois numeros via parametro
def sum(a, b):
    print(a + b)

# argumento default numa função
def address(country="Brasil"):
    print(f"Eu moro no {country}")

full_name("Rodrigo", "Macedo")
sum(20, 10)
address()
address("Canadá")

# avaliação do jogo
def rating_game(qtdRating):
    game_name = input("Digite o nome do jogo\n")
    sum = 0
    for i in range(qtdRating):
        note = float(input("Digite a nota para o jogo \n"))
        sum += note
    print(f"Média de avaliação do jogo {game_name} é: {sum/qtdRating}")

rating = int(input("Digite quantas avaliações deseja fazer no jogo\n"))
rating_game(rating)