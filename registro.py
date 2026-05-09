import flet as ft
import database  

def vista_registro(page: ft.Page):
    logo = ft.Image(src="logo.png", width=120, height=120)
    titulo_universidad = ft.Text("UNIVERSIDAD TÉCNICA\nDE MANABÍ", size=16, color="#008f39", weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER)
    icono_appts = ft.Icon(ft.Icons.CLOUDY_SNOWING, color="#fbca03", size=40)

    def crear_campo(label, es_password=False):
        return ft.TextField(
            label=label, label_style=ft.TextStyle(weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK, size=12),
            bgcolor=ft.Colors.GREY_200, border=ft.InputBorder.NONE, filled=True, 
            border_radius=8, password=es_password, expand=True, content_padding=10
        )

    txt_nombres = crear_campo("Nombres")
    txt_apellidos = crear_campo("Apellidos")
    txt_cedula = crear_campo("Cédula")
    txt_correo = crear_campo("Correo electrónico")
    txt_password = crear_campo("Contraseña", True)
    txt_confirmar = crear_campo("Confirmar contraseña", True)

    fila1 = ft.Row([txt_nombres, txt_apellidos])
    fila2 = ft.Row([txt_cedula, txt_correo])
    fila3 = ft.Row([txt_password, txt_confirmar])

    # Función infalible para mostrar mensajes por encima de todo
    def mostrar_mensaje(texto, color):
        snack = ft.SnackBar(content=ft.Text(texto), bgcolor=color)
        page.overlay.append(snack)
        snack.open = True
        page.update()

    def intentar_registro(e):
        # 1. Validar campos vacíos
        if not txt_nombres.value or not txt_apellidos.value or not txt_cedula.value or not txt_correo.value or not txt_password.value or not txt_confirmar.value:
            mostrar_mensaje("Error: Todos los campos son obligatorios", "red")
            return

        # 2. Validar que las contraseñas coincidan
        if txt_password.value != txt_confirmar.value:
            mostrar_mensaje("Error: Las contraseñas no coinciden", "red")
            return

        # 3. Enviar a la base de datos
        exito = database.registrar_usuario(
            txt_nombres.value, txt_apellidos.value, 
            txt_cedula.value, txt_correo.value, txt_password.value
        )

        # 4. Mostrar el mensaje correspondiente
        if exito:
            mostrar_mensaje("Usuario registrado correctamente", "green")
            # Limpiamos los campos
            txt_nombres.value = ""
            txt_apellidos.value = ""
            txt_cedula.value = ""
            txt_correo.value = ""
            txt_password.value = ""
            txt_confirmar.value = ""
            page.update()
        else:
            mostrar_mensaje("Error: La cédula o correo ya están registrados", "red")

    btn_registrar = ft.FilledButton(
        content=ft.Text("REGISTRAR", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE), 
        bgcolor="#149444", width=300, height=50, 
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
        on_click=intentar_registro 
    )

    def volver(e):
        page.route = "/"
        page.on_route_change(None)

    return ft.View(
        route="/registro",
        controls=[
            ft.AppBar(leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=volver), bgcolor=ft.Colors.TRANSPARENT),
            ft.Column(
                [
                    logo, titulo_universidad, ft.Container(height=10),
                    icono_appts, ft.Container(height=20),
                    fila1, fila2, fila3, ft.Container(height=30),
                    btn_registrar
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10
            )
        ],
        bgcolor=ft.Colors.WHITE, padding=20
    )