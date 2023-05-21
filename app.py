from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('page.html')

@app.route('/shar.html', methods=['post', 'get'])
def shar():
    R = 0
    toch = 0
    if request.method == 'POST':
        R = float(request.form.get('R'))
        toch = int(request.form.get('toch'))
    gdz = round(((4 / 3) * 3.14 * R * R * R), toch)
    return render_template('shar.html', ans = gdz)

@app.route('/kub.html', methods=['post', 'get'])
def kub():
    a = 0
    toch = 0
    if request.method == 'POST':
        a = float(request.form.get('a'))
        toch = int(request.form.get('toch'))
    gdz = round(a * a * a, toch)
    return render_template('kub.html', ans = gdz)

@app.route('/konus.html', methods=['post', 'get'])
def konus():
    R = 0
    h = 0
    toch = 0
    if request.method == 'POST':
        R = float(request.form.get('R'))
        h = float(request.form.get('h'))
        toch = int(request.form.get('toch'))
    gdz = round((1/3) * 3.14 * R * R *h, toch)
    return render_template('konus.html', ans = gdz)

@app.route('/tcilindr.html', methods=['post', 'get'])
def tcilindr():
    R = 0
    h = 0
    toch = 0
    if request.method == 'POST':
        R = float(request.form.get('R'))
        h = float(request.form.get('h'))
        toch = int(request.form.get('toch'))
    gdz = round(3.14 * R * R * h, toch)
    return render_template('tcilindr.html', ans = gdz)

@app.route('/piramida.html', methods=['post', 'get'])
def piramida():
    S = 0
    h = 0
    toch = 0
    if request.method == 'POST':
        S = float(request.form.get('S'))
        h = float(request.form.get('h'))
        toch = int(request.form.get('toch'))
    gdz = round((1/3) * S * h, toch)
    return render_template('piramida.html', ans = gdz)

@app.route('/parallelepiped.html', methods=['post', 'get'])
def parallelepiped():
    a = 0
    b = 0
    c = 0
    toch = 0
    if request.method == 'POST':
        a = float(request.form.get('a'))
        b = float(request.form.get('b'))
        c = float(request.form.get('c'))
        toch = int(request.form.get('toch'))
    gdz = round(a * b * c, toch)
    return render_template('parallelepiped.html', ans = gdz)

if __name__ == '__main__':
    app.run()