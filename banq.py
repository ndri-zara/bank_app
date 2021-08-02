import streamlit as st
import numpy as np
import pandas as pd
from pickle import load


def main():

   st.write("App Simple pour la prévision des porteurs de carte bancaire Cette application prédit si le client de la carte bancaire restera")

   st.sidebar.header("les paramètres d'entrée")

   with st.form(key='form1'):
       Customer_Age = st.slider('l age du customer',26.0,73.0,5.3)
       Gender	 = st.slider('le genre',0.0,1.0,0.5)
       Education_Level = st.slider('le niveau d education',0.0,9.9,5.3)
       Income_Category = st.slider('le niveau de revenu' ,0.0,9.9,5.3)
       Card_Category	= st.slider('la catégorie de card' ,0.0,9.9,5.3)
       Credit_Limit	= st.slider('la limite de credit' ,4.3,100000.0,5.3)
       Avg_Utilization_Ratio = st.slider('le taux moyen dutilisation',0.0,1.0,0.5)
    
       bouton_prevision=st.form_submit_button(label='prévision')

   if bouton_prevision :
       data=[Customer_Age,
       Gender,
       Education_Level,
       Income_Category,
       Card_Category,
       Credit_Limit,
       Avg_Utilization_Ratio ]

       X = np.array(data).reshape(1,7)
       model = load(open('model.plk', 'rb'))

       y_pred = model.predict(X)
       st.write(y_pred)

if __name__=='__main__':
    main()

