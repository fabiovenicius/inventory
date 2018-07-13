#coding:UTF-8


import pymysql as my
import xml.etree.ElementTree as ET


def analisar_inventario_xml():
    arquivos = ['ipscanner 10252.xml','ipscanner 10253.xml']
    for arquivo in arquivos:
        tree = ET.parse(arquivo)
        root = tree.getroot()
        for x in root.iter('row'):
            inventario = 1
            name = x.get('name')
            ip = x.get('ip')
            manufacturer = x.get('manufacturer')
            mac = x.get('mac')
            has_http  = x.get('has_http')
            is_http8080 = x.get('is_http8080')
            has_https = x.get('has_https')
            has_ftp = x.get('has_ftp')
            has_rdp = x.get('has_rdp')
            expanded = x.get('expanded')
            os_version = x.get('os_version')
            http_title = x.get('http_title')
            device_type = x.get('device_type')
            sentenca = 1,name,ip,manufacturer,mac,has_http,\
            http_title,is_http8080,has_https,has_ftp,\
            has_rdp,expanded,os_version,\
            device_type
            valores = str.replace(str(sentenca),'None',"''")
            campos = "inventario,name,ip,manufacturer,mac,has_http,http_title,is_http8080,has_https,has_ftp,has_rdp,expanded,os_version,device_type"
            sql = "insert into equipamento({}) values{};".format(campos,valores)
            gravar_inventario_mysql(sql)
            
def gravar_inventario_mysql(sql):
    conn = my.connect(host='localhost',
                      user='root',
                      password='',                             
                      db='inventario',
                      charset='latin1',
                      cursorclass=my.cursors.DictCursor)
    try:
        with conn.curso r()
            # Execute query.
            cursor.execute(sql)
    finally:
        conn.close()


if __name__ == '__main__':
    analisar_inventario_xml()