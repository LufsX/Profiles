# 分流

有这几个地方的文件

- `List/*.conf`
  - 原始规则
- `List/Clash/*.conf`
  - 基于原始规则添加了对 domainset 的 Clash 格式适配
- `List/Surge/*.conf`
  - 直接复制原始规则的
- `List/sing-box/*.json`
  - 基于原始规则制作的对应 sing-box 的规则格式
- `List/smartdns/*.txt`
  - 基于 dnsmasq_china_list 和原始规则中的 Guard.conf 的 smartdns 所用的 domainset 格式

---

目前所有规则均为在以下之列

- DOMAIN-SUFFIX: 11244 (61.13%)
- IP-CIDR: 6547 (35.60%)
- DOMAIN: 460 (2.50%)
- DOMAIN-KEYWORD: 80 (0.43%)
- PROCESS-NAME: 50 (0.27%)
- IP-CIDR6: 12 (0.07%)

---

注意 ⚠️: 已剔除了 YAML 格式的 Clash 规则支持，最后版本可见[该 commit](https://github.com/LufsX/Profiles/tree/4b5a19c07e4de5872db18064c281ee9c34c747cc/List/Clash)

## 默认配置

以下是默认配置中包含的规则集：

<!-- prettier-ignore -->
| 名称 | 用途 |
|:-|:-|
| Apple.conf | Apple 相关内容服务|
| AppleCDN.conf | Apple 相关 CDN |
| ChatAI.conf | 部分 AI 聊天服务 |
| China.conf | 大陆正常访问的服务 |
| ChinaIP.conf | 大陆 IP 集 |
| DirectCustom.conf | 自用直连/补充集 |
| Global.conf | 代理集 |
| Guard.conf | 去广告/隐私保护 |
| OneDrive.conf | OneDrive 可直连集 |
| ProxyCustom.conf | 自用代理/补充集 |
| Streaming.conf | 流媒体服务集 |
| StreamingSE&CDN.conf | 港澳台流媒体服务集（不含 B 站 CDN） |
| Telegram.conf | Telegram 相关 |
| Unbreak.conf | 部分需要不间断连接的域名 |

## 按需配置

以下规则集暂未加入默认配置中，需要的可以自行添加：

<!-- prettier-ignore -->
| 名称 | 用途 |
| :- | :- |
| BOCHK.conf | BOCHK 相关 |
| HSBCHK.conf | HSBC HK 相关 |
| ZABank.conf | ZA Bank 相关 |
| BankHK.conf | BOCHK、HSBC HK、ZA Bank 这三个配置的合集（为啥只有这三个呢？因为我就只有这三家… |
| Gamer.conf | 游戏平台 |
| MyFin.conf | MyFin 相关 |
| N26.conf   | N26 相关   |
| StreamingSE.conf | 流媒体服务集（含 B 站的 CDN） |
| WARP.conf | Cloudflare WARP 相关 |
| Wise.conf  | Wise 相关  |
