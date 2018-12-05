##Activities 4, Alif Fauzia Rama Wahyu K
import shelve

data = shelve.open("Alif")
print(data["newdata"][0])
print(data["newdata"][1])
print(data["newdata"][2])
print(data["newdata"][3])
