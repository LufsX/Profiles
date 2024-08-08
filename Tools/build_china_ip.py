import requests, os, datetime, ipaddress
from until import run_in_threads

def download_and_process(link, exclude):
    print(f"[ChinaIP] Downloading and processing {link} ...")
    content = requests.get(link).text
    lines = [
        line
        for line in content.split("\n")
        if line and not line.startswith("#") and line.strip() not in exclude
    ]
    return lines


def build(china_ip_sources, out_dir):
    print("[ChinaIP] Start building from China IP sources…")

    update_info = f'''#####################
# China IP List
# Last Updated: {(datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=8)).strftime("%Y-%m-%dT%H:%M:%S") + "+08:00"}
#
# Build form:
{'\n'.join([f"#  - {link}" for link in china_ip_sources])}
#####################
'''
    exclude = {"223.118.0.0/15", "223.120.0.0/15", ""}

    all_lines = set()

    def download_and_process_wrapper(link, exclude):
        lines = download_and_process(link, exclude)
        all_lines.update(lines)

    download_functions = [
        lambda link=link: download_and_process_wrapper(link, exclude)
        for link in china_ip_sources
    ]

    run_in_threads(download_functions)

    all_networks = set()

    for line in all_lines:
        try:
            network = ipaddress.ip_network(line.strip(), strict=False)
            all_networks.add(network)
        except ValueError:
            print(f"[ChinaIP] Invalid network format: {line}")

    merged_networks = ipaddress.collapse_addresses(all_networks)

    with open(os.path.join(out_dir, "ChinaIP.conf"), "w", newline="\n") as f:
        f.write(update_info)
        for network in merged_networks:
            f.write(f"IP-CIDR,{network}\n")

    print("[ChinaIP] End building from china IP sources")


if __name__ == "__main__":
    import config

    build(config.china_ip_sources, config.out_ruleset_dir)
