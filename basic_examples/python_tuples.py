#!/usr/bin/python

#Note: Python tuples are immutable just like strings

jvm_langs = ('Java', 'Jython', 'JRuby')
print jvm_langs

print 'Oops I forgot Scala and Groovy but I cannot add to an existing tuple'

jvm_langs_revised = ('Scala', 'Groovy', 'Clojure', jvm_langs)
#Notice that the earlier sequence is retained and not flattened
print jvm_langs_revised

