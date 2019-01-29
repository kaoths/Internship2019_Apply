import xmltodict
import json
import time

while True:
    print("Enter file name: ",end='')
    fname = input().strip()
    if fname.lower() == 'exit': break
    try:
        with open(fname,"r") as fd:
            xml_dict = xmltodict.parse(fd.read(),attr_prefix = '')
        with open("weather.json","w") as tg:
            tg.write(json.dumps(xml_dict,indent = 2))
        print("Your file is successfully converted")
        time.sleep(2)
        break
    except (OSError, IOError):
        print("File cannot be found. Please try again")
        print("Or type \"exit\" to close program")
        
