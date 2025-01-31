# 懒人版食用说明

## Surge

1. 订阅远程代理：`https://api.isteed.cc/sub?target=surge&url=` + `你的 Surge 订阅地址`
2. 打开 `首页` - `修改` 中的 `MitM`、`Rewrite` 和 `脚本`
3. 在 `MitM` 中生成并安装证书
4. Enjoy ～

## Clash

1. 订阅远程代理：`https://api.isteed.cc/sub?target=clash&url=` + `你的 Clash 订阅地址`
2. Enjoy ～

# 手动版食用说明

## Surge

Surge 于 2024-04-03 的 5.21.0 (**3088**) 新增了智能策略组，若 Surge 低于此版本，请使用 [Autotest 兼容配置](https://ruleset.isteed.cc/Config/surge-autotest.conf)

---

[Surge 配置](https://ruleset.isteed.cc/Config/surge.conf)要求较新版本的 Surge（iOS **4.13.0** 或 Mac **4.5.2** 以上）

这个版本更新了以下功能，本配置中用于处理订阅链接

- `You can now use a full profile as the external policy group (policy-path). All proxies in the [Proxy] section will be used.`

配置使用方法：将 [Proxy Group] 中的 `https://example.com/sub` 替换为你的订阅地址

## Clash

Clash 仅兼容 **Premium 内核**

仅 Premium 内核才可使用 `proxy-providers` 与 `rule-providers`，本配置可搭配个人自建 API 来提取订阅中的 NodeList

配置使用方法：将 `proxy-providers` 下的 `ProxyList` 中的 `https://example.com/nodelist` 替换为 `https://api.isteed.cc/sub?url=` + 你的订阅地址

例如你的订阅地址为 `https://example.com/api/v1/client/subscribe?token=1145141919810`

那就将配置文件中的 `https://example.com/nodelist` 替换为 `https://api.isteed.cc/sub?url=https://example.com/api/v1/client/subscribe?token=1145141919810` 即可

<!-- prettier-ignore -->
| 软件 | 内核 |
| :- | :- |
| Clash For Windows | Premium 内核 |
| ClashX | 普通内核 |
| ClashX Pro | Premium 内核 |
| ClashForAndroid 的 foss | 普通内核 |
| ClashForAndroid 的 premium | Premium 内核 |

# 策略组说明

策略组是可以嵌套选择的，比如现在有个 `PROXY` 策略组，这个策略组选择了 `EXAMPLE` 策略组，而 `EXAMPLE` 策略组选择了 `TEST` 策略组，`TEST` 策略组选择了 `HK1`

则整个链路为 `PROXY` -> `EXAMPLE` -> `TEST` -> `HK1`，既最后为 `HK1` 在起作用

<!-- prettier-ignore -->
| 策略组 | 默认值 | 说明 |
|:-|:-|:-|
| 代理 | 自动测试 | 选择你需要的代理，默认自动测试，可以手动选择你需要的 |
| 直连 | - | 常用与国内网站，不需要走代理的东西 |
| 匹配 | 代理 | 黑白名单制，选择的即为没有规则匹配到时走的 |
| 广告拦截 | 拒绝 | 拒绝连接，常用于广告拦截 |
| 自动测试 | - | 自动测试延迟最低的节点并使用 |
| 自动回退 | - | 按照代理列表顺序依次测试，若不可用则切换到下一个 |
| 流媒体 | 代理 | 大部分海外流媒体平台，如 Netflix |
| 港澳台流媒体 | 直连 | 在大陆提供服务，但港澳台有限定资源的流媒体，如哔哩哔哩 |
| 部分 AI 聊天服务 | 代理 | ChatGPT、Claude 和 Bard |
| Apple | 直连 | Apple 及其相关服务 |
| Telegram | 代理 | Telegram 及其相关服务 |
| OneDrive | 直连 | OneDrive 及其相关服务 |

# 策略组名称对照表

<!-- prettier-ignore -->
| 策略组 | Clash 策略组 | Surge 策略组 |
|:-|:-|:-|
| 代理 | `PROXY` | `Proxy` |
| 直连 | `DIRECT` | `Direct` |
| 拒绝 | `REJECT` | `Reject` |
| 匹配 | `Final` | `Final` |
| 流媒体 | `Streaming` | `Streaming` |
| 广告拦截 | `Guard` | `Guard` |
| 自动测试 | `Autotest` | `Autotest` |
| 自动回退 | `Fallback` | `Fallback` |
| 港澳台流媒体 | `StreamingSE` | `StreamingSE` |
| 部分 AI 聊天服务 | `ChatAI` | `ChatAI` |
| Apple | `Apple` | `Apple` |
| Telegram | `Telegram` | `Telegram` |
| OneDrive | `OneDrive` | `OneDrive` |
