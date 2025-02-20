import openpyxl
import pandas as pd
import streamlit as st
import markdown

header = st.container()
dataset = st.container()
trainingOutput = st.container()
col1, col2 = st.columns(2)

# load excel with its path 
trainingMatrix = openpyxl.load_workbook("TrainingMatrix.xlsx") 
trainingDates = openpyxl.load_workbook("trainingDates.xlsx")

trainingMatrix_sh = trainingMatrix.active
trainingDates_sh = trainingDates.active

with header:
    st.title('Infor LN Role Related Training')
    st.image("PR.jpg")
    st.divider()
    st.subheader('Find the training related to your Infor LN role.')
    roleData = pd.read_csv('inforRoles.csv')
    #st.write(roleData.head()) 

with col1:
    role = st.selectbox('Select a role', roleData, index = None,
    placeholder="Select your Infor Ln role",)
      
# iterate through excel and display data 

    for j in range(1, trainingMatrix_sh.max_column+1): 

        for i in range(1, trainingMatrix_sh.max_row+1): 
            cell_obj = trainingMatrix_sh.cell(i, column=j)
            role_name = trainingMatrix_sh.cell(1,column=j)
            training_catagory = trainingMatrix_sh.cell(i,column=1)
            training_name = trainingMatrix_sh.cell(row=i,column=2)
            training_description = trainingMatrix_sh.cell(row=i,column=3)    
            training_date = trainingMatrix_sh.cell(row=i,column=4)  
                 
            
            if cell_obj.value == "x":
                if role_name.value == role:                                                         
                                                
                            st.write("Training name: " + f"**{training_name.value}**")
                            st.text("Description: " + training_description.value)
                            st.text("Dates: " + "\n" + str(training_date.value))
                            st.divider()
    
with col2:
    trainingDatesData = st.selectbox('Select date', trainingMatrix_sh.values, index = None,
    placeholder="Select date",)

    

                