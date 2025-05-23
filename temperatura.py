from flask import Flask, request, flash, render_template_string

app = Flask(__name__)
app.secret_key = 'clave_super_secreta'

HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>Formulario de Sensor</title>
    <style>
        body { 
            font-family: Arial, sans-serif; 
            max-width: 500px; 
            margin: 0 auto; 
            padding: 20px;
        }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; font-weight: bold; }
        input, select { 
            width: 100%; 
            padding: 8px; 
            box-sizing: border-box;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        button { 
            background-color: #4CAF50; 
            color: white; 
            padding: 10px 15px; 
            border: none; 
            border-radius: 4px; 
            cursor: pointer;
            width: 100%;
        }
        button:hover { background-color: #45a049; }
        .flash { 
            padding: 10px; 
            background-color: #dff0d8; 
            border: 1px solid #d6e9c6; 
            color: #3c763d; 
            border-radius: 4px; 
            margin-bottom: 15px;
        }
        .data-display {
            margin-top: 20px;
            padding: 15px;
            background-color: #f8f9fa;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <h1>Formulario de Datos de Sensor</h1>
    
    {% with messages = get_flashed_messages() %}
        {% if messages %}
            {% for message in messages %}
                <div class="flash">{{ message }}</div>
            {% endfor %}
        {% endif %}
    {% endwith %}
    
    <form method="POST">
        <div class="form-group">
            <label for="sensor_id">ID del Sensor:</label>
            <input type="text" id="sensor_id" name="sensor_id" required>
        </div>
        
        <div class="form-group">
            <label for="temperature">Temperatura:</label>
            <input type="number" id="temperature" name="temperature" step="0.1" required>
        </div>
        
        <div class="form-group">
            <label for="vibration">Vibración:</label>
            <input type="number" id="vibration" name="vibration" step="0.01" required>
        </div>
        
        <div class="form-group">
            <label for="status">Estado:</label>
            <select id="status" name="status">
                <option value="normal">Normal</option>
                <option value="warning">Advertencia</option>
                <option value="critical">Crítico</option>
                <option value="offline">Desconectado</option>
            </select>
        </div>
        
        <button type="submit">Enviar Datos</button>
    </form>
    
    {% if data %}
    <div class="data-display">
        <h2>Datos Enviados:</h2>
        <p><strong>ID del Sensor:</strong> {{ data.sensor_id }}</p>
        <p><strong>Temperatura:</strong> {{ data.temperature }}</p>
        <p><strong>Vibración:</strong> {{ data.vibration }}</p>
        <p><strong>Estado:</strong> {{ data.status }}</p>
    </div>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def formulario_sensor():
    data = None
    if request.method == 'POST':
        sensor_id = request.form['sensor_id']
        temperature = request.form['temperature']
        vibration = request.form['vibration']
        status = request.form['status']

        data = {
            'sensor_id': sensor_id,
            'temperature': temperature,
            'vibration': vibration,
            'status': status
        }

        flash('Datos enviados correctamente.')

    return render_template_string(HTML, data=data)

# IMPORTANTE: No uses app.run() en Render
# Esto permite que Gunicorn lo reconozca como punto de entrada
application = app

