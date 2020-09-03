"""
Author:dxl
Time: 2020/8/18 21:33
File: handle_db.py
"""
import pymysql
from common.myconifg import conf

class HandleDb:

    def __init__(self):
        # 新建连接
        self.con=pymysql.connect(host=conf.get('mysql','host'),
                    user=conf.get('mysql','user'),
                    password=conf.get('mysql','password'),
                    port=conf.getint('mysql','port'),
                    charset='utf8')
        #新建游标
        self.cur=self.con.cursor()

    def get_one(self,sql):
        '''
        获取查询到的第一条数据
        '''
        self.con.commit()
        self.cur.execute(sql)
        return self.cur.fetchone()

    def get_all(self,sql):
        '''获取查询到的所有数据'''
        self.con.commit()
        self.cur.execute(sql)
        return self.cur.fetchall()

    def get_count(self,sql):
        '''获取查询到的所有数量'''
        self.con.commit()
        res=self.cur.execute(sql)
        return res

    def close(self):
        # 关闭游标对象
        self.cur.close()
        #关闭连接对象
        self.con.close()

if __name__ == '__main__':
    db=HandleDb()
    sql='SELECT id from futureloan.member where mobile_phone=13641878150'
    # res=db.get_one(sql)[0]
    count=db.get_count(sql)
    print(count)

