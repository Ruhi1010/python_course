#8.12
def make_sandwich(*items):
    print("\nMaking a sandwich with the following ingredients:")
    for item in items:
        print(f"- {item}")
    print("Sandwich order complete!\n")

make_sandwich("chicken", "cheese")
make_sandwich("beef", "cheese")
