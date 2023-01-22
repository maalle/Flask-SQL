# SQL-Python-Web interface

## SQL
A simple database file is being accessed through the Python program with the **sqlite3** library. 
Prepare / reset the database with:  
```
sqlite3 ruokalista.db < ruokalista.sql
```

## Python
The **Flask** library is being used to run a web page containing the user interface.
Virtual environment is being used, it's activated with:
```
python3 -m venv venv/
source venv/bin/activate
```
The program is being run with:
```
python3 app.py
```
Or alternatively in the debug mode with:
```
flask --app app --debug run
```
The virtual environment is being deactivated with:
```
deactivate
```

## Web
A HTML page contains a table of forms with **Jinja** templates to view and manipulate the database. It's being hosted in:

http://localhost:5000
