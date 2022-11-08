from flask import Flask, render_template, url_for, request, redirect
import pandas as pd

  # collegamento Database SQL
import pymssql
conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS', user='bono.walter1', password='xxx123##', database='bono.walter')

app = Flask(__name__)



@app.route('/', methods=['GET','POST'])
def home():
    return  render_template('home.html')

@app.route('/infoUser', methods=['GET'])
def infoUser():
  return  render_template('infoUser.html')


@app.route('/result', methods=['GET'])
def result():
  first_name = request.args['first_name']
  last_name = request.args['last_name']
  query = f"SELECT * FROM sales.customers WHERE first_name = '{first_name}' and last_name = '{last_name}'"
  df_clients = pd.read_sql(query,conn)
  return  render_template('result.html',colonne = df_clients.columns.values, dati = df_clients.values)

    
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)