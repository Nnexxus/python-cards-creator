import yaml

class Card(yaml.YAMLObject):
    yaml_tag = u'!Card'
    def __init__(self, title, text=None, image=None, copies=1):
        self.title = title
        self.text = text
        self.image = image
        self.copies = copies
        
    @property
    def filename(self):
        return self.title.replace(" ", "_") + ".png"
