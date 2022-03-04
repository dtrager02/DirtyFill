import json
if __name__ == "__main__":
    with open("info.json","r") as f:
        a =  json.load(f)           
        print("".join([f"""
                document.querySelectorAll(\"input[id*={key}]\").forEach((a) => a.value = \"{value}\");
                document.querySelectorAll(\"input[class*={key}]\").forEach((a) => a.value = \"{value}\");
                document.querySelectorAll(\"input[placeholder*={key}]\").forEach((a) => a.value = \"{value}\");
                document.querySelectorAll(\"label[id*={key}] + input\").forEach((a) => a.value = \"{value}\");
                document.querySelectorAll(\"label[id*={key}] + input\").forEach((a) => a.value = \"{value}\");
                document.querySelectorAll(\"label[id*={key}] + input\").forEach((a) => a.value = \"{value}\");
                """ for key,value in zip(a.keys(),a.values())]))