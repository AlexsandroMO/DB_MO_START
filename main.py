# https://maxcnunes.com/post/2012/12/24/desenvolvendo-pequena-aplicacao-web-python-flask/
#https://gilcierweb.com.br/posts/formulario-de-contato-com-python-flask-e-envio-de-e-mail


# Created by:  Alexsandro Monteiro
# Date:        24/08/2019
# Banco de Dados Medicina Ocupacional

# Python any Where
# https://www.pythonanywhere.com/user/AlexsandroMO/
# pip install flask

from flask import Flask, render_template, url_for, request, redirect, send_file, send_from_directory
from datetime import date
from datetime import datetime
import db
import os
import dbpy
# import xlrd

# ==================================
app = Flask(__name__)

class Var_State():
    def __init__(self, login_acess, read_db, user, idd):
        self.login_acess = login_acess
        self.read_db = read_db
        self.user = user
        self.idd = idd

Var_State.login_acess = False

@app.route("/")
@app.route("/home")
def home():
    status = Var_State.login_acess
    return render_template('home.html', status=status)

@app.route("/create")
def create():
    return render_template('create.html')

@app.route("/userarea_loged")
def userarea_loged():
    Var_State.login_acess = True

    status = Var_State.login_acess

    return render_template('userarea_loged.html', status=status)

@app.route("/cadastro")
def cadastro():
    name_user = Var_State.user

    return render_template('cadastro.html', name_user=name_user)

@app.route("/consultclient")
def consultclient():
    name_user = Var_State.user

    return render_template('consultclient.html', name_user=name_user)

@app.route("/dataedition")
def dataedition():
    name_user = Var_State.user

    return render_template('dataedition.html', name_user=name_user)

@app.route('/editionresult', methods=['POST', 'GET'])
def editionresult():
    if request.method == 'POST':
        resultclient = request.form
        print(resultclient)

        nome = resultclient['nome']
        sobrenome = resultclient['sobrenome']

        dia = resultclient['dia']
        mes = resultclient['mes']
        ano = resultclient['ano']

        sexo = resultclient['sexo']

        cpf1 = resultclient['cpf']
        cpf2 = resultclient['cpf2']

        rua = resultclient['rua']
        numero = resultclient['numero']

        bairro = resultclient['bairro']
        estado = resultclient['estado']
        cidade = resultclient['cidade']

        cep1 = resultclient['cep']
        cep2 = resultclient['cep2']

        company = resultclient['company']
        exam_type = resultclient['name-type']
        exame = resultclient['exame']

        idade = dia + '/' + mes + '/' + ano
        cpf = cpf1 + '-' + cpf2
        cep = cep1 + '-' + cep2

        idd = Var_State.idd

        read_db = dbpy.atualyze(idd, nome, sobrenome, idade, sexo, cpf, rua, numero, bairro, estado, cidade, cep, company, exam_type, exame)
        print(read_db)

    return render_template('editionresult.html', tables=[read_db.to_html(classes='data')], titles=read_db.columns.values)

@app.route('/cadastroresult', methods=['POST', 'GET'])
def cadastroresult():

    if request.method == 'POST':
        resultclient = request.form
        print(resultclient)

        nome = resultclient['nome']
        sobrenome = resultclient['sobrenome']

        dia = resultclient['dia']
        mes = resultclient['mes']
        ano = resultclient['ano']

        sexo = resultclient['sexo']

        cpf1 = resultclient['cpf']
        cpf2 = resultclient['cpf2']

        rua = resultclient['rua']
        numero = resultclient['numero']

        bairro = resultclient['bairro']
        estado = resultclient['estado']
        cidade = resultclient['cidade']

        cep1 = resultclient['cep']
        cep2 = resultclient['cep2']

        company = resultclient['company']
        exam_type = resultclient['name-type']
        exame = resultclient['exame']

        idade = dia + '/' + mes + '/' + ano
        cpf = cpf1 + '-' + cpf2
        cep = cep1 + '-' + cep2

        read_db = dbpy.additional(nome, sobrenome, idade, sexo, cpf, rua, numero, bairro, estado, cidade, cep, company, exam_type, exame)
        print(read_db)

        return render_template("cadastroresult.html", tables=[read_db.to_html(classes='data')], titles=read_db.columns.values)

@app.route('/consultresult', methods=['POST', 'GET'])
def consultresult():

    if request.method == 'POST':
        resultclient = request.form
        print(resultclient)

        action = resultclient['edit']
        nome = resultclient['nome']
        sobrenome = resultclient['sobrenome']
        cpf1 = resultclient['cpf']
        cpf2 = resultclient['cpf2']

        cpf = cpf1 + '-' + cpf2

        if nome != '' and action == 'edita':
            print('aqui: aaaa')
            read_db = dbpy.read_df_nome(nome, sobrenome)

            for i in range(len(read_db['NOME'])):
                idd = read_db['ID'].loc[i]
                nome = read_db['NOME'].loc[i]
                sobrenome = read_db['SOBRENOME'].loc[i]
                idade = read_db['IDADE'].loc[i]
                sexo = read_db['SEXO'].loc[i]
                cpf = read_db['CPF'].loc[i]
                rua = read_db['RUA'].loc[i]
                numero = read_db['NUMERO'].loc[i]
                bairro = read_db['BAIRRO'].loc[i]
                estado = read_db['ESTADO'].loc[i]
                cidade = read_db['CIDADE'].loc[i]
                cep = read_db['CEP'].loc[i]
                company = read_db['COMPANY'].loc[i]
                exam_type = read_db['EXAM_TYPE'].loc[i]
                exame = read_db['EXAME'].loc[i]

                age = idade.split('/')
                dia = age[0]
                mes = age[1]
                ano = age[2]

                cpfx = cpf.split('-')
                cpf1 = cpfx[0]
                cpf2 = cpfx[1]

                cepx = cep.split('-')
                cep1 = cepx[0]
                cep2 = cepx[1]

                Var_State.idd = idd

            return render_template("dataedition.html", nome=nome, sobrenome=sobrenome,
                                   dia=dia, mes=mes, ano=ano, sexo=sexo, cpf1=cpf1, cpf2=cpf2, rua=rua, numero=numero,
                                   bairro=bairro, estado=estado, cidade=cidade, cep1=cep1, cep2=cep2,
                                   company=company, exam_type=exam_type, exame=exame)

        elif cpf != '-' and action == 'edita':
            print('aqui: bbbb')
            read_db = dbpy.read_df_cpf(cpf)

            return render_template("dataedition.html", tables=[read_db.to_html(classes='data')], titles=read_db.columns.values)

        elif nome != '' and action == 'ler':
            print('aqui: cccc')
            read_db = dbpy.read_df_nome(nome, sobrenome)

            return render_template("consultresult.html", tables=[read_db.to_html(classes='data')], titles=read_db.columns.values)

        elif cpf != '-' and action == 'ler':
            print('aqui: addd')
            read_db = dbpy.read_df_cpf(cpf)

            return render_template("consultresult.html", tables=[read_db.to_html(classes='data')], titles=read_db.columns.values)

        else:
            print('aqui: eeee')
            read_db = dbpy.read_df()
            return render_template("consultresult.html", tables=[read_db.to_html(classes='data')], titles=read_db.columns.values)


@app.route('/dataeditionresult', methods=['POST', 'GET'])
def dataeditionresult():

    if request.method == 'POST':
        resultclient = request.form
        print(resultclient)

        nome = resultclient['nome']
        sobrenome = resultclient['sobrenome']

        dia = resultclient['dia']
        mes = resultclient['mes']
        ano = resultclient['ano']

        sexo = resultclient['sexo']

        cpf1 = resultclient['cpf']
        cpf2 = resultclient['cpf2']

        rua = resultclient['rua']
        numero = resultclient['numero']

        bairro = resultclient['bairro']
        estado = resultclient['estado']
        cidade = resultclient['cidade']

        cep1 = resultclient['cep']
        cep2 = resultclient['cep2']

        company = resultclient['company']
        exam_type = resultclient['name-type']
        exame = resultclient['exame']

        idade = dia + '/' + mes + '/' + ano
        cpf = cpf1 + '-' + cpf2
        cep = cep1 + '-' + cep2

        idd = Var_State.idd

        read_db = dbpy.additional(idd, nome, sobrenome, idade, sexo, cpf, rua, numero, bairro, estado, cidade, cep, company, exam_type, exame)
        print(read_db)

        return render_template("dataeditionresult.html", tables=[read_db.to_html(classes='data')], titles=read_db.columns.values)

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/upload")
def upload():
    create_var = db.create_list()
    print(create_var)
    return render_template('upload.html')

@app.route("/logout")
def logout():
    Var_State.login_acess = False
    return render_template('home.html')

@app.route("/download")
def download():
    return redirect(url_for('static', filename='NCR_RAI_LIBERAR.xlsx'))

@app.route("/query")
def query():
    return render_template('query.html')

@app.route('/queryresult', methods=['POST', 'GET'])
def queryresult():
  if request.method == 'POST':
    resultquery = request.form
    code_query = resultquery['query']

    print('>>>',code_query)

    read_db = dbpy.query_read(code_query)
    print(read_db)

    return render_template("queryresult.html", tables=[read_db.to_html(classes='data')], titles=read_db.columns.values)

@app.route('/userarea', methods=['POST', 'GET'])
def userarea():
    if request.method == 'POST':
        resultuserarea = request.form
        email = resultuserarea['email']
        password = resultuserarea['password']

        convert_ = db.query_email_confere(email, password)

        email_ = convert_[0]['EMAIL']
        password_ = convert_[0]['PASSWORD']
        name_user = convert_[0]['FIRST_NAME']

        print('>>>>>>>>>>', name_user)

        Var_State.user = name_user

        if email == '' or password == '':
            return f"""
        <p>Atenção, Todos os campos precisam ser preenchidos... :( </p>
        <br>
        <br>
        <br>
        <p><a href="/cotation"><img src="https://image.flaticon.com/icons/png/512/54/54906.png" alt="some text" width=40 height=40></p>

     """

        if email == email_.lower() and password == password_:
            Var_State.login_acess = True

            status = Var_State.login_acess

            if status == True:
                return render_template("userarea.html", title='Python_Flask', status=status,
                                       name_user=name_user.lower().capitalize())

            else:
                return render_template("login.html", email=email)

        else:
            return render_template("message.html", email=email)

@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/erro')
def erro():
    return render_template('erro.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
