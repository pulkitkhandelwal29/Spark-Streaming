#!/usr/bin/env python
# coding: utf-8

# In[3]:


import tweepy
from tweepy import OAuthHandler,Stream


# In[1]:


from tweepy.streaming import StreamListener


# In[2]:


import socket
import json


# In[3]:


consumer_key = 'tAkMNMoZ6xpvjGF2oNitG9c25'
consumer_secret = '2fa80tTbvdvbiTnvmQmdXfkRfiNj761Hczvje4OLbKf6uVk00v'
access_token = '1378067595719368706-lwM3rDXj2EmR7hXFqEm985TAxvavyi'
access_secret = 'jg2P9KzoU2dWQNmqf7L5ra8jIKqJ3B38HeX9izQXYjdeK'


# In[4]:


class TweetsListener(StreamListener):

  def __init__(self, csocket):
      self.client_socket = csocket

  def on_data(self, data):
      try:
          msg = json.loads( data )
          print( msg['text'].encode('utf-8') )
          self.client_socket.send((str(msg['text']) + "\n").encode('utf-8'))
          return True
      except BaseException as e:
          print("Error on_data: %s" % str(e))
      return True

  def on_error(self, status):
      print(status)
      return True


# In[6]:


def sendData(c_socket):
  auth = OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_secret)

  twitter_stream = Stream(auth, TweetsListener(c_socket))
  twitter_stream.filter(track=['cricket']) #searching for term on twitter


# In[ ]:


if __name__ == "__main__":
  s = socket.socket()         # Create a socket object
  host = "127.0.0.1"          # Get local machine name
  port = 9994                 # Reserve a port for your service.
  s.bind((host, port))        # Bind to the port

  print("Listening on port: %s" % str(port))

  s.listen(5)                 # Now wait for client connection.
  c, addr = s.accept()        # Establish connection with client.

  print( "Received request from: " + str( addr ) )

  sendData( c )


# In[ ]:




