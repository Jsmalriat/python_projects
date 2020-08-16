def main():
    codewords = int(amount_of_codewords())
    code = []
    code = list_of_codewords(code, codewords)
    print(code)
    min_dist = int(mindist(code, codewords))
    received_codeword = str(rec_codeword(code))
    errors_detected = []
    errors_detected = error_detect(received_codeword, code, min_dist, codewords)
    correct_codeword = error_correct(received_codeword, code, min_dist, codewords)
    print(f"Errors were found at indicies {errors_detected}, and the corrected codeword would be {correct_codeword}")

def amount_of_codewords():
    x = int(0)
    while x < 1:
        codewords = int(input("""
How many codewords will this code contain? 
=> """))
        if (codewords <= 0):
            print("Number of codewords must be a positive integer.")
        else:
            return codewords 

def list_of_codewords(code, codewords):
    print("\nType each of the codewords and press Enter until all codewords have been entered.")
    binary = {'0', '1'}
    x = int(0)
    while (x < 1):
        cword1 = str(input("=> "))
        string = set(cword1)
        if (string == binary) or (string == {'1'}) or (string == {'0'}):
            length = int(len(cword1))
            code.append(cword1)
            x = (x + 1)
        else:
            print("Codewords must be in a binary format.")
    y = int(0)
    while y < (codewords - 1):
        cword = str(input("=> "))
        string = set(cword)
        if len(cword) != length:
            print("""I'm sorry, all codewords must be the same length in order to determine minimum distance. Try again.""")
        else:
            if (string == binary) or (string == {'1'}) or (string == {'0'}):
                if cword == cword1:
                    print("Codewords must be unique.")
                else:
                    length = int(len(cword))
                    code.append(cword)
                    y = int(y + 1)
            else:
                print("Codewords must be in a binary format.")
    return code
    
def mindist(code, codewords):
    min_dist_counter = int(30)
    for i in range(codewords):
        current_code = str(code[i])
        for j in range(codewords):
            counter = int(0)
            if (j + i) < (codewords - 1):
                comp_code = str(code[i + j + 1])
                for k in range(len(current_code)):
                    if current_code[k] != comp_code[k]:
                        counter = (counter + 1)
                if (counter < min_dist_counter):
                    min_dist_counter = counter
    return min_dist_counter

def rec_codeword(code):
    x = int(0)
    length = int(len(code[0]))
    while x < 1:
        codeword = str(input("""What is the codeword you'd like to detect/correct errors in? 
    => """))
        binary = {'0', '1'}
        string = set(codeword)
        if ((len(codeword) == length) and ((string == binary) or (string == {'1'}) or (string == {'0'}))):
            x = (x + 1)
            return codeword
        else:
            print("Codeword must be the same length as all others in the code and must be in binary format.")

def error_detect(rec_codeword, code, min_dist, codewords):
    k = int(min_dist - 1)
    current_code = rec_codeword
    for i in range(codewords):
        errors = int(0)
        error_indicies = []
        comp_code = str(code[i])
        for j in range(len(current_code)):
            if current_code[j] != comp_code[j]:
                errors += 1
                error_indicies.append(j)
        if (k >= errors):
            return error_indicies

def error_correct(rec_codeword, code, min_dist, codewords):
    k = int((min_dist - 1) / 2)
    current_code = rec_codeword
    for i in range(codewords):
        errors = int(0)
        comp_code = str(code[i])
        for j in range(len(current_code)):
            if current_code[j] != comp_code[j]:
                errors += 1
            if (k >= errors):
                return comp_code

if __name__ == "__main__":
    main()