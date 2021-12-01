from flask import Flask, request, jsonify
import requests
import json
import sqlite3

app = Flask(__name__)

@app.route('/companyDetails', methods=['GET'])
def insert_data():
    try:
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&apikey=NQCFKOVGZASY3EZ9&symbol=MSFT'
        response = requests.get(url).json()
        print(data)
        #companyId = request.json['companyId']
        company_name = response['Meta Data']['2. Symbol']
        transaction_date = response['Time Series (Daily)']["2021-11-30"]
        open = response['Time Series (Daily)']["2021-11-30"]['1. open']
        high = response['Time Series (Daily)']["2021-11-30"]['2. high']
        low = response['Time Series (Daily)']["2021-11-30"]['3. low']
        close = response['Time Series (Daily)']["2021-11-30"]['4. close']
        adjusted_close = response['Time Series (Daily)']["2021-11-30"]['5. adjusted_close']
        volume = response['Time Series (Daily)']["2021-11-30"]['6. volume']
        print(company_name,transaction_date,open)
        response.content_type = 'application/json'
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
        #return dumps(("OK"),default=json_util.default)
            #return redirect(url_for('root'))

    except:
        print('Error Occurred while inserting data')
        return None            

    
if __name__ == '__main__':
    
    app.run(port=8000,debug=True)
