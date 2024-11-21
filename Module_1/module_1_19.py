#Словари
my_dict = {'Ann': 1989, 'Boris': 1984, 'Julia': 1996, 'Pavel': 1987}
print('Dict:',my_dict)
print('Existing value:', my_dict['Ann'])
print('Not existing value:', my_dict.get('Kate'))
my_dict['Vikki'] = 2011
my_dict['Lin'] = 2017
a = my_dict.pop('Julia')
print('Deleted value:',a)
print('Modified dictionary:',my_dict)

#Множества
my_set = {11, 22, 33, 44, 44, 33, 22, 'Text', (99, 88, 77), 'Text'}
print('Set:',my_set)
my_set.add('New_Text')
my_set.add(1911.2014)
my_set.discard('Text')
print('Modified set:',my_set)