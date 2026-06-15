from flask import Flask, render_template
import socket

app = Flask(__name__)
HOST = "192.168.101.4"
PORT = 12345

def leer_sensor():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            data = s.recv(1024).decode().strip()
            ejeX, ejeY = data.split(',')
            ejeX = float(ejeX.replace('X:', ''))
            ejeY = float(ejeY.replace('Y:', ''))
            return ejeX, ejeY
    except Exception as e:
        print("ERROR:", e)
        return 0, 0

@app.route('/')
def index():
    ejeY, ejeX = leer_sensor()
    return render_template('index.html', ejeX=ejeY, ejeY=ejeX)

# --- NUEVA RUTA PARA EL EJE X ---
@app.route('/ejex')
def vista_x():
    ejeY, ejeX = leer_sensor()
    return render_template('ejex.html', ejeX=ejeY)

# --- NUEVA RUTA PARA EL EJE Y ---
@app.route('/ejey')
def vista_y():
    ejeY, ejeX = leer_sensor()
    return render_template('ejey.html', ejeY=ejeX)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
 
