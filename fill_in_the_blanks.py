EASY_MAD_LIB = """HyperText Markup Language (___1___) is the standard markup
language for creating web pages and web applications. With Cascading Style
Sheets (___2___), and ___3___, it forms a triad of cornerstone technologies
for the World Wide Web. Web browsers receive ___1___ documents from a webserver
or from local storage and render them into multimedia web pages. ___1___
describes the structure of a web page semantically and originally included cues
for the appearance of the ___4___."""
EASY_ANSWERS = ["HTML", "CSS", "JavaScript", "document"]

MEDIUM_MAD_LIB = """___1___ is a widely used high-level, general-purpose,
interpreted, dynamic programming language. Its design philosophy emphasizes
code readability, and its syntax allows programmers to express concepts in
fewer lines of code than possible in languages such as C++ or Java. The
language provides constructs intended to enable writing ___2___ programs on
both a small and large scale. ___1___ supports multiple programming paradigms,
including object-___3___, imperative, ___4___ programming, and procedural
styles. It features a dynamic type system and automatic memory management and
has a large and comprehensive standard library."""
MEDIUM_ANSWERS = ["Python", "clear", "oriented", "functional"]

HARD_MAD_LIB = """A video ___1___ is an electronic ___1___ that involves human
interaction with a user interface to generate visual feedback on a video
device such as a ___2___ screen or ___3___ monitor. The word video in
video ___1___ traditionally referred to a raster display device, but as of the
2000s, it implies any type of display device that can produce two or
three-dimensional images. Some theorists categorize video games as
an ___4___ form, but this designation is controversial."""
HARD_ANSWERS = ["game", "TV", "computer", "art"]


def select_game_difficulty():
    """Prompts user for difficulty level, repeats until the user chooses one.
    Function returns a string: either 'easy', 'medium', or 'hard'."""
    prompt = "Please select a game difficulty by typing it in!\n"
    prompt += "Possible choices include easy, medium and hard.\n"
    equivalents_difficulty = {x: "easy" for x in ("easy", "e", "1", "1.")}
    equivalents_difficulty.update(
        {y: "medium" for y in ("medium", "m", "2", "2.")}
    )
    equivalents_difficulty.update(
        {z: "hard" for z in ("hard", "h", "3", "3.")}
    )
    chosen_difficulty = input(prompt).lower()
    while chosen_difficulty not in equivalents_difficulty:
        print("That's not an option!")
        chosen_difficulty = input(prompt).lower()
    print(
        "You've chosen " +
        str(equivalents_difficulty[chosen_difficulty]) +
        "!\n"
    )
    return equivalents_difficulty[chosen_difficulty]


def get_mad_lib_and_answers(difficulty):
    """Takes a difficulty ('easy', 'medium' or 'hard').
    Returns mad_lib string and answers list."""
    if difficulty == "easy":
        return (EASY_MAD_LIB, EASY_ANSWERS)
    elif difficulty == "medium":
        return (MEDIUM_MAD_LIB, MEDIUM_ANSWERS)
    elif difficulty == "hard":
        return (HARD_MAD_LIB, HARD_ANSWERS)
    else:
        print("Error! That isn't a difficulty!")


def ask_question(mad_lib, blank_num, answers, max_attempts=4):
    """Takes the current mad_lib (str), current_question (int), and
    answer (str). Returns the partially answered madlib (or None if the user
    takes too many guesses) and the number of the next blank."""
    limit_attempts = 1
    attempts_left = max_attempts
    to_replace = "___" + str(blank_num) + "___"
    prompt = make_display(mad_lib, to_replace, attempts_left, max_attempts)
    user_guess = input(prompt).lower()
    while user_guess != answers.lower() and attempts_left > limit_attempts:
        attempts_left -= 1
        prompt = make_display(mad_lib, to_replace, attempts_left, max_attempts)
        user_guess = input(prompt).lower()
    if attempts_left > limit_attempts:
        print("\nCorrect!\n")
        return (mad_lib.replace(to_replace, answers), blank_num + 1)
    return (None, blank_num + 1)


def make_display(current_mad_lib, to_replace, attempts_left, max_attempts):
    """Returns a string to be printed out to the user based on the user's
    current progress in the game."""
    prompt = "\nThe current paragraph reads as such:\n{}\n\n"
    prompt += "What should be substituted in for {}? "
    prompt = prompt.format(current_mad_lib, to_replace)
    limit_attempts = 1
    if attempts_left == max_attempts:
        return prompt
    new_prompt = "That isn't the correct answer! "
    if attempts_left == max_attempts:
        return prompt
    new_prompt = "That isn't the correct answer! "
    if attempts_left > limit_attempts:
        new_prompt += "Let's try again; you have {} trys left!\n\n"
    else:
        new_prompt += "You only have {} try left!  Make it count!\n\n"
    return new_prompt.format(attempts_left) + prompt


def find_max_guesses():
    """Number of attempts the user has to win."""
    print("You'll get 5 guesses per problem!")
    return 5


def play_game():
    """Plays the reverse mad_libs game.
    Returns True if the user wins, False otherwise."""
    difficulty = select_game_difficulty()
    mad_lib, answers = get_mad_lib_and_answers(difficulty)
    max_guesses = find_max_guesses()
    current_blank = 1
    while current_blank <= len(answers):
        mad_lib, current_blank = ask_question(
            mad_lib, current_blank, answers[current_blank - 1], max_guesses
        )
        if mad_lib is None:
            return False
    print(mad_lib + "\nYou won!\n")
    return True


play_game()
