from scrapy.exporters import BaseItemExporter

class AutorCitaSQLExporter(BaseItemExporter):
    def __init__(self, file, **kwargs):
        self._configure(kwargs, dont_fail=True)
        self.file = file
        self.first_item = True
    def export_item(self, item, id_autor, id_cita):
        ins_autor_query="insert into autor('id', 'nombre')  values({0}, '{1}')"
        sel_autor_query="select id from autor where nombre='{0}'"
        ins_cita_query="insert into cita(cita,id_autor) values('{0}', {1})"
        ins_etiqueta_query="insert into etiqueta('nombre') values('{0}')"
        sel_etiqueta_query="select id from etiqueta where nombre='{0}'"
        ins_cita_etiqueta_query="insert into cita_etiqueta('id_cita', 'id_etiqueta') values({0}, {1})"
        print(item)
        if self.first_item:
            self.first_item = False
        else:
            self.file.write(u'\n')
        self.file.write(ins_autor_query.format(id_autor, item['autor']))