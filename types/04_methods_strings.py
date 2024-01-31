"""Methods Strings"""

animal = "  vElociraptor dinosaur  "
print(animal.upper())
print(animal.lower())
print(animal.capitalize())
print(animal.title())
print(animal.strip())
print(animal.lstrip().capitalize())

print(animal.find("di"))
print(animal.replace("di", "Fo"))
print("sa" in animal)
print("sa" not in animal)
