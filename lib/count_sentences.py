#!/usr/bin/env python3

class MyString:
  def __init__(self, value):
    if isinstance(value, str):
      self._value = value
    else:
      print("The value must be a string.")
  
  def is_sentence(self):
    if (self._value.endswith(".")):
      print(True)
      return True
    else:
      print(False)
      return False 
  
  def is_question(self):
    if (self._value.endswith("?")):
      print(True)
      return True
    else:
      print(False)
      return False  
  
  def is_exclamation(self):
    if (self._value.endswith("!")):
      print(True)
      return True
    else:
      print(False)
      return False  
  
  def count_sentences(self):
        # Replace periods with an empty string and count the occurrences
        sentence_count = self._value.split(".").count(".") and self._value.split("!").count("!") and self._value.split("?").count("?")
        return sentence_count

# sentence = MyString("Hello World?")
# # sentence_result = sentence.is_sentence()
# # sentence_result = sentence.is_question()
# sentence_result = sentence.is_exclamation()
#print(sentence_result)

string = MyString("This is a string! It has three sentences. Right?")
sentence_count = string.count_sentences()
print(sentence_count)



