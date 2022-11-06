import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer

def music_that_i_like(df, like = False):
    """
    This function add a column which is 1 if a like the song, otherwise its value is 0. 

    Args:
        df (pd.DataFrame): The dataframe to add the column to.
        like (bool, optional): If the song is liked or not. Defaults to False.
    Return:
        df (pd.DataFrame): The dataframe with the new column.
    
    """
    if like:
        df['like'] = 1
    else:
        df['like'] = 0
    return df

def get_data():
    """
    This function gets the data for this project.
    Args:
        None
    Return:
        df (pd.DataFrame): The dataframe with the data.
    """
    # Read the data
    # Music that I like
    artic_monkeys_df = pd.read_csv('../data/arctic_monkeys_data.csv')
    artic_monkeys_df = music_that_i_like(artic_monkeys_df, like = True)
    cerati_df = pd.read_csv('../data/cerati_data.csv')
    cerati_df = music_that_i_like(cerati_df, like = True)
    new_fang_df = pd.read_csv('../data/new_fang_radio.csv')
    new_fang_df = music_that_i_like(new_fang_df, like = True)
    pink_floyd_df = pd.read_csv('../data/pink_floyd_data.csv')
    pink_floyd_df = music_that_i_like(pink_floyd_df, like = True)
    qotsa_df = pd.read_csv('../data/qotsa_data.csv')
    qotsa_df = music_that_i_like(qotsa_df, like = True)

    # Music that I don't like
    kpop_df = pd.read_csv('../data/kpop_radio.csv')
    kpop_df = music_that_i_like(kpop_df, like = False)
    reggaeton_df = pd.read_csv('../data/reggaeton1.csv')
    reggaeton_df = music_that_i_like(reggaeton_df, like = False)
    trapper_df = pd.read_csv('../data/trappers_argentina.csv')
    trapper_df = music_that_i_like(trapper_df, like = False)
    latino_df = pd.read_csv('../data/viva_latino.csv')
    latino_df = music_that_i_like(latino_df, like = False)
    tini_df = pd.read_csv('../data/tini.csv')
    tini_df = music_that_i_like(tini_df, like = False)
    camilo_df = pd.read_csv('../data/camilo.csv')
    camilo_df = music_that_i_like(camilo_df, like = False)
    top_hits_df = pd.read_csv('../data/top_hits.csv')
    top_hits_df = music_that_i_like(top_hits_df, like = False)
    cumbia_df = pd.read_csv('../data/cumbia.csv')
    cumbia_df = music_that_i_like(cumbia_df, like = False)
    elegante_df = pd.read_csv('../data/elegante.csv')
    elegante_df = music_that_i_like(elegante_df, like = False)
    villagran_df =pd.read_csv('../data/villagran.csv')
    villagran_df = music_that_i_like(villagran_df, like = False)
    pop_list_df = pd.read_csv('../data/pop_list.csv')
    pop_list_df = music_that_i_like(pop_list_df, like = False)
    bad_bunny_df = pd.read_csv('../data/bad_bunny.csv')
    bad_bunny_df = music_that_i_like(bad_bunny_df, like = False)
    daddy_yankee_df = pd.read_csv('../data/daddy_yankee.csv')
    daddy_yankee_df = music_that_i_like(daddy_yankee_df, like = False)

    ## Concat all the datasets
    df = pd.concat([artic_monkeys_df, cerati_df, new_fang_df, pink_floyd_df, qotsa_df,
    kpop_df, reggaeton_df, trapper_df, latino_df,
    tini_df, camilo_df, top_hits_df,villagran_df, elegante_df, cumbia_df, pop_list_df, bad_bunny_df,
    daddy_yankee_df], ignore_index=True)

    ## Drop duplicates
    df.drop_duplicates(inplace=True)

    return df

if __name__ == '__main__':
    df = get_data()
    ## Categorical an numerical variables that I'll use.
    numerical =['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness',
       'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo',
       'duration_ms', 'time_signature']
    categorical = ['year']
    #Splitting the data
    df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)
    df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=1)

    df_train = df_train.reset_index(drop=True)
    df_val = df_val.reset_index(drop=True)
    df_test = df_test.reset_index(drop=True)

    y_train = df_train.like.values
    y_val = df_val.like.values
    y_test = df_test.like.values

    del df_train['like']
    del df_val['like']
    del df_test['like']

    ## One Hot Encoding
    dv = DictVectorizer(sparse=False)

    train_dict = df_train[categorical + numerical].to_dict(orient='records')
    X_train = dv.fit_transform(train_dict)

    val_dict = df_val[categorical + numerical].to_dict(orient='records')
    X_val = dv.transform(val_dict)

    ## Logistic Regression
    model = LogisticRegression(solver='lbfgs', C = 0.01)
    model.fit(X_train, y_train)
    ## Saving the model as a pickle
    with open('../models/model.pkl', 'wb') as f:
        pickle.dump(model, f)
    ## Saving the DictVectorizer as a pickle
    with open('../models/dv.pkl', 'wb') as f:
        pickle.dump(dv, f)
