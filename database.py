import sqlite3

#Open database
conn = sqlite3.connect('database.db')

#Create table
conn.execute('''create table company
        (companyId INTEGER PRIMARY KEY,
        company_name TEXT,
        transaction_date DATE,
        open DECIMAL,
        high DECIMAL,
        low DECIMAL,
        close DECIMAL,
        adjusted_close DECIMAL,
        volume BIGINT
		)''')


conn.close()