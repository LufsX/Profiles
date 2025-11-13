import config
import datetime
import os
import shutil
import until

start_time = datetime.datetime.now()

out_dir: str = config.out_dir
init_dir_name: tuple = config.init_dir_name
copy_path: tuple = config.copy_path
copy_source_path: dict = config.copy_source_path
process_dir: str = config.process_dir
ruleset_dir: str = config.ruleset_dir
out_ruleset_dir: str = config.out_ruleset_dir
out_source_ruleset_dir: str = config.out_source_ruleset_dir


def init():
    if os.path.exists(out_dir):
        print("[Build] Clear the last generated files…")
        shutil.rmtree(out_dir)
    for dir_name in init_dir_name:
        os.makedirs(os.path.join(out_dir, dir_name))


def copy_files():
    print("[Build] Copy files that do not need to be generated…")
    for path in copy_path:
        src, dest = os.path.join(process_dir, path), os.path.join(out_dir, path)
        (
            shutil.copytree(src, dest, dirs_exist_ok=True)
            if os.path.isdir(src)
            else shutil.copy2(src, dest)
        )

    for src, dest in copy_source_path.items():
        shutil.copytree(
            os.path.join(process_dir, src),
            os.path.join(out_source_ruleset_dir, dest),
            dirs_exist_ok=True,
        )


def clear_config_comment():
    print("[Build] Start clearing config comment…")

    clear_functions = [
        lambda src=src, dest=dest: until.clear_comment(src, dest)
        for src, dest in config.config_file_clear.items()
    ]
    until.run_in_threads(clear_functions)

    print("[Build] End clearing config comment")


def build_form_dnsmasq_china_list():
    import build_form_dnsmasq_china_list

    build_form_dnsmasq_china_list.build(
        config.dnsmasq_china_list, out_source_ruleset_dir
    )


def build_smartdns():
    import build_smartdns

    build_smartdns.build(config.smartdns_file, out_source_ruleset_dir)


def build_china_ip():
    import build_china_ip

    build_china_ip.build(config.china_ip_sources, out_source_ruleset_dir)


def build_china_ipv6():
    import build_china_ipv6

    build_china_ipv6.build(config.china_ipv6_sources, out_source_ruleset_dir)


def build_guard():
    import build_guard

    build_guard.build(config.guard_sources, out_source_ruleset_dir)


def build_singbox():
    import build_singbox

    build_singbox.build(out_source_ruleset_dir, config.out_singbox_ruleset_dir)


def build_surge():
    import build_surge

    build_surge.build(out_source_ruleset_dir, config.out_surge_ruleset_dir)


def build_clash():
    import build_clash

    build_clash.build(out_source_ruleset_dir, config.out_clash_ruleset_dir)


def build_bankhk():
    import build_bankhk

    build_bankhk.build(config.bankhk_sources, ruleset_dir, out_source_ruleset_dir)


def build_web():
    import build_web

    build_web.build_file_list_page(
        config.out_dir,
        os.path.join(config.out_dir, "index.html"),
        github_token=config.github_token,
    )


init()
copy_files()
# clear_config_comment()
# build_form_dnsmasq_china_list()
# build_china_ip()
# build_guard()

until.run_in_threads(
    [
        clear_config_comment,
        build_form_dnsmasq_china_list,
        build_china_ip,
        build_china_ipv6,
        build_guard,
        build_bankhk,
    ]
)

until.run_in_threads(
    [
        build_singbox,
        build_smartdns,
        build_surge,
        build_clash,
    ]
)

build_web()


end_time = datetime.datetime.now()

print(f"Total time: {end_time - start_time}")
