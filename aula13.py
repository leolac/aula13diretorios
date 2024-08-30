import os
import shutil

# Criar
os.mkdir('novo_diretorio')
with open(R'C:\Users\aluno\Downloads\aula\novo_diretorio\novo_arquivo', 'w') as novo:
    print('arquivo criado')

# Listar
with os.scandir(R'C:\Users\aluno\Downloads\aula') as pasta:
      for arquivo in pasta:
         print(f'Diretório: {arquivo.name}')

# Renomear
os.rename(R'C:\Users\aluno\Downloads\aula\novo_diretorio\novo_arquivo', 'arquivo_renomeado')

# Copiar
shutil.copytree('novo_diretorio', 'copia')

# Remover
shutil.rmtree(R'C:\Users\aluno\Downloads\aula\novo_diretorio')
