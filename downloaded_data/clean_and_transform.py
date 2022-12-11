import json
import urllib.parse


ed = open("okok.json","r",encoding="utf-8").read()

jjj = json.loads(ed)

links = []
new = []
for i in jjj:
    if i["image"] not in links:
        links.append(i["image"])
        new.append(i)

new_new = []
rejected = []
for i in new:
    
    new_url = urllib.parse.urljoin("https://www.flickr.com/",i["owner_profile_link"])
    formated = {
        "title": i["title"],
        "description": i["description"],
        "copyright_link": new_url,
        "copyright_name": i["owner_name"],
        "media_type": "image",
        "media_link": i["image"],
    }
    if "mitosis" in i["description"].lower() or "mitosis" in i["title"].lower() or "mitosis" in [x.lower() for x in i["tags"]]:
        new_new.append(formated)    
    else:
        rejected.append(formated)

open("new.json","w+",encoding="utf-8").write(json.dumps(new_new,indent=4,ensure_ascii=False))
open("rejected.json","w+",encoding="utf-8").write(json.dumps(rejected,indent=4,ensure_ascii=False))
