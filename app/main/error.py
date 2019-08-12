from flask import render_template
from . import main

@main.app_errorhandler(404)
def four_Ow_four(error):
    '''
    Function to render the 404 error pag
    '''
    return render_template('fourOfour.html'),404
