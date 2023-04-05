# 配置说明

Surge 配置兼容较新版本的 Surge（iOS 4.13.0 或 Mac 4.5.2 以上）

这个版本更新了这个功能，本配置中用于处理订阅链接

- `You can now use a full profile as the external policy group (policy-path). All proxies in the [Proxy] section will be used.`

---

Clash 仅兼容 Premium 内核

仅 Premium 内核才可使用 `proxy-providers` 与 `rule-providers`，本配置可搭配 [LufsX/shell-sub](https://github.com/LufsX/shell-sub) 来提取订阅中的 NodeList

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
| Telegram | 代理 | Telegram 及其相关服务 |
| OneDrive | 直连 | OneDrive 及其相关服务 |

# 策略组名称对照表

<!-- prettier-ignore -->
| 策略组 | Clash 策略组 | Surge 策略组 |
|:-|:-|:-|
| 代理 | `PROXY` | `Proxy` |
| 直连 | `DIRECT` | `Direct` |
| 拒绝 | `REJECT` | `Reject` |
| 匹配 | `MATCH` | `Final` |
| 流媒体 | `Streaming` | `Streaming` |
| 广告拦截 | `GURAD` | `Guard` |
| 自动测试 | `Autotest` | `Autotest` |
| 自动回退 | `Fallback` | `Fallback` |
| 港澳台流媒体 | `StreamingSE` | `StreamingSE` |
| Telegram | `Telegram` | `Telegram` |
| OneDrive | `OneDrive` | `OneDrive` |
