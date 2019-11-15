#Takes in inputs of instructions. Only prints instructions where simon says so.

numberInputs = input("How many instructions: ")
instructions = []

for x in range(numberInputs):

    words = raw_input("Enter instruction: ").split()

    #Check if instruction has 'Simon Says'
    if words[0].lower() == "simon" and words[1].lower() == "says":

        #Remove 'Simon Says'
        for y in range(2):
            words.pop(0)

        instruction = " ".join(words)
        instructions.append(instruction)

#Print valid instructions
for x in instructions:
    print(x)
