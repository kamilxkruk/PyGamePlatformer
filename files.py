
class FileManagement():

    def __init__(self):
        pass

    def WriteLevelToFile(self,fileName: str, levelData: [[]]):
        plikTestowy = open(fileName, "w")
        plikTestowy.write('[')
        for rowId in range(len(levelData)):
            plikTestowy.write(str(levelData[rowId]))
            if rowId<len(levelData)-1:
                plikTestowy.write(',\n')
        plikTestowy.write(']')
        plikTestowy.close()

    def ReadLevelFromFile(self, fileName: str):
        textFile = open(fileName)
        levelData = []

        rawText = textFile.read()
        listLines = rawText[1:len(rawText)-1]
        splittedLines = listLines.split(',\n')
        for line in splittedLines:
            singleList = line.strip('[]').split(',')
            mappedList = list(map(int,singleList))
            levelData.append(mappedList)

        return levelData


    def WritePlatformsToFile(self, fileName : str, platformList: []):
        plikTestowy = open("level1.txt", "w")
        for platform in platformList:
            plikTestowy.write(str(platform) + '\n')
        plikTestowy.close()

    def ReadPlatformsFromFile(self, fileName: str):
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
