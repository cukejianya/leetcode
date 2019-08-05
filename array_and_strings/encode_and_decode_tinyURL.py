import string
import random

class Codec:
    def __init__(self):
        self.url_dict = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        param_array = random.sample(string.ascii_letters + string.digits, 6) 
        tinyURL_param = "".join(param_array)
        self.url_dict[tinyURL_param]  = longUrl
        return 'http://tinyurl.com/' + tinyURL_param

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        tinyURL_param = shortUrl.replace('http://tinyurl.com/', '')
        return self.url_dict[tinyURL_param]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
