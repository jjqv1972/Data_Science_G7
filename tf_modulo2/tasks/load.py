import mysql.connector

def load(data):
    resultado = 0
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='mysql2026$',
        database='db_g7'
    )
    cursor = conn.cursor()
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS pais(
                        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                        nombre VARCHAR(255) NOT NULL,
                        capital VARCHAR(255) NOT NULL,
                        region VARCHAR(255),
                        poblacion BIGINT);
                    """)
    conn.commit()
    
    insert_query = """
                   insert into pais(nombre,capital,region,poblacion)
                   values(%s,%s,%s,%s)
                   """
    cursor.executemany(insert_query,data)
    conn.commit()
    resultado = cursor.rowcount
    
    cursor.close()
    conn.close()
    
    return resultado