from flask import  Flask , render_template , url_for
app = Flask(__name__)
from app import app

posts = [
    {
        'author': 'David',
        'name': 'human'
    },
    {
        'author': 'Agg',
        'name': 'human2'
    }
]



# Views
@app.route('/')
@app.route('/home')
def index():
    '''
    View root page function that returns the index page and its data
    '''  
    return render_template('home.html',posts = posts)

@app.route('/about')
def about():

    '''
    View root page function that returns the index page and its data
    '''

    about_page= 'Into the'
    return render_template('about.html',title = 'About')