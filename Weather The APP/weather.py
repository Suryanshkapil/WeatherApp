from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk

root=Tk()
root.title("Weather App")
root.geometry("890x470+300+200")
root.configure(bg="#57adff")
root.resizable(False,False)

def getWeather():
    city=textfield.get()

    geolocator=Nominatim(user_agent="geoapiExercises")
    location= geolocator.geocode(city)
    obj= TimezoneFinder()

    result= obj.timezone_at(lng=location.longitude,lat=location.latitude)

    timezone.config(text=result)
    long_lat.config(text=f"{round(location.latitude,4)}°N,{round(location.longitude,4)}°E")

    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    latitutor=float(location.latitude)
    longitutor=float(location.longitude)

    #weather
    api_url = "https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&units=metric&appid=eb40a87352a4b60ab827a590636e5eb5"
    api = api_url.format(latitude=location.latitude, longitude=location.longitude)

    json_data = requests.get(api).json()
    print(json_data)

    
    #current
    temp= json_data['main']['temp']
    humidity= json_data['main']['humidity']
    pressure= json_data['main']['pressure']
    wind= json_data['wind']['speed']
    description= json_data['weather'][0]['description']

    t.config(text=f"{temp} °C")
    h.config(text=f"{humidity} %")
    p.config(text=f"{pressure} hPa")
    w.config(text=f"{wind} m/s")
    d.config(text=description)

    #days
    first= datetime.now()
    day1.config(text=first.strftime("%A"))

    second=first+timedelta(days=1)
    day2.config(text=second.strftime("%A"))

    third=first+timedelta(days=2)
    day3.config(text=third.strftime("%A"))

    forth=first+timedelta(days=3)
    day4.config(text=forth.strftime("%A"))

    fifth=first+timedelta(days=4)
    day5.config(text=fifth.strftime("%A"))

    sixth=first+timedelta(days=5)
    day6.config(text=sixth.strftime("%A"))

    seventh=first+timedelta(days=6)
    day7.config(text=seventh.strftime("%A"))

##icon
image_icon=PhotoImage(file="D:\Coding\Python\Weather The APP\Images\logo.png")
root.iconphoto(False,image_icon)                 

Round_box=PhotoImage(file="D:\Coding\Python\Weather The APP\Images\Rounded Rectangle 1.png")
Label(root,image=Round_box, bg="#57adff").place(x=30,y=110)

#label
label1=Label(root,text="Temperature",font=('Helvetica', 11), fg="white", bg="#203242")
label1.place(x=50,y=120)

label2=Label(root,text="Humidity",font=('Helvetica', 11), fg="white", bg="#203242")
label2.place(x=50,y=140)

label3=Label(root,text="Pressure",font=('Helvetica', 11), fg="white", bg="#203242") 
label3.place(x=50,y=160)

label4=Label(root,text="Wind Speed",font=('Helvetica', 11), fg="white", bg="#203242")
label4.place(x=50,y=180)

label5=Label(root,text="Description",font=('Helvetica', 11), fg="white", bg="#203242")
label5.place(x=50,y=200)
             
#search_box
Search_Image=PhotoImage(file="D:\Coding\Python\Weather The APP\Images\Rounded Rectangle 3.png")
myimage=Label(image=Search_Image, bg='#57adff')
myimage.place(x=270,y=120)

weat_image=PhotoImage(file="D:\Coding\Python\Weather The APP\Images\Layer 7.png")
weatherimage=Label(root,image=weat_image,bg="#203243")
weatherimage.place(x=290,y=127)

textfield=tk.Entry(root,justify='left',width=15,font=('poppins',25,'bold'),bg='#203243',border=0,fg="white")
textfield.place(x=370,y=130)
textfield.focus()

Search_icon=PhotoImage(file="D:\Coding\Python\Weather The APP\Images\Layer 6.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#203243",command=getWeather)
myimage_icon.place(x=645,y=125)

#Bottom box
frame=Frame(root,width=900,height=180,bg="#212120")
frame.pack(side=BOTTOM)

#DayNightInfo
Sunrise_image=PhotoImage(file="D:\Coding\Python\Weather The APP\icon\Sunrise.png")
sunriseimage=Label(root,image=Sunrise_image,bg="#212120")
sunriseimage.place(x=40,y=300)

#bottom subboxes
firstbox=PhotoImage(file="D:\Coding\Python\Weather The APP\Images\Rounded Rectangle 2.png")
secondbox=PhotoImage(file="D:\Coding\Python\Weather The APP\Images\Rounded Rectangle 2 copy.png")

#Label(frame,image=firstbox,bg="#212120").place(x=30,y=20)
Label(frame,image=secondbox,bg="#212120").place(x=300,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=400,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=500,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=600,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=700,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=800,y=30)

# Create labels to display weather information
t = Label(root, font=('Helvetica', 12), fg="white", bg="#203242")
t.place(x=150, y=120)

h = Label(root, font=('Helvetica', 12), fg="white", bg="#203242")
h.place(x=150, y=140)

p = Label(root, font=('Helvetica', 12), fg="white", bg="#203242")
p.place(x=150, y=160)

w = Label(root, font=('Helvetica', 12), fg="white", bg="#203242")
w.place(x=150, y=180)

d = Label(root, font=('Helvetica', 12), fg="white", bg="#203242")
d.place(x=150, y=200)

#first cell
firstframe=Frame(root,width=230,height=132,bg="#282829")
firstframe.place(x=35,y=315)

day1=Label(firstframe,font="arial 20", bg="#282829", fg="#fff")
day1.place(x=70,y=5)

#second cell
secondframe=Frame(root,width=70,height=115,bg="#282829")
secondframe.place(x=305,y=325)

day2=Label(secondframe, bg="#282829", fg="#fff")
day2.place(x=10,y=5)

#third cell
thirdframe=Frame(root,width=70,height=115,bg="#282829")
thirdframe.place(x=405,y=325)

day3=Label(thirdframe, bg="#282829", fg="#fff")
day3.place(x=10,y=5)

#forth cell
forthframe=Frame(root,width=70,height=115,bg="#282829")
forthframe.place(x=505,y=325)

day4=Label(forthframe, bg="#282829", fg="#fff")
day4.place(x=10,y=5)

#fivth cell
fifthframe=Frame(root,width=70,height=115,bg="#282829")
fifthframe.place(x=605,y=325)

day5=Label(fifthframe, bg="#282829", fg="#fff")
day5.place(x=6,y=5)

#sixth cell
sixthframe=Frame(root,width=70,height=115,bg="#282829")
sixthframe.place(x=705,y=325)

day6=Label(sixthframe, bg="#282829", fg="#fff")
day6.place(x=10,y=5)

#seventh cell
seventhframe=Frame(root,width=70,height=115,bg="#282829")
seventhframe.place(x=805,y=325)

day7=Label(seventhframe, bg="#282829", fg="#fff")
day7.place(x=10,y=5)

# ... (your code) ...

# Create labels for temperature values
temp1 = Label(firstframe, text="25°C", font=("Helvetica", 14), bg="#282829", fg="#fff")
temp1.place(x=70, y=40)

temp2 = Label(secondframe, text="26°C", bg="#282829", fg="#fff")
temp2.place(x=10, y=40)

temp3 = Label(thirdframe, text="24°C", bg="#282829", fg="#fff")
temp3.place(x=10, y=40)

temp4 = Label(forthframe, text="27°C", bg="#282829", fg="#fff")
temp4.place(x=10, y=40)

temp5 = Label(fifthframe, text="28°C", bg="#282829", fg="#fff")
temp5.place(x=6, y=40)

temp6 = Label(sixthframe, text="26°C", bg="#282829", fg="#fff")
temp6.place(x=10, y=40)

temp7 = Label(seventhframe, text="25°C", bg="#282829", fg="#fff")
temp7.place(x=10, y=40)

#image addition to columns
image1 = PhotoImage(file="D:\Coding\Python\Weather The APP\icon\Sunrise.png")
image_label1 = Label(firstframe, image=image1, bg="#282829")
image_label1.place(x=70, y=40)

image2 = PhotoImage(file="D:\Coding\Python\Weather The APP\icon\Sunrise.png")
image_label2 = Label(secondframe, image=image2, bg="#282829")
image_label2.place(x=10, y=60)

image3 = PhotoImage(file="D:\Coding\Python\Weather The APP\icon\Sunrise.png")
image_label3 = Label(thirdframe, image=image3, bg="#282829")
image_label3.place(x=10, y=60)

image4 = PhotoImage(file="D:\Coding\Python\Weather The APP\icon\Sunrise.png")
image_label4 = Label(forthframe, image=image4, bg="#282829")
image_label4.place(x=10, y=60)

image5 = PhotoImage(file="D:\Coding\Python\Weather The APP\icon\Sunrise.png")
image_label5 = Label(fifthframe, image=image5, bg="#282829")
image_label5.place(x=6, y=60)

image6 = PhotoImage(file="D:\Coding\Python\Weather The APP\icon\Sunrise.png")
image_label6 = Label(sixthframe, image=image6, bg="#282829")
image_label6.place(x=10, y=60)

image7 = PhotoImage(file="D:\Coding\Python\Weather The APP\icon\Sunrise.png")
image_label7 = Label(seventhframe, image=image7, bg="#282829")
image_label7.place(x=10, y=60)

# ... (rest of your code) ...


#clock
clock=Label(root,font=("Helvetica",30,'bold'),fg="white",bg="#57adff")
clock.place(x=30,y=20)

#timezone
timezone=Label(root,font=("Helvetica",20),fg="white",bg="#57adff")
timezone.place(x=700,y=20)

long_lat=Label(root,font=("Helvetica",10),fg="white",bg="#57adff")
long_lat.place(x=700,y=50)




root.mainloop()
