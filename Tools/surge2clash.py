import os

for dirpath, dirnames, filenames in os.walk('../List/Surge'):
    for filename in filenames:
        print(os.path.join(dirpath, filename))
        with open(os.path.join(dirpath, filename),"rt") as content:
            text = content.readlines()
            filePath = '../List/Clash/'+filename.replace("conf","yaml")
            if os.path.exists(filePath):
                os.remove(filePath)
            f = open('../List/Clash/'+filename.replace("conf","yaml"),"a")
            f.writelines("payload:\n")
            for line in text:
                if line.strip()=="":
                    f.writelines("")
                elif line.startswith('#'):
                    line = '  '+line
                elif line.startswith('USER-AGENT'):
                    line = '  # - '+line
                else:
                    line = '  - '+line
                f.writelines(line)
