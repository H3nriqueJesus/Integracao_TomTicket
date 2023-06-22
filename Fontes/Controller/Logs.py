import os.path
import logging
from logging.handlers import RotatingFileHandler

#sistema flexível de registro de eventos para aplicativos e bibliotecas.
#Para obter uma lista de manipuladores incluídos como padrão, consulte logging.handlers.

# O processo principal obtém uma configuração simples que imprime no console.
log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s')
logFile = r'C:\Users\LEDAX\Documents\Codigos\TomticketIntegration\logFile.log'
# configure o registro em arquivo
logging.basicConfig(filename=logFile, encoding='utf-8', level=logging.DEBUG)

#O tamanho dos arquivos girados é reduzido para que você possa ver os resultados facilmente.
my_handler = RotatingFileHandler(logFile, mode='a', maxBytes=5*1024*1024, 
                                backupCount=2, encoding=None, delay=0)
#seleciona um objeto Formatter para este manipulador usar.
my_handler.setFormatter(log_formatter)

#Confirmação de que as coisas estão funcionando como esperado.
my_handler.setLevel(logging.INFO)

# create logger
app_log = logging.getLogger('root')
#Confirmação de que as coisas estão funcionando como esperado.
app_log.setLevel(logging.INFO)

#adicionar e remover objetos manipuladores do objeto logger.
app_log.addHandler(my_handler)

#Informa o sistema de registro para executar um desligamento ordenado, liberando e fechando todos os manipuladores.
logging.shutdown()

def LOG(origem,e):
    #LOG
    app_log = logging.getLogger(origem)
    app_log.info(e)
    #END LOG