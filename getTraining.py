import openpyxl
import pandas as pd
import streamlit as st
import markdown

header = st.container()
dataset = st.container()
trainingOutput = st.container()
#col1, col2= st.columns(2, gap="small", border=True)
col1= st.columns(1, border=True)

# load excel with its path 
trainingMatrix = openpyxl.load_workbook("TrainingMatrix.xlsx") 
trainingNames = openpyxl.load_workbook("trainingNames.xlsx")

trainingMatrix_sh = trainingMatrix.active
trainingNames_sh = trainingNames.active

with header:
    st.title('Infor LN Role Related Training')
    st.image("PR.jpg")
    st.divider()
    st.subheader('Find the training related to your Infor LN role.')
    roleData = pd.read_csv('inforRoles.csv')
    #st.write(roleData.head()) 
    trainingNames = pd.read_excel('trainingNames.xlsx')

#with col1:
    role = st.selectbox('Select a role', roleData, index = None,
    placeholder="Select your Infor LN role",)
      
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
                                                
                    st.write(f"**{training_name.value}**")
                    #st.write(f"**{training_name.value}**")
                    st.text("Description: " + "\n" + training_description.value)
                    st.link_button("Find training dates", "https://boskalis.sharepoint.com/sites/D001418/SitePages/Training-Dates.aspx#register-for-training")
                    st.divider()
    
# with col2:
#     trnName = st.selectbox('Register for training', trainingNames, index = None,
#     placeholder="Select training name",)
   
    
#     df = pd.DataFrame(trainingNames)
#     #st.write(trainingNames.head()) 
#     #df.loc[:,"January 2025" : "December 2025"]
#     #df.iloc[1:2, 1:13]

#     for i in range(1, trainingNames_sh.max_row+1):

#         for j in range(1, trainingNames_sh.max_column+1): 
        
#             cell_objName = trainingNames_sh.cell(i, column=1) #1,1; 2,1; 3,1
#             Dates = trainingNames_sh.cell(i,column=j + 1) #1,2; 2,3; 3;4
                                
#             if cell_objName.value == trnName:                                                     

#                 with col2:                                        
#                     st.text("Available Date: " + "\n" + str(Dates.value))  
#                     st.divider()

        



               

    

                