# main.py
"""Main module for loading settings from a configuration file."""

import configparser

def load_settings(filepath):
    """
    Load settings from a configuration file.

    Args:
        filepath (str): Path to the configuration file.

    Returns:
        configparser.ConfigParser: Parsed configuration settings.
    """
    config = configparser.ConfigParser()
    config.read(filepath)
    return config

if __name__ == "__main__":
    settings = load_settings('settings.cfg')
    print(settings['DEFAULT']['Setting1'])
