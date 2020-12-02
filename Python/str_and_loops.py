sent_original = input("Type a simple sentence and press enter.")
sent_words = sent_original.split() # splits
final_list = [] # creates the final list that each letter will go into

for word in sent_words: # cycles through each word in the list of words
  word += "-" # adds a hyphen to the end of each word
  split_letters = list(word) # splits each word into a list of letters
  for letter in split_letters: # cycles through each letter in each list of letters
    final_list.append(letter) # adds each letter to the final list

for thing in final_list:
  print(thing) # prints everything that has been put into the final list
