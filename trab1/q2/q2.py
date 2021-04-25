import time
import threading
import random as rd
from faker import Faker


class Crianca:
    tempo_de_espera = 3

    def __init__(self, nome, priority, meta):
        self.com_bola = False
        self.pontos = 0
        self.meta = meta
        self.nome = nome
        self.priority = priority

    def jogando(self, jogo):
        while jogo.em_progresso:
            if jogo.bola_em_uso == False:
                self.pegar_bola(jogo)
                if self.pontos >= self.meta:
                    print(f'Fim de jogo! {self.nome} ganhou.')
                    jogo.em_progresso = False
                    break
                time.sleep(self.tempo_de_espera)
                self.soltar_bola(jogo)
            else:
                time.sleep(1-self.priority)

    def pegar_bola(self, jogo):
        jogo.bola_em_uso = True
        self.com_bola = True
        self.pontos += 1
        print(f'{self.nome}: Peguei a bola! | {self.pontos} Pontos!\n')

    def soltar_bola(self, jogo):
        jogo.bola_em_uso = False
        self.com_bola = False
        print(f'{self.nome}: Soltei!\n')


class Jogo:
    em_progresso = True
    bola_em_uso = True


def start_game(num_criancas, meta):
    fake = Faker('pt_BR')
    parametros_do_jogo = [{'nome': fake.name(), 'prioridade': rd.uniform(0, 1)} for i in range(num_criancas)]
    print('Parâmetros dos jogadores:')

    # Criando crianças
    criancas = []
    for parametros in parametros_do_jogo:
        print(parametros)
        criancas.append(Crianca(parametros['nome'], parametros['prioridade'], meta))

    jogo = Jogo()
    threads = []

    # Atribuindo a cada criança uma thread e iniciando essas threads
    for c in criancas:
        t = threading.Thread(target=c.jogando, kwargs=dict(jogo=jogo))
        t.start()
        threads.append(t)

    # Começando a brincadeira
    print(f'\nO Jogo começou com {num_criancas} jogadores, e terminará quando algum jogador atingir {meta} pontos.\n')
    jogo.bola_em_uso = False


start_game(num_criancas=10, meta=10)
