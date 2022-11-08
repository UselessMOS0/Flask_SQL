from flask import Flask, render_template, url_for, request, redirect
import pandas as pd
import pymssql
import math

conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS', user='bono.walter1', password='xxx123##', database='bono.walter')

app = Flask(__name__)



@app.route('/', methods=['GET','POST'])
def home():
  return  render_template('home.html')

@app.route('/bestCustomers', methods=['GET','POST'])
def bestCustomers():
    query = 'SELECT customers.customer_id, SUM(products.list_price) as totale_spesa FROM sales.customers inner join sales.orders on customers.customer_id = orders.customer_id inner join sales.order_items on orders.order_id = order_items.order_id inner join production.products on order_items.product_id = products.product_id GROUP BY customers.customer_id ORDER BY SUM(products.list_price) DESC;'
    clients = pd.read_sql(query,conn).head(10)
    return  render_template('bestCustomers.html',colonne = clients.columns.values, dati = clients.values)

@app.route('/ordini/<value>', methods=['GET','POST'])
def ordini(value):
  value = math.floor(float(value))
  print(value)
  query = f'SELECT customer_id, count(order_id) as ordini FROM sales.orders WHERE customer_id = {value} GROUP BY customer_id'
  ordini_cliente = pd.read_sql(query,conn)
  return  render_template('ordini.html',colonne = ordini_cliente.columns.values, dati = ordini_cliente.values)
    
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)