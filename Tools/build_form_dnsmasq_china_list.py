import requests, re, os


def build(dnsmasq_china_list, out_dir):
    # 临时措施
    os.makedirs(os.path.join(out_dir, "smartdns"))
    for name, link in dnsmasq_china_list.items():
        content = requests.get(link).text

        pattern = r"^server=/(.*)/114\.114\.114\.114$$"
        matches = re.findall(pattern, content, re.MULTILINE)

        filtered_matches = [match for match in matches if not match.startswith("#")]

        with open(
            os.path.join(out_dir, "smartdns", name + ".txt"), "w"
        ) as outfile:
            outfile.write("\n".join(filtered_matches))
        if name != "ChinaDomain":
            with open(os.path.join(out_dir, name + ".conf"), "w") as outfile:
                outfile.write("." + "\n.".join(filtered_matches))
