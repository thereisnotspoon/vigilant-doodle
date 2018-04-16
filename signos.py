import psycopg2
import psycopg2.extras
import sys

#metodos para crear ipRecords
import prosur_cli.create_record as cr
import prosur_cli.get_record as gr
import prosur_cli.remove_record as rr

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
    
    import time
    start_time = time.time()
    #ejecutar un comando
    signos = consultarSignosDistintivos() 
    
    #rr.removeRecordById(19654000)
    #gr.getRecord('EC', '1706136665488629998', 'DISTINCTIVE_SIGN' )

    for signo in signos:
        cr.createDistinctiveSign(signo)      
        minutos = ( time.time() - start_time) / 60
        print("--- %s minutos ---" % (minutos))
        pass
        
    for signo in signos:
        #gr.getRecord(signo)      
        #minutos = ( time.time() - start_time) / 60
        #print("--- %s minutos ---" % (minutos))
        pass
    
    for signo in signos:
        #rr.removeRecord(signo)      
        #minutos = ( time.time() - start_time) / 60
        #print("--- %s minutos ---" % (minutos))
        pass

    return

if __name__ == "__main__":
    main() 
