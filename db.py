import mysql.connector


def _executar(query):

    con = mysql.connector.connect(
        host='localhost',
        user='mysql',
        password='mysql',
        database='galo'
    )
    resultado = None
    try:
        cursor = con.cursor()
        cursor.execute(query)
        resultado = cursor.fetchall()
        con.commit()
    except Exception as err:
        print(f'Erro no Banco de Dados -> [+] {err}')
    con.close()
    return resultado
