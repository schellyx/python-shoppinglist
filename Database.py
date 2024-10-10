import sqlite3

#verbinden mit datenbank
def connect_database():
    return sqlite3.connect("shoppinglist.db")

def create_table():
    db = connect_database()
    cursor = db.cursor()

#erstellt eine tabelle namens items
    query = """
            CREATE TABLE IF NOT EXISTS Items
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(64) NOT NULL,
            amount INTEGER NOT NULL,
            price REAL NOT NULL
        )
            """
    cursor.execute(query)
#damit wird execute ausgeführt
    db.commit()
    db.close()

def add_item(name, amount, price):
    db = connect_database()
    cursor = db.cursor()

    query = f"""
            INSERT INTO Items (name, amount, price)
            values
            ('{name}', {amount}, {price})
            """
    cursor.execute(query)
#damit wird execute ausgeführt
    db.commit()
    db.close()

def select_items():
    db = connect_database()
    cursor = db.cursor()

    query = f"""
            select * from Items
            """
    cursor.execute(query)
    items = cursor.fetchall()
#damit wird execute ausgeführt
    db.commit()
    db.close()
    return items

def update_item(id, name, amount, price):
    db = connect_database()
    cursor = db.cursor()

#item verändern 
    query = f"""
            update items set name = '{name}', amount = {amount}, price = {price} where id = {id} 
            """
    cursor.execute(query)
#damit wird execute ausgeführt
    db.commit()
    db.close()

def delete_item(id):
    db = connect_database()
    cursor = db.cursor()

    query = f"""
            delete from items where id = {id}
            """
    cursor.execute(query)
#damit wird execute ausgeführt
    db.commit()
    db.close()
    