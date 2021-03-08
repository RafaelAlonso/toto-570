from termcolor import colored

def get_my_name():
  return "Rafa"

def who_am_i():
  print(colored(f"Hello my name is {get_my_name()}", "blue"))

