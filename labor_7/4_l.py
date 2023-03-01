# create an empty list to store crop dictionaries
crops = []

# create a function to add a crop dictionary to the list
def add_crop():
    # get information about the crop from the user
    name = input("Enter the name of the crop (or type 'done' to finish): ")
    country = input("Enter the country of origin of the seeds: ")
    yield_per_hectare = float(input("Enter the average yield per hectare (in tons): "))
    requires_pest_control = input("Does this crop require pest control (yes or no)? ")
    harvest_method = input("Enter the harvest method for this crop: ")
    
    # create a dictionary for the crop
    crop = {
        "name": name,
        "country": country,
        "yield": yield_per_hectare,
        "pest_control": requires_pest_control.lower() == "yes",
        "harvest_method": harvest_method,
        "fruits": {}  # empty dictionary for fruit information
    }
    
    # add information about fruits of the crop
    fruit_count = int(input("Enter the number of fruits for this crop: "))
    for i in range(fruit_count):
        fruit_name = input(f"Enter the name of fruit {i+1}: ")
        fruit_color = input(f"Enter the color of fruit {i+1}: ")
        fruit_weight = int(input(f"Enter the average weight of fruit {i+1}: "))
        fruit_unit = input(f"Enter the unit of weight for fruit {i+1}: ")
        crop["fruits"][fruit_name] = {
            "color": fruit_color,
            "weight": fruit_weight,
            "unit": fruit_unit
        }
    
    # add the crop dictionary to the list
    crops.append(crop)

# call the add_crop function to add crops to the list'
  add_crop()

# print information about all the crops in the list
for crop in crops:
    print("Crop:", crop["name"])
    print("Country of origin of the seeds:", crop["country"])
    print("Average yield per hectare (in tons):", crop["yield"])
    print("Requires pest control:", "Yes" if crop["pest_control"] else "No")
    print("Harvest method:", crop["harvest_method"])
    print("Fruits:")
    for fruit_name, fruit_info in crop["fruits"].items():
        print(f"\t{fruit_name}:")
        print(f"\t\tColor: {fruit_info['color']}")
        print(f"\t\tWeight: {fruit_info['weight']} {fruit_info['unit']}")
    print()