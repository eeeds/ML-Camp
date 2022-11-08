from contextlib import suppress
import streamlit as st
from PIL import  Image
import pickle 
import json 
import pandas as pd 

st.write("""
# Would I like this music?
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
##Select the music
music = st.selectbox(
    'Music',
    musics
)
image = Image.open('images/spotify.PNG')
st.image(image, caption='')


music_selected = final_data_df[final_data_df['name']==music].reset_index()
music_selected.drop(['like'], inplace= True, axis = 1)


music_selected = music_selected.to_dict(orient='records')[0]
X = dv.transform(music_selected)
pred = model.predict_proba(X)[0, 1]


col1, col2 = st.columns(2)


col1.write("Probability of liking this music:")
col2.write(f"{pred*100:.2f}%")




st.write("""
This project was done as a part of [Midterm-Project](https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp), this project is part of ML-Zoomcamp provided by DataTalkClub.
""")