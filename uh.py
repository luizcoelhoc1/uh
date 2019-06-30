# -*- coding: utf-8 -*-

"""
uh.py

Estende a classe MaquinaDeTuringUniversal, incluindo heurísticas para
identificar se a MT para ou entra em loop com uma determinada entrada.
"""

import sys
import itertools
from MaquinaDeTuringUniversal import MaquinaDeTuringUniversal

class MTUcomHeuristicas(MaquinaDeTuringUniversal):
    """Estende a MTU com heurísticas para identificar se ela para ou entra em loop."""

    spinner = itertools.cycle(['-', '/', '|', '\\'])

    # experimental
    def mostrar_progresso(self):
        sys.stdout.write(self.spinner.next())  # write the next character
        sys.stdout.flush()                     # flush stdout buffer (actual character display)
        sys.stdout.write('\b')                 # erase the last written char


    def executar_simulacao(self):
        # verifica se existem loop para todos simbolos em alguma transicao
        if self.verifica_qerro():
            return False
        # verifica se o número de iterações ultrapassa o numero maximo de combinações 
        max_combinacoes = self.calcula_max_combinacoes()
        iteracoes = 0
        # executa a simulação
        while not self.simularTransicao():
            iteracoes += 1
            if iteracoes >= max_combinacoes:
                return False
            #self.printBonito()
            #self.mostrar_progresso()
        return True

    def resultado(self):
        """Retorna string informando se a mt simulada para ou entra em loop."""
        status = self.executar_simulacao()
        if status:
            return "A MT simulada aceita w e para."
        else:
            return "A MT entra em loop com a entrada w."

    def verifica_qerro(self):
        NUM_SIMBOLOS = 3
        num_transicoes_estado = {}
        for transicao in self.transicoes:
            elementos = transicao.split("0")
            if elementos[0] in num_transicoes_estado:
                num_transicoes_estado[elementos[0]] += 1
            else:
                num_transicoes_estado[elementos[0]] = 1
        for estado, num_transicoes in num_transicoes_estado.items():
            #print('TRANSICOES POR ESTADO:', estado, num_transicoes)
            if num_transicoes >= NUM_SIMBOLOS:
                return True
        return False

    def calcula_max_combinacoes(self):
        num_transicoes_mt = len(self.transicoes)
        #print(num_transicoes_mt)
        tam_palavra = len(self.palavra.split('0'))
        #print(tam_palavra)
        num_simbolos = 3
        _max = num_transicoes_mt * tam_palavra * (num_simbolos ** tam_palavra)
        return _max
