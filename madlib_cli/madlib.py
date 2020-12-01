import re

"""
read_template function that takes in a path to text file and returns a stripped string of the file’s contents.
"""
def read_template(file_path):
    with open(file_path, "r") as file:
        text = file.read()
    return(text)

"""
parse function that takes in a template string and returns a string with language parts removed,
and a separate list of those language parts.
"""
def parse(text):
    placeholders = re.findall(r"\{(.*?)\}", text)
    words = re.sub(r"\{(.*?)\}", "$", text)
    return words, placeholders

"""
merge function that takes in a “bare” template and a list of user entered language parts, 
and returns a string with the language parts inserted into the template.
"""
def  merge(words, user_words):
    for word in user_words:
        words = words.replace("$", word, 1)
    return(words)


if __name__ == "__main__":
    text = (read_template("assets/text.txt"))
    words, placeholders = parse(text)
    print("**************************************")
    print("**          THIS IS MADLIB          **")
    print("**************************************")
    print("--            LET'S PLAY!           --")
    print("--------------------------------------")
    user_words = []
    for placeholder in placeholders:
        user_words.append(input(f"Enter a {placeholder}: "))
    game_result = merge(words, user_words)
    f = open("assets/game_results.txt", "w")
    f.write(game_result)
    print("********YOUR MADLIBS says:************")
    print(game_result)

  