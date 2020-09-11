from xml.etree import ElementTree


class IMS:
    def __init__(self, file):
        tree = ElementTree.parse(file)
        self.root = tree.getroot()

    def persons(self, role=None):
        if not role:
            return self.root.findall('.//person')
        else:
            return self.root.findall('.//person/institutionrole[@institutionroletype="%s"]/..' % role)
