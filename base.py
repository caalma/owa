from configuracion import *
import urls
from subprocess import Popen, PIPE


def abrir_url(args, modo=''):
    param_app = '--app=' if abrir_como_app else ''
    if len(args) > 1:
        for val in args[1:]:
            if val in dir(urls):
                url = eval(f'urls.{val}')
            else:
                url = val
            Popen(f'{browser} {modo} {param_app}{url}', shell=True)


def mostrar_url(i):
    u = eval(f'urls.{i}')
    print(f'{i} => {u}')


def idu_valido(tex):
    return tex in [i for i in dir(urls) if not i.endswith('__')]


def url_valida(tex):
    ini = ['http', 'www', 'ftp']
    for i in ini:
        if tex.startswith(i):
            return True
    return False


def listar_urls(args):
    ids = [i for i in dir(urls) if not i.endswith('__')]

    if len(args) > 1:
        for f in args[1:]:
            for i in ids:
                if f in i:
                    mostrar_url(i)
    else:
        for i in ids:
            mostrar_url(i)


def agregar_url(args):
    if len(args) > 2:
        v = args[1:]
        v[-1] = f'"{v[-1]}"'
        with open('urls.py', 'a') as f:
            f.write('\n' + (' = '.join(v)))


def editar(arc):
    Popen(f'{editor} {arc}', shell=True)


def ayuda():
      Popen(f'{browser} ./ayuda.html', shell=True)
