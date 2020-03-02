from tweepy import Stream
from tweepy.streaming import StreamListener

class MyListener(self, data):
  def on_data(self, data):
    try:
      with open('python.json', 'a') as f:
        f.write(data)
        return True
    except BaseException as e:
      print('Error on_data: %s' % str(e))
    return True

  def on_error(self, status):
    print(status)
    return True

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#python'])