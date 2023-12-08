import sqlite3
import hashlib
from SampleDataGeneration import *


def sample_data_fill():
    # Establishing a Connection
    con = sqlite3.connect('websitedata.db')  # , autocommit = False)
    cursor = con.cursor()
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (primaryKey TEXT PRIMARY KEY, name TEXT NOT NULL, age INTEGER NOT NULL, 
    gender TEXT NOT NULL, linkedinProfURL TEXT, designation TEXT, country TEXT, disabled TEXT, FreshExp TEXT, 
    joinedDate TEXT, profileDescription TEXT, username TEXT NOT NULL, email TEXT NOT NULL, password TEXT NOT NULL);""")
    
    data_list = create_sample_dataset()

    # Iterate through each record and insert into the 'users' table
    for data in data_list:
        cursor.execute('''
            INSERT INTO users (
                primaryKey, name, age, gender, linkedinProfURL,
                designation, country, disabled, FreshExp,
                joinedDate, profileDescription, username, email,
                password
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            data['primaryKey'],
            data['name'],
            data['age'],
            data['gender'],
            data['linkedinProfURL'],
            data['designation'],
            data['country'],
            data['disabled'],
            data['FreshExp'],
            data['joinedDate'],
            data['profileDescription'],
            data['username'],
            data['email'],
            data['password']
        ))

    # Commit changes and close the connection
    con.commit()
    con.close()
    
    
    
def data_fill(**kwargs):
    # Establishing a Connection
    con = sqlite3.connect('websitedata.db')  # , autocommit = False)
    cursor = con.cursor()
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (primaryKey TEXT PRIMARY KEY, name TEXT NOT NULL, age INTEGER NOT NULL, 
    gender TEXT NOT NULL, linkedinProfURL TEXT, designation TEXT, country TEXT, disabled TEXT, FreshExp TEXT, 
    joinedDate TEXT, profileDescription TEXT, username TEXT NOT NULL, email TEXT NOT NULL, password TEXT NOT NULL);""")
    
    data_list = [kwargs]
    
    # Iterate through each record and insert into the 'users' table
    for data in data_list:
        if existence_check(data['email']) != 1:
            cursor.execute('''
                INSERT INTO users (
                    primaryKey, name, age, gender, linkedinProfURL,
                    designation, country, disabled, FreshExp,
                    joinedDate, profileDescription, username, email,
                    password
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                data['primaryKey'],
                data['name'],
                data['age'],
                data['gender'],
                data['linkedinProfURL'],
                data['designation'],
                data['country'],
                data['disabled'],
                data['FreshExp'],
                data['joinedDate'],
                data['profileDescription'],
                data['username'],
                data['email'],
                str(hashlib.sha1(data['password'].encode()).hexdigest())
            ))
        else:
            return 'User Already Exists!'

    # Commit changes and close the connection
    con.commit()
    con.close()
    


def data_fetch(email, password):
    con = sqlite3.connect('websitedata.db')
    con.row_factory = sqlite3.Row  # Set row factory to return rows as dictionaries
    cursor = con.cursor()

    query = 'SELECT * FROM users WHERE email=? AND password=?'
    data = cursor.execute(query, (email, password)).fetchall()
    
    con.close()

    return [dict(row) for row in data]



def existence_check(email):
    con = sqlite3.connect('websitedata.db')
    cursor = con.cursor()

    query = 'SELECT COUNT(*) FROM users WHERE email=?'
    data = list(cursor.execute(query, (email,)))[0][0]
    
    con.close()

    return data



def update_pass(email, new_password):
    con = sqlite3.connect('websitedata.db')
    cursor = con.cursor()

    query = 'UPDATE users SET password=? WHERE email=?'
    cursor.execute(query, (str(hashlib.sha1(new_password.encode()).hexdigest()), email))
    print('Password Updated!')

    con.commit()
    con.close()
