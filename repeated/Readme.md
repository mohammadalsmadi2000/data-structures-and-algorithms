## Problem Domain

The problem is to find the first repeated word in a given string. The input string can be a sentence, a paragraph, or even a book.

To solve the problem, we will split the input string into individual words and keep track of the count of each word using a hashmap. We will iterate through each word, check if it already exists in the hashmap, and return the first word that occurs more than once.

## Big O Analysis

Let's analyze the time and space complexity of the `repeated` function.

The time complexity of the function depends on the number of words in the input string, which we can denote as `n`:

1. Splitting the input string into words using the `split()` method has a time complexity of O(n), where `n` is the length of the string.

2. Iterating through each word and performing operations like stripping punctuation marks, converting to lowercase, and checking the existence in the hashmap has a time complexity of O(n), where `n` is the number of words in the string.

Overall, the time complexity of the `repeated` function is O(n).

Regarding space complexity:

1. The space complexity of the function is O(n) because we need to store the individual words in a list and the count of each word in the hashmap. The space required is proportional to the number of words in the string.

In summary, the `repeated` function has a time complexity of O(n) and a space complexity of O(n), where `n` is the number of words in the input string.
