import os
import sys

proxy_setting = True

process_dir = os.path.abspath(os.path.dirname(sys.path[0]))
ruleset_dir = os.path.join(os.path.abspath(os.path.dirname(sys.path[0])), "List")
out_dir = os.path.join(os.path.abspath(os.path.dirname(sys.path[0])), "Public")

dnsmasq_china_list = {
    "ChinaDomain": "https://github.com/felixonmars/dnsmasq-china-list/raw/master/accelerated-domains.china.conf",
    "ChinaApple": "https://github.com/felixonmars/dnsmasq-china-list/raw/master/apple.china.conf",
    "ChinaGoogle": "https://github.com/felixonmars/dnsmasq-china-list/raw/master/google.china.conf",
}

init_dir_name = []
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
