def get_max():
    grades = [9.6, 9.2, 9.7]
    max_grade = max(grades)
    min_grade = min(grades)

    return f"\"Max: {max_grade},Min: {min_grade}\""

print(get_max())