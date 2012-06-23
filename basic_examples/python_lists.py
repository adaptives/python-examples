#!/usr/bin/python

jvm_langs = ['Java', 'Jython', 'Groovy', 'Scala', 'Jruby']

#How many JVM langs do you know ?
print 'I know of ', jvm_langs.__len__(), 'langs that can run on the JVM'

#It's not a good idea to directly us __xxx__ methods
#A better way is. Remember there is usually a top level function which  
#is the idoimatic way to access the __xxx__method
print 'I know of ', len(jvm_langs), 'langs that can run on the JVM'

print 'Oops I forgot Clojure'
jvm_langs.append('Clojure')

#Let's iterate across the list
for lang in jvm_langs:
  print lang
  
#Can we get the 3rd element of the list ?
print "The 3rd JVM language is ", jvm_langs[2]
print "The first 3 JVM languages are ", jvm_langs[:3]
print "The 2nd to 4th JVM languages are ", jvm_langs[1:4]

print "let's sort these languages"
jvm_langs.sort()
print jvm_langs


