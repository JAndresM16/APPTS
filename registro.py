import flet as ft

def vista_registro(page: ft.Page):
    logo = ft.Image(src="logo.png", width=120, height=120)
    titulo_universidad = ft.Text("UNIVERSIDAD TÉCNICA\nDE MANABÍ", size=16, color="#008f39", weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER)
    
    icono_appts = ft.Icon(ft.Icons.CLOUDY_SNOWING, color="#fbca03", size=40)

    def crear_campo(label, es_password=False):
        return ft.TextField(
            label=label, 
            label_style=ft.TextStyle(weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK, size=12),
            bgcolor=ft.Colors.GREY_200, 
            border=ft.InputBorder.NONE, 
            filled=True, 
            border_radius=8, 
            password=es_password, 
            expand=True,
            content_padding=10
        )

    fila1 = ft.Row([crear_campo("Nombres"), crear_campo("Apellidos")])
    fila2 = ft.Row([crear_campo("Cédula"), crear_campo("Correo electrónico")])
    fila3 = ft.Row([crear_campo("Contraseña", True), crear_campo("Confirmar contraseña", True)])

    btn_registrar = ft.FilledButton(
        content=ft.Text("REGISTRAR", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE), 
        bgcolor="#149444", 
        width=300, 
        height=50, 
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8))
    )

    def volver(e):
        page.route = "/"
        page.on_route_change(None)

    return ft.View(
        route="/registro",  # <-- CORRECCIÓN
        controls=[
            ft.AppBar(leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=volver), bgcolor=ft.Colors.TRANSPARENT),
            ft.Column(
                [
                    logo, 
                    titulo_universidad, 
                    ft.Container(height=10),
                    icono_appts,
                    ft.Container(height=20),
                    fila1,
                    fila2,
                    fila3,
                    ft.Container(height=30),
                    btn_registrar
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10
            )
        ],
        bgcolor=ft.Colors.WHITE,
        padding=20
    )