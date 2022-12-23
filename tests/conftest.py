def pytest_configure(config):
    plugin = config.pluginmanager.getplugin('mypy')

