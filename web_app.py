import webbrowser

from flask import Flask, render_template, request, jsonify
import inheritedglyphs


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def convert():
    output = inheritedglyphs.convert(request.form['input'])
    return render_template("index.html", output = output)

if __name__ == '__main__':
    app.run(debug=True)
    #webbrowser.open_new_tab("http://127.0.0.1:5000/")