import  pymysql as py
class Dbconnection:

    @staticmethod
    def createConnection():
       con = py.connect("localhost","root","","fdfs")
       return(con)

