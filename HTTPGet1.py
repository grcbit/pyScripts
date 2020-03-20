#/usr/bin/python

#rodolfo.lopez@grcbit.com
#Simple script to request HTTP GET resources, in order to identify public or unprotected data

from urllib import quote
import urllib2

url = "http://www.ejemplo.com/{}"

for i in range(1,1000):
    print('\n')
    u = url.format(quote(str(i)))
    print u
    q = urllib2.Request(u)
    r = urllib2.urlopen(q)
    print r.read()
