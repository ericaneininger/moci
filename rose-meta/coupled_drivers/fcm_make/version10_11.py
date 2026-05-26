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


class drivers10_t306(MacroUpgrade):

    """Upgrade macro for ticket #306 by Harry Shepherd."""
    BEFORE_TAG = "drivers_1.0"
    AFTER_TAG = "drivers_1.1"

    def upgrade(self, config, meta_config=None):
        """Upgrade a Driver make app configuration."""
        # Input your macro commands here
        self.change_setting_value(config, ["env", "config_rev"],
                                  "@drivers_1.1")
        self.change_setting_value(config, ["env", "driver_rev"],
                                  "drivers_1.1")
        return config, self.reports
