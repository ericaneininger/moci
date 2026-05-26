import sys
if sys.version_info[0] == 2:
    from rose.upgrade import MacroUpgrade
else:
    from metomi.rose.upgrade import MacroUpgrade

class UpgradeError(Exception):

    """Exception created when an upgrade fails."""

    def __init__(self, msg):
        self.msg = msg

    def __repr__(self):
        sys.tracebacklimit = 0
        return self.msg

    __str__ = __repr__


class OPTv3v4(MacroUpgrade):

    """Upgrade macro for MOCI ticket #299 by julienpalmieri."""

    BEFORE_TAG = "OPT-v3"
    AFTER_TAG = "OPT-v4"

    def upgrade(self, config, meta_config=None):
        """Upgrade an Ocean Passive Tracers make app configuration."""
        # Input your macro commands here
        return config, self.reports


