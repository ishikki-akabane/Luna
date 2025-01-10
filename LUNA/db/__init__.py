

from motor.

from LUNA import GRAMDB_URI, LOGGER
from datetime import datetime



class DATABASE():
    def __init__(self, uri):
        self.async_manager = GramDBAsync()
        self.db = GramDB(uri, self.async_manager)
        self.initialize()

    def initialize(self):
        return


db = DATABASE(GRAMDB_URI)


