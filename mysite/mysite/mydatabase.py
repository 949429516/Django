import pymysql

class mysqlpython:
    def __init__(self):
        self.host = "localhost"
        self.user = 'root'
        self.password = '19950811'
        self.database = 'person'
        self.charset = 'utf8'


    def find(self):
        L = []
        conn = pymysql.connect(host=self.host, user=self.user, passwd=self.password,
                               password=self.password, database=self.database,
                               charset=self.charset)
        cursor1 = conn.cursor()
        sql_find = "select * from student;"
        try:
            cursor1.execute(sql_find)
            data = cursor1.fetchall()
            for item in data:
                data_dict = {"id": item[0],
                 "name": item[1],
                 "email": item[2]}
                L.append(data_dict)
            return L
        except:
            conn.rollback()
        cursor1.close()
        conn.close()


    def Del(self, nid):
        conn = pymysql.connect(host=self.host, user=self.user, passwd=self.password,
                               password=self.password, database=self.database,
                               charset=self.charset)
        cursor1 = conn.cursor()
        sql_del = "delete from student where id = {};".format(nid)
        try:
            cursor1.execute(sql_del)
            conn.commit()
        except:
            conn.rollback()
        cursor1.close()
        conn.close()