def insert_or_delete_query(connection, sql, values):
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql, values)
    connection.commit()

def registro_diferente(row, data):
    for i in range(len(row)):    
        if i < len(data):  
            if row[i] != data[i]: 
                print(row[i],data[i])
                return True
    return False

def update(connection, dados, row):
    if registro_diferente(row, dados) == True:
        print("CHAMADO - ",dados[0]," Tem diferente")
        cursor = connection.cursor()
        cursor.execute("""UPDATE CHAMADOS SET titulo = %s, data_criacao = %s, nomecliente = %s, dataencerramento = %s, ultimasituacao = %s, descsituacao = %s, categoria = %s, departamento = %s, atendente = %s, D_E_L_E_T_E = ' ' WHERE protocolo = %s""", 
            (dados[1], dados[2], dados[3], dados[4], dados[5], dados[6], dados[7], dados[8], dados[9], dados[0])
        )
        connection.commit()

def insert(connection, dados):
    print(dados)
    cursor = connection.cursor()
    sql = """SELECT protocolo, titulo, data_criacao, nomecliente, dataencerramento, ultimasituacao, descsituacao, categoria, departamento, atendente FROM chamados WHERE protocolo = %i """ % (dados[0])
    cursor.execute(sql)
    row = cursor.fetchone() 
    if row or row is not None:
        update(connection, dados, row)
    else:
        insert_or_delete_query(connection, 
            """INSERT INTO CHAMADOS (protocolo, titulo, data_criacao, nomecliente, dataencerramento, ultimasituacao, descsituacao, categoria, departamento, atendente, D_E_L_E_T_E ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, ' ')""", 
            (dados[0], dados[1], dados[2],dados[3], dados[4], dados[5], dados[6], dados[7], dados[8], dados[9])
        )
def delete(connection, primary_keys):
    cursor = connection.cursor()
    sql = """SELECT protocolo FROM CHAMADOS"""
    cursor.execute(sql)
    row = cursor.fetchall()
    if row:
        for i in row:
            if not i[0] in primary_keys:
                cursor = connection.cursor()
                sql = """UPDATE CHAMADOS SET D_E_L_E_T_E = '*' WHERE protocolo = %i""" % (i[0])
                cursor.execute(sql)
                connection.commit()
                print("Protocolo - Delete ", i[0]," TOMTICKET.")