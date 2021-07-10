#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pytube  
from pytube import YouTube  
video_url = 'https://www.youtube.com/watch?v=s-O2tOEpO5Q'   
youtube = pytube.YouTube(video_url)  
video = youtube.streams.first()  
video.download('C:/Users/user/Desktop/')  
from pytube import YouTube  
video = YouTube('https://www.youtube.com/watch?v=s-O2tOEpO5Q')  
print(video.title)  
print(video.video_id)  
print(video.description)  
print(video.length)  
print(video.thumbnail_url)  
print(video.views)  
print(video.rating)  
print(video.age_restricted) 
from pytube import YouTube 
video = YouTube('https://www.youtube.com/watch?v=s-O2tOEpO5Q')  
video.streams.all()  
stream = video.streams.all()  
for i in stream:  
    print(i)


# In[ ]:




