import os
import sys

"""
配置相关
"""

proxy_setting = os.getenv("PROXY_SETTING", "False").lower() == "true"

process_dir = os.path.abspath(os.path.dirname(sys.path[0]))
ruleset_dir = os.path.join(process_dir, "List")
out_dir = os.path.join(process_dir, "Public")
out_ruleset_dir = os.path.join(process_dir, "Public", "List")

dnsmasq_china_list = {
    "ChinaDomain": "https://github.com/felixonmars/dnsmasq-china-list/raw/master/accelerated-domains.china.conf",
    "ChinaApple": "https://github.com/felixonmars/dnsmasq-china-list/raw/master/apple.china.conf",
    "ChinaGoogle": "https://github.com/felixonmars/dnsmasq-china-list/raw/master/google.china.conf",
}

misakaio_chnroutes2 = "https://github.com/misakaio/chnroutes2/raw/master/chnroutes.txt"

"""
文件相关
"""

init_dir_name = []
# 临时措施
# init_dir_name = [os.path.join("List", "smartdns")]

copy_dir_name = ["List", "Config", "Mock", "Script", "Module"]

config_file_clear = {
    os.path.join(out_dir, "Config", "clash.yaml"): os.path.join(
        out_dir, "Config", "clash-nocomment.yaml"
    ),
    os.path.join(out_dir, "Config", "surge.conf"): os.path.join(
        out_dir, "Config", "surge-nocomment.conf"
    ),
}

"""
处理相关
"""

if proxy_setting:
    for name, link in dnsmasq_china_list.items():
        dnsmasq_china_list[name] = "https://cors.isteed.cc/" + dnsmasq_china_list[name]
    misakaio_chnroutes2 = "https://cors.isteed.cc/" + misakaio_chnroutes2
