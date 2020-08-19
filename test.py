from funClass import function
from trainingClass import MyNum
from InsCount import InstanceCounter
from assigments import MaxSizeList

tab1 = [1, 2, 3, 4, 5, 6, 7]
tab2 = [1, 3, 5, 7, 9, 11]
p1 = function(tab1, tab2)
# print("kwadrta output")
# p1.kwadrat()
# print("showme output")
# p1.showme()
# print("random_value that is set in instance not class")
# p1.dothis()
# print (p1.randomVal)
#p1.set_val(10)
#print (p1.increment())

#p2 = MyNum('HI')
#p2.increment()
#p2.increment()
#print (p2.val)

#p31 = InstanceCounter(5)
#p32 = InstanceCounter(13)
#p33 = InstanceCounter(17)

#for obj in (p31, p32, p33):
#    print ("val of obj: %s" % (obj.get_val()))
#    print ("count: %s" % (obj.get_count()))

a = MaxSizeList(3)
b = MaxSizeList(1)

a.push("hey")
a.push("hi")
a.push("let's go")
a.push("go")

b.push("hey")
b.push("hi")
b.push("let's go")
b.push("go")

print (a.get_list())
print (b.get_list())