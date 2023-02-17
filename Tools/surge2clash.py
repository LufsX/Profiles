import os, sys

surgeRulesetDir = os.path.join(os.path.abspath(os.path.dirname(sys.path[0])),
                               'List', 'Surge') + '/'
clashRulesetDir = os.path.join(os.path.abspath(os.path.dirname(sys.path[0])),
                               'List', 'Clash') + '/'

for dirpath, dirnames, filenames in os.walk(surgeRulesetDir):
    for filename in filenames:
        print(os.path.join(dirpath, filename))
        with open(os.path.join(dirpath, filename), "rt") as content:
            text = content.readlines()
            filePath = clashRulesetDir + filename.replace("conf", "yaml")
            if os.path.exists(filePath):
                os.remove(filePath)
            f = open(clashRulesetDir + filename.replace("conf", "yaml"), "a")
            f.writelines("payload:\n")
            for line in text:
                # 处理空行
                if line.strip() == "":
                    f.writelines("")
                # 处理注释
                elif line.startswith('#'):
                    line = '  ' + line
                # 处理 Clash 不支持的规则
                elif line.startswith('USER-AGENT'):
                    line = '  # - ' + line
                # # 处理 Domainset
                # elif line.startswith('.'):
                #     line = '  - *'+line
                # 处理正常规则
                else:
                    line = '  - ' + line
                f.writelines(line)
