#     Copyright 2012, Kay Hayen, mailto:kayhayen@gmx.de
#
#     Python tests originally created or extracted from other peoples work. The
#     parts were too small to be protected.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
#
def dictOrderCheck():
    def key1():
        print "key1 called"

        return 1
    def key2():
        print "key2 called"

        return 2
    def value1():
        print "value1 called"

        return 11
    def value2():
        print "value2 called"

        return 22

    print "Checking order of calls in dictionary creation from callables:"

    print { key1() : value1(), key2() : value2() }

def listOrderCheck():
    def value1():
        print "value1 called"

        return 11
    def value2():
        print "value2 called"

        return 22

    print [ value1(), value2() ]

def sliceOrderCheck():
    d = range(10)

    def lvalue():
        print "lvalue",

        return d

    def rvalue():
        print "rvalue",

        return range(2)

    def rvalue4():
        print "rvalue",

        return range(4)

    def low():
        print "low",

        return 0

    def high():
        print "high",

        return 4

    def step():
        print "step",

        return 2

    print "Complex slice lookup", lvalue()[ low() : high() : step() ]

    print "Complex slice assignment",
    lvalue()[ low() : high() : step() ] = rvalue()
    print d

    print "Complex slice del",
    del lvalue()[ low() : high() : step() ]
    print d

    print "Complex inplace slice operation",
    # TODO: This gives an error in CPython, but not in Nuitka.
    # lvalue()[ low() : high() : step() ] += rvalue()
    print d

    d = range(10)

    print "Simple slice lookup", lvalue()[ low() : high() ]

    print "Simple slice assignment",
    lvalue()[ 3 + low() : 3 + high() ] = rvalue()
    print d

    print "Simple slice del",
    del lvalue()[ 3 + low() : 3 + high() ]
    print d

    print "Simple inplace slice operation",
    lvalue()[ low() : high() ] += rvalue4()
    print d


def subscriptOrderCheck():
    d={}

    def lvalue():
        print "lvalue",

        return d

    def rvalue():
        print "rvalue",

        return 2

    def subscript():
        print "subscript",

        return 1

    lvalue()[ subscript() ] = rvalue()
    print d

    print lvalue()[ subscript() ]

    del lvalue()[ subscript() ]
    print d

def attributeOrderCheck():
    try:
        zzz.xxx = yyy
    except Exception as e:
        print "Caught", repr(e)

def compareOrderCheck():
    def lvalue():
        print "lvalue",

        return 1

    def rvalue():
        print "rvalue",

        return 2

    print "==", lvalue() == rvalue()
    print "<=", lvalue() <= rvalue()
    print ">=", lvalue() >= rvalue()
    print "!=", lvalue() != rvalue()
    print ">", lvalue() > rvalue()
    print "<", lvalue() < rvalue()

def generatorOrderCheck():
    def default1():
        print "default1",

        return 1

    def default2():
        print "default2",

        return 2

    def default3():
        print "default3",

        return 3

    def generator( a = default1(), b = default2(), c = default3() ):
        yield a
        yield b
        yield c

    print list( generator() )

def classOrderCheck():
    print "Checking order of class constructions:"

    class B1:
        pass

    class B2:
        pass

    def base1():
        print "base1",

        return B1

    def base2():
        print "base2",

        return B2

    def deco1( cls ):
        print "deco1",

        return cls

    def deco2( cls ):
        print "deco2",

        return B2


    @deco2
    @deco1
    class X( base1(), base2() ):
        print "class body",

    print

def inOrderCheck():
    print "Checking order of in operator:"

    def container():
        print "container",

        return [ 3 ]

    def searched():
        print "searched",

        return 3

    print searched() in container()

def unpackOrderCheck():
    class Iterable:
        def __init__( self ):
            self.consumed = 2

        def __iter__( self ):
            return Iterable()

        def next( self ):
            print "Next with", self.consumed

            if self.consumed:
                self.consumed -=1
            else:
                raise StopIteration

            return self.consumed

    iterable = Iterable()

    try:
        x, y = a, b = Iterable()
    except Exception as e:
        print "Caught", repr(e)


def superOrderCheck():
    try:
        super( zzz, xxx )
    except Exception as e:
        print "Caught", repr(e)

def rangeOrderCheck():
    try:
        range( zzz, yyy, xxx )
    except Exception as e:
        print "Caught", repr(e)

    try:
        range( zzz, xxx )
    except Exception as e:
        print "Caught", repr(e)

def typeOrderCheck():
    try:
        type( zzz, yyy, xxx )
    except Exception as e:
        print "Caught", repr(e)

def iterOrderCheck():
    try:
        iter( zzz, xxx )
    except Exception as e:
        print "Caught", repr(e)

def openOrderCheck():
    try:
        open( zzz, yyy, xxx )
    except Exception as e:
        print "Caught", repr(e)

def longOrderCheck():
    try:
        long( zzz, xxx )
    except Exception as e:
        print "Caught", repr(e)

def intOrderCheck():
    try:
        int( zzz, xxx )
    except Exception as e:
        print "Caught", repr(e)

def nextOrderCheck():
    try:
        next( zzz, xxx )
    except Exception as e:
        print "Caught", repr(e)

dictOrderCheck()
listOrderCheck()
subscriptOrderCheck()
attributeOrderCheck()
compareOrderCheck()
sliceOrderCheck()
generatorOrderCheck()
classOrderCheck()
inOrderCheck()
unpackOrderCheck()
superOrderCheck()
rangeOrderCheck()
typeOrderCheck()
iterOrderCheck()
openOrderCheck()
nextOrderCheck()
longOrderCheck()
intOrderCheck()
