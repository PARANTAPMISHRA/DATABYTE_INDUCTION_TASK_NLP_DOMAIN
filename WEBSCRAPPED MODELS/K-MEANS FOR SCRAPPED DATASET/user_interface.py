# IMPORTING ALL THE LIBRARIES.
from flask import Flask,render_template,json,request
import pandas as pd
import numpy as np

# CREATING AN INSTANCE OF A FLASK CLASS SO THAT WE CAN ACCESS FILES (HTML,CSS,JS) WHICH ARE STORED IN TEMPLATES AND STATIC FOLDER.
app=Flask(__name__)

def find_8_very_similar_movies(similar_movies_vectors,vector_of_entered_movie):
    d=[]
    for i in (similar_movies_vectors):
    
        #print((i-vector_of_entered_movie).shape)
        d.append(np.sqrt(np.dot((i-vector_of_entered_movie).reshape(-1),(i-vector_of_entered_movie).reshape(-1)))) # HERE I AM RESHAPING THE (i-vector_of entered_movie) as shape of vector of entered movie is 
                                                                                                                   #(1,5557) DUE TO WHCIH I AM NOT ABLE TO FIND THE dot product directly.                                                                                                                
    d=sorted(list(enumerate(d)),key=lambda x:x[1])
    return(d)

#LOADING THE DATASET
data=pd.read_excel(r'C:\Users\pc\OneDrive\Desktop\MOVIE RECOMMENDATION SYSTEM USING TF-IDF\model\DATASET_SCRAPPED_FROM_IMDb..xlsx')
movie_names=list(data['title'])

#LOADING THE COSINE_SIMILARITY_VECTORS
vectors=pd.read_pickle(r'C:\Users\pc\OneDrive\Desktop\K-MEANS FOR SCRAPPED DATASET\model\tfidf_vectors.pkl')
vectors=list(np.array(vectors))

a=pd.read_pickle(r'C:\Users\pc\OneDrive\Desktop\K-MEANS FOR SCRAPPED DATASET\model\clusterinfo.pkl')
a=list(np.array(a))
# CREATING A DECORATOR WHICH IS USED TO SIGNIFY WHAT FUNCTION IS NEED TO BE PERFORMED WHEN USER IS DIRETED TO A SPECIFIC PAGE.
@app.route('/')

def home():
    

    return render_template('HOME_PAGE.HTML',movie_names=movie_names)
@app.route('/RECOMMENDATION_PAGE',methods=['post'])
def suggestions():
    movie_posters=[]
    movie_genre=[]
    movie_summary=[]
    movie_entered=request.form.get('movie')                    # GETTING THE INPUT OF THE USER FROM THE FORM NAMED 'movie'.
    movie_index=np.array(data[data['title']==movie_entered].Column1)[0] # FINDING THE INDEX OF THE MOVIE ENTERED.
    print(movie_index)
    vector_of_the_entered_movie=vectors[movie_index] # VECTOR OF THE ENTERED MOVIE.
    cluster_to_which_movie_belong=a[movie_index] # FINDING THE CLUSTER TO WHICH THE MOVIE BELONGS.
    similar_movies_index=[] # LIST TO STORE THE MOVIES IN THE SAME CLUSTER.
    similar_movies_vectors=[] # LIST TO STORE THE VECTORS OF THE MOVIES IN THE SAME CLUSTER.
    for i in range(0,len(a)):
        if cluster_to_which_movie_belong==a[i]:
            similar_movies_index.append(i)
           # print(data.iloc[i].title)
    for i in similar_movies_index:
        similar_movies_vectors.append(vectors[i])
    idx_of_very_similar_movies=[]
    very_similar_movies=[]
    distance=find_8_very_similar_movies(np.array(similar_movies_vectors),np.array(vector_of_the_entered_movie)) # FINDING THE 8 VERY SIMILAR MOVIES.
    #print(vector_of_the_entered_movie)
    #print(np.array(vector_of_the_entered_movie).shape)
    for i in distance:
        idx_of_very_similar_movies.append(similar_movies_index[i[0]])
    for i in idx_of_very_similar_movies[1::]:
        looping_variable1=data.iloc[i].title
        looping_variable2=data.iloc[i].posterlink
        looping_variable3=data.iloc[i].genre
        looping_variable4=data.iloc[i].summary
        very_similar_movies.append(looping_variable1)
        movie_posters.append(looping_variable2)
        movie_genre.append(looping_variable3)
        movie_summary.append(looping_variable4)

        
    return render_template('RECOMMENDATION_PAGE.HTML',  movie_entered=movie_entered,similar_movies=very_similar_movies,posterlink=movie_posters,movie_genre=movie_genre,movie_summary=movie_summary)
if __name__=='__main__':
    app.run(debug=True)
    