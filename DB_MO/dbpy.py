import pandas as pd
import pandasql as pdsql
import sqlite3
import xlrd
from datetime import date
from datetime import datetime


def query_read(code_query):

  conn = sqlite3.connect('static/DB_ALL.db')
  c = conn.cursor()

  select_query = f"""

                    {code_query}
                  
  """

  read_db = pd.read_sql_query(select_query, conn)
  conn.close()

  print("--------------------------------------------------")
  print(read_db)
  print("--------------------------------------------------\n\n" )

  return read_db










##############
## CADASTRO ##
##############

def read_df_nome(nome, sobrenome):

  conn = sqlite3.connect('DB_JSON/DB_MO.db')

  conn.commit()

  select_nome = f"""
                  SELECT * FROM DBMO
                  WHERE NOME LIKE '%{nome}%' AND SOBRENOME LIKE '%{sobrenome}%'

  """

  read_db = pd.read_sql_query(select_nome, conn)
  conn.close()

  return read_db


def read_df_cpf(cpf):

  if cpf[-1] == '-':
    cpfx = cpf[:len(cpf) - 1:]

    conn = sqlite3.connect('DB_JSON/DB_MO.db')
    conn.commit()

    select_nome = f"""
                      SELECT * FROM DBMO
                      WHERE CPF LIKE '%{cpfx}%'
                      ;
      """

    read_db = pd.read_sql_query(select_nome, conn)
    conn.close()

    return read_db

  else:
    conn = sqlite3.connect('DB_JSON/DB_MO.db')
    conn.commit()

    select_nome = f"""
                      SELECT * FROM DBMO
                      WHERE CPF LIKE '%{cpf}%'
                      ;
      """

    read_db = pd.read_sql_query(select_nome, conn)
    conn.close()

    return read_db


def read_df():
  conn = sqlite3.connect('DB_JSON/DB_MO.db')

  conn.commit()

  select_nome = f"""
                    SELECT * FROM DBMO
                    ;
    """

  read_db = pd.read_sql_query(select_nome, conn)
  conn.close()

  return read_db


def additional(nome, sobrenome, idade, sexo, cpf, rua, numero, bairro, estado, cidade, cep, company, exam_type, exame):
  current_date = datetime.now()
  now_date = current_date.strftime('%d/%m/%Y %H:%M:%S')

  read_db = read_df()
  id_seq = len(read_db)

  input_datas = f"""
          INSERT INTO DBMO(ID,NOME,SOBRENOME,IDADE,SEXO,CPF,RUA,NUMERO,
          BAIRRO,ESTADO,CIDADE,CEP,COMPANY,EXAM_TYPE,EXAME,DATA)
          VALUES ({id_seq},'{nome.upper()}','{sobrenome.upper()}','{idade}','{sexo.upper()}','{cpf}',
          '{rua.upper()}','{numero}','{bairro.upper()}','{estado.upper()}','{cidade.upper()}',
          '{cep}','{company.upper()}','{exam_type.upper()}','{exame.upper()}','{now_date}');

  """

  conn = sqlite3.connect('DB_JSON/DB_MO.db')
  c = conn.cursor()

  c.execute(input_datas)

  conn.commit()

  select_nome = f"""
                  SELECT * FROM DBMO
                  ;
  """

  read_db = pd.read_sql_query(select_nome, conn)
  conn.close()

  return read_db

def atualyze(idd, nome, sobrenome, idade, sexo, cpf, rua, numero, bairro, estado, cidade, cep, company, exam_type, exame):
  current_date = datetime.now()
  now_date = current_date.strftime('%d/%m/%Y %H:%M:%S')

  conn = sqlite3.connect('DB_JSON/DB_MO.db')
  c = conn.cursor()

  update0 = f""" UPDATE DBMO
                SET NOME = '{nome}'
                WHERE ID = '{idd}';
  """

  c.execute(update0)

  update1 = f""" UPDATE DBMO
                SET SOBRENOME = '{sobrenome}'
                WHERE ID = '{idd}';
  """

  c.execute(update1)

  update2 = f""" UPDATE DBMO
                SET IDADE = '{idade}'
                WHERE ID = '{idd}';
  """

  c.execute(update2)

  update3 = f""" UPDATE DBMO
                SET SEXO = '{sexo}'
                WHERE ID = '{idd}';
  """

  c.execute(update3)

  update4 = f""" UPDATE DBMO
                SET CPF = '{cpf}'
                WHERE ID = '{idd}';
  """

  c.execute(update4)

  update5 = f""" UPDATE DBMO
                SET RUA = '{rua}'
                WHERE ID = '{idd}';
  """

  c.execute(update5)

  update6 = f""" UPDATE DBMO
                SET NUMERO = '{numero}'
                WHERE ID = '{idd}';
  """

  c.execute(update6)

  update7 = f""" UPDATE DBMO
                SET BAIRRO = '{bairro}'
                WHERE ID = '{idd}';
  """

  c.execute(update7)

  update8 = f""" UPDATE DBMO
                SET CIDADE = '{cidade}'
                WHERE ID = '{idd}';
  """

  c.execute(update8)

  update9 = f""" UPDATE DBMO
                SET ESTADO = '{estado}'
                WHERE ID = '{idd}';
  """

  c.execute(update9)

  update10 = f""" UPDATE DBMO
                SET CEP = '{cep}'
                WHERE ID = '{idd}';
  """

  c.execute(update10)

  update11 = f""" UPDATE DBMO
                SET COMPANY = '{company}'
                WHERE ID = '{idd}';
  """

  c.execute(update11)

  update12 = f""" UPDATE DBMO
                SET EXAM_TYPE = '{exam_type}'
                WHERE ID = '{idd}';
  """

  c.execute(update12)

  update13 = f""" UPDATE DBMO
                SET EXAME = '{exame}'
                WHERE ID = '{idd}';
  """

  c.execute(update13)

  update14 = f""" UPDATE DBMO
                SET DATA = '{now_date}'
                WHERE ID = '{idd}';
  """

  c.execute(update14)

  conn.commit()

  select_nome = f"""
                  SELECT * FROM DBMO              
                  ;

  """

  read_db = pd.read_sql_query(select_nome, conn)
  conn.close()

  return read_db

#edition(nome, idade, cpf, mom, cep, street, number, city, country, company, exam_type, exam_name, now_date, read_db)

