import re
import sys
import vim

# Get values from VIM script
findInFile = vim.eval('g:currentFileFindFunctions').replace("'", "")
print("Find js functions in: " + findInFile + "\n\n")

# Vanilla js
vanillaJsRegex = re.compile(r"function( )?(.)*[(]{1}.*[)]{1}.*[{]")
vanillaJsMatches = []

# Anonymous functions
es6Regex = re.compile(r".*( )?=>( )?")
es6Matches = []

# Class functions
classRegex = re.compile(r"^(?!default|function|return|var|case|delete|if|switch|void|catch|do|in|this\.|while|const|else|insnceof|throw|with|continue|finally|let|try|debugger|for|new|typeof|function|export)[a-zA-Z]( )?(.)*[(]*[)].*[{]")
classMatches = []

class Match:
  def __init__(self, number, line):
    self.number = number
    self.line = line

  def __repr__(self):
    return str(self.number) + ": " + str(self.line)


# open the files
with open(findInFile, "r") as inputFile:
    with open("OutputLineNumbers", "w") as outputLineNumbers:
        # loop through each line in corpus
        for line_i, line in enumerate(inputFile, 1):
            # check if we have a regex match
            if vanillaJsRegex.search(line.strip()):
                vanillaJsMatches.append(Match(line_i, line.strip()))

            if es6Regex.search(line.strip()):
                es6Matches.append(Match(line_i, line.strip()))

            if classRegex.search(line.strip()):
                classMatches.append(Match(line_i, line.strip()))

print("\n--- Vanilla js ---")
if int(len(vanillaJsMatches)) > 0:
  print("\n".join(str(p) for p in vanillaJsMatches))
else:
  print("No found functions")

print("\n--- Class functions ---")
if int(len(classMatches)) > 0:
  print("\n".join(str(p) for p in classMatches))
else:
  print("No found functions")

print("\n\n--- ES6 ---")
if int(len(es6Matches)) > 0:
  print("\n".join(str(p) for p in es6Matches))
else:
  print("No found functions...")
