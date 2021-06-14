#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 31 22:31:18 2021

@author: ely
"""
import pymysql
from server import app
from db_config import mysql
from flask import jsonify
from flask import flash, request

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/js/<path:path>')
def send_js(path):
    return app.send_static_file('js/' + path)


@app.route("/pessoas/<idpessoa>", methods = ['DELETE'])
def excluirPessoa(idpessoa):
    try:
            conn=mysql.connect()
            cur = conn.cursor(pymysql.cursors.DictCursor)
            
            if request.method == 'DELETE':
                sql = '''DELETE FROM `Pessoas` WHERE idpessoa = %s'''
                val = (idpessoa)
                
                cur.execute(sql, val)
                conn.commit()

                resp = jsonify(idpessoa)
                resp.status_code=200
                return resp
            else:
                return "método desconhecido: " + request.method
                
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()
        
@app.route("/pessoas", methods = ['GET', 'POST', 'PUT'])
def user():
    try:
            conn=mysql.connect()
            cur = conn.cursor(pymysql.cursors.DictCursor)
            
            if request.method == 'GET':
                cur.execute("SELECT * FROM `Pessoas`")
                rows = cur.fetchall()
                resp = jsonify(rows)
                resp.status_code=200
                return resp
            elif request.method == 'POST':
                
                obj = request.json
                cpf = obj["cpf"]
                nome = obj["nome"]
                telefone = obj["telefone"]
                
                sql = '''INSERT INTO `Pessoas` (cpf, nome, telefone) VALUES (%s, %s, %s)'''
                val = (cpf, nome, telefone)
                
                cur.execute(sql, val)
                conn.commit()
  
                resp = jsonify(obj)
                resp.status_code=200
                return resp
            elif request.method == 'PUT':
                obj = request.json
                idpessoa = obj["idpessoa"]
                cpf = obj["cpf"]
                nome = obj["nome"]
                telefone = obj["telefone"]
                
                sql = '''UPDATE `Pessoas` SET cpf=%s, nome=%s, telefone=%s  WHERE idpessoa = %s'''
                val = (cpf, nome, telefone, idpessoa)
                
                cur.execute(sql, val)
                conn.commit()

                resp = jsonify(obj)
                resp.status_code=200
                return resp
            else:
                return "método desconhecido: " + request.method
                
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()
        
        
@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status':404,
            'message':'Not Found ' + request.url,
            }
            
    resp = jsonify(message)
    resp.status_code = 404
    return resp


if __name__ == "__main__":
    app.run()    
    