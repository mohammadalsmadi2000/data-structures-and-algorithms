from collections import deque

# create a deque

class Animal:
    """
    Represents an animal with a species and name.
    """
    def __init__(self, species, name):
        """
        Initializes an Animal object with the given species and name.

        :param species: A string representing the species of the animal ("dog" or "cat").
        :param name: A string representing the name of the animal.
        """
        self.species = species
        self.name = name

    def __str__(self):
        """
        Returns a string representation of the animal.

        :return: A string representing the animal.
        """
        return f"{self.species.capitalize()}: {self.name}"


class AnimalShelter:
    """
    Represents an animal shelter that holds dogs and cats.
    """
    def __init__(self):
        """
        Initializes an AnimalShelter object with empty lists for dogs and cats and an order counter.
        """
        self.dogs = deque()
        self.cats = deque()
        self.order = 0

    def enqueue(self, animal):
        """
        Adds an animal to the shelter based on its species.

        :param animal: An Animal object to be added to the shelter.
        """
        animal.order = self.order
        self.order += 1
        if animal.species == 'dog':
            self.dogs.append(animal)
        elif animal.species == 'cat':
            self.cats.append(animal)

    def dequeue(self, pref=None):
        """
        Removes and returns the first animal in the shelter based on the given preference.

        :param pref: A string representing the preferred species ("dog" or "cat"). Default is None.
        :return: An Animal object representing the dequeued animal. Returns None if no animal is dequeued.
        """
        if pref == 'dog':
            if self.dogs:
                return self.dogs.popleft()
        elif pref == 'cat':
            if self.cats:
                return self.cats.popleft()
        else:
            if self.dogs and self.cats:
                if self.dogs[0].order < self.cats[0].order:
                    return self.dogs.popleft()
                else:
                    return self.cats.popleft()
            elif self.dogs:
                return self.dogs.popleft()
            elif self.cats:
                return self.cats.popleft()
        return None

    def __str__(self):
        """
        Returns a string representation of the animals in the shelter.

        :return: A string representing the animals in the shelter.
        """
        dog_str = "Dogs:\n" + "\n".join(str(dog) for dog in self.dogs) + "\n" if self.dogs else ""
        cat_str = "Cats:\n" + "\n".join(str(cat) for cat in self.cats) + "\n" if self.cats else ""
        return dog_str + cat_str



if __name__=="__main__":
    # Create an animal shelter
    shelter = AnimalShelter()
    D1=Animal("dog", "D1")
    D2=Animal("dog", "D2")
    D3=Animal("dog", "D3")
    C1=Animal("cat", "C1")
    # Enqueue some animals
    shelter.enqueue(D1)
    shelter.enqueue(D2)
    shelter.enqueue(D3)
    shelter.enqueue(C1)
    shelter.dequeue("dog")
    print(shelter)
