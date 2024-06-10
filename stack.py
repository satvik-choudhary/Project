#there are 5 plates in weeding and named them 1 2 3 4 5 respectively 
#a person come and taked a plate on top named 5 which is at last
#this happen 2 more times means plate number 4 and plate and 3 are also taken away
#this works on principle of last in first out(lifo)
print("there are plate with number 1 2 3 4 5") 
plate=[1,2,3,4,5]
print("plate remove from stack of plate number is")
print(plate.pop())
print(plate.pop())
print(plate.pop())
print("plate remain",plate)