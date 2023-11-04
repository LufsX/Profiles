import requests, re, os, datetime


def build(dnsmasq_china_list, out_dir):
    update_info = (
        f'# Updated: {datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"}\n'
    )
    for name, link in dnsmasq_china_list.items():
        content = requests.get(link).text

        pattern = r"^server=/(.*)/114\.114\.114\.114$$"
        matches = re.findall(pattern, content, re.MULTILINE)

        filtered_matches = [match for match in matches if not match.startswith("#")]

        with open(os.path.join(out_dir, "smartdns", name + ".txt"), "w") as outfile:
            outfile.write(update_info)
            outfile.write("\n".join(filtered_matches))
        if name != "ChinaDomain":
            with open(os.path.join(out_dir, name + ".conf"), "w") as outfile:
                outfile.write(update_info)
                outfile.write("." + "\n.".join(filtered_matches))
