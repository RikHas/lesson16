class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType
    def __eq__(self, other):
        return (self.numberOfFloors == other.numberOfFloors and
                self.buildingType == other.buildingType)

B1 = Building('lee', 7)
B2 = Building('lee', 7)
B3 = Building(9, 'Kir')

print(B1 == B2)
print(B1 == B3)
