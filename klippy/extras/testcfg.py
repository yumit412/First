# Demo code for local config reading
import os, ConfigParser, logging
import klippy

class TestCfg:
    def __init__(self, config):
        self.printer = config.get_printer()
        # Parse options from local config file in same directory as source code
        fileconfig = ConfigParser.RawConfigParser()
        localname = os.path.join(os.path.dirname(__file__), 'testcfg.cfg')
        fileconfig.read(localname)
        localconfig = klippy.ConfigWrapper(self.printer, fileconfig, {}, None)
        self.handle_config(localconfig)
        # Parse options from main config
        self.handle_config(config)
    def handle_config(self, config):
        for cfg in config.get_prefix_sections("testitem "):
            logging.info("Got %s %s", cfg.get_name(), cfg.get("value"))

def load_config(config):
    return TestCfg(config)
