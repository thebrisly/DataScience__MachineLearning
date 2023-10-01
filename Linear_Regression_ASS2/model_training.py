"""
# Assignment part two

We received new intelligence about the rogue agent which lets us discover his age.
Use the table "social_media_SIMF_archive.csv" to create a model that predicts the age of a person. Use this model to predict the ages of the table of suspects "suspect_social_media_statistics.csv".

Retain only the list of suspects whose age is between 25-35.

##Getting to know our data
- userId: Unique number given to each user.
- tier: Tier of the city in which the user is residing.
- gender: Categorical feature representing the gender of the user. 1 represents male and 2 represents female.
- following_rate: Number of accounts followed by the user(feature is normalized)
- followers_avg_age: Average of age groups of all the followers of the user.
- following_avg_age: Average of age groups of all the accounts followed by the user.
- max_repetitive_punc: Maximum repititive punctuations found in the bio and comments of the user.
- num_of_hashtags_per_action: Average nubmer of hashtags used by the user per comment.
- emoji_count_per_action: Average number of emojis used by the user per comment
- punctuations_per_action: Average number of punctuations used by the user per comment.
- number_of_words_per_action: Average number of words used by the user per comment.
- avgCompletion: Average watch time completion rate of the videos.
- avgTimeSpent: Average time spent by the user on a video in seconds.
- avgDuration: Average duration of the videos that the user has watched till date.
- avgComments: Average number of comments per video watched.
- creations: Total number of videos uploaded by the user.
- content_views: Total number of videos watched.
- num_of_comments: Total number of comments made by the user (normalized)
- weekends_trails_watched_per_day: Number of videos watched on weekends per day.
- weekdays_trails_watched_per_day: Number of videos watched on weekdays per day.
- slot1_trails_watched_per_day: The day is divided into 4 slots. This feature represents the average number of videos watched in this particular time slot.
- slot2_trails_watched_per_day: The day is divided into 4 slots. This feature represents the average number of videos watched in this particular time slot.
- slot3_trails_watched_per_day: The day is divided into 4 slots. This feature represents the average number of videos watched in this particular time slot.
- slot4_trails_watched_per_day: data
- avgt2: Average number of followers of all the accounts followed by the user.
- age : The age of the user
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
train_dataset = pd.read_csv("https://raw.githubusercontent.com/michalis0/DataScience_and_MachineLearning/master/Assignements/Part%202/data/social_media_SIMF_archive.csv")
suspects = pd.read_csv("https://raw.githubusercontent.com/michalis0/DataScience_and_MachineLearning/master/Assignements/Part%202/data/suspects_social_media.csv")

"""### Training a model
Select the features which by convention are called X. We will also choose the target variable which we typically call y.

You can use the features 'tier', 'gender', 'following_rate', 'followers_avg_age', 'following_avg_age', 'max_repetitive_punc', 'num_of_hashtags_per_action', 'emoji_count_per_action', 'punctuations_per_action', 'number_of_words_per_action', 'avgCompletion', 'avgTimeSpent', 'avgDuration', 'avgComments', 'creations', 'content_views', 'num_of_comments', 'weekends_trails_watched_per_day', 'weekdays_trails_watched_per_day', 'slot1_trails_watched_per_day', 'slot2_trails_watched_per_day', 'slot3_trails_watched_per_day', 'slot4_trails_watched_per_day', 'avgt2'
"""

feature_names = ['tier', 'gender', 'following_rate', 'followers_avg_age', 'following_avg_age', 'max_repetitive_punc', 'num_of_hashtags_per_action', 'emoji_count_per_action', 'punctuations_per_action', 'number_of_words_per_action', 'avgCompletion', 'avgTimeSpent', 'avgDuration', 'avgComments', 'creations', 'content_views', 'num_of_comments', 'weekends_trails_watched_per_day', 'weekdays_trails_watched_per_day', 'slot1_trails_watched_per_day', 'slot2_trails_watched_per_day', 'slot3_trails_watched_per_day', 'slot4_trails_watched_per_day', 'avgt2']
target = ['age']

X = train_dataset[feature_names]
y = train_dataset[target]

#just to check what the dataset looks like :
train_dataset.head()
suspects.head()

"""Now, do the test-trainsplit, using as train 80% of the data and random state 42"""

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#check if the len of the training is 80% of train_dataset (X) and if the test if 20%
print(train_dataset.shape)
print(len(X_train)) #(it is !)
print(len(X_test)) # also correct

"""#Here we could add one hot encoding, what do you think ?

##Linear regression
Now, create the linear model. Train it with the train set and use the model to make predictions on the test set. Which accuracy do you achieve on the test set?
"""

# do the right imports
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# create the model
model = LinearRegression()

# Fit the model
model.fit(X_train, y_train)

"""and we do the predictions on the test set:"""

#Your code here
#we want to predct on the test set
predicted = model.predict(X_test)
print(y_test)

#if i want to check the accuracy of the values
model.score(X_test, y_test) # result is 66% so not that good but not that bad tho

"""What are the model's $MAE$ and $R^2$ ?"""

#mae needs to be small
#https://www.sciencedirect.com/topics/engineering/mean-absolute-error
mae = mean_absolute_error(y_test, predicted)
print("MAE :", mae)

#the more r2 is next to 1, the more accurate my model is
r2 = r2_score(y_test, predicted)
print("R^2 :", r2)

"""## Retraining on the full dataset

Before predicting the age of the suspects, retrain the model on the full training dataset to ensure the greater results.

You can reuse the same features as before, but make sure those are also available on the suspects dataset.
"""

suspects_features = suspects[feature_names]

# create the new model
# Fit the new model
new_model = model.fit(X, y)

# Make the predictions
suspects['predicted_age'] = new_model.predict(suspects_features)

"""## Which suspects remain after identifying users between 25 and 35 years old ?"""

filtered_suspects = suspects[(suspects['predicted_age'] >= 25) & (suspects['predicted_age'] <= 35)]
print(filtered_suspects['predicted_age'])
print(filtered_suspects.shape)