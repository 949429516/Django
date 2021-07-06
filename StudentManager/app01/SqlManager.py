import pymysql


class dbManager:

    def commit(self, sql_find):
        conn = pymysql.connect(host="localhost", port=3306, user="root",
                               password="19950811", database="oldboy",
                               charset="utf8")
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            cursor.execute(sql_find)
            id = int(conn.insert_id())
            conn.commit()
            return id
        except:
            conn.rollback()
        cursor.close()
        conn.close()

    def findmany(self, sql_find):
        conn = pymysql.connect(host="localhost", port=3306, user="root",
                               password="19950811", database="oldboy",
                               charset="utf8")
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            cursor.execute(sql_find)
            data = cursor.fetchall()
        except:
            conn.rollback()
        cursor.close()
        conn.close()
        return data

    def findone(self, sql_find):
        conn = pymysql.connect(host="localhost", port=3306, user="root",
                               password="19950811", database="oldboy",
                               charset="utf8")
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            cursor.execute(sql_find)
            data = cursor.fetchone()
        except:
            conn.rollback()
        cursor.close()
        conn.close()
        return data