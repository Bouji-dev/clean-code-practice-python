import json

def main():
    try:
        with open('todos.json', 'r') as f:
            d = json.load(f)
    except:
        d = []
    while True:
        c = input("1:add,2:show,3:del,4:done,5:exit ")
        if c == '1':
            t = input("task: ")
            d.append({"task":t,"done":False})
        elif c == '2':
            for i, item in enumerate(d):
                print(i, item['task'], 'done' if item['done'] else '')
        elif c == '3':
            i = int(input("index: "))
            del d[i]
        elif c == '4':
            i = int(input("index: "))
            d[i]['done'] = True
        elif c == '5':
            with open('todos.json', 'w') as f:
                json.dump(d, f)
            break

main()