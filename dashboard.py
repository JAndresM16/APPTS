import flet as ft

def vista_dashboard(page: ft.Page, router):
    
    def cerrar_sesion(e):
        # Borramos el nombre por seguridad al salir
        page.mi_usuario = None 
        page.route = "/"
        router(None) 

    def proximamente(e):
        snack = ft.SnackBar(content=ft.Text("Próximamente..."), bgcolor="#0089bd")
        page.overlay.append(snack)
        snack.open = True
        page.update()

    # SOLUCIÓN INFALIBLE: Obtenemos el nombre del objeto "page" (Python puro)
    nombre_usuario = getattr(page, "mi_usuario", "Usuario")

    img_logo = ft.Image(src="logo.png", width=45, height=45)
    txt_header = ft.Text("UNIVERSIDAD TÉCNICA\nDE MANABÍ", size=11, color="#008f39", weight=ft.FontWeight.BOLD)
    titulo_appbar = ft.Row([img_logo, txt_header], spacing=10)

    menu_opciones = ft.PopupMenuButton(
        items=[
            ft.PopupMenuItem(
                content=ft.Row([
                    ft.Icon(ft.Icons.LOGOUT, color=ft.Colors.BLACK),
                    ft.Text("Cerrar sesión", color=ft.Colors.BLACK)
                ]),
                on_click=cerrar_sesion
            ),
        ],
        icon=ft.Icons.MENU,
        icon_color=ft.Colors.BLACK,
        icon_size=35
    )

    app_bar = ft.AppBar(
        automatically_imply_leading=False, # Quita la flecha de retroceso
        title=titulo_appbar,
        center_title=False,
        bgcolor=ft.Colors.WHITE,
        actions=[menu_opciones, ft.Container(width=10)] 
    )

    saludo = ft.Row(
        [
            ft.Text("Hola:", size=32, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
            # Imprimimos el nombre que extrajimos de la BD
            ft.Text(nombre_usuario, size=32, weight=ft.FontWeight.BOLD, color="#149444"), 
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    lbl_nuevo = ft.Text("Nuevo Proyecto", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK)
    
    btn_nuevo = ft.Container(
        content=ft.Column(
            [ft.Icon(ft.Icons.ADD, size=100, color=ft.Colors.BLACK)],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        bgcolor=ft.Colors.GREY_200,
        border_radius=10,
        height=200,
        on_click=proximamente,
        ink=True 
    )

    lbl_mis_proyectos = ft.Text("Mis Proyectos", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK)
    contenedor_proyectos = ft.Container(
        bgcolor=ft.Colors.GREY_200,
        border_radius=10,
        expand=True, 
        padding=15
    )

    return ft.View(
        route="/dashboard",
        controls=[
            app_bar,
            ft.Container(height=10),
            saludo,
            ft.Container(height=20),
            ft.Column([lbl_nuevo, btn_nuevo], spacing=5),
            ft.Container(height=20),
            ft.Column([lbl_mis_proyectos, contenedor_proyectos], spacing=5, expand=True)
        ],
        bgcolor=ft.Colors.WHITE,
        padding=20
    )