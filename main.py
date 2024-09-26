from flask import Flask
import random
app = Flask(__name__)

facts_list = [
    "Kebanyakan orang yang menderita kecanduan teknologi mengalami stres yang kuat ketika mereka berada di luar area jangkauan jaringan atau tidak dapat menggunakan perangkat mereka",
    "Menurut sebuah studi yang dilakukan pada tahun 2018, lebih dari 50% orang berusia 18 hingga 34 tahun menganggap diri mereka bergantung pada ponsel pintar mereka.",
    "Studi tentang ketergantungan teknologi adalah salah satu bidang penelitian ilmiah modern yang paling relevan"
]

elements = "+-/*!&$#?=@<>"

def gen_pass(pass_length):
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

@app.route("/")
def hello_world():
    return '<h1>Hello, World!</h1><a href="/acak">View a random fact!</a><a href="/password">View a random password!</a>'


@app.route("/acak")
def nama():
    return f'{random.choice(facts_list)}'

@app.route("/password")
def password():
    return f'Password: {gen_pass(12)}'


app.run(debug=True)
