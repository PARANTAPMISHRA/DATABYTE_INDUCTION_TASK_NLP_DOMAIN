# DATABYTE_INDUCTION_TASK_NLP_DOMAIN
 
This repository is for the DATABYTE INDUCTIONS TASK FOR NLP DOMAIN FOR CREATING THE THE MOVIE RECOMMENDER SYSTEM.

RECOMMENDER SYSTEM IS THE AREA WHICH IS HIGHLY USED IN THE COMPANIES FOR SUGGESTING THEIR CONSUMERS THE ITEM/PRODUCT WHICH THEY MAY LIKE.

# TYPES OF RECOMMENDATION SYSTEMS:
A) Content Based
B) Collaborative Filtering
C) Deep Neural Network Based

In my task I will be implementing the content based recommendation system using KNN ( which was mandatory ) and the K - Means ( which I did only to check how does the model perform on different algorithm). 
For converting the word into vectors so that we can feed it to the model I have used 2 techniques :
  1. Bag Of Words ( Binary Bag of Words to be specific ).
  2. Term-Frequency and Inverse-Document-Frequency (Tf-IDF)


## I have also made a data set which I have scraped from the IMDb website using BeautifulSoup. I used it because its doucmentation was very much detiled and self explainatory.

# AFTER IMPLEMENTING THE MODELS ON THE GIVEN DATASET FROM THE MOVIE_LENS I ALSO TRIED TO IMPELEMNT THE COLLABORATIVE FILTERING TECHNIQUE.
 Basically collaborative filetering can be divided into two domains:
 1. Memory Based
    1. User-User based
    2. Item-Item based
 2. Model Based:
    1. Matrix Factorization

For this task I have tried to implement the Matrix Factorization technique on the dataset which was given in the task as it has a dataset folder containg the rating of the movie given by the user having some id to some movie with its corresponding movie_id.

# Further I made a user interactive website in which user will enter the movie from the given list of the movies and model will recommend the similar movies based on either:
  1. Cosine Similarty ( for all models in which KNN is used ) and 
  2. Eucledian Distance ( for K-Means model )
