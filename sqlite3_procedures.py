import sqlite3

def import_contents():
    with sqlite3.connect( "Ruokalista.db") as con:
        cur = con.cursor(); contents = []

        for entry in cur.execute( "SELECT id, nimi, hinta FROM ruokalista"):
            contents.append( (entry[ 0], entry[ 1], entry[ 2]))

    return contents

def insert( article, price):
    with sqlite3.connect( "Ruokalista.db") as con:
        con.execute( "INSERT INTO ruokalista( nimi, hinta) VALUES( '" + article + "', '" + price + "')")

def modify( id, article, price):
    with sqlite3.connect( "Ruokalista.db") as con:
        con.execute( "UPDATE RUOKALISTA SET nimi = '" + article + "', hinta = '" + price + "' WHERE id = " + id)

def delete( id):
    with sqlite3.connect( "Ruokalista.db") as con:
        con.execute( "DELETE FROM ruokalista WHERE id = " + id)

def add_check( article):
    ok = True

    with sqlite3.connect( "Ruokalista.db") as con:
        cur = con.cursor()

        for entry in cur.execute( "SELECT nimi FROM ruokalista"):
            if str.lower( entry[ 0]) == str.lower( article): # Case insensitive
                ok = False; break

    return ok

def modify_check( id, article):
    ok = True

    with sqlite3.connect( "Ruokalista.db") as con:
        cur = con.cursor()

        for entry in cur.execute( "SELECT id, nimi FROM ruokalista"):
            if (entry[ 0] != int( id)) & (str.lower( entry[ 1]) == str.lower( article)):
                ok = False; break

    return ok
