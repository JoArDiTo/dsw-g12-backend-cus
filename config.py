from dotenv import load_dotenv
import os

load_dotenv()

server=os.getenv("SERVER")
user=os.getenv("USER")
password=os.getenv("PASSWORD")
host=os.getenv("HOST")
database=os.getenv("DATABASE")

DATABASE_CONNECTION=f'{server}://{user}:{password}@{host}/{database}'
