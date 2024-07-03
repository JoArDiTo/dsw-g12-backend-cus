from dotenv import load_dotenv
import os

load_dotenv()

#Para la conexión a la base de datos
server=os.getenv("SERVER")
user=os.getenv("USER")
password=os.getenv("PASSWORD")
host=os.getenv("HOST")
database=os.getenv("DATABASE")

DATABASE_CONNECTION=f'{server}://{user}:{password}@{host}/{database}'

#Para la conexion al servidor de correo
email=os.getenv("EMAIL")
pwd=os.getenv("PASSWORD_EMAIL")
