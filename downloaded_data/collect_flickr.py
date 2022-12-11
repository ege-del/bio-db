import flickr
import time
import json

data = []
for i in open("target.txt").readlines():
    if "flickr" in i:
        # print(i.strip())
        try:
            result = flickr.collect(i.strip())
            data.append(result)
            print("success on "+i.strip())
        except Exception as e:
            print("error on "+i.strip())
            
        time.sleep(3)
       
 
print(json.dumps(data,indent=4,ensure_ascii=False))
open("out_new.json","w+",encoding="utf-8").write(json.dumps(data,indent=4,ensure_ascii=False))
