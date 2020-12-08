import random
import copy

# This script will read in a csv file of intermediate vectors for a neural net
# It will then generate two specific exemplars by randomly 'flipping' units in the vector
# Finally, save these new vectors to a file called 'specific_exemplars.csv'

# Takes in one vector, returns two vectors--each with different units flipped
def randomize(input_vector):
    unit1 = random.randint(0, 31)

    unit2 = random.randint(0, 31)
    while (unit2 == unit1):
        unit2 = random.randint(0, 32)
    
    unit3 = random.randint(0, 31)
    while (unit3 == unit1 or unit3 == unit2):
        unit3 = random.randint(0,31)
    
    unit4 = random.randint(0, 31)
    while (unit4 == unit1 or unit4 == unit2 or unit4 == unit3):
        unit4 = random.randint(0, 31)
        

    out_vec1 = copy.deepcopy(input_vector)
    out_vec2 = copy.deepcopy(input_vector)

    #flip two units for first exemplar
    if (out_vec1[unit1] == -1):
        out_vec1[unit1] = 1
    else:
        out_vec1[unit1] = -1

    if (out_vec1[unit2] == -1):
        out_vec1[unit2] = 1
    else:
        out_vec1[unit2] = -1

    #flip two units for second exemplar
    if (out_vec2[unit3] == -1):
        out_vec2[unit3] = 1
    else:
        out_vec2[unit3] = -1

    if (out_vec2[unit4] == -1):
        out_vec2[unit4] = 1
    else:
        out_vec2[unit4] = -1

    return (out_vec1, out_vec2)


def generate_exemplars(file_handle):

    write_out = open('specific exemplars old.csv', 'w')

    lines = file_handle.readlines()
    i = 1
    for line in lines:
        line_data = line.split(',')

        #convert the string values to integers
        for k in range(len(line_data)):
            line_data[k] = int(line_data[k])
        
        print(line_data)
        exemplar1, exemplar2 = randomize(line_data)

        print_str_a = str(i) + 'a'
        print_str_b = str(i) + 'b'

        for j in range(len(exemplar1)):
            print_str_a = print_str_a + ', ' + str(exemplar1[j])
        print_str_a += '\n'

        for j in range(len(exemplar2)):
            print_str_b = print_str_b + ', ' + str(exemplar2[j])
        print_str_b += '\n'

        print(print_str_a)
        print(print_str_b)
        write_out.write(print_str_a)
        write_out.write(print_str_b)

        i += 1
    write_out.close()

# Driver Code  
if __name__ == "__main__":
    filename = "32_orthogonal_vectors_old_csv.csv"
    f = open(filename)
    generate_exemplars(f)
    f.close()