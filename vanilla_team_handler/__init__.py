from mcdreforged.api.all import PluginServerInterface


def on_load(server: PluginServerInterface, _):
    server.logger.info("on_load")
