# First-in, First-out Animal Shelter

## Problem Domain

We need to create an animal shelter that only accepts dogs and cats. The shelter operates on a "first-in, first-out" basis. That means the animal that has been in the shelter the longest will be the first one to be adopted. Implement a class called AnimalShelter which has two methods:

1. enqueue(animal): adds an animal to the shelter. The animal can be a dog or a cat object, with a "species" property that is either "cat" or "dog", and a "name" property that is a string.
2. dequeue(pref): removes the oldest animal of the preferred species ("dog" or "cat") from the shelter. If the preference is not specified or is not "dog" or "cat", then the oldest animal in the shelter will be removed.


## Algorithm
### enqueue(animal)
1. Increment the order counter.
2. Set the animal's order to the current order counter.
3. If the animal is a dog, add it to the list of dogs.
4. If the animal is a cat, add it to the list of cats.

### dequeue(pref)
1. If the preferred species is "dog", remove and return the first dog in the list of dogs.
2. If the preferred species is "cat", remove and return the first cat in the list of cats.
3. If the preferred species is not specified or is not "dog" or "cat":
* If there are both dogs and cats in the shelter, remove and return the animal with the oldest order (i.e., the animal that has been in the shelter the longest).
* If there are only dogs or only cats in the shelter, remove and return the animal with the oldest order.
4. If no animal is dequeued, return None.

## Big O
### enqueue(animal)
* Time Complexity: O(1)
The method performs constant time operations regardless of the number of animals in the shelter.
* Space Complexity: O(1)
The method does not use additional space that grows with the number of animals in the shelter.

### dequeue(pref)
* Time Complexity: O(1) to O(n)
If the preferred species is specified, the method performs constant time operations by removing the first animal of the specified species. If the preferred species is not specified or is not "dog" or "cat", the method needs to search through both the list of dogs and the list of cats to find the animal with the oldest order. In the worst case, the method needs to search through all animals in the shelter, which takes linear time.
* Space Complexity: O(1)
The method does not use additional space that grows with the number of animals in the shelter.