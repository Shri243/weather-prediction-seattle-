import numpy as np
import pandas as pd 

data = pd.read_csv('seattle-weather.csv')
data = data.drop(["date"], axis = 1)

y = data['weather']
features =['temp_max', 'temp_min', 'precipitation', 'wind']
x = data[features]

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score

from sklearn import preprocessing
lc = preprocessing.LabelEncoder()
data["weather"] = lc.fit_transform(data["weather"])

from sklearn.model_selection import  train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 2)

gbc = GradientBoostingClassifier()
gbcmodel = gbc.fit(x_train, y_train)
print("Accuracy of GBC Model is "+str(gbc.score(x_test, y_test)*100))

def predict():
    x = float(tit01.get())
    y = float(tit02.get())
    z = float(tit03.get())
    p = float(tit04.get())
    pr = gbcmodel.predict([[x,y,z,p]])
    print(pr[0])
    l5["text"] = "Predicted weather : "+str(pr[0])

from tkinter import *
from tkinter import messagebox 

col = 'aqua'

window = Tk()
window['background'] = col
window.geometry("665x450")
window.title("WEATHER PREDICTION SYSTEM")

l0 = Label(window, text = "WEATHER PREDICTION SYSTEM",font= 25)
l0['bg'] = col 
l0.place(x=180,y=20)

l1 = Label(window, text = "Min Temprachure",font= 35)
l1['bg'] = col
l1.place(x=100,y=90)

l2 = Label(window, text = "Max Temprachure",font= 35)
l2['bg'] = col
l2.place(x=100,y=150)

l3 = Label(window, text = "   Precipitasion",font= 35)
l3['bg'] = col 
l3.place(x=100,y=210)

l4 = Label(window, text = "     wind speed",font= 35)
l4['bg'] = col 
l4.place(x=100,y=270)

predict = Button(window,text = "Predict",font = 30,width=10,height=1,command=predict)
predict.place(x=110,y=350)
predict['bg'] = 'lawngreen'

tit01 = Entry(window,width = 20 ,font = 30)
tit01.place(x=300,y=90)

tit02 = Entry(window,width = 20 ,font = 30)
tit02.place(x=300,y=150)

tit03 = Entry(window,width = 20 ,font = 30)
tit03.place(x=300,y=210)

tit04 = Entry(window,width = 20 ,font = 30)
tit04.place(x=300,y=270)

l5 = Label(window, text = "Predict weather by entering the details",font= 35)
l5['bg'] = col 
l5.place(x=270,y=350)

window.mainloop()