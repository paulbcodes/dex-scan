from flask import Flask, render_template
import json
from web3 import Web3
import asyncio
import os
import sqlite3

infura_url = 'https://mainnet-rpc.satoshichain.io'
web3 = Web3(Web3.HTTPProvider(infura_url))

app = Flask(__name__)

def get_data_from_database():
    conn = sqlite3.connect('token_data.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT * FROM tokens ORDER BY id DESC LIMIT 15''')
    data = cursor.fetchall()

    return data

    # Close the connection
    #conn.close()

    #return data

def get_data_from_database1():
    conn = sqlite3.connect('token_data.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT * FROM tokens ORDER BY id ASC''')
    data = cursor.fetchall()
    return data

def get_data_from_database2():
    conn = sqlite3.connect('token_data.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT * FROM tokens ORDER BY id DESC LIMIT 3''')
    data = cursor.fetchall()
    return data




@app.route("/")

def display():
    # Read the price from the separate txt file
    with open('price.txt') as price_file:
        price = price_file.read()
    # Call the function to retrieve data from the database
    data = get_data_from_database2()

    # Pass the data to the template
    return render_template('index.html', data=data, price=price)

    

    # Close the database connection
    #conn.close()

    #return render_template('index.html', token_data=token_data, price=price)

    #return user_data
    #return render_template('index.html', token0_name=token0_name, token0_ticker=token0_ticker, token1_name=token1_name, token1_ticker=token1_ticker, web_link=web_link, token1_supply=token1_supply, price=price, deployer=deployer)

@app.route("/new")
def about():
    with open('price.txt') as price_file:
        price = price_file.read()
        # Call the function to retrieve data from the database
        data = get_data_from_database()

        # Pass the data to the template
        return render_template('new.html', data=data, price=price)

@app.route("/all")
def all():
    with open('price.txt') as price_file:
        price = price_file.read()

        # Call the function to retrieve data from the database
        data = get_data_from_database1()

        # Pass the data to the template
        return render_template('all.html', data=data, price=price)
    






if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
