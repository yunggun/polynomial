#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "liam"
__date__ = "$Jun 3, 2015 11:20:42 AM$"

from polynom import *

x= Polynomial(2, [0, 0, 1, 0, 0, 0, 10])

print str(x)+ " in its orig state has deg "+ str(x.deg())

x.reduce()

print str(x)+ " been reduced has deg "+ str(x.deg())

x.trim()

print str(x) +" been trimmmed has deg "+ str(x.deg())




if __name__ == "__main__":
    print "Hello World";
