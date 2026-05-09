import flet as ft
import database  

def vista_login(page: ft.Page):
    titulo_top = ft.Text("APPTS", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK)
    logo = ft.Image(src="logo.png", width=120, height=120)
    titulo_universidad = ft.Text("UNIVERSIDAD TÉCNICA\nDE MANABÍ", size=16, color="#008f39", weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER)
    header_appts = ft.Row([ft.Icon(ft.Icons.CLOUDY_SNOWING, color="#fbca03", size=30), ft.Text("APPTS", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK)], alignment=ft.MainAxisAlignment.CENTER)

    estilo_label = ft.TextStyle(weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK, size=14)
    
    txt_usuario = ft.TextField(label="Usuario (Correo)", label_style=estilo_label, bgcolor=ft.Colors.GREY_200, border=ft.InputBorder.NONE, filled=True, border_radius=8)
    txt_password = ft.TextField(label="Contraseña", label_style=estilo_label, password=True, can_reveal_password=True, bgcolor=ft.Colors.GREY_200, border=ft.InputBorder.NONE, filled=True, border_radius=8)
    
    # Función infalible para mostrar mensajes por encima de todo
    def mostrar_mensaje(texto, color):
        snack = ft.SnackBar(content=ft.Text(texto), bgcolor=color)
        page.overlay.append(snack)
        snack.open = True
        page.update()

    def intentar_login(e):
        if not txt_usuario.value or not txt_password.value:
            mostrar_mensaje("Por favor, llena ambos campos", "red")
            return

        correo = txt_usuario.value
        password = txt_password.value
        
        if database.verificar_login(correo, password):
            mostrar_mensaje("¡Inicio de sesión exitoso!", "green")
        else:
            mostrar_mensaje("Credenciales incorrectas", "red")

    btn_ingresar = ft.FilledButton(
        content=ft.Text("INGRESAR", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE), 
        bgcolor="#149444", width=300, height=50, 
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
        on_click=intentar_login 
    )

    def volver(e):
        page.route = "/"
        page.on_route_change(None)

    return ft.View(
        route="/login",
        controls=[
            ft.AppBar(leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=volver), bgcolor=ft.Colors.TRANSPARENT),
            ft.Column(
                [
                    titulo_top, logo, titulo_universidad, ft.Container(height=10),
                    header_appts, ft.Container(height=20),
                    txt_usuario, txt_password, ft.Container(height=20),
                    btn_ingresar
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10
            )
        ],
        bgcolor=ft.Colors.WHITE, padding=20
    )