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
                # 处理空行
                if line.strip()=="":
                    f.writelines("")
                # 处理注释
                elif line.startswith('#'):
                    line = '  '+line
                # 处理 Clash 不支持的规则
                elif line.startswith('USER-AGENT'):
                    line = '  # - '+line
                # 处理 Domainset
                elif line.startswith('.'):
                    line = '  - *'+line
                # 处理正常规则
                else:
                    line = '  - '+line
                f.writelines(line)
