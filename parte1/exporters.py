from scrapy.exporters import BaseItemExporter

class AutorSQLExporter(BaseItemExporter):
    def __init__(self, file, **kwargs):
        self._configure(kwargs, dont_fail=True)
        self.file=file
    def export_item(self, autor, id_autor):
        ins_autor_query="insert into autor('id', 'nombre')  values({0}, '{1}')"
        self.file.write(ins_autor_query.format(id_autor, autor).encode('utf-8'))
        self.file.write('\n'.encode('utf-8'))

class CitaSQLExporter(BaseItemExporter):
    def __init__(self, file, **kwargs):
        self._configure(kwargs, dont_fail=True)
        self.file=file
    def export_item(self, cita, id_autor, id_cita):
        ins_cita_query="insert into cita(id, cita, id_autor) values({0}, '{1}', {2})"
        self.file.write(ins_cita_query.format(id_cita, cita.replace("'","´"), id_autor).encode('utf-8'))
        self.file.write('\n'.encode('utf-8'))

class EtiquetaSQLExporter(BaseItemExporter):
    def __init__(self, file, **kwargs):
        self._configure(kwargs, dont_fail=True)
        self.file=file
    def export_item(self, etiqueta, id_etiqueta):
        ins_etiqueta_query="insert into etiqueta('id', 'nombre') values({0}, '{1}')"
        self.file.write(ins_etiqueta_query.format(id_etiqueta, etiqueta).encode('utf-8'))
        self.file.write('\n'.encode('utf-8'))

class CitaEtiquetaSQLExporter(BaseItemExporter):
    def __init__(self, file, **kwargs):
        self._configure(kwargs, dont_fail=True)
        self.file=file
    def export_item(self, id_cita, id_etiqueta):
        ins_cita_etiqueta_query="insert into cita_etiqueta('id_cita', 'id_etiqueta') values({0}, {1})"
        self.file.write(ins_cita_etiqueta_query.format(id_cita, id_etiqueta).encode('utf-8'))
        self.file.write('\n'.encode('utf-8'))
