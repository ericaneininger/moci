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


class drivers02(MacroUpgrade):

    """Upgrade macro for ticket #219 by harryshepherd."""
    BEFORE_TAG = "drivers_0.1"
    AFTER_TAG = "drivers_0.2"

    def upgrade(self, config, meta_config=None):
        return config, self.reports
