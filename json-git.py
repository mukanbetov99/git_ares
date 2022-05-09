"""
import json 
JSON - javascript object notation 

dump | dumps 

load | loads

Python  JSON 
dict     object 
list,tuple   array 
srt       string
int     integer
float    float 
bool      bool

"""


# with open("obj_info.json", mode="w") as file:
#     json.dump(obj, file, indent=4)
# json_object = json.dumps(obj)
# # print(json_object)
# # print(type(json_object))
# python_object = json.loads(json_object)
# print(python_object)
# print(type(python_object))

# with open("obj_info.json", "r") as file:
#     print(json.load(file)["gender"]import ]]]

import requests
import json


URL = "https://jsonplaceholder.typicode.com/posts"
def get_response(url: str):
    response = requests.get(url)
    return response.text # response.json()

def load_python_obj(response: str):
    return json.loads(response)

response = get_response(URL)
python_obj = load_python_obj(response)
# print(python_obj)
# print(python_obj[1]["body"])

# for obj in python_obj:
#     print(obj["title"])

class Post:


    def __init__(self, *args, **kwargs):
        self.__dict__.update(*args,**kwargs)

    def get_info(self):
        return f"{self.title} {self,body}"


obj1 = python_obj[0]
post = Post(obj1)
# print(post.__dict__)
print(post.get_info())







