import sqlite3
import os

# Esto fija la ruta para que siempre busque APPTS.db en esta misma carpeta
CARPETA_ACTUAL = os.path.dirname(os.path.abspath(__file__))
RUTA_BD = os.path.join(CARPETA_ACTUAL, "APPTS.db")

def conectar():
    return sqlite3.connect(RUTA_BD)

def inicializar_bd():
    conexion = conectar()
    cursor = conexion.cursor()
    # Si la tabla ya existe con tus datos, esta línea no hará nada. Es 100% segura.
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombres TEXT NOT NULL,
            apellidos TEXT NOT NULL,
            cedula TEXT UNIQUE NOT NULL,
            correo TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conexion.commit()
    conexion.close()

# Se ejecuta silenciosamente para asegurar que la tabla exista
inicializar_bd()

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
    
    cursor.execute(
        "SELECT nombres FROM Usuarios WHERE correo = ? AND password = ?",
        (usuario, password)
    )
    usuario_encontrado = cursor.fetchone()
    conexion.close()
    
    if usuario_encontrado:
        return usuario_encontrado[0] 
    return None