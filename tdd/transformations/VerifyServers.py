import urllib2

servers = ['http://localhost:8080']

for server in servers:
    try:
        urllib.urlopen(server)
    except urllib2.HTTPError, e:
        send_mail(e)
    except urllib2.URLError, e:
        send_mail(e)
        
def send_mail(e):
    #send an email to the admin with the details of this exception
    pass