
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
        ins_autor="insert into autor('nombre')  values('{0}')"
        ins_cita="insert into cita(cita,id_autor) values('{0}',{1})"
        sel_auid="select id from autor where nombre='{0}'"
        val=False
        conn= sqlite3.connect('parte1.db')
        cursor=conn.cursor()
        cursor.execute("Select nombre from autor")
        probando=cursor.fetchall()
        if len(probando)==0:
            cursor.execute(ins_autor.format(item['autor']))
            conn.commit()
            cursor.execute(sel_auid.format(item['autor']))
            idd=cursor.fetchall()
            idd=idd[0][0]
            cursor.execute(ins_cita.format(item['cita'],idd))
            conn.commit()
        else:
            for nombre in probando:
                if nombre[0]==(item['autor']):
                    val=True
            if val==True:
                cursor.execute(sel_auid.format(item['autor']))
                idd=cursor.fetchall()
                idd=idd[0][0]
                cursor.execute(ins_cita.format(item['cita'],idd))
                conn.commit()
            else:
                cursor.execute(ins_autor.format(item['autor']))
                conn.commit()
                cursor.execute(sel_auid.format(item['autor']))
                idd=cursor.fetchall()
                idd=idd[0][0]
                cursor.execute(ins_cita.format(item['cita'].replace("'","´"),idd))
                conn.commit()                        
        conn.close()
        return item

