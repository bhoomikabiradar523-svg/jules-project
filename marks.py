def calculate_total_and_average(marks):
    if not marks:
        return 0, 0.0
    total = sum(marks)
    average = total / len(marks)
    return total, average

def main():
    marks = [85, 90, 78, 92, 88]
    total, average = calculate_total_and_average(marks)
    print(f"Marks: {marks}")
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")

if __name__ == "__main__":
    main()
