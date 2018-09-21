#coding:utf8
import sys
import pymysql
class TransferMoney(object):
    def __init__(self,conn):
        self.conn=conn
    def check_out_count(self,out_count):
        cursor = self.conn.cursor()
        try:
            sql='select * from new_table where id=%s'% out_count
            cursor.execute(sql)
            rs = cursor.fetchall()
            if len(rs)!=1:
                raise Exception("账户%s不存在"% out_count)
        finally:
            cursor.close()

    def check_in_count(self,in_count):
        cursor = self.conn.cursor()
        try:
            sql = 'select * from new_table where id=%s'% in_count
            cursor.execute(sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception("账户%s不存在"% in_count)
        finally:
                cursor.close()

    def has_enough_money(self,out_count,money):
        cursor = self.conn.cursor()
        try:
            sql = 'select * from new_table where id=%d and money>%d'(out_count,money)
            cursor.execute(sql)
            print("have enough money:" + sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception("账户%s没有足够的钱" % out_count)
        finally:
                cursor.close()


    def reduce_money(self,out_count,money):
        cursor = self.conn.cursor
        try:
            sql='update new_table set money=money-%s where id=%s'(money,out_count)
            cursor.execute(sql)
            rs = cursor.rowcount
            if rs != 1:
                raise Exception("账户%s没有足够的钱" % out_count)
        finally:
            cursor.close()
    def add_money(self,in_count,money):
        cursor = self.conn.cursor
        try:

            sql = 'update new_table set money=money+%s where id=%s'(money, in_count)
            cursor.execute(sql)
            rs = cursor.rowcount
            if rs != 1:
                raise Exception("账户%s没有足够的钱" % in_count)
        finally:
                cursor.close()
    def transfer(self,out_count,in_count,money):
        try:
            self.check_out_count(out_count)
            self.check_in_count(in_count)
            self.has_enough_money(out_count,money)
            self.reduce_money(out_count,money)
            self.add_money(in_count,money)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e


if __name__=="__main__":
    out_count=sys.argv[1]
    in_count=sys.argv[2]
    money=sys.argv[3]
#创建于数据库连接
    conn=pymysql.connect(host='127.0.0.1',port =3306,user='root',password='password',db='test',charset='utf8')
    tr_money=TransferMoney(conn)
    try:
        tr_money.transfer(out_count,in_count,money)
    except Exception as e:
        print(e)
    finally:
        conn.close()
