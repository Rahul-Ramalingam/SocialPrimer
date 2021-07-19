
# import the necessary packages
import numpy as np
import argparse
import cv2
import os
from datetime import datetime
#import time
#import pandas as pd
#import requests 
# from openpyxl import Workbook
# from threading import Timer 
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_pdf import PdfPages
# import email, smtplib, ssl
# from email import encoders
# from email.mime.base import MIMEBase
# from email.mime.multipart import MIMEMultipart
# #from email.mime.text import MIMEText
# #import schedule


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
# li=[]
# n = int(input("No of persons to send email: "))
# for i in range(n):
# 	m = input("enter the mail ID: ")
# 	li.append(str(m))
def mailSend(li,place):
    print("mail sent")
    
    for list in li:
		
        subject = "Social Distancing report regarding"
        body = place
        sender_email = "aiminds.enquiry@gmail.com"
        receiver_email = list
        password = "Startup2020"

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message["Bcc"] = receiver_email  


        message.attach(MIMEText(body, "plain"))

        filename1 = "config/visualisation/Bar_Chart.pdf"  # In same directory as script
        filename2 = "sample.xlsx"
        # Open PDF file in binary mode
        with open(filename1, "rb") as attachment:
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment
            part1 = MIMEBase("application", "octet-stream")
            part1.set_payload(attachment.read())

        with open(filename2, "rb") as attachment:
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment
            part2 = MIMEBase("application", "octet-stream")
            part2.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email    
        encoders.encode_base64(part1)
        encoders.encode_base64(part2)

        # Add header as key/value pair to attachment part
        part1.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename1}",
        )
        part2.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename2}",
        )

        # Add attachment to message and convert message to string
        message.attach(part1)
        message.attach(part2)

        text = message.as_string()
        # Log in to server using secure context and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
            


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
def remDup(crowd, nosd):
    _crowd = []
    _nosd = []
    _crowd.append(crowd[i])
    _nosd.append(nosd[i])
    """for i in range(len(crowd)): 
        if not (crowd[i] in _crowd):
            _crowd.append(crowd[i])
        if not (nosd[i] in _nosd):
            _nosd.append(nosd[i])"""
           
    return _crowd, _nosd

#creating spreadsheet
#wb = Workbook()
def excel(t,c,sd,i):
    
	
	ws = wb.active
	ws['A1'] = 'Time'
	ws['B1'] = 'Crowd'
	ws['C1'] = 'No_SD'
	ws[str(str('A')+str(i))] = t
	ws[str(str('B')+str(i))] = c
	ws[str(str('C')+str(i))] = sd
	print("spread sheet updated")
	wb.save("sample.xlsx")

# Generating Graph
position = 1
global k 

def dataVis(crowd, nosd, Time, position):
	dt = datetime.now()
	angle = 90
	bar_width = 0.5
	
	# Displaying the count in Bar Graph
	def insert_data_labels(bars):		
		for bar in bars:
			bar_height = bar.get_height()
			ax.set_xticks(Time,angle)
			ax.annotate(
				'{0:.0f}'.format(bar.get_height()),
				xy=(bar.get_x() + bar.get_width() / 2, bar_height),
				xytext=(0, 3),
				textcoords='offset points',
				ha='center',
				va='bottom')

	fig, ax = plt.subplots(figsize=(10,10))
	Crowd = ax.bar(Time, crowd, bar_width, color="red",alpha=0.6, label='Crowd')	
	No_sd = ax.bar(Time, nosd, bar_width, color="blue",alpha=0.6, label='NO SD')
	
	ax.legend()
	for label in ax.xaxis.get_ticklabels():
		label.set_rotation(angle)
	insert_data_labels(No_sd)
	_a=str(dt)
	_a_ = str("config/visualisation/Bar_Chart.pdf")
	plt.savefig(_a_)#"database"+str(dt)+".pdf")
	
#index = 2
iu = []
def sheetUpdate(crowdStrength,noSDstrength):
    da = datetime.now()
    dt = da.strftime("%c")

    iu.append(noSDstrength)
    if len(iu) <= 2:
        index = 2
    else:
        index = len(iu)

    _b,_gws = crowdStrength, noSDstrength
    #print(_b)
    #print(_gws)
    try:
        _bb = int(sum(_b)/len(_b))*3
        print(_bb)
        _gwsgws = int(sum(_gws)/len(_gws))*2
        print(_gwsgws)
    except ZeroDivisionError:
        _bb=0
        _gwsgws=0
    excel(str(dt),int((_bb)),int((_gwsgws)),index)
    
    index = index+1

def mailUpdate(position,li,place):
    Input_Data = pd.read_excel("sample.xlsx")#"D:/projects/c19/opencv-dnn-gpu-examples/person/sample.xlsx"
    crowd = Input_Data["Crowd"][position:position+24]
    Time = Input_Data["Time"][position:position+24]
    nosd = Input_Data["No_SD"][position:position+24]	
    dataVis(crowd, nosd, Time, position)
    mailSend(li,place)
    position = position + 24

def one_hour():
    sheetUpdate(crowdStrength,noSDstrength)

def one_day():
    mailUpdate(position,li,place)


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
vidpath =r"C:\Users\rahul\Downloads\videoplayback.mp4"#0#input("video: ")
print("accessing video stream...")

vs = cv2.VideoCapture(vidpath)
#vs =  cv2.VideoCapture(0)



#schedule.every().hour.do(one_hour)
#schedule.every(1460).minutes.do(one_day)
#schedule.every(5).minutes.do(mapUpdate)

while True:
	#schedule.run_pending()

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
			if b!=0:
				crowdStrength.append(b)	
			#without social distancing
			lrp =z.count(2)
			hrp =z.count(1)
			gws = lrp+hrp
			if gws!=0:
				noSDstrength.append(gws)

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
		
	cv2.putText(frame, 'No of people without social distancing: '+str(gws), (50, 150), cv2.FONT_HERSHEY_SIMPLEX,  
                   0.7, (0, 0, 255), 2, cv2.LINE_AA)
			
	
	if 1 > 0:

		cv2.imshow("Frame", frame)
		key = cv2.waitKey(1) & 0xFF

		if key == ord("q"):
			break
		#print('without sd: '+str(gws))
		#print('maximum crowd strength '+str(b))
	