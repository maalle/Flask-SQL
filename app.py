import sqlite3_procedures
from flask import Flask, render_template, request
app = Flask( __name__)

def render( mode):
    data = sqlite3_procedures.import_contents()
    return render_template( 'main.html', data = data, mode = mode)

@app.get( "/") # The first page load
def init():
    return render( 'view')

@app.post( "/")
def display():
    action = request.form.get( 'action')
    id = request.form.get( 'id')
    article = request.form.get( 'article')
    price = request.form.get( 'price')

    if action == 'enter insert':
        mode = 'insert'
    elif action == 'complete insert':
        if sqlite3_procedures.add_check( article) == True: # Prevent duplicate
            sqlite3_procedures.insert( article, price)

        mode = 'view'
    elif action == 'enter modify':
        mode = int( id) # Data type!
    elif action == 'complete modify':
        if sqlite3_procedures.modify_check( id, article) == True: # Prevent duplicate
            sqlite3_procedures.modify( id, article, price)

        mode = 'view'
    elif action == 'cancel':
        mode = 'view'
    elif action == 'delete':
        sqlite3_procedures.delete( id)
        mode = 'view'

    return render( mode)