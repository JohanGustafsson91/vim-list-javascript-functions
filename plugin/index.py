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
            if vanillaJsRegex.search( line ):
                vanillaJsMatches.append(Match(line_i, line.strip()))
            elif es6Regex.search( line ):
                es6Matches.append(Match(line_i, line.strip()))



print("\n--- Vanilla js ---")
if int(len(vanillaJsMatches)) > 0:
  print("\n".join(str(p) for p in vanillaJsMatches))
else:
  print("No found functions")

print("\n\n--- ES6 ---")
if int(len(es6Matches)) > 0:
  print("\n".join(str(p) for p in es6Matches))
else:
  print("No found functions...")
