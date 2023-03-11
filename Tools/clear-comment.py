import os, sys

processDir = os.path.join(os.path.abspath(os.path.dirname(sys.path[0])), 'Config') + '/'

dict = {
    "clash.yaml": "clash-nocomment.yaml",
    "surge.conf": "surge-nocomment.conf",
}

for a, b in dict.items():
    text = os.popen(
        "cat {} | grep -o '^[^#]*' | sed '/^[ ]*$/d' | sed 's/ *$//'".format(
            processDir + a
        ),
        "r",
    )
    open(processDir + b, "w").write(text.read())
