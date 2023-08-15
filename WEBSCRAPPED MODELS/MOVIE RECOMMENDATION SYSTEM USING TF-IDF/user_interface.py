# IMPORTING ALL THE LIBRARIES.
from flask import Flask,render_template,json,request
import pandas as pd
import numpy as np

# CREATING AN INSTANCE OF A FLASK CLASS SO THAT WE CAN ACCESS FILES (HTML,CSS,JS) WHICH ARE STORED IN TEMPLATES AND STATIC FOLDER.
app=Flask(__name__)

#LOADING THE DATASET
data=pd.read_excel(r'C:\Users\pc\OneDrive\Desktop\MOVIE RECOMMENDATION SYSTEM USING TF-IDF\model\DATASET_SCRAPPED_FROM_IMDb..xlsx')
movie_names=list(data['title'])

#LOADING THE COSINE_SIMILARITY_VECTORS
cosine_similarty_vectors=pd.read_pickle(r'C:\Users\pc\OneDrive\Desktop\MOVIE RECOMMENDATION SYSTEM USING TF-IDF\model\cosine_similarity_vectors_by_tfidf.pkl')
cosine_similarty_vectors=list(np.array(cosine_similarty_vectors))

# CREATING A DECORATOR WHICH IS USED TO SIGNIFY WHAT FUNCTION IS NEED TO BE PERFORMED WHEN USER IS DIRETED TO A SPECIFIC PAGE.
@app.route('/')

def home():
    

    return render_template('HOME_PAGE.HTML',movie_names=movie_names)
@app.route('/RECOMMENDATION_PAGE',methods=['post'])
def suggestions():
    movie_entered=request.form.get('movie')                    # GETTING THE INPUT OF THE USER FROM THE FORM NAMED 'movie'.
    movie_index=int(data[data['title']==movie_entered].Column1)
    movie_vector=cosine_similarty_vectors[movie_index]
    sorted_movie_vectors=sorted(list(enumerate(movie_vector)),reverse=True,key=lambda x:x[1])[1:10]
    movie_names=[]
    movie_posters=[]
    movie_genre=[]
    movie_summary=[]
    for i in sorted_movie_vectors:
        looping_variable1=data.iloc[i[0]].title
        looping_variable2=data.iloc[i[0]].posterlink
        looping_variable3=data.iloc[i[0]].genre
        looping_variable4=data.iloc[i[0]].summary
        movie_names.append(looping_variable1)
        movie_posters.append(looping_variable2)
        movie_genre.append(looping_variable3)
        movie_summary.append(looping_variable4)

    return render_template('RECOMMENDATION_PAGE.HTML',  movie_entered=movie_entered,similar_movies=movie_names,posterlink=movie_posters,movie_genre=movie_genre,movie_summary=movie_summary)
@app.route('/templates/ABOUT')
def about():
    return render_template('ABOUT.HTML')


@app.route('/templates/CONTACT')
def contact():
    return render_template('CONTACT.HTML')
if __name__=='__main__':
    app.run(debug=True)
    