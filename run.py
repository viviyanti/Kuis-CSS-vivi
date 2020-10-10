from flask import Flask, render_template, redirect, url_for
from forms import mahasiswa_F

app=Flask(__name__)
app.config['SECRET_KEY']="vividaaaa"

data_mahasiswa=[
    {'nama':'Viviyanti iksan',
     'kelas':'info 3',
     'alamat':'jati'},

    {'nama':'evalovita',
     'kelas':'info 3',
     'alamat':'jati'},

    {'nama':'evalovita',
     'kelas':'info 3',
     'alamat':'jati'},
]
@app.route("/")
def home():
    return render_template ("home.html")

@app.route("/about")
def about():
    return render_template ("about.html")

@app.route("/data_mahasiswa", methods=['GET', 'POST'])
def data_m():
    form=mahasiswa_F()
    if form.validate_on_submit():
        return redirect(url_for('data_m'))
    return render_template ("data-mahasiswa.html", data_mahasiswa=data_mahasiswa, form=form)

@app.route("/artikel/<info>")
def artikel_info(info):
    return "halaman artikel " + info;

if __name__=="__main__":
    app.run(debug=True)