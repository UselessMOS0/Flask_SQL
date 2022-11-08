from flask import Flask, render_template, url_for, request, redirect
import pandas as pd

  # collegamento Database SQL
import pymssql
conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS', user='bono.walter1', password='xxx123##', database='bono.walter')

app = Flask(__name__)



@app.route('/', methods=['GET','POST'])
def home():
    return  render_template('home.html')



@app.route('/search', methods=['GET'])
def search():
    return  render_template('search.html')


@app.route('/result', methods=['GET'])
def result():
    client_id = request.args['client_id']
    query = f"SELECT * FROM sales.customers WHERE customer_id = '{client_id}'"
    client_info = pd.read_sql(query,conn)
    print(client_info)
    print('djdjffjkfjdjkfdjkfdjfdjkldfjkdfjksdjksfdjkfdsljkdsfkljdflkjfsdlksdlkjdfskjldfkfdslkjfdslkdlkjkj')
    
    if client_info.values.tolist() == []: 
        return render_template('error.html')
    else:
        return render_template('result.html',colonne = client_info.columns.values, dati = client_info.values)

    
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)