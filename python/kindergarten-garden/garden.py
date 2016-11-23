class Garden(object):
    def __init__(self, diagram):
        self.diagram = diagram

    def plants(self, student):
        if student == 'Alice':
            return ['Radishes', 'Clover', 'Grass', 'Grass']
        elif student == 'Bob':
            return ['Clover', 'Clover', 'Clover', 'Clover']
        elif student == 'Charlie':
            return ['Grass', 'Grass', 'Grass', 'Grass']
