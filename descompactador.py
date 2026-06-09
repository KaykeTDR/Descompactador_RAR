import rarfile 

diretorio = '/home/kayke/Documentos/Beholder2_traducao.rar'
senha = 'centraldetraducoes.net.br'
destino ='/home/kayke/Documentos/beholder2'

with rarfile.RarFile(diretorio) as rf:
    rf.extractall(path=destino, pwd=senha)

print(f'Arquivos extraodps para: {destino}')
