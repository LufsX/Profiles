import os

dict = {
"../Config/clash.yaml":"../Config/clash-nocomment.yaml",
"../Config/surge.conf":"../Config/surge-nocomment.conf"
}

for a,b in dict.items():
    text = os.popen("cat {} | grep -o '^[^#]*' | sed '/^[ ]*$/d' | sed 's/ *$//'".format(a),"r")
    open(b,"w").write(text.read())