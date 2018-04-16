import psycopg2
import psycopg2.extras

#metodos para crear ipRecords
from prosurc.prosur_cli import create_record

#obtiene un cursor diccionario
def getDictCursor():
    
    #conectar a la base de datos ipRecords
    conn_str = "dbname=iepi-postgres user=postgres" 
    conn = psycopg2.connect(conn_str)

    #abrir un cursor para realizar las operaciones a la base de datos
    #notese que con .DictCursor se crea un cursor especial para retornar los registros
    #en forma diccionario
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    return conn, cur

#cierra la conexión con la base de datos
def cerrarConexion(cursor, conection):
    cursor.close()
    conection.close()

#consula todas las patentes de invencion de la base, nótese que no retorna
#las prioridades asociadas
def consultarSignosDistintivos():
    conn, cur = getDictCursor()
    sql = """
            SELECT 
                *
            FROM 
                signos_distintivos
          """ 
    cur.execute(sql)
    SignosDistintivos = cur.fetchall()
    cerrarConexion(cur, conn)
    return SignosDistintivos

#metodo principal
def main():
    
    #ejecutar un comando
    signos = consultarSignosDistintivos() 
    
    for signo in signos:
        print(signo)
    


if __name__ == "__main__":
    main() 
