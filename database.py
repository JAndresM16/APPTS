import sqlite3

# Asegúrate de poner la extensión correcta de tu archivo (.db o .sqlite)
NOMBRE_BD = "APPTS.db" 

def conectar():
    return sqlite3.connect(NOMBRE_BD)

def registrar_usuario(nombres, apellidos, cedula, correo, password):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        
        # IMPORTANTE: Cambia "usuarios" por el nombre exacto de tu tabla 
        # y asegúrate de que los nombres de las columnas coincidan con los tuyos.
        cursor.execute(
            "INSERT INTO Usuarios (nombres, apellidos, cedula, correo, password) VALUES (?, ?, ?, ?, ?)",
            (nombres, apellidos, cedula, correo, password)
        )
        conexion.commit()
        return True # Se registró con éxito
    except sqlite3.IntegrityError:
        return False # Falló (probablemente la cédula o correo ya existen)
    finally:
        conexion.close()

def verificar_login(usuario, password):
    conexion = conectar()
    cursor = conexion.cursor()
    
    # Aquí busco por correo (asumiendo que el "Usuario" del login es el correo)
    cursor.execute(
        "SELECT * FROM Usuarios WHERE correo = ? AND password = ?",
        (usuario, password)
    )
    usuario_encontrado = cursor.fetchone()
    conexion.close()
    
    # Retorna True si encontró el usuario, False si no
    return usuario_encontrado is not None