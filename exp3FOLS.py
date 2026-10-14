# First-Order Logic: Family Relationships

# Store parent-child relationships
parents = [
    ("Ali", "Rahim"),
    ("Rahim", "Karim"),
    ("Rahim", "Sara"),
    ("Karim", "Nila"),
    ("Karim", "Rafi")
]

# Find grandparent relationships
grandparents = set()

for x, y in parents:
    for a, z in parents:
        if y == a:
            grandparents.add((x, z))

# Find sibling relationships
siblings = set()

for p, x in parents:
    for q, y in parents:
        if p == q and x != y:
            siblings.add(tuple(sorted((x, y))))

# Take user choice
print("1. Check Grandparent Relationship")
print("2. Check Sibling Relationship")
choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    person1 = input("Enter grandparent name: ").strip().title()
    person2 = input("Enter grandchild name: ").strip().title()

    if (person1, person2) in grandparents:
        print(person1, "is the grandparent of", person2)
    else:
        print("No grandparent relationship found.")

elif choice == "2":
    person1 = input("Enter first person's name: ").strip().title()
    person2 = input("Enter second person's name: ").strip().title()

    if person1 != person2 and tuple(sorted((person1, person2))) in siblings:
        print(person1, "and", person2, "are siblings.")
    else:
        print("No sibling relationship found.")

else:
    print("Invalid choice!")
