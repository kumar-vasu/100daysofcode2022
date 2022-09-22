class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        coordinates = [i for i in coordinates]
        coordinates[0] = ord(coordinates[0])
        if (int(coordinates[0]) + int(coordinates[1])) % 2 == 0:
            return False
            
        else:
            return True