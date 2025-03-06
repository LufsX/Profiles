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
out_singbox_ruleset_dir = os.path.join(out_ruleset_dir, "singbox")

dnsmasq_china_list = {
    "ChinaDomain": "https://github.com/felixonmars/dnsmasq-china-list/raw/master/accelerated-domains.china.conf",
    "ChinaApple": "https://github.com/felixonmars/dnsmasq-china-list/raw/master/apple.china.conf",
    "ChinaGoogle": "https://github.com/felixonmars/dnsmasq-china-list/raw/master/google.china.conf",
}

china_ip_sources = [
    "https://github.com/misakaio/chnroutes2/raw/master/chnroutes.txt",
    "https://github.com/17mon/china_ip_list/raw/master/china_ip_list.txt",
    "https://ispip.clang.cn/all_cn_cidr.txt",
]

guard_sources = [
    "https://github.com/SukkaW/Surge/raw/master/Source/domainset/reject_sukka.conf",
    "https://github.com/TG-Twilight/AWAvenue-Ads-Rule/raw/main/Filters/AWAvenue-Ads-Rule-Surge.list",
]

"""
文件相关
"""

init_dir_name = (os.path.join("List", "smartdns"),)

copy_path = ("List", "Config", "Mock", "Script", "Module", "vercel.json")

config_file_clear = {
    os.path.join(out_dir, "Config", "clash.yaml"): os.path.join(
        out_dir, "Config", "clash-nocomment.yaml"
    ),
    os.path.join(out_dir, "Config", "surge.conf"): os.path.join(
        out_dir, "Config", "surge-nocomment.conf"
    ),
    os.path.join(out_dir, "Config", "surge-autotest.conf"): os.path.join(
        out_dir, "Config", "surge-autotest-nocomment.conf"
    ),
    os.path.join(out_dir, "Config", "mihomo.yaml"): os.path.join(
        out_dir, "Config", "mihomo-nocomment.yaml"
    ),
}

"""
处理相关
"""

if proxy_setting:
    for name, link in dnsmasq_china_list.items():
        dnsmasq_china_list[name] = "https://cors.isteed.cc/" + dnsmasq_china_list[name]
    for i in range(len(china_ip_sources)):
        china_ip_sources[i] = "https://cors.isteed.cc/" + china_ip_sources[i]
