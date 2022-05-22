class Data:
    def __init__(self, st):
        self.input = st

    def __str__(self):
        return f'Entry date - {self.input}'

    @classmethod
    def to_int(cls, objs):
        obj = []
        for i in map(int, str(objs).split('-')):
            obj.append(i)
        return obj

    @staticmethod
    def is_valid(self, objs):
        obj = Data.to_int(objs)
        if (0 < obj[0] < 31) and (0 < obj[1] < 13) and (len(str(obj[2])) == 4):
            return True
        else:
            return False


date_1 = '11-12-1995'
date_2 = '66-66-66'
data_example = Data(date_1)
print(data_example, Data.to_int(date_1), Data.is_valid(Data, date_1), Data.is_valid(Data, date_2), sep='\n')
