import sqlite3
from taller1.exporters import AutorSQLExporter, CitaSQLExporter, EtiquetaSQLExporter, CitaEtiquetaSQLExporter
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
    def open_spider(self, spider):
        self.file = open('%s.sql' % spider.name, 'w+b')
        self.conn=sqlite3.connect('parte1.db')

    def process_item(self, item, spider):
        cursor=self.conn.cursor()
        ins_autor_query="insert into autor('nombre')  values('{0}')"
        sel_autor_query="select id from autor where nombre='{0}'"
        ins_cita_query="insert into cita(cita,id_autor) values('{0}', {1})"
        ins_etiqueta_query="insert into etiqueta('nombre') values('{0}')"
        sel_etiqueta_query="select id from etiqueta where nombre='{0}'"
        ins_cita_etiqueta_query="insert into cita_etiqueta('id_cita', 'id_etiqueta') values({0}, {1})"
        exporter_autor=AutorSQLExporter(self.file)
        exporter_cita=CitaSQLExporter(self.file)
        exporter_etiqueta=EtiquetaSQLExporter(self.file)
        exporter_cita_etiqueta=CitaEtiquetaSQLExporter(self.file)
        # Obtener id Autor o insertar
        cursor.execute(sel_autor_query.format(item['autor']))
        autor_db=cursor.fetchone()
        if autor_db is None:
            cursor.execute(ins_autor_query.format(item['autor']))
            self.conn.commit()
            id_autor=cursor.lastrowid
            exporter_autor.export_item(item['autor'], id_autor)
        else:
            id_autor=autor_db[0]
        # Insertar Cita
        cursor.execute(ins_cita_query.format(item['cita'].replace("'","´"), id_autor))
        self.conn.commit()
        id_cita=cursor.lastrowid
        exporter_cita.export_item(item['cita'], id_autor, id_cita)
        # Etiquetas
        for etiqueta in item['etiquetas']:
            cursor.execute(sel_etiqueta_query.format(etiqueta))
            etiqueta_db=cursor.fetchone()
            if etiqueta_db is None:
                cursor.execute(ins_etiqueta_query.format(etiqueta))
                self.conn.commit()
                id_etiqueta=cursor.lastrowid
                exporter_etiqueta.export_item(etiqueta, id_etiqueta)
            else:
                id_etiqueta=etiqueta_db[0]
            cursor.execute(ins_cita_etiqueta_query.format(id_cita, id_etiqueta))
            self.conn.commit()
            exporter_cita_etiqueta.export_item(id_cita, id_etiqueta)
        return item
    def spider_closed(self, spider):
        self.conn.close()