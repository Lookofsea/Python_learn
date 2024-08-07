class Student:
    def __init__(self, name, student_id) -> None:
        self.name = name
        self.student_id = student_id
        self.score = {
            "语文": 0,
            "数学": 0,
            "英语": 0
        }

    def set_score(self, course, score):
        if course in self.score:
            self.score[course] = score


    def get_total_score(self):
        
        for key,value in self.score.items():
            print(key,value)
        return sum(self.score.values())

# 示例用法
student = Student("张三", "123456")
student.set_score("语文", 90)
student.set_score("数学", 85)
student.set_score("英语", 88)
print(student.get_total_score())  # 输出: 263
print(student.score)


