# Idle curso python dia uno 

```
Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 1
1
>>> 'hola'
'hola'
>>> 2 + 2
4
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> help()

Welcome to Python 3.7's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.7/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> q

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> help (print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>> nombre = 'Guido'
>>> print(nombre)
Guido
>>> a=10
>>> b=a
>>> b=5
>>> print(b)
5
>>> b=7+3
>>> print(b)
10
>>> id(a)
1502569792
>>> id(b)
1502569792
>>> b=5
>>> id(b)
1502569712
>>> b=7+3
>>> id(b)
1502569792
>>> print('Hola' + nombre)
HolaGuido
>>> print('Hola ' + nombre)
Hola Guido
>>> RESET: C:\Users\teres\Desktop\uno.py
SyntaxError: invalid syntax
>>>  RESET: C\Users\teres\Desktop\uno.py
 
SyntaxError: unexpected indent
>>> RESET: C\Users\teres\Desktop\uno.py
SyntaxError: unexpected character after line continuation character
>>> RESTART: C\Users\teres\Desktop\uno.py
SyntaxError: unexpected character after line continuation character
>>> 
=============================== RESTART: Shell ===============================
>>> 
=================== RESTART: C:/Users/teres/Desktop/uno.py ===================
Guido
>>> es valido = True
SyntaxError: invalid syntax
>>> es_valido = True
>>> type(es valido)
SyntaxError: invalid syntax
>>> type(es_valido)
<class 'bool'>
>>> es_valido = 1
>>> type(es_valido)
<class 'int'>
>>> a = 1/3
>>> a
0.3333333333333333
>>> hex(id(a))
'0x2e41e60'
>>> b=10/30
>>> b
0.3333333333333333
>>> hex(id(b))
'0x2d8ef30'
>>> a = 1+j
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    a = 1+j
NameError: name 'j' is not defined
>>> a=1+1j
>>> a
(1+1j)
>>> type(a)
<class 'complex'>
>>> nombre
'Guido'
>>> type(nombre)
<class 'str'>
>>> casa_de_guido = "Guido's house"
>>> dos_lineas = 'primera linea \nsegunda linea'
>>> print(dos_lineas)
primera linea 
segunda linea
>>> literal = '"literal"'
>>> print(literal)
"literal"
>>> dos_lineas= 'lineas \\lineas'
>>> print (dos_lineas)
lineas \lineas
>>> dos_lineas= 'lineas \\nsegunda linea'
>>> print(dos_lineas)
lineas \nsegunda linea
>>> dos_lineas='linea \n\\segunda linea'
>>> print(dos_lineas)
linea 
\segunda linea
>>> nombre[0]
'G'
>>> my_tupa = (2,3,"Hola")
>>> my_tupla[0]
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    my_tupla[0]
NameError: name 'my_tupla' is not defined
>>> my_tupa[0]
2
>>> mi_lista = [2,3,4]
>>> mi_lista[0]
2
>>> mi_lista[0] = 52
>>> mi_lista[0]
52
>>> mi_dict = {"nombre": "Guido", "apellido": "Van Rossum", "popularidad": 8.0}
>>> mi_dict["nombre"]
'Guido'
>>> 
```