# spotify-recommender-systems
Exploration implementing recommender systems using Spotify data.

## Overview

Although traditional machine learning methods can work for recommendations, the requirement for labels and a training 
data set means we are reliant on the user to define their favourites (classification) or to accurately score songs 
(regression). This doesn't work well as a few cases of mislabelling can greatly reduce model performance. It also means
that when a user has a fresh account or doesn't provide any ratings (cold-start problem) then we can be stuck without training data. 

Recommendation systems avoid these caveats with a variety of techniques:

- Content filter: Generally use the cosine similarity on TF-IDF of features such as artist and genre.
We can also use the cosine similarity of various features here, but this tends not to be the best method
as in general most people listen to a variety of songs with variable 'acousticness' or 'danceability', not just 
a set.
- Collaborative filter: Recommend based on similar user preferences
- Hybrid filter: A mix of content and collaborative
- Popularity: Recommend popular songs regardless of user's preferences
- Popularity + Hybrid: So as to avoid high variance which can lead to only recommending a set group of 
songs, we can mix in some recommendations based on e.g. popularity and features such as 'energy'
- Genre Weighting: Can be set in the content filter or by scaling recommendations by % of genre matching. But in general 
this is covered by the content filter implementation

Useful links:

- https://developer.spotify.com/documentation/web-api/reference/
- https://spotipy.readthedocs.io/
- https://developer.spotify.com/dashboard/applications
- https://developer.spotify.com/documentation/general/guides/authorization-guide/#list-of-scopes
