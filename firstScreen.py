from tkinter import *
from PyQt5.QtWidgets import *
import pyttsx3
import threading
from userlogin import Ui_Login
class firstScreen(QFrame):
    def __init__(self):
        super(firstScreen,self).__init__()
        # self.setGeometry(50,50,600,750)
        # self.setFixedSize(600,750)
        self.Win = QFrame()
        self.ui = Ui_Login()
        self.ui.setupUi(self.Win)  # making all the configuration of ui
        root = Tk()
        root.title("Welcome")
        root.maxsize(380,380)
# canvas = Canvas(root,width=500,height=500)
# canvas.pack()
        frames = [PhotoImage(file='E:\\Precursor\\FDFS\\ui\\popcornsplash.gif',format="gif -index %i"%(i))for i in range(0,40)]
        def update(ind=0):
           frame = frames[ind]
           label.configure(image=frame)
           ind = ind+1
           root.after(50,update,ind)
        label =Label(root)
        label.pack()
        root.after(0,update,0)
        engine = pyttsx3.init()
        engine.setProperty('rate',140)
        engine.say("welcome to the movie rating app")
        root.after(4000,lambda :root.destroy())
        #file = gTTS("Welcome to the movie rating app", 'en')
        #filename = os.getcwd() + "/temp.mp3"
        #file.save(filename)
        #music = pyglet.media.load(filename, streaming=False)
        #music.play()
        #time.sleep(music.duration)
        #os.remove(filename)
        t1 = threading.Thread(target=engine.runAndWait)
        #t2 = threading.Thread(target=self.Win.show())
        t1.start()
        #t2.start()
        root.mainloop()
        self.Win.show()
        t1.join()


import myresources_rc

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    c = firstScreen()
    sys.exit(app.exec())
    # my_image=PhotoImage(file='E:\\Precursor\\FDFS\\ui\\popcornsplash.gif',format="gif -index "+str(i))
    # canvas.create_image(0,0,anchor=NW,image=my_image)
# from PyQt5.QtWidgets import *
# from PyQt5.uic import loadUi
# from PyQt5.QtCore import QSize
# from PyQt5.QtGui import *
# import speak
#
#
# class firstScreen(QMainWindow):
#     def __init__(self):
#         super(firstScreen,self).__init__()
#         # self.setGeometry(50,50,600,750)
#         # self.setFixedSize(600,750)
#         path = "E:/Precursor/FDFS/ui/"
#         loadUi(path+"firstScreen.ui",self)
#         # speak.tts("welocme to movie rating app",'en')
#         self.movie=QMovie(path+"popcornsplash.gif")
#         self.movie.frameChanged.connect(self.repaint)
#         self.movie.start()
#     def paintEvent(self, event):
#          currentFrame= self.movie.currentPixmap()
#          frameRect = currentFrame.rect()
#          frameRect.moveCenter(self.rect().center)
#          if frameRect.intersects(event.rect()):
#              painter = QPainter(self)
#              painter.drawPixmap(frameRect.left(),frameRect.top(),currentFrame)
#
#
#
# import myresources_rc
#
# if __name__ == '__main__':
#     import sys
#     app = QApplication(sys.argv)
#     c = firstScreen()
#     c.show()
#     sys.exit(app.exec())