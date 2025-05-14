# Exercicio Dicionário
alunos = {"Ana": 8.5,"Pedro": 7.0,"Maria": 9.2}

alunos["Carlos"] = 6.5
alunos["Ana"] = 9.0
alunos.pop("Pedro")
media = sum(alunos.values()) / len(alunos)
if "Maria" in alunos:
    print("Maria está presente no dicionário.")
else:
    print("Maria não está presente no dicionário.")
print(alunos)
print(f"Média das notas: {media:.2f}")
