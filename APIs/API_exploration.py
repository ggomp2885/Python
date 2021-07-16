### The most useful libraries/functions for API calls in Python ###
    # Any URL can be used in a request function, does not have to be a designated "API" link
    # Almost all APIs setup their responses in a JSON format (python dictionary)
    # "URL Parameters" are additions to the URL, such as httpbin.org/get?page=2&count=25
        # These can be added to the "get" method, in the form of a variable which contains this info in the format specific to the site.

                            # Imports
import requests

                            # Placeholder objects
# r = requests.            #saves the returned values into a variable

                            # Python Functions
# dir(r)              # shows an objects attributes and methods
# help(r)             # more detailed view of objs attributes and methods

                            # Functions
# requests.get('URL')      #This "gets" everything available from the URL
# requests.post('URL', params= , data= , headers= , json= ,)     # This "posts" the data to the URL, included in variables after the URL

                            # Methods

#r.status_code

                            # Http Response Codes
# 200s     #successful
# 300s     #redirects
# 400s     #client side failures
# 500s     #server side failures


                            # Working Example
# import requests
#
# r = requests.get('https://randomfox.ca/floof')
# fox_dict = r.json()
# print(r.status_code)
# print(fox_dict['image'])

#dict to df

                        # Working Example - Youtube Data API
                            # looks like they may already have most of the python code in their GH.
#import requests

# api_key = ''

                        # Working Example - Httpbin.org
import requests
r = requests.post('https://httpbin.org/post', json={'apiKey':'[aZmGv1wN41HLEE0RpPIDRZ0hAt7GUPmyjZXIgBg9]'})
print(r.text)
