import pymysql.cursors

connection =pymysql.connect(
    host="localhost",
    port=3307,
    db="bank",
    password="123456",
    user="root",
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor
)
surus=input("login in  'l' sing up 's' ")
if surus=="s":
    ad=input("adi daxil et: ")
    email=input("maili daxil et: ")
    parol=input("parolu daxil et: ")
    with  connection.cursor()  as cur:
        sql="insert into `siyahi` (ad,email,parol) values(%s,%s,%s)"
        cur.execute(sql,(ad,email,parol))
    connection.commit()
else:
    with connection.cursor() as cur:
        email=input("maili daxil et: ")
        parol=input("parolu daxil et: ")
        while True:
            sql="select * from `siyahi` where `email`=%s and `parol`=%s"
            cur.execute(sql,(email,parol))
            arr=cur.fetchone()
            if arr==None:
                continue
            else:
                emeliyyat=input("secin: take 't' add 'a'")
                miqdar=float(input("miqdari daxi et: "))
                if emeliyyat=="t":
                    miqdar*=-1
                sql="insert into `qiymet` (users_id,pul) values( %s,%s)"
                cur.execute(sql,(arr["id"],miqdar))
            connection.commit() 
   
                    
    

    


