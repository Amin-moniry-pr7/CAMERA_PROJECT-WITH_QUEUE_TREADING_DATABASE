from datetime import datetime
import sqlite3


def ENTERE():

    process = sqlite3.connect("FRAME_PROCESSING.db")
    cursor = process.cursor()
    cursor.execute(''' CREATE TABLE IF NOT EXISTS PROCESS 
    (id INTEGER PRIMARY KEY AUTOINCREMENT, class_name TEXT, file_path TEXT, timestamp TEXT) ''')
    process.commit()
    return process

def save_to_db(process, class_name, file_path):
    cursor = process.cursor()
    ALL_class_name = f"TABLE_{class_name.upper()}"
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {ALL_class_name} 
    (id INTEGER PRIMARY KEY AUTOINCREMENT, file_path TEXT, timestamp TEXT)''')

    # Insert the record into the class-specific table
    cursor.execute(f'''INSERT INTO {ALL_class_name} (file_path, timestamp) VALUES (?, ?)''', (file_path, timestamp))

    process.commit()
