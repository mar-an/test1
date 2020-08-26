
import yaml

mydict = {'a':1, 'b': 2, 'c': 3}
mylist = [1, 2, 3, 4, 5]
mytuple = ('x', 'y', 'z')

loaded_yaml = yaml.dump(mydict, default_flow_style=False)
print (loaded_yaml)

print (yaml.dump(mylist, default_flow_style=False))
print (yaml.dump(mytuple, default_flow_style=False))



myobj = (
        [1, 2, 3, 4, 5],
        {'a': 1, 'b': 2, 'c': 3 },
        [
                {'x': 98, 'y': 99, 'z': 100},
                3,
                4
                ],
        {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
        )
print ("\n######  complex YAML ######\n")
print(yaml.dump(myobj, default_flow_style = False))