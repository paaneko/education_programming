crops = [
    {
        "crop_name": "Tomato",
        "seed_origin_country": "Mexico",
        "average_yield": 25.5,
        "pesticides_needed": True,
        "harvest_method": "Handpicking"
    },
    {
        "crop_name": "Cabbage",
        "seed_origin_country": "Italy",
        "average_yield": 15.0,
        "pesticides_needed": False,
        "harvest_method": "Machine harvesting"
    },
    {
        "crop_name": "Carrot",
        "seed_origin_country": "Afghanistan",
        "average_yield": 19.8,
        "pesticides_needed": True,
        "harvest_method": "Handpicking"
    }
]

while True:
    crop_name = input("Enter the name of a vegetable crop (or type 'done' to finish): ")
    if crop_name == "done":
        break
    
    seed_origin_country = input("Enter the country of origin of the seeds for the crop: ")
    average_yield = float(input("Enter the average yield of the crop in tons per hectare: "))
    pesticides_needed = input("Does the crop need to be treated with pesticides to control pests? (y/n) ").lower() == "y"
    harvest_method = input("Enter the method used to harvest the crop: ")
    
    crop = {
        "crop_name": crop_name,
        "seed_origin_country": seed_origin_country,
        "average_yield": average_yield,
        "pesticides_needed": pesticides_needed,
        "harvest_method": harvest_method
    }
    
    crops.append(crop)

print("Information about the following crops has been recorded:")
for crop in crops:
    print(crop)