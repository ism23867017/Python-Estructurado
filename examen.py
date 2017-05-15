#coding: -utf8

# Des de 0 fins a 3-1(2)
# coding:utf-8

# Des de 0 fins a 3-1(2)
for cont in range(0, 3):
    print "Volta nº" , cont

print "-------------------------------"

# Des de 0 fins a 3-1(2)
for cont in range(3):
    print "Volta nº" , cont

print "-------------------------------"

# Des de 1 fins a 4-1(3)
for cont in range(1, 4):
    print "Volta nº" , cont

print "-------------------------------"


# Demostració de que xrange genera les llistes
# de manera més eficient
# Millor utilitzar xrange
import time

#use time.time() on Linux

start = time.clock()
for x in range(10000000):
    pass
stop = time.clock()

print "Temps range" , stop - start

start = time.clock()
for x in xrange(10000000):
    pass
stop = time.clock()

print "Temps xrange" ,stop - start

print "-------------------------------"



# Solució per generar les llistes des del
# "nº que vulguis", fins al "nº que vulguis"
# range i xrange ho fan fins el "nº que vulguis-1"
def my_range(inici, fi, increment):
    while inici <= fi:
        #Retorna l'element actual del rang (llista)
        yield inici
        inici = inici + increment

for x in my_range(1, 3, 0.5):
    print x

print "-------------------------------"

for x in my_range(0, 3, 0.5):
    print x
