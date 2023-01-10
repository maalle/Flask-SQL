import sqlite3
from flask import Flask, render_template, request
app = Flask(__name__)

@app.get( "/")
def listing():
    with sqlite3.connect( "Ruokalista.db") as con:
        cur = con.cursor()
        entries = []
       
        for row in cur.execute( "SELECT id, nimi, hinta FROM ruokalista"):
            rank = row[ 0]
            article = row[ 1]
            price = '{:.2f}'.format( row[ 2]) + '€'
            entries.append( [rank, article, price])

        return render_template( "Ruokalista2.html", entries = entries)
                                
@app.post( "/add<article>/<price>") #JQuery.post()
def addition( article, price):
    with sqlite3.connect( "Ruokalista.db") as con:
        con.execute( "INSERT INTO ruokalista (nimi, hinta) VALUES(article, price)")
        cur = con.cursor()
        entries = []
       
        for row in cur.execute( "SELECT id, nimi, hinta FROM ruokalista"):
            rank = str( row[ 0]) + '.'
            article = row[ 1]
            price = '{:.2f}'.format( row[ 2]) + '€'
            entries.append( [rank, article, price])

        return render_template( "Ruokalista2.html", entries = entries)
            
@app.delete( "/remove<row>") #JQuery.delete()
def removal( row):
    with sqlite3.connect( "Ruokalista.db") as con:
        con.execute( "DELETE FROM ruokalista WHERE id = " + row)
        cur = con.cursor()        
        entries = []
       
        for row in cur.execute( "SELECT id, nimi, hinta FROM ruokalista"):
            rank = str( row[ 0]) + '.'
            article = row[ 1]
            price = '{:.2f}'.format( row[ 2]) + '€'
            entries.append( [rank, article, price])

        return render_template( "Ruokalista2.html", entries = entries)
