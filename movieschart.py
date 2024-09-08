import matplotlib.pyplot as plt

from dbconnect import Dbconnection

class Graph():

    def graph(self):
        con = Dbconnection.createConnection()
        strsql = "select moviename , rating from reviews"
        dbcon = con.cursor()
        dbcon.execute(strsql)
        info = dbcon.fetchall()
        # con.commit()
        # con.close()
        movie = []
        rating = []

        for data in info:
            movie.append(data[0])
            rating.append(int(data[1]))
        # print(movie)
        # print(rating)

        plt.bar(movie, rating)
        plt.xlabel("movies")
        plt.ylabel("rating")
        plt.title("movie rating graph")
        plt.show()
        # print(data[1])



def main():

    ui = Graph()
    ui.graph()


if __name__ == "__main__":main()
