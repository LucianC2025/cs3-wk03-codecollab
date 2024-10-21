# A list to store recipes
recipes = []

# Function to add a recipe
def add_recipe():
    print("\n--- Add a Recipe ---")
    recipe_name = input("Enter the recipe name: ")
    ingredients = input("Enter the ingredients (separate with commas): ").split(',')
    cook_time = input("Enter the cook time in minutes: ")
    
    recipe = {
        'recipe name': recipe_name.strip(),
        'ingredients': [ingredient.strip() for ingredient in ingredients],
        'cook time': cook_time.strip()
    }
    
    recipes.append(recipe)
    print(f"\nRecipe '{recipe_name}' added successfully!\n")

# Function to view all recipes
def view_recipes():
    print("\n--- View All Recipes ---")
    if len(recipes) == 0:
        print("No recipes available yet.")
        return
    
    # Enumerate is a function for iteration thorugh a set
    # the object in the enumerate function must be a sequence, an iterator, or some other object which supports iteration
    # function returns a tuple
    # has a counter that defaults at zero, and counts up in index
    for i, recipe in enumerate(recipes, 1): 
        print(f"\nRecipe {i}: {recipe['recipe name']}")
        print(f"  Ingredients: {', '.join(recipe['ingredients'])}")
        print(f"  Cook time: {recipe['cook time']} minutes")

# Function to find a recipe by name
def find_recipe():
    print("\n--- Find a Recipe ---")
    search_name = input("Enter the recipe name to search: ").strip()
    
    for recipe in recipes:
        if recipe['recipe name'].lower() == search_name.lower():
            print(f"\nRecipe found: {recipe['recipe name']}")
            print(f"  Ingredients: {', '.join(recipe['ingredients'])}")
            print(f"  Cook time: {recipe['cook time']} minutes")
            return
    
    print(f"No recipe found with the name '{search_name}'.")

# Function to show menu and get user choice
def show_menu():
    print("\n--- Recipe Collector Menu ---")
    print("1. Add a recipe")
    print("2. View all recipes")
    print("3. Find a recipe by name")
    print("4. Exit")
    return input("Choose an option (1-4): ")

# Main interaction loop
def main():
    while True:
        choice = show_menu()
        
        if choice == '1':
            add_recipe()
        elif choice == '2':
            view_recipes()
        elif choice == '3':
            find_recipe()
        elif choice == '4':
            print("Exiting the Recipe Collector. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

# Run the main loop
if __name__ == "__main__":
    main()
