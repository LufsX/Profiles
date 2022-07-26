import os

for dirpath, dirnames, filenames in os.walk('../List/Clash'):
    for filename in filenames:
        print(os.path.join(dirpath, filename))
        with open(os.path.join(dirpath, filename),"rt") as content:
            text = content.read()
            text = text.replace("payload:\n","").replace("  ","").replace("- ","")
            file = open('../List/Surge/'+filename.replace("yaml","conf"),"w")
            file.write(text)