### Challenge #2##
### We need to write code that will query the meta data of an instance within AWS and provide a json formatted output.####
### Bonus Points
### The code allows for a particular data key to be retrieved individually
###############################################################################################################################
#!/usr/bin/env python

import requests
import json


# Converts AWS EC2 instance metadata to a dictionary
def load():
    metaUrl = 'http://169.254.169.254/latest'
    #  top subdirectories are not exposed with a final '/'
    metadict = {'dynamic': {},'meta-data': {}}

    for subsect in metadict.keys():
        data('{0}/{1}/'.format(  metaUrl, subsect), metadict[subsect])

    return metadict


def data(url, d):
    r = requests.get(url)
    if r.status_code == 404:
        return

    for l in r.text.split('\n'):
        if not l:
            continue
        newurl = '{0}{1}'.format(url, l)
        # a key is detected with a final '/'
        if l.endswith('/'):
            newkey = l.split('/')[-2]
            d[newkey] = {}
            data(newurl, d[newkey])

        else:
            r = requests.get(newurl)
            if r.status_code != 404:
                try:
                    d[l] = json.loads(r.text)
                except ValueError:
                    d[l] = r.text
            else:
                d[l] = None



def search(object, key):
        if isinstance(object, dict):
                if key in object:
                        yield object[key]
                for j in object.values():
                        for x in search(j, key):
                                yield x
if __name__ == '__main__':
    object = json.dumps(load())
    object = json.loads(object)
    key='meta-data/services/domain'
    k=key.split('/')
    print("value is : {}".format( list(search(object, k[-1]))))
