d = {'name' : 'ramesh','age' : 24,'city' : 'bangalore'}
>>> d1 = {1 : 'ramesh',2 : 24, 3 : 'bangalore'}
d['name']
'ramesh'
d.get('name')
'ramesh'
d.keys()
dict_keys(['name', 'age', 'city'])
d.values()
dict_values(['ramesh', 24, 'bangalore'])
d.pop('city')
'bangalore'
>>> d
{'name': 'ramesh', 'age': 24}


d['company'] = 'hp'
>>> d
{'name': 'ramesh', 'age': 24, 'city': 'bangalore', 'company': 'hp'}


d.popitem()
('company', 'hp')
>>> d
{'name': 'ramesh', 'age': 24, 'city': 'bangalore'}
