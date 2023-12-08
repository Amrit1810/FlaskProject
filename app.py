from flask import Flask, redirect, render_template
from views import views

app = Flask(__name__, static_folder='static')

app.secret_key = 'MySecretKey'

app.register_blueprint(views, url_prefix = "/")

@app.route('/')
def home():
    return redirect('/about')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug = True, port = 5000)
