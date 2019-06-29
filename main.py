# -*- coding: utf-8 -*-

"""
main.py


"""

import os
import os.path
from argparse import ArgumentParser
from uh import MTUcomHeuristicas


def le_arquivo(arquivo):
    with open(arquivo) as arquivo:
        mt = arquivo.read().replace('\n', '')
        print('Simulando {} ...'.format(arquivo.name))
        return mt

def executa_simulacao(mt):
    uh = MTUcomHeuristicas(mt)
    resultado = uh.resultado()
    print(resultado)

def main():
    parser = ArgumentParser(description='')
    parser.add_argument('arquivo', type=str, nargs='?',
                        help='Arquivo txt contendo R(M)w em representação unária',
                        default='teste.txt')
    parser.add_argument('-d', '--dir', type=str, nargs=1,
                        help='diretório contendo arquivos texto de R(M)w em \
                        representação unária')
    #parser.add_argument('-v', '--verbose', help='maior verbosidade na saída', action='store_true')
    args = parser.parse_args()

    if args.dir:
        arquivos = [arquivo for arquivo in os.listdir(args.dir[0])
                    if arquivo.endswith(".txt")]      
        for arquivo in arquivos:
            caminho_arquivo = os.path.join(args.dir[0], arquivo)
            mt = le_arquivo(caminho_arquivo)
            executa_simulacao(mt)
    elif args.arquivo:
        mt = le_arquivo(args.arquivo)
        executa_simulacao(mt) 

if __name__ == '__main__':
    main()