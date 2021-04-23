from flask import  Flask , render_template
app = Flask(__name__)
from app import app





# Views
@app.route('/')
@app.route('/home')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    
    return render_template('base.html',title = 'Home')

@app.route('/about')
def about():

    '''
    View root page function that returns the index page and its data
    '''

    about_page= 'Into the'
    return render_template('about.html',title = 'About')