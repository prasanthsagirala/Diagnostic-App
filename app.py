import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle
st.title('Health Diagnostics')

#step1 :  Load the model
model = open('knn.pickle','rb')
clf = pickle.load(model)
model.close()

#step2 : get user input
pregs = st.number_input('Pregnancies',1,20,step=1)
glucose = st.slider('Glucose',40.0,200.0,40.0)
bp = st.slider('BloodPressure',24.0,122.0,24.0)
skt = st.slider('SkinThickness',5,100,7) 
insulin = st.slider('Insulin',14.0,845.0,18.0)
bmi=st.slider('BMI',18.0,68.0,18.2)
dpf = st.slider('DiabetesPedigreeFunction',0.0,3.0,0.0)
age = st.slider('Age',10,100,25)

#step3: user input to model input
data = {
    'Pregnancies':pregs, 'Glucose':glucose, 'BloodPressure':bp, 'SkinThickness':skt, 'Insulin':insulin,
       'BMI':bmi, 'DiabetesPedigreeFunction':dpf, 'Age':age
}
input_data = pd.DataFrame([data])

#step4
preds = clf.predict(input_data)[0]
if st.button('Predict'):
    if preds==1:
        st.error('The person has diabetes')
    if preds==0:
        st.success('The person is diabetes free')
