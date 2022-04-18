from flask import Flask, render_template, render_template_string, make_response, send_from_directory, url_for, redirect, request, session
import os
import base64

app = Flask(__name__,static_folder='static')
app.secret_key = os.urandom(16)

rick_uname = 'r1CkA7sL3y'


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session['authed'] = True
        if request.form['username'] == rick_uname:
            resp = make_response(redirect(url_for('dashboard', username=rick_uname)))
            resp.set_cookie('user', (base64.b64encode(b'Rick')).decode())
            return resp
        else:
            return redirect(url_for('dashboard', username=request.form['username']))
    else:
        return render_template('login.html')


@app.route('/dashboard/<username>')
def dashboard(username):
    if 'authed' not in session:
        return redirect(url_for('login'))
    
    if username != rick_uname:
        return render_template('guest.html')

    if not request.cookies.get('user'):
            resp = make_response(redirect(url_for('dashboard', username=rick_uname)))
            resp.set_cookie('user', (base64.b64encode(b'Rick')).decode())
            return resp
    
    name = base64.b64decode(request.cookies['user']).decode()
    
    
    if '.' in name:
        return "Hey, I don't like dot"
    
    TEMPLATE = render_template_string("Wellcome <strong>" + name + "</strong>")
    return render_template('dashboard.html', wellcome=TEMPLATE)


@app.route('/logout')
def logout():
    session.pop('authed')
    return redirect(url_for('login'))


@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
