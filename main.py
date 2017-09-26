from flask import Flask
from caesar import rotate_string
from flask import Flask, request


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
        <form method="post">
            <div>
                <label for="rot">Rotate by:</label>
                <input type="text" name="rot" value="0">
                <p class="error"></p>
            </div>
            <textarea type="text" name="text">{0}</textarea>
            <br>
            <input type="submit">

        </form>
    </body>
</html>

"""
@app.route("/")
def index():
    return form.format()

@app.route("/", methods=['POST'])
def encrypt():
       
        rot = int(request.form['rot'])
        input_text = request.form['text']
        encrypted_text = rotate_string(input_text, rot) 
        #return '<h1>'+encrypted_text+'</h1>'
        return form.format(encrypted_text)
app.run() 