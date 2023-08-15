# IMPORTING ALL THE LIBRARIES.
from flask import Flask,render_template,json,request
import pandas as pd
import numpy as np
import requests

# CREATING AN INSTANCE OF A FLASK CLASS SO THAT WE CAN ACCESS FILES (HTML,CSS,JS) WHICH ARE STORED IN TEMPLATES AND STATIC FOLDER.

app=Flask(__name__)


# LOADING ALL THE FILES 

TMDbId=np.array(pd.read_pickle(r'C:\Users\pc\OneDrive\Desktop\MOVIE_LENS\MODEL\TMDbId.pkl'))

movie_names=pd.read_pickle(r'C:\Users\pc\OneDrive\Desktop\MOVIE_LENS\MODEL\movie_names.pkl')

similarity=np.array(pd.read_pickle(r'C:\Users\pc\OneDrive\Desktop\MOVIE_LENS\MODEL\vectors.pkl'))


movie_names=[i[0] for i in np.array(movie_names)]


url='http://image.tmdb.org/t/p/w185/'
headers={
        'accept':'application/json',
        'Authorization' : 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzMGM2NjhkNzI4NzhjZmM3N2FjOWEzMjllN2QwNWIwOSIsInN1YiI6IjY0YzIyNjRlZGI0ZWQ2MDEzYmYzYmFjZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.bbJZMwFW9E6Iuv1BbIGGeQjx4rXWaKJZ3iphFLCDBy4'
    }

@app.route('/')

def home():
    return render_template('HOME_PAGE.HTML', movie_names=movie_names)


@app.route('/RECOMMENDATION_PAGE',methods=['post'])

def recommend_movies():
    movie_entered=request.form.get('movie')
    movie_index=movie_names.index(movie_entered)
    movie_vector=similarity[movie_index]
    sorted_movie_vectors=sorted(list(enumerate(movie_vector)),reverse=True,key=lambda x:x[1])[1:6]
    similar_movies_names=[]
    tmdbids=[]
    for i in sorted_movie_vectors:
        similar_movies_names.append(movie_names[i[0]])
        tmdbids.append(int(TMDbId[i[0]][0]))

    poster_url=[]
    overview=[]
    homepage=[]
    for i in range(0,len(tmdbids)):
        g_url='https://api.themoviedb.org/3/movie/'+str(tmdbids[i])   
        movie_data=requests.get(g_url,headers=headers)
        movie_data=movie_data.json()
        overview.append(movie_data['overview'])
        homepage.append(movie_data['homepage'])
        poster_url.append(url+movie_data['poster_path'])
    return render_template('RECOMMENDATION_PAGE.HTML',movie_entered=movie_entered,tmdbId=poster_url,homepages=homepage,overviews=overview,recommends=similar_movies_names)

if __name__=='__main__':
    app.run(debug=True)