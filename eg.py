from __future__ import print_function
from Tkinter import *
import Tkinter as tk
import cv2
from Authorization import auth
from PIL import Image, ImageTk
import cv2.cv as cv
import pdb
import httplib, urllib, urllib2
import json
from datetime import datetime
import sys, json
import string
from random import randint
import shutil

class Frame(object):

	def __init__(self, master):
		self.master = master

		master.wm_title("")
		master.wm_protocol("WM_DELETE_WINDOW")
		self.cap = cv2.VideoCapture(0)

		self.b = Button(width = 25, height = 8, text = 'Music!',command = self.start)
		self.b.place(x = 30, y = 20)

		self.t = Text(font=('Helvetica',24),width=25,height=12,wrap=WORD)
		self.t.configure(state="disabled")
		self.t.pack(side = LEFT)

		self.tv = Text(font=('Helvetica',24),width=20,height=3,wrap=WORD)
		self.tv.configure(state="normal",background='grey')
		self.tv.insert(1.0, "")
		self.tv.place(x = 30, y = 500)

		self.bv = Button(width = 25, height = 8, text = 'Search!',command = self.setVkMusic)
		self.bv.place(x = 30, y = 600)

		self.lmain = tk.Label(master)
		self.lmain.pack(side = RIGHT)

		self.savingImage = None		

		self.r = ""
		

	def show_frame(self):
		_, frame = self.cap.read()
		frame = cv2.flip(frame, 1)
		self.savingImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
		img = Image.fromarray(self.savingImage)
		self.imgtk = ImageTk.PhotoImage(image=img)
		self.lmain.imgtk = self.imgtk
		self.lmain.configure(image=self.imgtk)
		self.lmain.after(50, self.show_frame)

	def takePhoto(self,s):
		ramp_frames = 30
		self.camera = cv2.VideoCapture(0)
		def get_image():
			retval, im = self.camera.read()
			return im
		 
		for i in xrange(ramp_frames):
			temp = get_image()
		camera_capture = get_image()
		cv2.imwrite(s, camera_capture)
		del(self.camera)

	def start(self):
		headers = {
		    # Request headers
		    'Content-Type': 'application/octet-stream',
		    'Ocp-Apim-Subscription-Key': 'faa920d267974c84a43a260a51454b7e',
		}

		try:
			s ="images/{}.png".format("{:%B_%d_%Y_%H:%M:%S}".format(datetime.now()))
			self.takePhoto(s)
			with open(s, "rb") as imageFile:
			    d = imageFile.read()

			conn = httplib.HTTPSConnection('api.projectoxford.ai')
			conn.request("POST", "https://api.projectoxford.ai/emotion/v1.0/recognize", d, headers)
			response = conn.getresponse()
			data = response.read()

			dat = json.loads(data)
 

			int_emotions = 0
			str_emotions = ""

			self.r = ""
			self.t.configure(state="normal")
			self.t.delete('1.0', END)

			for keys,values in dat[0]['scores'].items():
				self.r += keys
				self.r += " " + str(int(values*100))+ "\n"
				print(self.r)
				if int(values*100) > int_emotions:
					int_emotions = int(values*100)
					str_emotions = keys

			self.t.insert(1.0, self.r)
			print(self.r)
			self.t.configure(state="disabled")
			conn.close()

			s = str_emotions+"/"+ str(randint(1,4)) +".mp3"
			print(s)
			shutil.move(s, "/Volumes/one_direction/0.mp3")
			#self.setVkMusic()
		except Exception as e:
			print("{}".format(e.message))

	def setVkMusic(self):
		"""LOGIN = ("+")
		PASSWORD = ("")
		CLIENT = ("4949157")
		SCOPE = '341055' 
		token, user_id = auth(LOGIN, PASSWORD, CLIENT, SCOPE)"""
		ZAEBALO = self.tv.get("1.0",END)
		ZAEBALO = ZAEBALO.replace(" ", "_")
		ZAEBALO = ZAEBALO.replace("\n", "")
		print(ZAEBALO)
		token = 'f0c0eb66a45941864aae34fd62e21f46cdfcb67e47bef0658cb3a118d0817f040ba9d3c18790bcd0908d0'
		s = "https://api.vk.com/method/audio.search?q={0}&sort=2&count=1&access_token={1}".format(ZAEBALO,token)
		#print(s)
		h = json.loads(urllib2.urlopen(s).read())
		#print (h['response'][1]['url'].split('?')[0])
		print("Done")
		mp3 = h['response'][1]['url'].split('?')[0]
		mp3file = urllib2.urlopen(mp3)
		with open('/Volumes/one_direction/0.mp3','wb') as output:
			output.write(mp3file.read())
		output.close()



root = Tk()
x = Frame(root)
x.show_frame()
root.mainloop()