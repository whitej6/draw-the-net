"""Plugin declaration for draw_the_net."""
# Metadata is inherited from Nautobot. If not including Nautobot in the environment, this should be added
try:
    from importlib import metadata
except ImportError:
    # Python version < 3.8
    import importlib_metadata as metadata

__version__ = metadata.version(__name__)

from nautobot.extras.plugins import NautobotAppConfig


class DrawTheNetConfig(NautobotAppConfig):
    """Plugin configuration for the draw_the_net plugin."""

    name = "draw_the_net"
    verbose_name = "Draw The Net"
    version = __version__
    author = "Jeremy White"
    description = "Draw The Net."
    base_url = "draw-the-net"
    required_settings = []
    min_version = "1.6.1"
    max_version = "1.9999"
    default_settings = {}
    caching_config = {}


config = DrawTheNetConfig  # pylint:disable=invalid-name
