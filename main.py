import flet as ft
from view.produto_view import produto_view

def main(page: ft.Page):
    page.title="Lanchonete Siri Cascudo"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.window.height=600
    page.window.width=600
    page.scroll=ft.ScrollMode.AUTO
    
    
    def chama_produto(e):
        coluna = produto_view(page)
        page.clean()
        page.add(coluna)
    
    page.add(
            ft.ElevatedButton(
                    "Produtos", 
                    on_click=chama_produto
                    )
            )
    
ft.app(main)