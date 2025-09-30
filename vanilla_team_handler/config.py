from mcdreforged.api.all import Serializable


class MainConfig(Serializable):
    regex_display_name: str = r"[-+._\w]+"
    regex_prefix: str = r""
    regex_suffix: str = r""

