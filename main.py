import pandas as pd
import streamlit as st

## Role related Training
header = st.container()
dataset = st.container()
features = st.container()
modelTraining = st.container()

with header:
    st.title('Role Related Training')
    st.text('Find the training related to your Infor LN role.')
    roleData = pd.read_csv('inforRoles.csv')
    st.write(roleData.head())
    trainingData = pd.read_csv('TrainingMatrix.csv',sep=";")
    df = pd.DataFrame(trainingData)

with dataset:
    st.title('Select an Infor LN Role')
    role = st.selectbox('Select a role', roleData, index = None,
    placeholder="Select your Infor Ln role",)
    
    
selectedRole = st.write("You selected:", role)

if role == "BEFI20 - Accountant":
    st.text('yes')
else:
    st.text('no')

for index, row in df.iterrows():
    print(row['TrainingName'], row['TrainingDescription'])

