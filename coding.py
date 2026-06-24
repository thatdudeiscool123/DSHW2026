#!/usr/bin/env python
# coding: utf-8

# # Coding Assignment
# *Due Date: 06/23/2026 at 11:59 PM EST*
# 
# 
# Welcome to the coding assignment! This assignment is comprised of 5 questions:
# *   Welcome to Python
# *   Fibonacci Sequence
# *   Prime Number Generation
# *   Functions
# *   Goldbach's Conjecture
# 
# 
# You are free to edit either the `.ipynb` file or the `.py` file provided in Files > coding. However, when submitting, **you may only submit a .py file**.
# 
# 
# # Question 1: Welcome to Python!
# In the following, we will be writing a simple function that should familiarize you with string manipulation and basic control flow in Python.
# 
# (a) Write a function ```vowel_counter``` that takes a ```string s``` as input and counts the number of vowels in ```s```
# returning an ```int```. For this exercise, we take the vowels to be the following: ```[a, e, i, o, u]```. You may
# assume that the entire string is lowercase characters in a - z (no spaces, numbers, special characters, etc.)
# 
# Your Python function ```vowel_counter``` should take one argument ```s```. It should return one integer for the number of vowels.
# 
# **Hints:**
# 
# - You will need to be familiar with Python lists (which are just arrays), for loops, if statements, and basic string manipulation for this exercise. The following are links to the documentation of
# each, for your convenience:
#   - https://docs.python.org/3/tutorial/datastructures.html
#   - https://docs.python.org/3/tutorial/controlflow.html
#   - https://docs.python.org/3/library/string.html
# 
# - Strings in Python behave out of the box as lists of characters. This will be useful in iterating over a
# string.
# - Like in all programming, printing statements to debug is a useful tool. ```print()``` allows you to do just that.
# 

# In[2]:


def vowel_counter(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


# (b) Write a function ```sometimes_y``` that implements the annoying English rule that ```y``` is sometimes a vowel and
# sometimes not. We will go with a simplified rule for whether ```y``` is a vowel or not: **If 'y' appears at the
# end of the string, then it is a vowel. Otherwise, it is not.**
# 
# Instead of rewriting your previous function, however, we’ll get some practice calling other functions you
# have already written. For this exercise, you must use ```sometimes_y``` to call ```vowel_counter``` to determine the
# vowel count (do not duplicate the code from before). Then, you should just write some additional logic to
# compensate for the 'y' condition.
# 
# Our function should take a ```string s``` as input and return three outputs: whether 'y' is in the string or
# not (```Boolean```), the number of original vowels from ```vowel_counter``` (```int```), and the number of vowels with
# the additional rule of 'sometimes y' (```int```). Notice that Python allows you to return multiple outputs (of varying datatypes) by simply separating them with a comma in the return line. Useful!
# 
# For example, the string ```abcdef``` would return: ```False, 2, 2```. The string ```abcdefy``` would return: ```True,
# 2, 3```. The string ```yabcdef``` would return: ```True, 2, 2```.
# 
# **Hints:**
# - Be careful not to return a list. You want to use Python’s built-in functionality to return three objects.
# - To call another function you’ve written on some input ```x```, it suffices to just write: ```function(x)``` in your code.
# 

# In[3]:


def sometimes_y(s):
    y_in_string = 'y' in s
    original_vowels = vowel_counter(s)
    y_vowels = original_vowels + (1 if s[-1] == 'y' else 0)
    return y_in_string, original_vowels, y_vowels


# (c) Write a function ```sentence_counter``` that takes a ```string sentence``` as input and outputs a single list containing the number of vowels in each word of the sentence.
# 
# As before, you should use your previously implemented ```sometimes_y``` to accomplish this. **You must adhere to the 'sometimes y' rule.**
# 
# Unlike Part (a) you **may not assume** that your entire string is just lowercase alphabetical characters.
# This will give you some experience in cleaning messy strings up. However, you *can* assume the following
# conditions:
# 1. Spaces will separate each word in the sentence.
# 2. Special characters will be limited to: '.' (period), ',' (comma), '!' (exclamation), '?' (question mark).
# 3. There will be no numbers in the sentence.
# 4. Capital letters are allowed (which still increase your count if they are a vowel).
# 
# You may ask clarification questions about special cases on EdStem.
# 
# For example, ```"The boy, Sam, walked to the store."``` and ```"I went to office hours, and the TAs were so friendly!"``` are valid sentences. ```"I love that Terminal 5 is hosting Bacchanal this year"```
# and ```"Class 3203 - Discrete Math - is about integrals and continuity."``` are invalid sentences (both have numbers, and the second has numbers and dashes). You may simply assume that sentences of the second kind will not be given to your function.
# 
# On the input ```"The boy, Sam, walked to the store."```, your function should return the list: ```[1, 2, 1, 2, 1, 1, 2]```
# 
# **Hints:**
# - The functions ```.split()```, ```.strip()```, and ```.lower()``` are all built-in string functions that will be useful.
# A quick Google search for these will teach you what you need to know.
# - To adhere to the 'sometimes y' rule, you must retrieve the *third* output of your sometimes y function.
# - Note that the returned lists might have varying lengths depending on how long your string is.
# 

# In[4]:


def sentence_counter(sentence):
    words = sentence.split()
    result = []
    for word in words:
        cleaned = word.strip('.,!?').lower()
        _, _, vowel_count = sometimes_y(cleaned)
        result.append(vowel_count)
    return result


# Once you have completed your code, run the following cell to test your work. **DO NOT ALTER**!
# 

# In[5]:


"""Once you have completed your code, run the following cell to test your work. **DO NOT ALTER**!"""
if __name__ == '__main__':
  print("#######################################")
  print("Question 1: Welcome to Python!")
  print("#######################################")
  print()

  print("---------------------------------------")
  print("\'vowel_counter\' Tests")
  print("---------------------------------------")
  vowel_counter_tests = ['apple', 'cake', 'zzzz', 'aeiou',
  'pneumonoultramicroscopicsilicovolcanoconiosis']
  vowel_counter_answers = [2, 2, 0, 5, 20]
  for count, test in enumerate(vowel_counter_tests):
    if (vowel_counter(vowel_counter_tests[count]) == vowel_counter_answers[count]):
      passed = 'PASSED!'
    else:
      passed = "FAILED!"

    print("Test #{}: {}".format(count + 1, passed))
    print(f'Correct Answer: {vowel_counter_answers[count]}')
    print(f'Your Answer: {vowel_counter(vowel_counter_tests[count])}')

  print("---------------------------------------")
  print("\'sometimes_y\' Tests")
  print("---------------------------------------")

  sometimes_y_tests = ['apple', 'syzygy', 'zzzz', 'aeiouy',
  'pneumonoultramicroscopicsilicovolcanoconiosis', 'yellow', 'yesterday', 'y']
  sometimes_y_answers = [(False, 2, 2), (True, 0, 1), (False, 0, 0), (True, 5,
  6), (False, 20, 20), (True, 2, 2), (True, 3, 4), (True, 0, 1)]

  for count, test in enumerate(sometimes_y_tests):
    if (sometimes_y(sometimes_y_tests[count]) == sometimes_y_answers[count]):
      passed = 'PASSED!'
    else:
      passed = "FAILED!"

    print("Test #{}: {}".format(count + 1, passed))
    print(f'Correct Answer: {sometimes_y_answers[count]}')
    print(f'Your Answer: {sometimes_y(sometimes_y_tests[count])}')

  print("---------------------------------------")
  print("\'sentence_counter\' Tests")
  print("---------------------------------------")
  sentence_counter_tests = ['The boy, Sam, walked to the store.',
                            'Hello, how are you?',
                            'On a sunny day, the funny, punny bunny ran up the hill.',
                            'I went to office hours, and the TAs were so friendly!!!']
  sentence_counter_answers = [[1, 2, 1, 2, 1, 1, 2],
   [2, 1, 2, 2],
    [1, 1, 2, 2, 1, 2, 2, 2, 1, 1, 1, 1],
     [1, 1, 1, 3, 2, 1, 1, 1, 2, 1, 3]]

  for count, test in enumerate(sentence_counter_tests):
    if (sentence_counter(sentence_counter_tests[count]) == sentence_counter_answers[count]):
      passed = 'PASSED!'
    else:
      passed = 'FAILED!'

    print("Test #{}: {}".format(count + 1, passed))
    print(f'Correct Answer: {sentence_counter_answers[count]}')
    print(f'Your Answer: {sentence_counter(sentence_counter_tests[count])}')



# # Question 2: Fibonacci Sequence
# In this section, you will be implementing a simple recursive algorithm you’ve likely seen in previous classes. Recall from previous classes that we define the $n^{th}$ Fibonacci number $F_n$ as the sum of the previous two Fibonacci numbers, i.e.
# $$F_n = F_{n-1}+F_{n-2}$$
# where $F_0 = 0$ and $F_1 = 1$. For instance, the first 8 Fibonacci numbers (not including $F_0$) are
# $$1,1,2,3,5,8,13,21$$
# 
# (a) Write a function ```recursive_fib``` that takes in an integer ```n``` and outputs the $n^{th}$ Fibonacci number (also an
# ```int``` ). For this, you *must* use recursion.
# 
# **Hints:**
# - To do recursion using Python, simply call the same function you are implementing, *assuming* that
# you will get the right answer.
# - Recall that a recursive solution has three main components: (1) Base Case (2) Progress *towards* the
# base case and (3) Recursive calls to the same function.
# 

# In[6]:


def recursive_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return recursive_fib(n - 1) + recursive_fib(n - 2)


# (b) It is a known result (consequence of the Church-Turing thesis) that any recursive function can be written
# iteratively. In this exercise, you will implement Fibonacci iteratively instead of recursively.
# 
# Write a function iterative_fib that takes in an integer ```n``` and outputs the $n^{th}$ Fibonacci number (also an
# ```int```). This function *must not* use recursion.
# 
# **Hints:**
# - Recall the process of *memoization* from your intro CS classes. In memoization, you may store values
# in an array that correspond to your function on previous calls. This allows you to perform a recursive
# function iteratively by effectively "memorizing" previous results of your computation instead of keeping
# them on the recursion stack. You may also use the bottom-up dynamic programming approach, if
# you are more familiar with that solution.
# - You will still need the base case to get things going, however, which are still $F_0 = 0$ and $F_1 = 1$.
# 

# In[7]:


def iterative_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr


# Once you have completed your code, run the following cell to test your work. **DO NOT ALTER**!
# 

# In[8]:


"""Once you have completed your code, run the following cell to test your work. **DO NOT ALTER**!"""
if __name__ == '__main__':
  print("#######################################")
  print("Question 2: Fibonacci")
  print("#######################################")
  print()

  tests = [[1, 1], [4, 4], [10, 10]]
  answers = [[1, 1], [3, 3], [55, 55]]
  for count, test in enumerate(tests):
    if(answers[count][0] == recursive_fib(test[0]) and
      answers[count][1] == iterative_fib(test[1])):
      passed = "PASSED!"
    else:
      passed = "FAILED!"

    print("Test #{}: {}".format(count + 1, passed))
    print("Recursive Fibonacci (Correct): ", answers[count][0])
    print("Recursive Fibonacci (Your Answer): ", recursive_fib(test[0]))
    print("Iterative Fibonacci (Correct): ", answers[count][1])
    print("Iterative Fibonacci (Your Answer): ", iterative_fib(test[1]))



# # Question 3: Prime Number Generation
# 
# Prime number generation is crucial to many subfields of math and computer science, notably cryptography
# and security. Here, you will implement another ancient algorithm known as the Sieve of Eratosthenes to
# generate prime numbers.
# 
# Write a Python function prime_gen that implements the Sieve of Eratosthenes.
# 
# 1.   Write a Python function ```prime_gen``` that implements the Sieve of Eratosthenes. Your function will take in an integer $n > 1$ and will output all prime numbers up to (and including) $n$. Your function ```prime_gen``` will take in a single ```int``` as its argument and output a list of prime numbers
# (each also of type ```int```). **Make sure your output is a list, or your code will get zero points.**
# 
# For example, the following lines print the primes up to 5 and 10:
# ```
# print(prime_gen(5))
# print(prime_gen(10))
# ```
# where the output is:
# 
# ```
# [2, 3, 5]
# [2, 3, 5, 7]
# ```
# 

# In[9]:


def prime_gen(n):
    # Initialize all entries as True (assume all are prime)
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            # Mark all multiples of i as not prime
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    return [i for i in range(2, n + 1) if sieve[i]]


# 2.   Run your algorithm on the specified inputs in the main function to make sure your algorithm works.
# You may modify the main function to try other numbers but make sure to change it back, and do not
# turn in a modified main function.
# 

# In[10]:


if __name__ == '__main__':
  print("#######################################")
  print("Prime Number Generation")
  print("#######################################")
  print()

  prime_gen_test_1 = 42
  prime_gen_test_1_ans = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
  print("Test Case 1: Prime Numbers Up To:", prime_gen_test_1)
  print("Test Case 1 (Your Answer):", prime_gen(prime_gen_test_1))
  print("Test Case 1 (Correct Answer):", prime_gen_test_1_ans)
  print("Test Case 1:", ("# PASSED! #" if prime_gen(prime_gen_test_1) == prime_gen_test_1_ans  else "# INCORRECT #"))
  print()
  prime_gen_test_2 = 314
  prime_gen_test_2_ans = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
  47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127,
  131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
  211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283,
  293, 307, 311, 313]
  print("Test Case 2: Prime Numbers Up To:", prime_gen_test_2)
  print("Test Case 2 (Your Answer):", prime_gen(prime_gen_test_2))
  print("Test Case 2 (Correct Answer):", prime_gen_test_2_ans)
  print("Test Case 2:", ("# PASSED! #" if prime_gen(prime_gen_test_2) == prime_gen_test_2_ans  else "# INCORRECT #"))
  print()
  prime_gen_test_3 = 884
  prime_gen_test_3_ans = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
  31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109,
  113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197,
  199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283,
  293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389,
  397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487,
  491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599,
  601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,
  701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811,
  821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883]
  print("Test Case 3: Prime Numbers Up To:", prime_gen_test_3)
  print("Test Case 3 (Your Answer):", prime_gen(prime_gen_test_3))
  print("Test Case 3 (Correct Answer):", prime_gen_test_3_ans)
  print("Test Case 3:", ("# PASSED! #" if prime_gen(prime_gen_test_3) == prime_gen_test_3_ans  else "# INCORRECT #"))
  print("---------------------------------------")



# Once you have completed your code, run the following cell to test your work. **DO NOT ALTER!!**
# 
# # Question 4: Functions
# 
# In the following sections we will assess the properties of an inputted function. The function will be inputted in 3 parts:
# 
# - A list of values in domain, e.g.
# ```
# # domain = [1,2,3,4]
# ```
# - A list of values of the codomain, e.g.
# ```
# # co_domain = [1,2,3,4,5,6,7]
# ```
# - A dictionary of the function mapping between the domain and the co-domain, e.g.
# ```
# # mapping = {
#     1: 2,
#     2: 3,
#     3: 1,
#     4: 3
# }
# ```
# 
# (a) Write a function to check whether an inputted function is onto. The Python function should be called
# is_onto, should take in the 3 arguments representing the function (domain, co-domain, and mapping),
# and should return a boolean, **True** or **False**.
# 

# In[11]:


def is_onto(domain, co_domain, mapping):
    # Every co-domain element must be mapped to by at least one domain element
    mapped_values = set(mapping[x] for x in domain)
    return set(co_domain) == mapped_values


# (b) Write a function to check whether an inputted function is one-to-one. The python function should be called ```is_one_to_one```, should take in the 3 arguments representing the function (domain, co-domain, and mapping), and should return a boolean, **True** or **False**.
# 

# In[12]:


"""(b) Write a function to check whether an inputted function is one-to-one. The python function should be called ```is_one_to_one```, should take in the 3 arguments representing the function (domain, co-domain, and mapping), and should return a boolean, **True** or **False**."""
def is_one_to_one(domain, co_domain, mapping):
    # No two domain elements map to the same co-domain element
    mapped_values = [mapping[x] for x in domain]
    return len(mapped_values) == len(set(mapped_values))



# (c) Write a function to check whether an inputted function is bijective. (Hint: you can utilize your other functions in writing this one!) The python function should be called ```is_bijective```, should take in the 3 arguments representing the function (domain, co-domain, and mapping) and should return a boolean, **True** or **False**.
# 

# In[13]:


"""(c) Write a function to check whether an inputted function is bijective. (Hint: you can utilize your other functions in writing this one!) The python function should be called ```is_bijective```, should take in the 3 arguments representing the function (domain, co-domain, and mapping) and should return a boolean, **True** or **False**."""
def is_bijective(domain, co_domain, mapping):
    # Bijective = both onto AND one-to-one
    return is_onto(domain, co_domain, mapping) and is_one_to_one(domain, co_domain, mapping)



# Once you have completed the code, run the following cell to test your work. **DO NOT ALTER**!
# 

# In[15]:


"""Once you have completed the code, run the following cell to test your work. **DO NOT ALTER**!"""
if __name__ == '__main__':
  print("#######################################")
  print("Question 4: Functions")
  print("#######################################")
  print()

  example_1 = [[1 ,2 ,3 ,4],[1,2,3,4,5,6,7],{1:2, 2:3, 3:1,4:3}] #not anything
  example_2 = [[1 ,2 ,3 ,4],[1,2,3,4,5,6,7],{1:2, 2:3, 3:1,4:5}] #one to one (nothing else)
  example_3 = [[1 ,2 ,3 ,4],[1,2,3],{1:2, 2:3, 3:1,4:3}] #onto (nothing else)
  example_4 = [[1 ,2 ,3 ,4],[1,2,3,4],{1:2, 2:3, 3:1,4:4}] #bijective

  print("---------------------------------------")
  print("\'is_onto\' Tests")
  print("---------------------------------------")

  is_onto_tests = [example_1, example_2, example_3, example_4]
  is_onto_answers = [False, False, True, True]

  for count, test in enumerate(is_onto_tests):
    if (is_onto(is_onto_tests[count][0],is_onto_tests[count][1],
                is_onto_tests[count][2]) == is_onto_answers[count]):
      passed = 'PASSED!'
    else:
      passed = "FAILED!"

    print("Test #{}: {}".format(count + 1, passed))
    print(f'Correct Answer: {is_onto_answers[count]}')
    print(f'Your Answer: {is_onto(is_onto_tests[count][0], is_onto_tests[count][1],is_onto_tests[count][2])}')

  print("---------------------------------------")
  print("\'is_one_to_one\' Tests")
  print("---------------------------------------")

  is_one_to_one_tests = [example_1, example_2, example_3, example_4]
  is_one_to_one_answers = [False, True, False, True]

  for count, test in enumerate(is_one_to_one_tests):
    if (is_one_to_one(is_one_to_one_tests[count][0],is_one_to_one_tests[count][1], is_one_to_one_tests[count][2]) == is_one_to_one_answers[count]):
      passed = 'PASSED!'
    else:
      passed = "FAILED!"

    print("Test #{}: {}".format(count + 1, passed))
    print(f'Correct Answer: {is_one_to_one_answers[count]}')
    print(f'Your Answer: {is_one_to_one(is_one_to_one_tests[count][0],is_one_to_one_tests[count][1],is_one_to_one_tests[count][2])}')

  print("---------------------------------------")
  print("\'is_bijective\' Tests")
  print("---------------------------------------")

  is_bijective_tests = [example_1, example_2, example_3, example_4]
  is_bijective_answers = [False, False, False, True]

  for count, test in enumerate(is_onto_tests):
    if (is_bijective(is_bijective_tests[count][0],is_bijective_tests[count][1],is_bijective_tests[count][2]) == is_bijective_answers[count]):
      passed = 'PASSED!'
    else:
      passed = "FAILED!"

    print("Test #{}: {}".format(count + 1, passed))
    print(f'Correct Answer: {is_bijective_answers[count]}')
    print(f'Your Answer: {is_bijective(is_bijective_tests[count][0],is_bijective_tests[count][1],is_bijective_tests[count][2])}')



# # Question 5: Goldbach's Conjecture
# 
# 
# As seen in class, the Goldbach conjecture is still not proven or disproven and can be stated as follows:
# Every even integer greater than two can be written as the sum of two prime numbers.
# 
# (a) Write a function ```check_goldbach(n)``` that verifies the conjecture for a given (potentially large) even integer $n$ sent as a parameter to the function. The function should return the two primes that sum
# up to $n$, in the form of a list with two entries of type ```int```. As before, **make sure your return types are correct, or your code will receive zero points.** You may assume that your input will
# be a positive even integer. Also note that Goldbach decompositions are not unique, so there may be
# more than one correct answer for a given integer n (any satisfying sum will be correct).
# **Hint:**
# * use your function ```prime_gen(n)```
# 
# 

# In[16]:


def check_goldbach(n):
    primes = prime_gen(n)
    prime_set = set(primes)
    for p in primes:
        complement = n - p
        if complement in prime_set:
            return [p, complement]



# (b) Run your algorithm on the specified inputs in the main function to make sure your algorithm works.
# You may modify the main function to try other numbers but make sure to change it back, and do not turn in a modified main function.
# 

# In[17]:


if __name__ == '__main__':
  print("#######################################")
  print("Goldbach's Conjecture")
  print("#######################################")
  print()
  goldbach_test_1 = 8
  goldbach_test_1_ans = [3, 5]
  student_ans = check_goldbach(goldbach_test_1)
  print("Test Case 1: 2 Primes For:", goldbach_test_1)
  print("Test Case 1 (Your Answer):", check_goldbach(goldbach_test_1))
  print("Test Case 1 (A Correct Answer):", goldbach_test_1_ans)
  print("Test Case 1:", ("# PASSED! #" if student_ans[0] + student_ans[1] == goldbach_test_1  else "# INCORRECT #"))
  print()
  goldbach_test_2 = 482
  goldbach_test_2_ans = [3, 479]
  student_ans = check_goldbach(goldbach_test_2)
  print("Test Case 2: 2 Primes For:", goldbach_test_2)
  print("Test Case 2 (Your Answer):", check_goldbach(goldbach_test_2))
  print("Test Case 2 (A Correct Answer):", goldbach_test_2_ans)
  print("Test Case 2:", ("# PASSED! #" if student_ans[0] + student_ans[1] == goldbach_test_2  else "# INCORRECT #"))
  print()
  goldbach_test_3 = 1152
  goldbach_test_3_ans = [23, 1129]
  student_ans = check_goldbach(goldbach_test_3)
  print("Test Case 3: 2 Primes For:", goldbach_test_3)
  print("Test Case 3 (Your Answer):", check_goldbach(goldbach_test_3))
  print("Test Case 3 (A Correct Answer):", goldbach_test_3_ans)
  print("Test Case 3:", ("# PASSED! #" if student_ans[0] + student_ans[1] == goldbach_test_3  else "# INCORRECT #"))
  print("---------------------------------------")

