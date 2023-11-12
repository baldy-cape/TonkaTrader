# main.py
import configparser

def load_settings(filepath):
    config = configparser.ConfigParser()
    config.read(filepath)
    return config

if __name__ == "__main__":
    settings = load_settings('settings.cfg')
    print(settings['DEFAULT']['Setting1'])

