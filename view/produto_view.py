import flet as ft
from database.conector import Conector 
from controllers.produto_controller import ProdutoController
from models.produto import Produto 

def produto_view(page): 
    conexao =  Conector.conectar()
    
    viewprodutos = ft.View(
            route="/",
            controls=[                
            ],
            scroll=ft.ScrollMode.AUTO
        )

    if conexao != None:
        produtos =  ProdutoController.listar(conexao)
                

        def salvar(e):
            novoProduto = Produto(parCod=None, 
                                  parDescricao=desc_field.value,
                                  parPreco=valor_field.value,
                                  parQtd=qtd_field.value
                                  )
            ProdutoController.inserir(conexao, novoProduto)
            page.snack_bar = ft.SnackBar(ft.Text("Produto Salvo!"))
            page.snack_bar.open = True
            page.go("/produtos")
        
        snackbar = ft.SnackBar(ft.Text("Conexão estabelecida!"))
        page.overlay.append(snackbar)
        snackbar.open = True
        page.update()
        
        desc_field =  ft.TextField(label="Descição")
        valor_field =  ft.TextField(label="Valor")
        qtd_field =  ft.TextField(label="Quantidade")
        salvar_button = ft.ElevatedButton(text="Salvar", on_click=salvar)
                
        divisor =  ft.Divider(height=5)
        tabela = ft.DataTable(
            columns=[
                    ft.DataColumn(ft.Text("ID")),
                    ft.DataColumn(ft.Text("Produto")),
                    ft.DataColumn(ft.Text("Valor")),
                    ft.DataColumn(ft.Text("Qtd")),
                ],
                rows=[]
        )


        dt_rows = []
        for produto in produtos:
            dt_row = ft.DataRow(cells=[
                        ft.DataCell(ft.Text(produto.cod)),
                        ft.DataCell(ft.Text(produto.descricao)),
                        ft.DataCell(ft.Text(produto.preco)),
                        ft.DataCell(ft.Text(produto.qtd))
                    ])
            dt_rows.append(dt_row)
        tabela.rows=dt_rows


        viewprodutos.controls = [desc_field,valor_field,qtd_field,salvar_button,divisor,tabela]
        
        
    else:
        print("Falha na Conexão!")
        page.snack_bar = ft.SnackBar(ft.Text("Falha na Conexao!"))
        page.snack_bar.open = True
        page.go("/")
        
    return viewprodutos
        