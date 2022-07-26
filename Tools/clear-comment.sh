cat ./Config/clash.yaml | sed '/^[ ]*$/d' | sed 's/ *$//' >./Config/clash-nocomment.yaml
cat ./Config/surge.conf | sed '/^[ ]*$/d' | sed 's/ *$//' >./Config/surge-nocomment.conf
