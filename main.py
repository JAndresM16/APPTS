import flet as ft
from views.login import vista_login
from views.registro import vista_registro
from views.dashboard import vista_dashboard

def main(page: ft.Page):
    page.title = "UTM - APPTS"
    page.window.width = 380
    page.window.height = 700
    page.theme_mode = ft.ThemeMode.LIGHT 

    def route_change(e):
        page.views.clear()
        
        # --- VISTA PRINCIPAL (Home) ---
        logo = ft.Image(src="logo.png", width=150, height=150)
        titulo_universidad = ft.Text("UNIVERSIDAD TÉCNICA\nDE MANABÍ", size=18, color="#008f39", weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER)
        header_appts = ft.Row([ft.Icon(ft.Icons.CLOUDY_SNOWING, color="#fbca03", size=40), ft.Text("APPTS", size=32, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK)], alignment=ft.MainAxisAlignment.CENTER)
        
        btn_style = ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8), padding=20)
        
        def ir_registro(e):
            page.route = "/registro"
            route_change(None)

        def ir_login(e):
            page.route = "/login"
            route_change(None)

        btn_registro = ft.FilledButton(content=ft.Text("REGISTRO", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE), bgcolor="#0089bd", style=btn_style, width=250, on_click=ir_registro)
        btn_login = ft.FilledButton(content=ft.Text("LOGIN", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE), bgcolor="#149444", style=btn_style, width=250, on_click=ir_login)
        
        eslogan = ft.Column([ft.Text("Universidad que transforma", 
                                     size=14, italic=True, color="#0089bd"), ft.Text("Calidad que trasciende", size=14, italic=True, color="#0089bd")], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=0)

        vista_home = ft.View(
            route="/",
            controls=[
                logo, ft.Container(height=10), titulo_universidad, ft.Container(height=30), header_appts, ft.Container(height=40),
                btn_registro, ft.Container(height=10), btn_login, ft.Container(expand=True), eslogan
            ],
            bgcolor=ft.Colors.WHITE,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            padding=40
        )
        
        page.views.append(vista_home)

        # --- AHORA PASAMOS "route_change" A LAS OTRAS VISTAS ---
        if page.route == "/login":
            page.views.append(vista_login(page, route_change))
        elif page.route == "/registro":
            page.views.append(vista_registro(page, route_change))
        elif page.route == "/dashboard":
            page.views.append(vista_dashboard(page, route_change))
        
        page.update()

    def view_pop(e):
        page.views.pop()
        if len(page.views) > 0:
            top_view = page.views[-1]
            page.route = top_view.route
            route_change(None)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    
    page.route = "/"
    route_change(None)

if __name__ == "__main__":
    ft.run(main, assets_dir="assets")