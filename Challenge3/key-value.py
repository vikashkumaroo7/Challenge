### Challenge #3##
### We have a nested object, we would like a function that you pass in the object and a key and get back the value.####
###############################################################################################################################
#!/usr/bin/env python

def search(object, key):
        if isinstance(object, dict):
                if key in object:
                        yield object[key]
                for j in object.values():
                        for x in search(j, key):
                                yield x

object = {'a':{
                'b':{
                      'c':'d'
                    }
               }
         }
key='a/b/c'
k=key.split('/')
print("value is : {}".format( list(search(object, k[-1]))[-1]))
