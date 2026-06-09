import rarfile 

diretorio = input("Digite o caminho do arquivo RAR: ")
senha = input("Digite a senha: ")
destino = input("Digite a pasta de destino: diretorio ")

with rarfile.RarFile(diretorio) as rf:
    rf.extractall(path=destino, pwd=senha)

print(f'Arquivos extraidos para: {destino}')
