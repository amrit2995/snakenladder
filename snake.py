
class Snake:
    def __init__(self, source,destination):
        self._source = source
        self._destination = destination

    def get_source(self):
        return self._source

    def get_destination(self):
        return self._destination