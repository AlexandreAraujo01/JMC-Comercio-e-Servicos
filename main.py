from flask import Flask
from flask import jsonify,make_response
from flask import request
from flask_cors import CORS
from db import JMC
from flask import Flask, render_template, json, request, jsonify

db = JMC()
app = Flask(__name__)
CORS(app,resources={r'/*' : {"origins": '*'}})


@app.route('/api/exemplo',methods=['POST'])
def teste():
    data = request.get_json()
    print(data)
    return '1'


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_all/<table_name>',methods=["GET"])
def get_all(table_name):
    res = db.get_all_data(table_name)
    return res

@app.route('/Getfornecedores')
def get_fornecedores():
    res = db.get_fornecedores()
    return res

@app.route('/insert_data',methods=['POST'])
def post_data():
    data = request.get_json()
    res = db.new_insert_data(data['table'],data)
    return res


@app.route('/delete_data',methods=['DELETE'])
def delete_data():
    data = request.get_json()
    db.exclude_data(data['table'],data['column'],data['value'])
    return "linha excluida"

@app.route('/alter_data',methods=['PUT'])
def update_data():
    data = request.get_json()
    table =data['table']
    column = data['column']
    value = data['value']
    id = data['id']
    db.alter_data(table,column,value,id)
    return f"linha com id={id} alterada"


if __name__ == "__main__":
    app.run(debug=True)