from flask import Flask,render_template, request, redirect
from pathlib import Path
import dir

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", files=dir.list())

@app.route('/view')
def view():
    file = request.args.get('file')
    return render_template("view.html", content=dir.html(file), title=Path(file).name, file=file)

@app.route('/edit')
def edit():
    file = request.args.get('file')
    return render_template("edit.html", title=Path(file).name, content=dir.raw(file), file=file)

@app.route('/save', methods=['POST'])
def save():
    contents = request.form['contents']
    file = request.form['file']
    dir.save(file, contents)
    return redirect("/view?file="+file)

@app.route('/new', methods=['POST'])
def new():
    new_file = request.form['new_file']
    dir.new(new_file)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')