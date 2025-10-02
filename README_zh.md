# VanillaTeamHandler-MCDR

选择语言：[English](README.md) | 简体中文

用于解析队伍成员的聊天消息的MCDReforged服务端处理器。仅支持使用`/team`命令的原版服务器。
> 原版Fabric服务器也受支持，但目前不支持"."开头的floodgate玩家。
<!-- markdownlint-disable MD028 -->
> [!WARNING]
> 不要将此插件与其他类型的处理器一起使用，否则会发生冲突。

## 使用方法

### 命令 `/team`

基于[命令 `/team`](https://zh.minecraft.wiki/w/命令/team)。

队伍的前缀和后缀选项都会改变队伍中玩家的聊天格式，但目前仅支持前缀。因此您必须阅读以下指南以使此处理器正常工作。

> 未来版本将尝试支持更多可自定义的配置选项。

前缀必须由英文字母、数字或下划线组成，并用方括号括起来；括号内的内容不得包含括号或其他影响识别的特殊字符。
> 注意：中文和其他非英文语言字符也许可以使用，但尚未经过彻底验证。

例如，使用`default`作为队伍名称，`[Default]`作为队伍前缀，`Steve`作为玩家名称。

1. 创建一个队伍。
   > `/team add <队伍>`

   例如：`/team add default`

2. 设置前缀，因为它会影响有关该玩家的消息中的玩家名称。
   > `/team modify <队伍> prefix <前缀>`

   例如：`/team modify default prefix "[Default]"`

3. 将玩家添加到队伍中。
   > `/team join <队伍> [<成员>]`

   **玩家侧**：例如：`/team join default`

   **服务器（控制台）侧**：例如：`/team join default Steve`
   > 注意：如果您想将所有玩家添加到队伍中，可以使用`/team join default @a`

然后此处理器将按照预期工作。
