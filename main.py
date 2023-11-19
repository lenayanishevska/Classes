# import re
#
#
# # 1
# def add_to_shopping_list(shopping_list: dict, item: str, quantity: int ) -> dict:
#     if item in shopping_list:
#         shopping_list[item] += quantity
#     else:
#         shopping_list[item] = quantity
#     return shopping_list
#
#
# shopping_list = {}
# while True:
#     try:
#         item = input("Enter a shopping item: ")
#         quantity = int(input("Enter quantity;"))
#
#         add_to_shopping_list(shopping_list, item, quantity)
#         print(shopping_list)
#
#         break
#     except ValueError as e:
#         print(f"Error: {e}. Try again please!")
#
#
# # 2
# def email_validator(email_list: list) -> list:
#     valid_emails = []
#     pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
#     for email in email_list:
#         if re.match(pattern, email):
#             valid_emails.append(email)
#     return valid_emails
#
#
# email_list = ['user1@gmail.com', 'user2@lpnu.ua', 'user3@gmail.com', 'user4@ukr.net']
# print(email_validator(email_list))
#
#
# # 3
# def find_missing_number(numbers):
#     if not numbers:
#         return None
#
#     n = len(numbers) + 1
#     expected_sum = n * (n + 1) // 2
#     actual_sum = sum(numbers)
#     missing_number = expected_sum - actual_sum
#
#     if 1 <= missing_number <= n:
#         return missing_number
#     else:
#         return None
#
#
#
# def test_find_missing_number():
#     numbers = [1, 2, 3, 5, 6]
#     missing = find_missing_number(numbers)
#     assert missing == 4, "Test case failed"
#
#
# numbers_list = [1, 2, 3, 4, 5, 7, 8]
# missing = find_missing_number(numbers_list)
# test_find_missing_number()
# print(f"The missing number is: {missing}")
#
#
# # 4
# def grade_students(students_list: list, threshold) -> list:
#     students_names_list = [i for i, grade in students_list if grade >= threshold]
#     return students_names_list
#
#
# student_grades = [
#     ('Alice', 90),
#     ('Bob', 85),
#     ('Charlie', 92),
#     ('David', 78),
#     ('Eve', 95)
# ]
#
# threshold = 90
# above_threshold_students = grade_students(student_grades, threshold)
# print(above_threshold_students)


# 5
def book_tracker(book_transactions, book_title):
    books_in_library = {book[0]: book[1] for book in book_transactions}

    if book_title in books_in_library:
        if books_in_library[book_title]:
            print(f"The book '{book_title}' is available.")
        else:
            print(f"Sorry, book '{book_title}' is already borrowed.")
    else:
        print(f"The book '{book_title}' is not in our list.")


book_transactions = [("Book1", True), ("Book2", True), ("Book1", False)]
book_to_check = "Book2"
book_tracker(book_transactions, book_to_check)


# 6
def append_contact(contact_list: list, contact_to_manage: tuple):
    contact_list.append(contact_to_manage)
    return "Contact added successfully!", contact_list


def remove_contact(contact_list: list, contact_to_manage: tuple):
    if contact_to_manage in contact_list:
        contact_list.remove(contact_to_manage)
        return "Contact removed successfully!", contact_list
    else:
        return "There is no such contact in contacts list!"


def update_contact(contact_list: list, contact_to_manage: tuple):
    # name, new_phone = contact_to_manage
    for i, contact in enumerate(contact_list):
        if contact[0] == contact_to_manage[0]:
            contact_list[i] = contact_to_manage
            return "Contact updated successfully!", contact_list
    return "There is no such contact in contacts list!"


def manage_contacts(func, contacts_list, contact_to_manage):
    return func(contacts_list, contact_to_manage)


contact_list = [
    ("Alice", "0688685641"),
    ("Bob", "0976785467"),
    ("Charlie", "0986858345")
]

print(manage_contacts(append_contact, contact_list, ("David", "0688685841")))
print(manage_contacts(remove_contact, contact_list, ("Alice", "0688685641")))
print(manage_contacts(update_contact, contact_list, ("Bob", "0976785467")))


# 7
def flight_itinerary(flight_routes, source, destination):
    flight_plan = []
    current = source

    while current != destination:
        found_next = False
        for route in flight_routes:
            src, dest = route
            if src == current:
                flight_plan.append(src)
                current = dest
                found_next = True
                break

        if not found_next:
            return None

    flight_plan.append(destination)
    return flight_plan


flight_routes = [
    ("New York", "Los Angeles"),
    ("Los Angeles", "San Francisco"),
    ("San Francisco", "Seattle"),
    ("Seattle", "Chicago")
]

source_city = "New York"
destination_city = "San Francisco"

itinerary = flight_itinerary(flight_routes, source_city, destination_city)

if itinerary:
    print(f"Flight itinerary from {source_city} to {destination_city}:")
    print(" -> ".join(itinerary))
else:
    print(f"No valid flight itinerary from {source_city} to {destination_city}.")
