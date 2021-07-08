class Student:

    def __init__(self, name="student", age="student", class_="student", test1=0, test2=0, test3=0, overall=0):
        def scores(t1, t2, t3):
            avg = (t1 + t2 + t3) / 3
            return avg

        self.name = name
        self.age = age
        self.class_ = class_
        self.test1 = test1
        self.test2 = test2
        self.test3 = test3
        self.overall = scores(test1, test2, test3)


test = Student()

daniel = Student("daniel", "29", "maths", 5, 5, 5)



print(test.overall)
print([getattr(daniel, x) for x in ("name", "age", "class_", "test1", "test2", "test3", "overall")])