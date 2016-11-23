PLANT_MAP = {
    'C': 'Clover',
    'G': 'Grass',
    'R': 'Radishes',
    'V': 'Violets',
}
STUDENTS = [
    'Alice',
    'Bob',
    'Charlie',
    'David',
    'Eve',
    'Fred',
    'Ginny',
    'Harriet',
    'Ileana',
    'Joseph',
    'Kincaid',
    'Larry',
]



class Garden(object):
    def __init__(self, diagram):

        self.diagram = diagram.split('\n')

    def plants(self, student):
        if student == 'Alice':
            return [
                PLANT_MAP[self.diagram[0][0]],
                PLANT_MAP[self.diagram[0][1]],
                PLANT_MAP[self.diagram[1][0]],
                PLANT_MAP[self.diagram[1][1]],
            ]
        elif student == 'Bob':
            return [
                PLANT_MAP[self.diagram[0][2]],
                PLANT_MAP[self.diagram[0][3]],
                PLANT_MAP[self.diagram[1][2]],
                PLANT_MAP[self.diagram[1][3]],
            ]
        elif student == 'Charlie':
            return [
                PLANT_MAP[self.diagram[0][4]],
                PLANT_MAP[self.diagram[0][5]],
                PLANT_MAP[self.diagram[1][4]],
                PLANT_MAP[self.diagram[1][5]],
            ]
        elif student == 'Kincaid':
            return [
                PLANT_MAP[self.diagram[0][20]],
                PLANT_MAP[self.diagram[0][21]],
                PLANT_MAP[self.diagram[1][20]],
                PLANT_MAP[self.diagram[1][21]],
            ]
        elif student == 'Larry':
            return [
                PLANT_MAP[self.diagram[0][22]],
                PLANT_MAP[self.diagram[0][23]],
                PLANT_MAP[self.diagram[1][22]],
                PLANT_MAP[self.diagram[1][23]],
            ]
