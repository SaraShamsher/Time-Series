from flask import Flask, request, jsonify
import requests
import json
import sqlite3

app = Flask(__name__)

@app.route('/companyDetails',methods=['GET'])
def insert_data(url):
    try:
        
        response = requests.get(url).json()
        return response

    except:
        print('Error Occurred while inserting data')
        return None



if __name__ == '__main__':
    insert_data('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&apikey=NQCFKOVGZASY3EZ9&symbol=MSFT')
    app.run(port=5000,debug=True)

