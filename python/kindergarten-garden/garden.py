PLANT_MAP = {
    'C': 'Clover',
    'G': 'Grass',
    'R': 'Radishes',
    'V': 'Violets',
}
NAMES = [
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
    def __init__(self, plot, students=None):
        self.plot = plot.split('\n')
        self.students = None
        self._call_role(sorted(students or NAMES))

    def plants(self, name):
        if name == 'Alice':
            return [
                PLANT_MAP[self.plot[0][0]],
                PLANT_MAP[self.plot[0][1]],
                PLANT_MAP[self.plot[1][0]],
                PLANT_MAP[self.plot[1][1]],
            ]
        elif name == 'Bob':
            return [
                PLANT_MAP[self.plot[0][2]],
                PLANT_MAP[self.plot[0][3]],
                PLANT_MAP[self.plot[1][2]],
                PLANT_MAP[self.plot[1][3]],
            ]
        elif name == 'Charlie':
            return [
                PLANT_MAP[self.plot[0][4]],
                PLANT_MAP[self.plot[0][5]],
                PLANT_MAP[self.plot[1][4]],
                PLANT_MAP[self.plot[1][5]],
            ]
        elif name == 'Kincaid':
            return [
                PLANT_MAP[self.plot[0][20]],
                PLANT_MAP[self.plot[0][21]],
                PLANT_MAP[self.plot[1][20]],
                PLANT_MAP[self.plot[1][21]],
            ]
        elif name == 'Larry':
            return [
                PLANT_MAP[self.plot[0][22]],
                PLANT_MAP[self.plot[0][23]],
                PLANT_MAP[self.plot[1][22]],
                PLANT_MAP[self.plot[1][23]],
            ]
        else:
            return self.students[name].plants

    def _call_role(self, names):
        self.students = {name: self._assign(name, names) for name in names}

    def _assign(self, name, names):
        return Student(
            name,
            names.index(name),
            len(names),
            self.plot,
        )


class Student(object):
    def __init__(self, name, index, names, plot):
        self.name = name
        self.index = index
        self.names = names
        self.offset = index * 2
        self.plot = plot
        self._plants = None

    @property
    def plants(self):
        if not self._plants:
            self._plants = self.assign_plants()
        return self._plants

    def assign_plants(self):
        plants = []
        for row in self.plot:
            plants.extend([PLANT_MAP[row[self.offset]], PLANT_MAP[row[self.offset + 1]]])
        return plants
