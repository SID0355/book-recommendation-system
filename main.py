import streamlit as st
import numpy as np
import pandas as pd

books = pd.read_csv("Books.csv",encoding = "latin-1")
users = pd.read_csv("Users.csv",encoding = "latin-1")
ratings = pd.read_csv("Ratings.csv",encoding = "latin-1")
similarity_score = np.load('similarity_score.npy')
pivot_table = pd.read_pickle('pivot_table.pkl')
df = pd.read_pickle('df.pkl')


def recommend(book_name):
  index = np.where(pivot_table.index == book_name)[0][0] # index fetch
  similar_items = sorted(list(enumerate(similarity_score[index])), key = lambda x:x[1], reverse=True)[1:6]   
  # to get similar top 5 similar books, index form 1 because at 0th index the book itself present

  book = []
  for i in similar_items:
    book.append(pivot_table.index[i[0]])

  return book

def pred(user_id):
    for i in ratings[ratings['User-ID'] == user_id].sort_values('Book-Rating', ascending=False).loc[:,'ISBN'].values:
        r = np.where(pivot_table.index == i)[0]
        if r.size != 0:
            a =  recommend(i)
            if len(a) == 0:
                new = df.copy()
                new.reset_index(inplace=True)
                new.drop(columns='index',inplace=True)
                return new
            else :
                ind = []
                for i in a:
                    n = books[books['ISBN'] == i].index[0]
                    ind.append(n)
                ok = books.loc[ind,['Book-Title', 'Book-Author', 'Publisher', 'Image-URL-M']]
                ok.reset_index(inplace=True)
                ok.drop(columns='index',inplace=True)
                return ok


with open('bookstyle.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        
st.header("Books Recommenders System")
uid = st.number_input('User ID :',1)

ag = pred(uid)
if ag.shape[0] == np.nan:

    ag = df.copy()
    ag.reset_index(inplace=True)
    ag.drop(columns='index',inplace=True)

t11 = st.columns(2)

with t11[0]:
    st.text(ag.loc[0,'Book-Title'])
    st.text(ag.loc[0,'Book-Author'])
    st.text(ag.loc[0,'Publisher'])

with t11[1]:
    st.image(ag.loc[0,'Image-URL-M'], width=200)


t21 = st.columns(2)

with t21[0]:
    st.text(ag.loc[1,'Book-Title'])
    st.text(ag.loc[1,'Book-Author'])
    st.text(ag.loc[1,'Publisher'])

with t21[1]:
    st.image(ag.loc[1,'Image-URL-M'], width=200)


t31 = st.columns(2)

with t31[0]:
    st.text(ag.loc[2,'Book-Title'])
    st.text(ag.loc[2,'Book-Author'])
    st.text(ag.loc[2,'Publisher'])

with t31[1]:
    st.image(ag.loc[2,'Image-URL-M'], width=200)


t41 = st.columns(2)

with t41[0]:
    st.text(ag.loc[3,'Book-Title'])
    st.text(ag.loc[3,'Book-Author'])
    st.text(ag.loc[3,'Publisher'])

with t41[1]:
    st.image(ag.loc[3,'Image-URL-M'], width=200)


t51 = st.columns(2)

with t51[0]:
    st.text(ag.loc[4,'Book-Title'])
    st.text(ag.loc[4,'Book-Author'])
    st.text(ag.loc[4,'Publisher'])

with t51[1]:
    st.image(ag.loc[4,'Image-URL-M'], width=200)