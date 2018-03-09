import Tkinter as tk
from PIL import Image,ImageDraw
import pickle
import numpy as np
from sklearn import datasets, svm, metrics
import cv2

 
 
class ImageGenerator:
    def __init__(self,parent,posx,posy,*kwargs):
        self.learning
        self.parent = parent
        self.posx = posx
        self.posy = posy
        self.sizex = 1080
        self.sizey = 600
        self.b1 = "up"
        self.xold = None
        self.yold = None
        self.drawing_area=tk.Canvas(self.parent,width=self.sizex,height=self.sizey)
        self.drawing_area.place(x=self.posx,y=self.posy)
        self.drawing_area.bind("<Motion>", self.motion)
        self.drawing_area.bind("<ButtonPress-1>", self.b1down)
        self.drawing_area.bind("<ButtonRelease-1>", self.b1up)
        self.button=tk.Button(self.parent,text="Done",width=20,bg='white',command=self.save)
        self.button.place(x=1100,y=40)
        self.button1=tk.Button(self.parent,text="Clear",width=20,bg='white',command=self.clear)
        self.button1.place(x=1100,y=100)
        self.recognizeButton = tk.Button(self.parent, text = "Recognize", width=20,bg='white', command = self.recognize)
        self.recognizeButton.place(x=1100,y=140)
 
        self.image=Image.new("RGB",(1080,600),(255,255,255))
        self.draw=ImageDraw.Draw(self.image)
 
    def recognize(self):
        #size = 28,28
        #img = Image.open(r"/Users/Konstantin/Desktop/gg_eZ.jpg")

                # Load digit database
        digits = datasets.load_digits()
        n_samples = len(digits.images)
        data = digits.images.reshape((n_samples, -1))

        # Train SVM classifier
        classifier = svm.SVC(gamma = 0.001)
        classifier.fit(data[:n_samples], digits.target[:n_samples])
 
        img = cv2.imread(r"/Users/Konstantin/Desktop/gg_eZ.jpg")
        img = img[:,:,0];
        img = cv2.resize(img, (8, 8))

        # Normalize the values in the image to 0-16
        minValueInImage = np.min(img)
        maxValueInImage = np.max(img)
        normaliizeImg = np.floor(np.divide((img - minValueInImage).astype(np.float),(maxValueInImage-minValueInImage).astype(np.float))*16)

        # Predict
        predicted = classifier.predict(normaliizeImg.reshape((1,normaliizeImg.shape[0]*normaliizeImg.shape[1] )))
        print predicted
 
    def save(self):
        filename = r"/Users/Konstantin/Desktop/gg_eZ.jpg"
        self.image.save(filename)
 
    def clear(self):
        self.drawing_area.delete("all")
        self.image=Image.new("RGB",(1080,600),(255,255,255))
        self.draw=ImageDraw.Draw(self.image)
 
    def b1down(self,event):
        self.b1 = "down"
 
    def b1up(self,event):
        self.b1 = "up"
        self.xold = None
        self.yold = None
 
    def motion(self,event):
        if self.b1 == "down":
            if self.xold is not None and self.yold is not None:
                event.widget.create_line(self.xold,self.yold,event.x,event.y,smooth='true',width=3,fill='black')
                self.draw.line(((self.xold,self.yold),(event.x,event.y)),(0,128,0),width=3)
 
        self.xold = event.x
        self.yold = event.y

    def learning(self):
        # Load digit database
        digits = datasets.load_digits()
        n_samples = len(digits.images)
        data = digits.images.reshape((n_samples, -1))

        # Train SVM classifier
        classifier = svm.SVC(gamma = 0.001)
        classifier.fit(data[:n_samples], digits.target[:n_samples])


 
if __name__ == "__main__":
    root=tk.Tk()
    root.wm_geometry("%dx%d+%d+%d" % (1080, 600, 10, 10))
    root.config(bg='white')
    ImageGenerator(root,10,10)
    root.mainloop()