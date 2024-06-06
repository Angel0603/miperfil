from flask import Flask, url_for, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    # Estado inicial es ocultar la información
    mostrar_info = 'ocultar'
    
    # Cuando el formulario se envía, se chequea el valor del campo oculto
    if request.method == 'POST':
        if request.form.get('mostrar_info') == 'mostrar':
            mostrar_info = 'ocultar'  # Cambiar el estado a ocultar para el siguiente clic
        else:
            mostrar_info = 'mostrar'  # Cambiar el estado a mostrar para el siguiente clic

    imagen_url = url_for('static', filename='images/mifoto.png')
    texto_boton = 'Ocultar información' if mostrar_info == 'mostrar' else 'Ver información'
    
    html_content = f"""
    <html>
    <head>
        <title>Mi Perfil Web con Flask</title>
        <style>
            body {{ font-family: 'Arial', sans-serif; background-color: #f4f4f4; color: #333; }}
            img {{ display: block; margin: 20px auto; width: 250px; height: 250px; }}
            button {{ background-color: #36A3EB; color: white; border: none; padding: 10px 20px; text-align: center; display: inline-block; font-size: 16px; margin: 20px auto; cursor: pointer; border-radius: 5px; }}
            #info {{ display: {'block' if mostrar_info == 'mostrar' else 'none'}; text-align: center; }}
            div {{ width: 350px}}
        </style>
    </head>
    <body>
        <img src="{imagen_url}" alt="Mi foto de perfil">
        
        <center>
        <form method="post">
            <input type="hidden" name="mostrar_info" value="{mostrar_info}">
            <button type="submit">{texto_boton}</button>
        </form>
        <center/>
        <center>
        <div id="info">
            <ul>
                <li>Ángel de Jesús Lara Barrera</li>
                <li>9no</li>
                <li>B</li>
            </ul>
        </div>
        
    </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    app.run(debug=True)
