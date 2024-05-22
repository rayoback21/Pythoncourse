with open("estudiante.txt", "r")as file:
    cont = file.readlines()
    print(cont[0:2])

#cear una funcion 
#recivir 


def read_lines(filename, num_lines):
    with open(filename, "r") as file:
        for _ in range(num_lines):
            line = file.readline()
            if not line:
                break
            print(line.strip())