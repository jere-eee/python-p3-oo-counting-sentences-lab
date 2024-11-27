#!/usr/bin/env python3

class MyString:
  def __init__(self, value='') -> None:
    self.value = value
    
  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, val):
    if isinstance(val, str):
      self._value = val
    else:
      print('The value must be a string.')
    
  def is_sentence(self):
    if self.value[-1] == ".":
      return True
    else:
      return False
  
  def is_question(self):
    if self.value[-1] == "?":
      return True
    else:
      return False
    
  def is_exclamation(self):
    if self.value[-1] == "!":
      return True
    else:
      return False
  
  def count_sentences(self):
    count = 0
    for w in self.value.split(" "):
      if w and w[-1] == ".": 
        count += 1
      elif w and w[-1] == "?":
        count += 1
      elif w and w[-1] == "!":
        count += 1
    return count     
