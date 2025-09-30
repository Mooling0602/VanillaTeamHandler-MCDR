from mcdreforged.api.all import PluginServerInterface
from .handler import VanillaTeamHandler


def on_load(server: PluginServerInterface, _):
    server.logger.info(server.rtr(f"{server.get_self_metadata().id}.on_load"))
    server.register_server_handler(VanillaTeamHandler())
