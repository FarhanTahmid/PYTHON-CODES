def describePet(animalType,petName):
    """Display info about pet"""
    print(f"I have a {animalType}")
    print(f"Its name is {petName}")

#you write the value and its name with in the argument
describePet(animalType='dog',petName='safwan')
#doesn't happen anything when we change the position
describePet(petName="Harry",animalType="Cat")