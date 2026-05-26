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


class drivers03(MacroUpgrade):

    """Upgrade macro for ticket #223 by harryshepherd."""
    BEFORE_TAG = "drivers_0.2.1"
    AFTER_TAG = "drivers_0.3"

    def upgrade(self, config, meta_config=None):
        '''Upgrade the tags'''
        self.change_setting_value(config, ["env", "config_rev"],
                                  "@drivers_0.3")
        self.change_setting_value(config, ["env", "driver_rev"],
                                  "drivers_0.3")
        return config, self.reports
