import os
import sys

"""
配置相关
"""

proxy_setting = os.getenv("PROXY_SETTING", "False").lower() in ("true", "1")

process_dir = os.path.abspath(os.path.dirname(sys.path[0]))
ruleset_dir = os.path.join(process_dir, "List")
out_dir = os.path.join(process_dir, "Public")
out_ruleset_dir = os.path.join(out_dir, "List")
out_source_ruleset_dir = os.path.join(out_dir, "List", "Source")
out_singbox_ruleset_dir = os.path.join(out_ruleset_dir, "sing-box")
out_clash_ruleset_dir = os.path.join(out_ruleset_dir, "Clash")
out_surge_ruleset_dir = os.path.join(out_ruleset_dir, "Surge")
out_smartdns_ruleset_dir = os.path.join(out_ruleset_dir, "smartdns")

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

china_ipv6_sources = ["https://gaoyifan.github.io/china-operator-ip/china6.txt"]

guard_sources = [
    "https://github.com/SukkaW/Surge/raw/master/Source/domainset/reject.conf",
    "https://github.com/TG-Twilight/AWAvenue-Ads-Rule/raw/main/Filters/AWAvenue-Ads-Rule-Surge.list",
]

bankhk_sources = [
    "BankHK_AirStar.conf",
    "BankHK_AntBank.conf",
    "BankHK_BOCHK.conf",
    "BankHK_CNCBI.conf",
    "BankHK_Fusion.conf",
    "BankHK_HSBCHK.conf",
    "BankHK_ICBCA.conf",
    "BankHK_PAOBank.conf",
    "BankHK_WeLab.conf",
    "BankHK_ZABank.conf",
]

"""
文件相关
"""

init_dir_name = (
    os.path.join("List", "Clash"),
    os.path.join("List", "Source"),
    os.path.join("List", "Surge"),
    os.path.join("List", "smartdns"),
)

copy_path = ("Config", "Mock", "Script", "Module", "vercel.json")
copy_source_path = {ruleset_dir: out_source_ruleset_dir}

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

smartdns_file = {
    os.path.join(out_source_ruleset_dir, "Guard.conf"): os.path.join(
        out_smartdns_ruleset_dir, "Guard.txt"
    ),
    os.path.join(out_source_ruleset_dir, "ChinaApple.conf"): os.path.join(
        out_smartdns_ruleset_dir, "ChinaApple.txt"
    ),
    os.path.join(out_source_ruleset_dir, "ChinaDomain.conf"): os.path.join(
        out_smartdns_ruleset_dir, "ChinaDomain.txt"
    ),
    os.path.join(out_source_ruleset_dir, "ChinaGoogle.conf"): os.path.join(
        out_smartdns_ruleset_dir, "ChinaGoogle.txt"
    ),
}

"""
处理相关
"""

if proxy_setting:
    proxy_prefix = "https://cors.isteed.cc/"

    dnsmasq_china_list = {
        name: proxy_prefix + link for name, link in dnsmasq_china_list.items()
    }
    china_ip_sources = [proxy_prefix + source for source in china_ip_sources]
    china_ipv6_sources = [proxy_prefix + source for source in china_ipv6_sources]
    guard_sources = [proxy_prefix + source for source in guard_sources]
