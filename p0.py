'''Autores:
Juan Felipe Caraballo 201923741
Juliana Ahumada 201921471'''




def llaves_y_parentesis_balanceados(texto):
    pila = []
    for caracter in texto:
        if caracter in '([{':
            pila.append(caracter)
        elif caracter in ')]}':
            if not pila:
                return False
            ultimo_caracter = pila.pop()
            if (caracter == ')' and ultimo_caracter != '(') or \
               (caracter == ']' and ultimo_caracter != '[') or \
               (caracter == '}' and ultimo_caracter != '{'):
                return False

    return len(pila) == 0



def check_instruction(line, dictionary,check):
    line1 = ""
    for m in range(len(line)):
        if line[m] == '{' and m > 0:
            line1 += ';'
        else:
            line1 += line[m]

    newLine = ""
    for x in line1:
        if x == '{' or x == '}':
            continue
        else:
            newLine += x
    #print(newLine.strip())


    instructions = list(map(str.strip, newLine.split(';')))
    instructions = [x for x in instructions if x.strip() != '']
    #print(instructions)

    for x in instructions:
        #En caso de que sea un while o un if

        if 'while' in x or 'if' in x:
            startIndex = x.index('(')+1
            endIndex = x.index(')')+1
            nameOfProc = x[startIndex:endIndex][0:x[startIndex:endIndex].index('(')].strip().lower()
            parameters = list(map(str.strip, x[startIndex:endIndex][x[startIndex:endIndex].index('(')+1:x[startIndex:endIndex].index(')')].split(',')))
            if nameOfProc not in dictionary:
                check[0] = False

            else:
                if not('can' in dictionary[nameOfProc]['accepted_types']):
                    check[0] = False

                else:
                    for w in parameters:
                        if w not in dictionary and not(w.isdigit()):
                            check[0] = False

                        if w in dictionary:
                            if not(dictionary[nameOfProc]['type'] in dictionary[w]['accepted_types']):
                                check[0] = False
                        elif w.isdigit():
                            continue
                        else:
                            check[0] = False
        else:

            nameOfProc = x[0:x.index('(')].strip().lower()
            parameters = list(map(str.strip,x[x.index('(')+1:x.index(')')].split(',')))
            parameters = [x for x in parameters if x.strip() != '']

            if nameOfProc not in dictionary and nameOfProc != '(null)':
                check[0] = False

            else:
                for w in parameters:
                        if w not in dictionary and not(w.isdigit()):
                            check[0] = False

                        if w in dictionary or w.isdigit():
                            if not w.isdigit():
                                if not(dictionary[nameOfProc]['type'] in dictionary[w]['accepted_types']):
                                    check[0] = False


                        else:
                            check[0] = False




def add_variables_to_dictionary(line, dictionary, type):
    variable_name_and_value = list(line.split(" "))
    dictionary[variable_name_and_value[0]] = {'type':type, 'accepted_types':['procediment', 'instruction', 'balloonsOrChips', 'move', 'skip', 'C', 'c','b','B'] }

def add_procs_to_dictionary(line, dictionary):
    index_of_parenthesis1 = line.index('(')
    index_of_parenthesis2 = line.index(')')

    proc_name = line[0:index_of_parenthesis1].strip()
    dictionary[proc_name] = {'type':"procediment", 'accepted_types':['procediment']}
    parameters = list(map(str.strip, line[index_of_parenthesis1+1:index_of_parenthesis2].split(',') ))
    for k in parameters:
        dictionary[k] = {'type':'variable', 'accepted_types':['procediment', 'instruction', 'balloonsOrChips', 'move', 'skip', 'C', 'c','b','B']}


myDict = {
    'move': {'type':'move', 'accepted_types' :['procediment','can']},
    'turn': {'type':"turn", 'accepted_types':['procediment','can'] },
    'face': {'type':"face", 'accepted_types':['procediment','can'] },
    'C':{'type':'C', 'accepted_types':['procediment','can']},
    'c':{'type':'c', 'accepted_types':['procediment','can']},
    'b':{'type':'b', 'accepted_types':['procediment','can']},
    'B':{'type':'B', 'accepted_types':['procediment','can']},
    'skip':{'type': "skip", 'accepted_types': ['procediment','can']},
    '(null)': {'type':"instruction", 'accepted_types':['procediment','can'] },
    'jump':{'type':'jump', 'accepted_types':['procediment', 'can']},
    
    #preguntar esto
    'if':  {'type':"conditional", 'accepted_types':['procediment'] },
    'while':  {'type':"loop", 'accepted_types':['procediment'] },
    'repeat':  {'type':"instruction", 'accepted_types':['procediment'] },
   
    'left': {'type': "directionT1", 'accepted_types': ['turn', 'move', 'skip']},
    'right': {'type': "directionT1", 'accepted_types': ['turn', 'move','skip']},
    'around':{'type': "directionT1", 'accepted_types': ['turn']},
    'front': {'type': "directionT2", 'accepted_types': ['move','skip']},
    'back': {'type': "directionT2", 'accepted_types': ['move','skip']},
    'north': {'type': "directionT3", 'accepted_types': ['face', 'facing', 'move', 'skip' ]},
    'south': {'type': "directionT3", 'accepted_types': ['face', 'facing', 'move', 'skip' ]},
    'west': {'type': "directionT3", 'accepted_types': ['face', 'facing', 'move', 'skip' ]},
    'east': {'type': "directionT3", 'accepted_types': ['face', 'facing', 'move', 'skip' ]},
    
    'balloons': {'type': "balloons", 'accepted_types': ['b', 'B']},
    'chips': {'type': "chips", 'accepted_types': ['C','c']},
    #unir esto
    'facing': {'type':"facing", 'accepted_types':['conditional', 'loop', 'not_condition']},
    #qué hacemos con el can
    'can': {'type':'can', 'accepted_types':['conditional','loop', 'not_condition']},
    'not': {'type':"not_condition", 'accepted_types':['conditional', 'loop', 'not_condition']},
    'blocked?': {'type': 'condition', 'accepted_types': ['conditional', 'loop', 'not_condition']},
    'can-put?': {'type': 'condition', 'accepted_types': ['conditional', 'loop', 'not_condition']},
    'can-pick?': {'type': 'condition', 'accepted_types': ['conditional', 'loop', 'not_condition']},
    'can-move?': {'type': 'condition', 'accepted_types': ['conditional', 'loop', 'not_condition']},
    'isZero?': {'type': 'condition', 'accepted_types': ['conditional', 'loop', 'not_condition']},
}


archivoALeer = 'p.txt'

# Open the input file for reading
with open(archivoALeer, 'r') as input_file:
    # Read the content of the input file
    content = input_file.read()

# Create a list to store the separated lines
separated_lines = []

# Initialize an empty line
current_line = ""

# Iterate through each character in the content
for char in content:
    if char == '{':
        # If '{' is encountered, add the current line to the list and reset it
        if current_line.strip():
            separated_lines.append(current_line.strip())
        separated_lines.append("{")
        current_line = ""
    elif char == '}':
        # If '}' is encountered, add it as a separate line
        if current_line.strip():
            separated_lines.append(current_line.strip())
        separated_lines.append("}")
        current_line = ""
    else:
        # Otherwise, add the character to the current line
        current_line += char

# Add any remaining content as a separate line
if current_line.strip():
    separated_lines.append(current_line.strip())

# Open the output file for writing
with open('output.txt', 'w') as output_file:
    # Write each separated line to the output file, skipping empty lines
    for line in separated_lines:
        if line.strip():  # Check if the line is not empty
            output_file.write(line + '\n')

input_file_path = "output.txt"
output_file_path = "blanklines.txt"

with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    # Iterate through each line in the input file
    for line in input_file:
        # Strip leading and trailing whitespace from the line
        stripped_line = line.strip()

        # Check if the line is not empty after stripping
        if stripped_line:
            # If the line is not empty, write it to the output file
            output_file.write(line)


f = open("./blanklines.txt", "r")

linea = f.readline()

check = []
check.append(True)

while linea.strip() != "":


    if linea[0:6].strip().lower() == "defvar":

        add_variables_to_dictionary(linea[6:len(linea)].strip().lower(), myDict, 'variable')

        linea = f.readline();

#defun en vez de defProc
    elif linea[0:7].strip().lower() == "defun":
        add_procs_to_dictionary(linea[7:len(linea)].strip().lower(), myDict)

        linea = f.readline();

#cambio de corchetes
        lines_in_block_of_commands = ""
        while linea.strip() != "}" :
            lines_in_block_of_commands += linea.strip()
            linea = f.readline();
        while linea.strip() == "}":
            lines_in_block_of_commands += linea.strip()
            linea = f.readline();

        check_instruction(lines_in_block_of_commands, myDict, check)

    elif linea.strip().lower() == 'else':
        linea = f.readline();

#cambio de bloques {} a ()
        lines_in_block_of_commands = ""
        while linea.strip() != "}" :
            lines_in_block_of_commands += linea.strip()
            linea = f.readline();
        while linea.strip() == "}":
            lines_in_block_of_commands += linea.strip()
            linea = f.readline();
        check_instruction(lines_in_block_of_commands, myDict, check)

    elif linea.strip() == '{':
        linea = f.readline();

        lines_in_block_of_commands = ""
        while linea.strip() != "}" :
            lines_in_block_of_commands += linea.strip()
            linea = f.readline();
        while linea.strip() == "}":
            lines_in_block_of_commands += linea.strip()
            linea = f.readline();
        check_instruction(lines_in_block_of_commands, myDict, check)

    else:
        linea = f.readline();

with open('blanklines.txt', 'r') as archivo:
            contenido = archivo.read()
            if not llaves_y_parentesis_balanceados(contenido):
                check[0] = False

if check[0]:
    print("YES")
else:
    print('NO')