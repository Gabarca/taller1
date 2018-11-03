
import sqlite3
# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
 #See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

####

class MaxLengthPipeline(object):
    def process_item(self, item, spider):
        largo=len(item['cita'])
        if largo>255:
            item['cita']=item['cita'][0:256]
            return item
        else:
            return item    
            
#Pipeline encargado de agregar tanto autor como las citas
class SQLiteCitasPipeline(object):            
    def process_item(self, item, spider):
        # print(item)
        ins_autor_query="insert into autor('nombre')  values('{0}')"
        ins_cita_query="insert into cita(cita,id_autor) values('{0}',{1})"
        sel_autor_query="select id, nombre from autor where nombre='{0}'"
        val=False
        conn=sqlite3.connect('parte1.db')
        cursor=conn.cursor()

        cursor.execute(sel_autor_query.format(item['autor']))
        autor_db=cursor.fetchone()
        if autor_db is None or len(autor_db) == 0:
            cursor.execute(ins_autor_query.format(item['autor']))
            conn.commit()
            id_autor = cursor.lastrowid
        else:
            id_autor = autor_db[0]
            
        cursor.execute(ins_cita_query.format(item['cita'].replace("'","´"), id_autor))
        conn.commit()
        conn.close()
        return item