import psycopg2
import psycopg2.extras

#obtiene un cursor diccionario
def getDictCursor():
    
    #conectar a la base de datos ipRecords
    conn = psycopg2.connect("dbname=ipRecords user=postgres")

    #abrir un cursor para realizar las operaciones a la base de datos
    #notese que se crea un cursor especial para retornar los registros
    #en forma diccionario
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    return conn, cur

#cierra la conexión con la base de datos
def cerrarConexion(cursor, conection):
    cursor.close()
    conection.close()

#consulta los fileData que puede tener un registro
def consultarFileData(iprecordid):
    conn, cur = getDictCursor()
    sql = """
            SELECT  
                filename as \"fileName\", 
                filetitle as \"fileTitle\", 
                filedescription as \"fileDescription\"
            FROM 
                file_data
                JOIN ip_record_file_data USING (file_data_id)
                JOIN ip_record USING (ip_record_id)
            WHERE 
                ip_record_id = %s
        """
    cur.execute(sql, (iprecordid,))
    fileData = cur.fetchall()
    cerrarConexion(cur, conn)
    return fileData


#consulta las clases  niza que puede tener un signo distintivo
#la función espera el id de un ipRecord de tipo Signo Distintivo
def consultarNizas(iprecordid):
    conn, cur = getDictCursor()
    sql = """
            SELECT 
                activity,
                classnumber as \"niceClass\" 
            FROM 
                nice_class 
                JOIN distinctive_sign_nice_class USING (nice_class_id)
                JOIN distinctive_sign USING (distinctive_sign_id)
            WHERE 
                ip_record_id = %s
        """
    cur.execute(sql, (iprecordid,))
    niceClasses = cur.fetchall()
    cerrarConexion(cur, conn)
    return niceClasses

#consulta las prioridades que puede tener una patente
#la función espera el id de un ipRecord de tipo Patente
def consultarPrioridades(iprecordid):
    conn, cur = getDictCursor()
    sql = """
            SELECT
                prioritynumber as \"priorityNumber\", 
                prioritydate as \"priorityDate\", 
                prioritycountryid as \"priorityCountryId\"
	    FROM
	        priority
	        JOIN patent_priority USING (priority_id)
	        JOIN patent USING (patent_id)
            WHERE 
                ip_record_id = %s
        """
    cur.execute(sql, (iprecordid,))
    niceClasses = cur.fetchall()
    cerrarConexion(cur, conn)
    return niceClasses

#consula todos los signo distintivos de la base, notese que no retorna
#los file data asociados, ni las clase niza
def consultarSignos():
    conn, cur = getDictCursor()
    sql = """
            SELECT 
                *
            FROM 
                ip_record
		JOIN distinctive_sign USING (ip_record_id) 
          """ 
    cur.execute(sql)
    signos = cur.fetchall()
    return signos


#consula todas las patentes de diseño de la base, nótese que no retorna
#las prioridades asociadas
def consultarPatentesDisenio():
    conn, cur = getDictCursor()
    sql = """
            SELECT 
                *
            FROM 
                design_patent
	        JOIN patent USING (patent_id)
	        JOIN ip_record USING (ip_record_id)
          """ 
    cur.execute(sql)
    patentesDisenio = cur.fetchall()
    return patentesDisenio


#consula todas las patentes de invencion de la base, nótese que no retorna
#las prioridades asociadas
def consultarPatentesInvencion():
    conn, cur = getDictCursor()
    sql = """
            SELECT 
                *
            FROM 
                invention_patent
	        JOIN patent USING (patent_id)
	        JOIN ip_record USING (ip_record_id)
          """ 
    cur.execute(sql)
    patentesInvencion = cur.fetchall()
    return patentesInvencion

