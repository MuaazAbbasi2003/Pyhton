numbers= range(1,5)

new_numbers=[n * 2 for n in numbers]

print(new_numbers)

students = {
    "Ali": 85,
    "Ahmed": 72,
    "Sara": 95,
    "Usman": 68,
    "Ayesha": 91,
    "Hamza": 77,
    "Zain": 88,
    "Fatima": 93,
    "Hassan": 56,
    "Mariam": 82,
    "Bilal": 64,
    "Zoya": 98,
    "Omar": 74,
    "Hira": 89,
    "Daniyal": 61,
    "Noor": 96,
    "Saad": 79,
    "Iqra": 87,
    "Talha": 70,
    "Maryam": 84
}

new_dict={student:value for (student,value) in students.items() if value >= 90}

print(new_dict)