import json
import pymysql


class JMC():
    "bla bla"
    def __init__(self):
        self.conection = pymysql.connect(host="localhost",database='impacta',user='root',password='admin',port=3306)
        self.db_cursor = self.conection.cursor()

    def get_all_data(self,table):
        """seleciona todas as linhas da tabela especificada"""
        query = f"SELECT * FROM `{table}`;"
        self.db_cursor.execute(query)
        res = self.db_cursor.fetchall()
        return json.dumps(res,default=str)
    
    def get_fornecedores(self):
        query = f"SELECT id,razao_social from Fornecedor"
        self.db_cursor.execute(query)
        res = self.db_cursor.fetchall()
        return json.dumps(res,default=str)
        
    
    def get_specific(self,table,column,value):
        query = f"SELECT * FROM `{table}` WHERE {column} = {value}"
        self.db_cursor.execute(query)
        res = self.db_cursor.fetchall()
        return json.dumps(res,default=str)

    def new_insert_data(self,table,dict):

        dic_columns = {'FORNECEDOR': ['cnpj','razao_social','email','telefone','logradouro','complemento','bairro','cep'],
                        'CLIENTE' :  ['cpf','nome','telefone','cep','logradouro','complemento','bairro'],
                        'PRODUTOS': ['id_fornecedor','nome_produto','valor','descricao','quantidade','data_validade']}

        values_list = [f'"{value}"' if isinstance(value,str) else str(value)  for value in dict['values']]
        values = ','.join(values_list)
        

        columns_list = dic_columns[table.upper()]
        columns_list = columns_list[:len(values_list)]
        columns = ','.join(columns_list)
        try:
            query = f"INSERT INTO `{table}` ({columns}) VALUES ({values});"
            self.db_cursor.execute(query)
            self.db_cursor.fetchall()
            self.conection.commit()
            return "Adicionado com sucesso"
        except Exception as e:
            print(e)
            return "erro ao adicionar cpf já existente"
   
    def exclude_data(self,table,column,value):
        """Função que exclui uma linha de uma tabela especificada"""
        query = f"delete from {table} where {column} = {value};"
        self.db_cursor.execute(query)
        self.conection.commit()
    
    def alter_data(self,table,column,value,id):
        dic = {"CLIENTE": "id_cliente","PRODUTO": "id_produto"}
        id_column = dic.get(table.upper(),'NULO')
        
        if id_column == 'NULO':
            print('Tabela não existe')
        else:
            query = f'UPDATE {table} SET {column} = "{value}" WHERE {id_column} = {id};'
            print(query)
            self.db_cursor.execute(query)
            self.conection.commit()


if __name__ == "__main__":
    x = JMC()
    # x.get_all_data('Fornecedor')
    # x.insert_data('Fornecedor','12345678912','teste','teste@gmail.com',1)
    # x.get_all_data('Fornecedor')
    #print(x.get_all_data('Cliente'))
    #print(x.insert_data('Cliente','49000535931','Monique','5511955527089','02231007'))
    #x.new_insert_data('Cliente',{"table": "Cliente","values": ['49000535931','Monique','5511955527089','02231007']})
    x.alter_data('Cliente','nome','Alexandre',9)
    print(x.get_all_data('Cliente'))

   

