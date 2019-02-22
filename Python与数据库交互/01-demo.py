from pymysql import *

def main():
    conn = connect(host='localhost', port=3306, 
                   user='root', password='123456',
                   database='jing_dong', charset='utf8')

    csl = conn.cursor()

    count = csl.execute("select * from goods;")

    print(count)


if __name__ == "__main__":
    main()
    
