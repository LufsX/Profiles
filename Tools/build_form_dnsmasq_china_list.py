import requests, re, os, datetime
from until import run_in_threads


def download_and_process(name, link, out_dir, update_info):
    content = requests.get(link).text

    pattern = r"^server=/(.*)/114\.114\.114\.114$$"
    matches = [
        match
        for match in re.findall(pattern, content, re.MULTILINE)
        if not match.startswith("#")
    ]

    with open(os.path.join(out_dir, "smartdns", f"{name}.txt"), "w") as outfile:
        outfile.write(update_info)
        outfile.write("\n".join(matches))

    if name != "ChinaDomain":
        with open(os.path.join(out_dir, f"{name}.conf"), "w") as outfile:
            outfile.write(update_info)
            outfile.write("\n".join(matches))


def build(dnsmasq_china_list, out_dir):
    print("Start building from dnsmasq china list…")

    update_info = f'# Updated: {datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"}\n'

    download_functions = [
        lambda: download_and_process(name, link, out_dir, update_info)
        for name, link in dnsmasq_china_list.items()
    ]

    run_in_threads(download_functions)

    print("End building from dnsmasq china list")
