from flask import Flask, render_template, jsonify
from tinydb import TinyDB, Query
import random
app = Flask(__name__)
db = TinyDB('db.json')


@app.route('/')
def hello_world():
    db_list = db.all()
    ran_rec = random.choice(db_list)
    return render_template('index.html', recipe=ran_rec)
