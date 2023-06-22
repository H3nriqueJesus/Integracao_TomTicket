import time
import Fontes.Controller.CHAMADOS.CHAMADOS as chamados
from connect_mysql import *

def CHAMADOS():
    chamado = chamados.TOMTICKET(connect_tomticket_prod())
    chamado.obterDados()

time_start = time.time()

CHAMADOS()

time_fim = time.time()
print("Duracao ", time_fim-time_start)
hours, rem = divmod(time_fim-time_start, 3600)
minutes, seconds = divmod(rem, 60)
print("{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))