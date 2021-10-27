#dictionary= a changeable, unordered collection of unique key: value pairs

capitals ={'USA':'Washington DC',
           'India':'New Dehli',
           'Viet Nam':'Ha Noi',
           'Russia':'Moscow'}
capitals.update({'Germany':
                'Berlin'})
#capitals.update({'USA':'LA'})
#print(capitals['USA'])
#print(capitals.get('Germany'))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())
#capitals.pop('Viet Nam')
#capitals.clear()

for key,value in capitals.items() :
    print(key,value)