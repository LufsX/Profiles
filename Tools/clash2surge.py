import os, sys

surgeRulesetDir = os.path.join(os.path.abspath(os.path.dirname(sys.path[0])),
                               'List', 'Surge') + '/'
clashRulesetDir = os.path.join(os.path.abspath(os.path.dirname(sys.path[0])),
                               'List', 'Clash') + '/'

for dirpath, dirnames, filenames in os.walk(clashRulesetDir):
    for filename in filenames:
        print(os.path.join(dirpath, filename))
        with open(os.path.join(dirpath, filename), "rt") as content:
            text = content.readlines()
            filePath = surgeRulesetDir + filename.replace("yaml", "conf")
            if os.path.exists(filePath):
                os.remove(filePath)
            f = open(surgeRulesetDir + filename.replace("yaml", "conf"), "a")
            for line in text:
                if line == "payload:":
                    break
                # 处理 Surge 支持而 Clash 不支持的规则
                elif line.startswith("  # - USER-AGENT"):
                    f.writelines(line.replace("  # - ", ""))
                elif line.startswith("  - "):
                    f.writelines(line.replace("  - ", ""))
                elif line.startswith("  #"):
                    f.writelines(line.replace("  #", "#"))
                # 处理空行
                elif line == "\n":
                    f.writelines("\n")
