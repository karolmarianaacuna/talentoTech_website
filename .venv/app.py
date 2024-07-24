from flask import Flask, render_template, request
import numpy as np
import pandas as pd

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/blog')
def blog():
    
    archivo1 = r'.venv\data\datosCundinamarca.csv'
    
    df = pd.read_csv(archivo1)
    
    # Asegurarse de que los nombres de las columnas están correctos
    df.columns = df.columns.str.strip()
    
    df = df.drop_duplicates()

   # Obtener solo los primeros 50 registros
    df = df.head(50)
    
    # Convertir df a una lista de diccionarios para pasar a la plantilla
    data = df.to_dict(orient='records')
    
   
    # Renderizar la plantilla HTML y pasar los datos
    return render_template('blog.html', data=data)
    
    

@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/store')
def store():
    
    archivo= r'.venv\data\DatosTemperatura.csv'
    
    df = pd.read_csv(archivo)
    
    # Asegurarse de que los nombres de las columnas están correctos
    df.columns = df.columns.str.strip()
    
    df = df.drop_duplicates()

   # Obtener solo los primeros 50 registros
    df = df.head(50)
    
    # Convertir df a una lista de diccionarios para pasar a la plantilla
    data = df.to_dict(orient='records')
    
    # Renderizar la plantilla HTML y pasar los datos
    return render_template('store.html', data=data)




@app.route('/testimonial')
def testimonial():
    return render_template('testimonial.html')

if __name__ == '__main__':
    app.run(debug=True)