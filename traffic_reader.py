# quick snippet to read live reddit traffic stats
# author: m1kael

import urllib2
import json
import numpy as np
import datetime
import matplotlib.pyplot as plt


url = 'http://www.reddit.com/r/soccer/about/traffic/.json'
#url = 'http://www.reddit.com/r/discgolf/about/traffic/.json'


response = urllib2.urlopen(url)
data = json.load(response)   
print data



print 'day = ', data['day']

data = np.array(data['day'])

print data[0,:]
print data[:,0]


ts = data[0,0]
date = datetime.datetime.fromtimestamp(ts)
print date

'''
print data[:,0]
print data[:,1]
print data[:,2]
print data[:,3]
exit()
'''

plt.figure()
plt.plot(data[:,0], data[:,1], 'r-')
plt.title('uniques per day')
plt.show()

plt.plot(data[:,0], data[:,2], 'b-')
plt.title('pageviews per day')
plt.show()

plt.plot(data[:,0], data[:,3], 'g-')
plt.title('subscriptions per day')
plt.show()


