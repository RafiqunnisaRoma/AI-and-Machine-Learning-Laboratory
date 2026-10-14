# Knowledge-Based Agent using Propositional Logic

# Rules of the knowledge base
rules = [
    ({"Rain", "Cold"}, "WearJacket"),
    ({"Rain"}, "CarryUmbrella"),
    ({"Rain"}, "WearSunglasses"),
    ({"Rain"}, "WetGround"),
    ({"WetGround"}, "Slippery"),
    ({"Slippery"}, "DriveSlowly")
]


# Forward chaining function
def forward_chain(facts):

    # Store the initial facts
    knowledge = set(facts)

    # Check each rule
    for conditions, result in rules:

        # If all conditions are known
        if conditions <= knowledge:

            # Add the result to knowledge
            knowledge.add(result)

            # Display the applied rule
            print(conditions, "->", result)

    # Return final knowledge
    return knowledge


# -------------------------------
# Take test case from user
# -------------------------------

print("Knowledge-Based Agent")
print("---------------------")

# Ask the user to enter facts
user_input = input("Enter initial facts separated by comma (e.g., Rain, Cold): ")

# Convert user input into a set
facts = set(fact.strip().title() for fact in user_input.split(","))


# Display the initial facts
print("\nInitial Facts:", facts)

# Perform forward chaining
final_knowledge = forward_chain(facts)

# Display final knowledge
print("\nFinal Knowledge:", final_knowledge)

