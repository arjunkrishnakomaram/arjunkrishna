l = [1,2,3,4,5]
>>> l.append(6)
>>> l
[1, 2, 3, 4, 5, 6]
>>> t = (1,2,3,4,5)
>>> t.append(6)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    t.append(6)
AttributeError: 'tuple' object has no attribute 'append'
>>> t.count(3)
1
>>> t.index(5)
4
>>> type(t)
<class 'tuple'>
>>> t1 = (1)
>>> t1
1
>>> type(t1)
<class 'int'>
>>> t2 = ('a')
>>> type(t2)
<class 'str'>
>>> t3 = (1,)
>>> type(t3)
<class 'tuple'>
>>> t4 = ('a',)
>>> type(t4)
<class 'tuple'>
>>> 
>>> l1 = [7,8]
>>> l + l1
[1, 2, 3, 4, 5, 6, 7, 8]








s = 'Ramesh is a good boy'
>>> s
'Ramesh is a good boy'
>>> s1 = 'Indian's are good'
SyntaxError: invalid syntax
>>> s1 = 'Indian''s are good'
>>> s1
'Indians are good'
>>> s1 = "Indian's are good"
>>> s1
"Indian's are good"
>>> s2 = 'Indian"s are good'
>>> s2
'Indian"s are good'
>>> s3 = '''Indian"s are good , india population is more tha 130 cr's'''
>>> s3
'Indian"s are good , india population is more tha 130 cr\'s'
>>> s4 = """my country'''Indian"s are good , india population is more tha 130 cr's'''"""
>>> 
>>> s4 = """my country'''Indian"s are good , india population is more tha 130 cr's'''"""
>>> 
>>> a = 'sai'
>>> b = 'kumar'
>>> a + b
'saikumar'
>>> s.capitalize()
'Ramesh is a good boy'
>>> s=  'ramesh'
>>> s.capitalize()
'Ramesh'


s =  'ramesh'
>>> s.casefold()
'ramesh'
>>> s.center(100)
'                                               ramesh                                               '
>>> s.center(50)
'                      ramesh                      '
>>> s1 = "qwertyuiop"
>>> s1.center(20)
'     qwertyuiop     '



s  = 'ramesh is a good boy'
>>> q = 'ramesh'
>>> s.count(q)
1






