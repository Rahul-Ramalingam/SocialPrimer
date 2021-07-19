#192.168.29.34:554
# rtsp//






# import the necessary packages
import numpy as np
import argparse
import cv2
import os
from datetime import datetime
import time
import pandas as pd
import requests 
from openpyxl import Workbook
from threading import Timer 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
from twilio.rest import Client 

# Your Account Sid and Auth Token from twilio.com / console 
account_sid = 'AC6a4213666cea6a9461298301bac9e13c'
auth_token = '0bbc48629c5b08d1625476237e57c3ec'
def conn():
	client = Client(account_sid, auth_token)
	message = client.messages.create( 
								from_='+15714512731', 
								body ='crowd detected', 
								to ='+918778614371')


#initializing variables
threshold = 0.3
confidence1 = 0.5
count = 0
l = 0
latitude = input("latitude: ")#11.077811
longitude = input("longitude: ")#77.140938
place = input("place: ")
gpu = input("y to use gpu: ")
b=0
gws=0


crowdStrength = []
noSDstrength = []
dateNow = []


#To send Email

            


#api call to server
def make_api_call(latitude,longitude,total_people,violated_people):
	res =requests.post("https://locationappp.herokuapp.com/add",data = {
		"latitude":latitude,
		"longitude":longitude,
		"total_people":total_people,
		"violated_people":violated_people

		}).json()
	print(res)


def mapUpdate():
	try:
		make_api_call(latitude,longitude,b,gws)

	except requests.exceptions.ConnectionError:
		print("No internet connection cannot update map")


#to remove dupiclate


#social distancing analysis
angle_factor = float(input("threshold: "))
H_zoom_factor = 1.2
def dist(c1, c2):
    return ((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2) ** 0.5

def T2S(T):
    S = abs(T/((1+T**2)**0.5))
    return S

def T2C(T):
    C = abs(1/((1+T**2)**0.5))
    return C

def isclose(p1,p2):

    c_d = dist(p1[2], p2[2])
    if(p1[1]<p2[1]):
        a_w = p1[0]
        a_h = p1[1]
    else:
        a_w = p2[0]
        a_h = p2[1]

    T = 0
	
    try:	
        T=(p2[2][1]-p1[2][1])/(p2[2][0]-p1[2][0])

    except ZeroDivisionError:
        T = 1.633123935319537e+16
    S = T2S(T)
    C = T2C(T)
    d_hor = C*c_d
    d_ver = S*c_d
    vc_calib_hor = a_w*1.3
    vc_calib_ver = a_h*0.4*angle_factor
    c_calib_hor = a_w *1.7
    c_calib_ver = a_h*0.2*angle_factor

    if (0<d_hor<vc_calib_hor and 0<d_ver<vc_calib_ver):
        return 1
    elif 0<d_hor<c_calib_hor and 0<d_ver<c_calib_ver:
        return 2
    else:
        return 0




#accessing the yolo model
labelsPath = "config/labels.names"
LABELS = open(labelsPath).read().strip().split("\n")

np.random.seed(42)
color = (0, 255, 200) 

#weightsPath = os.path.sep.join([args["yolo"], "yolov3.weights"])
#configPath = os.path.sep.join([args["yolo"], "yolov3.cfg"])
weightsPath = "config/wghts.weights"
configPath = "config/configuration.cfg"


net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)

if gpu == "y":

	print(" setting preferable backend and target to CUDA...")
	net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
	net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

ln = net.getLayerNames()
ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]

W = None
H = None
vidpath = "D:\projects\c19\opencv-dnn-gpu-examples\example_videos\cam.mp4" #input("video: ")
print("accessing video stream...")

vs = cv2.VideoCapture(vidpath)
#vs =  cv2.VideoCapture(0)

schedule.every(5).minutes.do(mapUpdate)

while True:
	schedule.run_pending()

	(grabbed, frame1) = vs.read()
	frame = cv2.resize(frame1,(858,480),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
	if not grabbed:
		break

	if W is None or H is None:
		(H, W) = frame.shape[:2]

	blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416),
		swapRB=True, crop=False)
	net.setInput(blob)
	layerOutputs = net.forward(ln)


	boxes = []
	confidences = []
	classIDs = []
	
	for output in layerOutputs:

		for detection in output:

			scores = detection[5:]
			classID = np.argmax(scores)
			confidence = scores[classID]

			if confidence > confidence1  and LABELS[classID]=='person':

				box = detection[0:4] * np.array([W, H, W, H])
				(centerX, centerY, width, height) = box.astype("int")


				x = int(centerX - (width / 2))
				y = int(centerY - (height / 2))

				boxes.append([x, y, int(width), int(height)])
				confidences.append(float(confidence))
				classIDs.append(classID)


	idxs = cv2.dnn.NMSBoxes(boxes, confidences, confidence, threshold)


	if len(idxs) > 0:
		center = []
		z=[]
		co_info = []
		r=0
		for i in idxs.flatten():
			(x, y) = (boxes[i][0], boxes[i][1])
			(w, h) = (boxes[i][2], boxes[i][3])
			cen = [int(x + w / 2), int(y + h / 2)]
			center.append(cen)
			co_info.append([w,h,cen]) 
			z.append(0)
			
			for i in range(len(center)):
				for j in range(len(center)):
					o = isclose(co_info[i],co_info[j])
					if o==1:
						z[i]=1
						z[j]=2
						
					elif o==2:
						if z[i] != 1:
							z[i] =2
						if z[j] != 1:
							z[j] = 2
						
			
				 

			#color = [int(c) for c in COLORS[classIDs[i]]]
			

			
			#crowd strength
			b = len(center)
			#without social distancing
			lrp =z.count(2)
			hrp =z.count(1)
			gws = lrp+hrp
			if gws>5:
				cv2.putText(frame, 'crowded', (50, 150), cv2.FONT_HERSHEY_SIMPLEX,  
                   0.7, (0, 0, 255), 2, cv2.LINE_AA)
				#conn()

			if z[r] == 0:
				cv2.rectangle(frame, (x, y), (x + (int(w*1)), (y) + (int(h*1))), color, 2)

			if z[r] == 2 or z[r] == 1:
				cv2.rectangle(frame, (x, y), (x + (int(w*1)), (y) + (int(h*1))), (0,0,255), 2)


			text = LABELS[classIDs[i]]
			cv2.putText(frame, text, (x, y - 5),
				cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
			r+=1
			
		
		cv2.putText(frame, 'Crowd Strength: '+str(b), (50, 50), cv2.FONT_HERSHEY_SIMPLEX,  
                   1.5, (200, 100, 0), 3, cv2.LINE_AA) 
			
	
	if 1 > 0:

		cv2.imshow("Frame", frame)
		key = cv2.waitKey(1) & 0xFF

		if key == ord("q"):
			break
		#print('without sd: '+str(gws))
		#print('maximum crowd strength '+str(b))
	