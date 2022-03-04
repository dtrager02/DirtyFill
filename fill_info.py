import json
from json.tool import main
def load():
    with open("info.json","r") as f:
        return json.load(f)
    
def commit(info):
    with open("info.json","w+") as f:
        return json.dump(info,f)
 
def main_loop():
    print("Input a common Resume input field and your value in the form 'field:value'. Common fields include 'First' (implying first name attributes),'Country','School'")
    t = ""
    while not t == "exit":
        try: 
            t = input(">")
            if(t == "view"):
                print(current)
            elif(t == "undo"):
                current.pop(last)
            elif(t == "exit"):
                continue
            s = t.split(":")
            current[s[0]] = s[1]
            last = s[0]
        except:
            print("Invalid input")
            continue
        print("Added! \n Submit 'exit' to stop.\n Submit 'undo' if you messed up the previous. \n Submit 'view' to see your current field:value pairs.")   
if __name__ == "__main__":
    current = dict()
    try:
        current =  load()
        print("Continuing where you left off")
        main_loop()
        commit(current)
        
    except FileNotFoundError:
        print("Existing data not found. Starting new file")
        print("Input a common Resume input field and your value in the form 'field:value'. Common fields include 'First' (implying first name attributes),'Country','School'")
        main_loop()
        commit(current)
            
            
            
            
        