from flask import Flask , render_template
import random
from Data.film import pictures

app = Flask(__name__)


@app.route('/')
def home():
       return render_template('home.html')

@app.route('/pictures')
def show_pictures():
       return render_template('pictures.html', pictures=pictures)

@app.route('/api/picture/<int:id>')
def getpictureid(id):
       id=int(id)
       picture=None
       if 0 <= id < len(pictures):
        picture = pictures[id]
       return render_template('picture.html', picture = picture)

# def shuffle_pictures():
#        random.shuffle(pictures)


