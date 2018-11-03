
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
        ins_autor_query="insert into autor('nombre')  values('{0}')"
        sel_autor_query="select id from autor where nombre='{0}'"
        ins_cita_query="insert into cita(cita,id_autor) values('{0}', {1})"
        ins_etiqueta_query="insert into etiqueta('nombre') values('{0}')"
        sel_etiqueta_query="select id from etiqueta where nombre='{0}'"
        ins_cita_etiqueta_query="insert into cita_etiqueta('id_cita', 'id_etiqueta') values({0}, {1})"
        conn=sqlite3.connect('parte1.db')
        cursor=conn.cursor()
        # Obtener id Autor o insertar
        cursor.execute(sel_autor_query.format(item['autor']))
        autor_db=cursor.fetchone()
        if autor_db is None:
            cursor.execute(ins_autor_query.format(item['autor']))
            conn.commit()
            id_autor=cursor.lastrowid
        else:
            id_autor=autor_db[0]
        # Insertar Cita
        cursor.execute(ins_cita_query.format(item['cita'].replace("'","´"), id_autor))
        conn.commit()
        id_cita=cursor.lastrowid
        # Etiquetas
        for etiqueta in item['etiquetas']:
            cursor.execute(sel_etiqueta_query.format(etiqueta))
            etiqueta_db=cursor.fetchone()
            if etiqueta_db is None:
                cursor.execute(ins_etiqueta_query.format(etiqueta))
                conn.commit()
                id_etiqueta=cursor.lastrowid
            else:
                id_etiqueta=etiqueta_db[0]
            cursor.execute(ins_cita_etiqueta_query.format(id_cita, id_etiqueta))
            conn.commit()

        conn.close()
        return item