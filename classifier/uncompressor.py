from loguru import logger
from pathlib import Path


class Uncompressor:
    def __init__(self):
        pass

    def uncompress(self, filePath):
        pass


if __name__ == "__main__":
    filePath = sys.argv[2]
    uncompressor = Uncompressor()
    uncompressor.uncompress(filePath)
