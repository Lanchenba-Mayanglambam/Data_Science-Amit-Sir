with open("lect-3/myfile.txt","w") as file:
    file.write("this is line 1")
    file.writelines(["\nthis is line 1","\nthis is line 2","\nthis is line 3"])



# "x" works as if the file is already present then it dosnot create a new one if not then it will
try:
 with open("lect-3/myfile.txt","x") as file:
    file.write("this is line 1")
except FileExistsError:
   print("file is already exist")


# "r" is used to read
with open("lect-3/myfile.txt","r") as file:
   data = file.readlines()
   print(data)


# "a" used to append 
with open("lect-3/myfile.txt","a") as file: 
   file.write("\nthis is line 4")  



# to delete a file
import os
filepath = "lect-3/myfile.txt"   
if(os.path.exists(filepath)):
   os.remove(filepath)
else:
   print("file not exists")

# to delete folder using rm directory
folderpath = "lect-3/dummy"
if(os.path.exists(folderpath)):
   os.rmdir(folderpath)
else:
   print("folder not exists")



# json data
import json
with open("lect-3/js/data.json","w") as file:
   student = [{
      'name':"LB",
      'roll no':2345,
      "class":"section alpha",
      "batch":"CS",
      "year":1
   }]   
   json.dump(student,file)
   print("json data inserted")  




with open("lect-3/js/data.json","r") as file:
   data = json.load(file)
   print(type(data))
#    print(data["name"])
   print(data)
   print(data[0])
   data.append({
      'name':"LB",
      'roll no':2345,
      "class":"section alpha",
      "batch":"CS",
      "year":1
   })
   with open("lect-3/js/data.json","w") as file:
    json.dump(student,file,indent=2)