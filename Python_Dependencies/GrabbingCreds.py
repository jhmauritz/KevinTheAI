import configparser


# TODO config parsing for keys
class GrabingCreds:
    def __init__(self):
        self.file = 'Creds/Creds.ini'

#TODO make this wokrk better
    def GrabCreds(self, section, item):
        config = configparser.ConfigParser()
        config.read(self.file)
        needed_section = config[section]
        items = needed_section[item]
        return items