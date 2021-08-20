nome_aluno = input("Digite seu nome e sobrenome:")
idade_aluno = input("Digite sua idade:")
escola = input("Digite o nome de sua escola:")
nota1 = input("Digite a sua nota da primeira unidade:")
nota2 = input("Digite a sua nota da segunda unidade:")
nota3 = input("Digite a sua nota da terceira unidade:")
nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)
soma_notas = nota1 + nota2 + nota3
media = soma_notas/3

print("Seu nome é", nome_aluno, ", estudante do", escola)
print("Você tem", idade_aluno, "anos.")
print("Sua média é", media)
