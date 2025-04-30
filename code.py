import pandas as pd



hot = pd.Series([72.0 , 41.0 , 70.0 , 38.0 , 62.0 , 38.0 , 61.0 , 34.0 , 68.0 , 36.8] ,
index = ["Joey Chestnut" , "Miki Sudo" , "Joey Chestnut" , "Miki Sudo" , "Matthew Stonie" , "Miki Sudo" , "Joey Chestnut" , "Miki Sudo" ,"Joey Chestnut" , "Sonya Thomas" ] )




print("Name              Hot Dogs")
print(hot)



print()

print("Mean")
print(hot.mean())

print()
print("medium")
print(hot.median())

print()
print("mode")
print(hot.mode())

print()


print("Summery")
print(str(hot.describe()))

print()

print("Joey Chestnut" in hot)
print("Miki Sudo" in hot)

print()
print("varience")
print(hot.var())
print()

print("standerd deviation of hot dogs eaten")
print(hot.std())
print()

print("range")
max = hot.max()
min = hot.min()
range = max - min
print(range)


print()
print("interquaetile")
q1 = hot.quantile(0.25)
q3 = hot.quantile(0.75)
IQR = q3 - q1
print(IQR)
