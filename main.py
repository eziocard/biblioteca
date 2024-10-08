
from fastapi import FastAPI,Request,Form
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from datetime import date
from DataBase import *
from typing import List
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="./view")

@app.get("/",response_class= HTMLResponse)
def root(req:Request):
    return templates.TemplateResponse("index.html",{"request":req})

@app.post("/",response_class= HTMLResponse)
def root(req:Request):
    return templates.TemplateResponse("index.html",{"request":req})

@app.get("/mostrar_datos",response_class= HTMLResponse)
def mostrar(req:Request):
    return templates.TemplateResponse("mostrar_datos.html",{"request":req})

@app.post("/ingresar-libro",response_class= HTMLResponse)
def ingresar(isbn:str=Form(),titulo: str = Form(),autor: str = Form(),fecha: date = Form(),editorial: str = Form(),
             precio: int = Form()):
    print(isbn)
    print(titulo)
    print(autor)
    print(fecha)
    print(editorial)
    print(precio)
    database = DataBase()
    database.ingresar(isbn,titulo,autor,str(fecha),editorial,precio)
    print("datos ingresados") 
    return RedirectResponse("/")

@app.get("/mostrar_libros",response_model = List[dict])
def mostrar_libros():
    database = DataBase()
    return database.get_database()
