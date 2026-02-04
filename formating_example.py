import json
def load_todos():try:with open('todos.json','r')as f:return json.load(f)
 except:return[]
def save_todos(todos):with open('todos.json','w')as f:json.dump(todos,f)
def main():todos=load_todos()
 while True:c=input("cmd: ")
  if c=='1':t=input();todos.append({"t":t,"d":False})
  # ...