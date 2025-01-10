import mysql.connector
import os
from dotenv import load_dotenv


load_dotenv()
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")



class Conector:
    
    #retorna a conexâo extabelecida ou retorna None quando der errado
    def conectar():
        conexao=None
        try:
            conexao =  mysql.connector.connect(
                host=db_host,
                user=db_user,
                password=db_password,
                database=db_name
            )
            print("Conexão com o BD estabelecida!")
        except mysql.connector.Error as e:
            print(f"Erro ao conectar com o BD:{e}")

        return conexao

    #finalizar a conexão o fim das operações
    def fechar_conexao(conexao):
        if conexao.is_connected():
            conexao.close()
            print("Conexão com o BD encerrada!")
        

