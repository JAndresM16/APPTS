import sqlite3

NOMBRE_BD = "APPTS.db" 

def conectar():
    return sqlite3.connect(NOMBRE_BD)

def registrar_usuario(nombres, apellidos, cedula, correo, password):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        
        cursor.execute(
            "INSERT INTO Usuarios (nombres, apellidos, cedula, correo, password) VALUES (?, ?, ?, ?, ?)",
            (nombres, apellidos, cedula, correo, password)
        )
        conexion.commit()
        return True 
    except sqlite3.IntegrityError:
        return False 
    finally:
        conexion.close()

def verificar_login(usuario, password):
    conexion = conectar()
    cursor = conexion.cursor()
    
    # MODIFICACIÓN: En vez de "SELECT *", pedimos específicamente los "nombres"
    cursor.execute(
        "SELECT nombres FROM Usuarios WHERE correo = ? AND password = ?",
        (usuario, password)
    )
    usuario_encontrado = cursor.fetchone()
    conexion.close()
    
    # Si encuentra al usuario, devuelve el nombre. Si no, devuelve None.
    if usuario_encontrado:
        return usuario_encontrado[0] # Retorna el texto del nombre
    return None