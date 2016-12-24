easy_mad_lib = """A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions."""
easy_answers = ["test1", "test2", "test3", "test4"]

def select_game_difficulty():
  prompt = "Please select a game difficulty by typing it in!\n"
  prompt += "Possible choices include easy, medium and hard.\n"
  equivalents_difficulty = { x: "easy" for x in ("easy", "e", "1", "1.") }
  equivalents_difficulty.update({ y: "medium" for y in ("medium", "m", "2", "2.") })
  equivalents_difficulty.update({ z: "hard" for z in ("hard", "h", "3", "3.") })
  chosen_difficulty = raw_input(prompt).lower()
  while chosen_difficulty not in equivalents_difficulty:
    print "That's not an option!"
    chosen_difficulty = raw_input(prompt).lower()

  print "You've chosen " + str(equivalents_difficulty[chosen_difficulty]) + "!\n"
  return equivalents_difficulty[chosen_difficulty]


def get_mad_lib_and_answers(difficulty):
  if difficulty == "easy":
    return (easy_mad_lib, easy_answers)
  elif difficulty == "medium":
    return (medium_mad_lib, medium_answers)
  elif difficulty == "hard":
    return (hard_mad_lib, hard_answers)
  else:
    print "Error!  That isn't a difficulty!"


def ask_question(mad_lib, blank_num, answers, max_attempts = 4):
  attempts_left = max_attempts
  to_replace = "___" + str(blank_num) + "___"
  prompt = make_display(mad_lib, to_replace, attempts_left, max_attempts)
  user_guess = raw_input(prompt).lower()
  while user_guess != answers.lower() and attempts_left > 1:
    attempts_left -= 1
    prompt = make_display(mad_lib, to_replace, attempts_left, max_attempts)
    user_guess = raw_input(prompt).lower()

  if attempts_left > 1:
    print "\nCorrect!\n"
    return (mad_lib.replace(to_replace, answers), blank_num + 1)

  return (None, blank_num + 1)


def make_display(current_mad_lib, to_replace, attempts_left, max_attempts):
  prompt = "\nThe current paragraph reads as such:\n{}\n\n"
  prompt += "What should be substituted in for {}? "
  prompt = prompt.format(current_mad_lib, to_replace)
  if attempts_left == max_attempts:
    return prompt
  new_prompt = "That isn't the correct answer!  "
  if attempts_left == max_attempts:
    return prompt
  new_prompt = "That isn't the correct answer!  "
  if attempts_left > 1:
    new_prompt += "Let's try again; you have {} trys left!\n\n"
  else:
    new_prompt += 'You only have {} try left!  Make it count!\n\n'
  return new_prompt.format(attempts_left) + prompt


def find_max_guesses():
  print "You'll get 5 guesses per problem!"
  return 5


def play_game():
  difficulty = select_game_difficulty()
  mad_lib, answers = get_mad_lib_and_answers(difficulty)
  max_guesses = find_max_guesses()
  current_blank = 1
  while current_blank <= len(answers):
    mad_lib, current_blank = ask_question(mad_lib, current_blank, answers[current_blank - 1], max_guesses)
    if mad_lib is None:
      return False

  print mad_lib + "\nYou won!\n"
  return True

play_game()
