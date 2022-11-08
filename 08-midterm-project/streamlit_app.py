from contextlib import suppress
import streamlit as st
from PIL import  Image
import pickle 
import json 
import pandas as pd 

st.write("""
# I would like this music?
# Well, we can find out.
This app predicts if I will like a music or not.
"""
)
st.markdown("""
<style>
.big-font {
    font-size:50px !important;
}
</style>
""", unsafe_allow_html=True)

@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_model():
    model = 'models/model.pkl'
    dv = 'models/dv.pkl'

    with open(model, 'rb') as f_in:
        model = pickle.load(f_in)
    with open(dv, 'rb') as f_in:
        dv = pickle.load(f_in)
    return model, dv 

model, dv = load_model()

final_data_df = pd.read_csv('data/final_data.csv')

musics = final_data_df.name 
artists = final_data_df.
##Select the music
music = st.selectbox(
    'Music',
    musics
)

image = Image.open('images/spotify.PNG')
st.image(image, caption='')





# customer = {'CreditScore': float(credit_score),
#  'Geography': str(geography),
#  'Gender': str(gender),
#  'Age': int(age),
#  'Tenure': int(tenure),
#  'Balance': float(balance),
#  'NumOfProducts': int(num_of_products),
#  'HasCrCard': str(has_cr_card)=='Yes',
#  'IsActiveMember': str(is_active_member)=='Yes',
#  'EstimatedSalary': float(estimated_salary),
#  }
# pred = pipeline.predict_proba(customer)[0,1]
# pred = float(pred)
# col1_pred, col2_pred = st.columns(2)

# col1_pred.write("Probability of living the bank:")
# col2_pred.write(f"{pred*100:.2f}%")


st.write("""
This project was done as a part of [the project-of-the-week 
initiative at DataTalks.Club](https://github.com/DataTalksClub/project-of-the-week/blob/main/2022-08-14-frontend.md).
""")