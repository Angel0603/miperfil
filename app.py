from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head>
        <title>Mi Perfil Web con Flask</title>
    </head>
    <body>
        <!-- Mostrar una imagen -->
        <img src="images/mifoto.png" alt="Mi foto de perfil">

        <!-- Botón para mostrar la información -->
        <button onclick="mostrarInfo()">Ver información</button>

        <!-- Contenedor donde se mostrará la información -->
        <div id="info" style="display:none;">
            <ul>
                <li>Ángel de Jesús Lara Barrera</li>
                <li>9no</li>
                <li>B</li>
            </ul>
        </div>

        <script>
        function mostrarInfo() {
            // Cambia el estilo del contenedor para mostrarlo cuando se hace clic en el botón
            var contenedorInfo = document.getElementById('info');
            contenedorInfo.style.display = 'block';
        }
        </script>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
