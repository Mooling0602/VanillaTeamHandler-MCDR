import re

from mcdreforged.handler.impl import VanillaHandler
from mcdreforged.utils import string_utils
from mcdreforged.info_reactor.info import InfoSource, Info


def strip_ansi(o: str) -> str:
    """
    Removes ANSI escape sequences from `o`, as defined by ECMA-048 in
    https://www.ecma-international.org/wp-content/uploads/ECMA-48_5th_edition_june_1991.pdf
    """

    pattern = re.compile(r"\x1B\[\d+(;\d+){0,2}m")
    stripped = pattern.sub("", o)
    return stripped


class VanillaTeamHandler(VanillaHandler):
    __regex_team = r"[-+._\w]+"
    __regex_display_name = r"read_config_plz"
    __regex_prefix = r"read_config_plz"
    __regex_suffix = r"read_config_plz"

    def get_name(self) -> str:
        return "vanilla_team_handler"

    @classmethod
    def get_server_stdout_raw_result(cls, text: str) -> Info:
        if type(text) is not str:
            raise TypeError("The text to parse should be a string")
        result = Info(InfoSource.SERVER, text)
        result.content = strip_ansi(
            string_utils.clean_console_color_code(text))
        return result
