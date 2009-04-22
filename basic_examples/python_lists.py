#!/usr/bin/python
# Filename : python_collections.py

jvm_langs = ['Java', 'Jython', 'Groovy', 'Scala', 'Jruby']
print 'I know of ', jvm_langs.__len__, 'langs that can run on the JVM'

print 'Oops I forgot Clojure'
jvm_langs.append('Clojure')
for lang in jvm_langs:
  print lang

print "let's sort these languages"
jvm_langs.sort()
print jvm_langs


