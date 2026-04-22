from sorting import random_numbers

class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        """vrátí počet bodů studenta na zadané pozici"""
        return self.scores[index]

    def count(self):
        """vrátí počet studentů"""
        return len(self.scores)

    def get_grade(self, index):
        score = self.get_by_index(index)

        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        elif score >= 50:
            return "E"
        else:
            return "F"


    def find(self, score):
        idx = 0
        count = 0
        positions = []
        searched_data = self.scores
        while idx < len(searched_data):
            if searched_data[idx] == score:
                positions.append(idx)
            idx += 1
        return positions

    def get_sorted(self):
        numbers = self.scores
        numbers = numbers.copy
        n = len(numbers)
        for it in range(n - 1):
            for idx in range(n - 1 - it):
                if numbers[idx] > numbers[idx + 1]:
                    numbers[idx], numbers[idx + 1] = numbers[idx + 1], numbers[idx]




def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    print(f"Počet studentů: {results.count}")
    for student_id in range(results.count):
        print(f"Student {student_id}: {results.get_by_index(student_id)} points - {results.get_grade()}")

    print(f"Plný počet bodů měl/i student/i: {results.find(100)}")
    print(f"Seřazené výsledky {results.get_sorted()}")

    random_results = StudentsGrades(random_numbers(30, 0, 100))
    print(random_results.count())
    print(random_results.get_sorted())

    if __name__ == "__main__":
        results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

        print(results.count())
        print(results.get_by_index(2))
        print(results.scores)
        print(results.get_grade(2))
        print(results.find(2))
        print(results.get_sorted())
        print(results.scores)



