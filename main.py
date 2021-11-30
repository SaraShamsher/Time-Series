from flask import Flask, request, jsonify
import requests
import json
import sqlite3

app = Flask(__name__)

@app.route('/companyDetails', method=['POST'])
def insert_data(url):
    try:
        data = requests.get(url).json()
        for row in data:
            #companyId = request.json['companyId']
            company_name = request.json['Symbol']
            transaction_date = request.json['Time Series']
            open = request.json['open']
            high = request.json['high']
            low = request.json['low']
            close = request.json['close']
            adjusted_close = request.json['adjusted_close']
            volume = request.json['volume']
            with sqlite3.connect('database.db') as conn:
                try:
                    cur=conn.cursor()
                    cur.execute('''INSERT INTO company (company_name,transaction_date,open,high,low,close,adjusted_close,volume)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (company_name,transaction_date,open,high,low,close,adjusted_close,volume))
                    conn.commit()
                    msg='added successfully'
                except:
                    msg='error'
                    conn.rollback()
            conn.close()
            print(msg)
            #return redirect(url_for('root'))

    except:
        print('Error Occurred while inserting data')
        return None

            

    
if __name__ == '__main__':
    insert_data('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&apikey=NQCFKOVGZASY3EZ9&symbol=MSFT')
    app.run(port=8000,debug=True)
