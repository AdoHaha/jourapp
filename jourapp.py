#!/usr/bin/env python
from flask import Flask, request
from subprocess import call
import flask
#from flask.ext.restful import reqparse, abort, Api, Resource
import os

from flask import g

import sqlite3
app = Flask(__name__)
#api =Api(app)
import datetime
import json
MAINFOLD=os.path.dirname(os.path.realpath(__file__))
#CREATE TABLE journal(id INTEGER PRIMARY KEY NOT NULL,DATE TEXT NOT NULL,ALLWORDS TEXT,NOOFWORDS INT, USER INT);
#CREATE TABLE journal(id integer PRIMARY KEY autoincrement, addeddate text not null, allwords text, userid integer);

#flask.url_for('static', filename='style.css')
DATABASE = MAINFOLD+'/db/journal.db'
DROPBOXSTRING= "/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload "+DATABASE
#HELPER functions from http://flask.pocoo.org/docs/patterns/sqlite3/
def save_DB_to_Dropbox():
        try:
        	call([DROPBOXSTRING],shell=True)
	except:
		logstr=str(datetime.date.today())+" "+"there was problem with dropbox \n"
		command='echo "'+logstr+'" >> logproblems.txt'
		call([command],shell=True)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    get_db().commit()
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


class NotUnique(Exception):
        pass
        
        
def makeJournalDict(arg,val,unique=True,simple=False):
        allwords = query_db('select * from journal where '+arg+' = ?',
                [val], one=False)
        if( unique and len(allwords)>1):
                raise NotUnique("value it is unique, but it should")
        if allwords is None:
                        return 404
        if simple:
		return json.dumps({"id":allwords[0][0],"addeddate":allwords[0][1]})
        else:
		return json.dumps({"id":allwords[0][0],"addeddate":allwords[0][1],"allwords":allwords[0][2],"noofwords":allwords[0][3],"userid":allwords[0][4]})


@app.route("/journals/<int:idd>",methods=['GET','PUT'])
def singlejournal(idd):
        if request.method == 'GET':
                return makeJournalDict("id",idd)
        elif request.method == 'PUT':
                reqdict2=json.loads(request.get_data())
                querystring='UPDATE journal SET allwords=?, noofwords = ? WHERE id=?'
                cur = get_db().execute(querystring, [reqdict2["allwords"],reqdict2["noofwords"],idd])
                get_db().commit()
                save_DB_to_Dropbox()
                return makeJournalDict("id",idd,True)
                                    
@app.route("/")
def hello():
        todaydate=datetime.date.today()
        
        allwords = query_db('select * from journal where addeddate = ?',
                [str(todaydate)], one=True)
        
        if allwords is None:
            journaltext=""
            querystring='INSERT INTO journal(addeddate) VALUES (?)'
           
            res=query_db(querystring,[str(todaydate)])
            get_db().commit()
            allwords = query_db('select * from journal where addeddate = ?',
                [str(todaydate)], one=True)
            
        #else:
        journaltext= allwords[2] if allwords[2]!=None else ""
        journalid=allwords[0]
        #journaltext="costam testowego wtf?????"    
        return flask.render_template('main.html', journaltext=journaltext, date=todaydate,journalid=journalid)
    #return "Hello World!"

#todo: looks like s....
approved=["css","lib","scripts","images"]
@app.route("/<folder>/<name>")
def loadApprovedFolders(folder,name):
        if folder in approved:
                return staticrender(folder,name)
        else:
                return 404


def staticrender(folder,nazwapliku):
    #ciag=folder+"/"+nazwapliku
    #return flask.render_template(ciag)
    fold= os.path.dirname(os.path.realpath(__file__))+"/"+folder
   
    return flask.send_from_directory(fold,nazwapliku )
    
    
    
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=1515,debug=True)
