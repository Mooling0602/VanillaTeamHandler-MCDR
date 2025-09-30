import re

from typing import List
from typing_extensions import override
from mcdreforged.handler.impl import VanillaHandler


class VanillaTeamHandler(VanillaHandler):
    def get_name(self) -> str:
        return "vanilla_team_handler"

    def parse_server_stdout(self, text: str):
        info = super().parse_server_stdout(text)
        if info.player is None:
            if info.content:
                m = re.fullmatch(
                    r"(\[Not Secure] )?<\[\w+](?P<name>[^>]+)> (?P<message>.*)",
                    info.content,
                )
                if m is not None and self._verify_player_name(m["name"]):
                    info.player, info.content = m["name"], m["message"]
        return info

    @classmethod
    @override
    def get_player_message_parsing_formatter(cls) -> List[re.Pattern]:
        # [Not Secure] <Alex> hello
        return [
            re.compile(
                r"(\[Not Secure] )?"  # mc1.19+ un-verified chat message
                r"<(?P<name>[^>]+)> (?P<message>.*)"
            )
        ]

