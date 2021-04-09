
class FileManagement():

    def __init__(self):
        pass

    def WriteLevelToFile(self, fileName : str, platformList: []):
        plikTestowy = open("level1.txt", "w")
        for platform in platformList:
            plikTestowy.write(str(platform) + '\n')
        plikTestowy.close()

    def ReadLevelFromFile(self, fileName: str):
        plikTestowy = open("level1.txt", "r")
        filePlatforms = []

        for platform in plikTestowy.readlines():
            stripped = platform.strip('()\n')
            splitted = stripped.split(',')
            mapped = map(int, splitted)
            tupled = tuple(mapped)
            filePlatforms.append(tupled)

        plikTestowy.close()

        return filePlatforms
