import sqlite3_procedures
from flask import Flask, render_template, request
app = Flask( __name__)

def is_valid_price( price):
    try: # Is the price a valid number?
        price = float( price)

        if (price > 0) & (100 * price == int( 100 * price)): return True # Does the price round to cents?
        else: return False

    except: return False

def render( mode, feedback):
    data = sqlite3_procedures.import_contents()
    return render_template( 'main.html', data = data, mode = mode, feedback = feedback)

@app.get( "/") # The first page load
def init():
    return render( 'view', [])

@app.post( "/")
def display():
    action = request.form.get( 'action'); id = request.form.get( 'id'); article = request.form.get( 'article'); price = request.form.get( 'price')
    feedback = []

    if action == 'enter insert':
        mode = 'insert'
    elif action == 'complete insert':
        if len( article) == 0:
            feedback = ['Attempt to insert an empty article rejected.']
        elif sqlite3_procedures.add_check( article) == False: # Prevent duplicate
            feedback = ['Attempt to insert a duplicate article rejected.']

        if is_valid_price( price) == False:
            feedback.append( 'Attempt to insert an invalid price rejected.')

        if feedback == []:
            sqlite3_procedures.insert( article, price)

        mode = 'view'
    elif action == 'enter modify':
        mode = int( id) # Data type!
    elif action == 'complete modify':
        if len( article) == 0:
            feedback = ['Attempt to remove an article name rejected.']
        elif sqlite3_procedures.modify_check( id, article) == False: # Prevent duplicate
            feedback = ['Attempt to take a name of an existing article rejected.']

        if is_valid_price(price) == False:
            feedback.append( 'Attempt to change a price into invalid value rejected.')

        if feedback == []:
            sqlite3_procedures.modify( id, article, price)

        mode = 'view'
    elif action == 'cancel':
        mode = 'view'
    elif action == 'delete':
        sqlite3_procedures.delete( id)
        mode = 'view'

    return render( mode, feedback)