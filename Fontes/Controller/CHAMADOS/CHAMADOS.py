import pandas as pd
import time

def update_excel(filePath, data, variacao):
    #file = filePath.split("\\")[-1]
    file = filePath.split("/")[-1]
    try:
        if file == "888 - TGFEPR.xlsx":
            f = pd.read_excel("entrada_TGFEPR.xlsx")
            for e in range(len(f)):
                codlocal = f.iloc[e]["codlocal"]
                if codlocal == 1171:
                    for i in range(1, 7):
                        codprod = f.iloc[e]["codprod"]
                        
                        
                        if i == 1: codetapa = 0
                        elif i == 2: codetapa = 9
                        elif i == 3: codetapa = 8
                        #elif i == 3: codetapa = 15
                        elif i == 4: codetapa = 10
                        #elif i == 5: codetapa = 11
                        elif i == 5: codetapa = 12
                        
                        newRow = [len(data), codprod, codlocal, " ", "H"]
                        data.loc[len(data)] = newRow
            
                elif codlocal == 1172:
                    for i in range(1, 3):
                        codprod = f.iloc[e]["codprod"]
                        
                        
                        if i == 1: codetapa = 0
                        elif i == 2: codetapa = 9
                        elif i == 3: codetapa = 8
                        #elif i == 3: codetapa = 15
                        elif i == 4: codetapa = 10
                        #elif i == 5: codetapa = 11
                        elif i == 5: codetapa = 12
                        
                        
                        newRow = [len(data), codprod, codlocal, " ", "H"]
                        data.loc[len(data)] = newRow

                elif codlocal == 1173:
                    for i in range(1, 3):
                        codprod = f.iloc[e]["codprod"]
                        
                        
                        if i == 1: codetapa = 0
                        elif i == 2: codetapa = 9
                        elif i == 3: codetapa = 8
                        #elif i == 3: codetapa = 15
                        elif i == 4: codetapa = 10
                        #elif i == 5: codetapa = 11
                        elif i == 5: codetapa = 12
                        
                        
                        newRow = [len(data), codprod, codlocal, " ", "H"]
                        data.loc[len(data)] = newRow
                        data.to_excel(filePath)
        
        elif file == "888 - TGFFCP.xlsx":
            f = pd.read_excel("entrada_TGFFCP.xlsx")
            for e in range(len(f)):

                codprod = f.iloc[e]["codprod"]
                codlocal = f.iloc[e]["codlocal"]

                newRow = [len(data), codprod, variacao, codlocal, " ", "S", "H", " ", 1, 1, " ", " ", " ", "S", " ", "N", "P", "N", " ", " ", " ", " ", " ", " ", " ", " ", " "]

                data.loc[len(data)] = newRow
                data.to_excel(filePath)

        elif file == "888 - TGFICP.xlsx":
            f = pd.read_excel("entrada_TGFICP.xlsx")
            print("Arquivo 888 - TGFICP.xlsx selecionado")
            print("Quantidade de registros:", len(f))
            dict_list = []
            start_time = time.time()
            for e in range(len(f)):
                d = {}
                d["ID"] = len(data) + e
                d["CODPROD"] = f.iloc[e]["codprod"]
                d["VARIACAO"] = variacao
                d["CODLOCAL"] = f.iloc[e]["codlocal"]
                d["CONTROLE"] = " "
                d["CODETAPA"] = f.iloc[e]["codetapa"]
                d["CODMATPRIMA"] = f.iloc[e]["CODMATPRIMA"]
                d["QTDMISTURA"] = f.iloc[e]["QTDMISTURA"]
                d["CODVOL"] = f.iloc[e]["CODVOL"]
                d["DESVIOPADRAO"] = " "
                d["ATUALESTOQUE"] = "S"
                d["CODLOCALMP"] = 1140
                d["CONTROLEMP"] = " "
                d["SEQUENCIA"] = 0
                d["OBSERVACAO"] = " "
                d["FIXO"] = "N"
                d["OPCIONAL"] = "N"
                d["MANTEMQTD"] = "N"
                d["TERCEIROS"] = "N"
                d["ONDEEXEC"] = " "
                d["SINCRFLUXO"] = " "
                d["SELECIONAPROX"] = " "
                d["PODECONCLUIR"] = " "
                d["SEGUEANTERIOR"] = " "
                d["NIVEISRECUO"] = " "
                d["TIPTRANSICAO"] = "A"
                d["TRANSICAO"] = "N"
                d["PRECO"] = " "
                d["ATUALESTINDIVIDUAL"] = "N"
                d["ULOCETPAESTIND"] = "N"
                d["TIPTROCPRODKIT"] = "K"
                d["VARIARCONTROLE"] = "N"
                d["DESCONTOECONECT"] = " "
                
                dict_list.append(d)
            
            df_final = pd.DataFrame.from_dict(dict_list)
            data = data.append(df_final)
            data.to_excel(filePath)
            end_time = time.time()
            print("tempo de execução: " + str(end_time - start_time))
        else:
            print("até a próxima!!")
            quit()
        data.pop("Unnamed: 0")
        data.to_excel(filePath)
        return True
    except:
        return False