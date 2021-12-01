from flask import Flask, request, jsonify
import requests
import json
import sqlite3

app = Flask(__name__)

@app.route('/companyDetails',methods=['GET'])
def insert_data(url):
    try:
        
        response = requests.get(url).json()
        #print(response)
        print(response['Meta Data']['2. Symbol'])
        print(response['Time Series (Daily)']['2021-11-30'])
        print(response['Time Series (Daily)'][0])
        for row in response['Time Series (Daily)']['2021-11-29']:
            print(row)
            
    except:
        print('Error Occurred while inserting data')
        return None



if __name__ == '__main__':
    insert_data('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&apikey=NQCFKOVGZASY3EZ9&symbol=MSFT')
    app.run(port=5000,debug=True)

