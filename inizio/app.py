from flask import Flask, render_template, url_for, request, redirect
import pandas as pd

  # collegamento Database SQL
import pymssql
conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS', user='bono.walter1', password='xxx123##', database='bono.walter')

app = Flask(__name__)



@app.route('/', methods=['GET','POST'])
def home():
  if not request.method == 'POST':
    return  render_template('home.html')
  else:
    selectedValue = int(request.form['flexRadioDefault'])
    if selectedValue in range(0,2):
      
      return redirect(url_for('tabella', selectedValue=selectedValue))
    else:
      return redirect(url_for('search'))


@app.route('/tabella-<selectedValue>', methods=['GET'])
def tabella(selectedValue):
  return  render_template('tabella.html')


@app.route('/search', methods=['GET'])
def search():
  return  render_template('search.html')


@app.route('/result', methods=['GET'])
def result():
  # invio query al Database e ricezionee informazioni
  NomeProdotto = request.args['NomeProdotto']
  query = f"SELECT * FROM production.products WHERE product_name LIKE '{NomeProdotto}%'"
  df_prodotti = pd.read_sql(query,conn)
  # visualizzare le informazioni
  
  return  render_template('result.html',colonne = df_prodotti.columns.values, dati = df_prodotti.values)

    
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)