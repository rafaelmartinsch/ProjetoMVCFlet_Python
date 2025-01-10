import flet as ft
from database.conector import Conector
from view.produto_view import produto_view

def main(page: ft.Page):
    page.title="Lanchonete Siri Cascudo"
    page.window.height=600
    page.window.width=600
    page.scroll=ft.ScrollMode.AUTO
    
    viewHome = ft.View(
            route="/",
            controls=[ft.Row( 
                        controls=[ft.Column(
                            controls=[
                                ft.ElevatedButton(
                                    icon=ft.icons.SHOPPING_CART,
                                    text="Gerir Pedidos",
                                    on_click=lambda e: page.go('/pedidos'),
                                    style=ft.ButtonStyle(
                                        color=ft.colors.WHITE,
                                        bgcolor=ft.colors.RED,
                                        shape=ft.RoundedRectangleBorder(radius=10),
                                    ),
                                    width=150,
                                    height=150
                                ),
                                ft.ElevatedButton(
                                    icon=ft.icons.STORE,
                                    text="Gerir Produtos",
                                    on_click=lambda e: page.go('/produtos'),
                                    icon_color=ft.colors.BLUE,
                                    width=150,
                                    height=100
                                ),
                                ft.ElevatedButton(
                                    icon=ft.icons.PEOPLE,
                                    text="Gerir Clientes",
                                    on_click=lambda e: page.go('/clientes'),
                                    icon_color=ft.colors.GREEN,
                                    width=150,
                                    height=100
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=20,
                        )],
                        alignment=ft.MainAxisAlignment.CENTER,
                    )]
                 
            )
    
            
    
    # Definição das rotas
    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(viewHome)
        elif page.route == "/produtos":
            page.views.append(produto_view(page))
        elif page.route == "/pedidos":
            #page.views.append(produto_view(page))
            snackbar = ft.SnackBar(ft.Text("Não Disponível!"))
            page.overlay.append(snackbar)
            snackbar.open = True
            page.update()
            page.go("/")
        elif page.route == "/clientes":
            #page.views.append(produto_view(page))
            snackbar = ft.SnackBar(ft.Text("Não Disponível!"))
            page.overlay.append(snackbar)
            snackbar.open = True
            page.update()
            page.go("/")
        page.update()

    page.on_route_change = route_change
    page.go("/")


ft.app(main)