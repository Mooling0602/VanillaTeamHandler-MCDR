# VanillaTeamHandler-MCDR

A handler for MCDReforged to parse chat messages from team members. Only support vanilla servers with `/team` command.
> Vanilla Fabric server is also supported, but floodgate players with "." not at present.
<!-- markdownlint-disable MD028 -->
> [!WARNING]
> Don't use this plugin with other handler type ones, or conflicts will happen.

## Usage

### Command `/team`

Based on [Command `/team`](https://minecraft.wiki/w/Commands/team).

Both prefix and suffix options of a team will change the chat format of a player who is in it, but only prefix supported at present. So you have to read the following guides to make this handler works fine.

> Future versions will attempt to support more customizable configuration options.

The prefix must consist of English letters, digits, or underscores, enclosed in square brackets; the content within brackets must not contain brackets or other special characters that affect recognition.
> Note: Chinese and other non-English language characters may also be usable, but have not been thoroughly verified.

For example, use `default` as a team's name, `[Default]` as a team's prefix, and `Steve` as a player's name.

1. Create a team.
   > `/team add <team>`

   e.g.`/team add default`

2. Set the prefix, because it will affect the player's name in messages about the player.
   > `/team modify <team> prefix <prefix>`

   e.g.`/team modify default prefix "[Default]"`

3. Add the player to the team.
   > `/team join <team> [<members>]`

   **Player side**: e.g.`/team join default`

   **Server side**: e.g.`/team join default Steve`
   > Note: if you want to add all players to the team, you can use `/team join default @a`

Then this handler will work as expected.
