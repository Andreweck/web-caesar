from flask import Flask, request
import cgi
app = Flask(__name__)
app.config['DEBUG'] = True
form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="csr" method="post">
            <label for="first_name">Rotate by:</label>
            <input id="first_name" type="text" name="rot" value="0"></input>
            <textarea name="text">{0}</textarea>
            <input type="submit" />
        </form>
    </body>
</html>
"""
from caesar import rotate_character, encrypt

@app.route("/csr", methods=['POST'])
def rme():
    message = request.form['text']
    rt = request.form['rot']
    tb = int(rt)
    ecnrypmesse = encrypt(message, tb)
    return form.format(ecnrypmesse)

@app.route("/")
def index():
    return form.format('')
app.run()