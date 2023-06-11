import os
import random
import string

import cherrypy as cherrypy
from peewee import *
import datetime

db = SqliteDatabase('base.db')


def parseToHtmlTable(strings):
    stringi = ""
    for x in strings:
        stringi += "<tr>"
        for y in x:
            stringi += "<th style='color: white; border-collapse: separate; " \
                       " border: 2px solid black; padding: 10px; text-align:center; font-size: 20px'> "
            stringi += str(y)
            stringi += "</th>"
        stringi += "</tr>"
    return stringi





class BaseModel(Model):
    class Meta:
        database = db


class APPLab(BaseModel):
    class Meta:
        db_table = 'patients'

    idx = PrimaryKeyField(unique=True)
    # number = IntegerField()
    name = TextField()
    doctor_name = TextField()
    reason = TextField()
    duration = IntegerField()

    def Update(self, sid, name, doctor_name, reason, duration):
        appLab = APPLab.get(idx=sid)
        appLab.name = name
        appLab.doctor_name = doctor_name
        appLab.reason = reason
        appLab.duration = duration
        appLab.save()

    def Add(self, name, doctor_name, reason, duration):
        APPLab(name=name, doctor_name = doctor_name, reason = reason, duration = duration).save()

    def getColumn(self):
        cursor = db.cursor()

        cursor.execute('PRAGMA table_info("patients")')
        column_names = [i[1] for i in cursor.fetchall()]

        return column_names

    def getStrings(self):
        cursor = db.cursor()

        sqlite_select_query = """SELECT * from patients"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()

        return records


class Page(object):
    columns = {}
    visit = ""

    def __init__(self, c, v):
        self.columns = c
        self.visit = v

    @cherrypy.expose
    def index(self):
        return f'''
        <html>
            <head>
                <meta charset="utf-8">
                <title>lab6</title>
            </head>
                <body style="background: whitesmoke">
                    <table  style="
                                margin-left: auto;
                                margin-right: auto;
                                text-align: left;
                                border-collapse: separate;                                
                                border-spacing: 5px;
                                background: grey;
                                color: #430AB1;
                                border: 2px solid black"
                    >
                        <h1 style="text-align: center; font-size: 40px;">lab6</h1>
                            <tr>
                                {
                                    "".join(["<th style='background: black; color: white; border: 2px solid white; text-align:center; padding: 10px; font-size: 25px; '>" + i + "</th>"
                                            for i in self.columns])
                                }
                            </tr>   
                                {stringi}
                    </table>
                </body>
        </html>
        
        '''


if __name__ == '__main__':
    db.create_tables([APPLab])
    app = APPLab()
    app.Add("Петушков Игорь Алексеевич", "Урсов Сергей Павлович", "Артроз коленного сустава", 3)
    app.Update(3, "Курчатов Игорь Алексеевич",  "Акела Сергей Павлович", "Артроз коленного сустава", 3)

    columns = app.getColumn()
    strings = app.getStrings()

    stringi = parseToHtmlTable(strings)

    cherrypy.quickstart(Page(columns, stringi))

    db.close()
