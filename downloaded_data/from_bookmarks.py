


for i in open("input.html",encoding="utf-8").readlines():
    if "HREF" in i :
        # print(i)
        if "search" not in i:
            print(i.split("HREF=")[1].split("\"")[1])