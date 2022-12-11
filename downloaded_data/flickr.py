from bs4 import BeautifulSoup
import requests
import json
import sys

def collect(url):
    res = requests.get(url)

    st = BeautifulSoup(res.content.decode('utf-8','ignore'),features='lxml')

    data = {}

    out = st.find("a",{"class":["owner-name","truncate"]})

    data["owner_name"] = out.text
    data["owner_profile_link"] = out["href"]

    out = st.find("meta",{"property":"og:title"})
    data["title"] = out["content"]
    
    out = st.find("meta",{"property":"og:description"})
    data["description"] = out["content"]

    out = st.find("meta",{"property":"og:image"})
    data["image"] = out["content"]

    out = st.find("meta",{"name":"keywords"})
    data["tags"] = [x.strip() for x in out["content"].split(",")]
    
        
    return data
if __name__ == "__main__":
    res = collect(sys.argv[1])
    out = json.dumps(res,indent=4,ensure_ascii=False)
    print(out)
