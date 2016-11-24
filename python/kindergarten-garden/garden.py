PLANT_MAP = {'C': 'Clover', 'G': 'Grass', 'R': 'Radishes', 'V': 'Violets'}

NAMES = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny',
         'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']


class Garden(object):
    def __init__(self, plot, students=None):
        self.plot = plot.split('\n')
        self.__names = sorted(students or NAMES)
        self.rolebook = {name: self._assign(name) for name in self.__names}

    def plants(self, name):
        return self.rolebook[name].plants

    def _assign(self, name):
        return Student(
            name,
            self.__names.index(name),
            self.plot,
        )


class Student(object):
    def __init__(self, name, index, plot):
        self.name = name
        self.index = index
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
            plants.extend([PLANT_MAP[row[self.offset]],
                           PLANT_MAP[row[self.offset + 1]]])
        return plants
