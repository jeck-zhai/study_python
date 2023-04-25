# dict
import os
cwd = os.getcwd()

path = r"E:\pythonProject1"
os.listdir(path)

textdict = [
    {
    "name": "张山",
    "age": "18",
},
    {
    "name": "李四",
    "age": "19",
}
]
obj = {}
for item in textdict:
    obj[item["name"]] = str(item['age']) #输出{“张山”：“18”，“李四”：“19”}



