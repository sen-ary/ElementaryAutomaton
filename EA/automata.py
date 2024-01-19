from p5 import *

history = {}

def apply_rule (x , y , z , bin_rule):
   if (x == False and y == False and z == False):return bool (int (bin_rule[7]))
   if (x == False and y == False and z == True):return bool (int (bin_rule[6]))
   if (x == False and y == True and z == False):return bool (int (bin_rule[5]))
   if (x == False and y == True and z == True):return bool (int(bin_rule[4]))
   if (x == True and y == False and z == False):return bool (int (bin_rule[3]))
   if (x == True and y == False and z == True):return bool (int (bin_rule[2]))
   if (x == True and y == True and z == False):return bool (int (bin_rule[1]))
   if (x == True and y == True and z == True):return bool (int (bin_rule[0]))

def generate (curr_gen , bin_rule):
    first = apply_rule (curr_gen[0] , curr_gen [len(curr_gen)-1] , curr_gen [1] , bin_rule)
    #last = curr_gen [len(curr_gen)-1]
    new_gen = []
    new_gen.append (first)
    start = 0 
    end = 3
    while (end <= len(curr_gen)):
        #print (start)
        #print (end)
        x,y,z = curr_gen[start:end]
        #print (x,y,z)
        new_cell = apply_rule (x , y , z , bin_rule)
        new_gen.append (new_cell)
        start = start + 1
        end = end +1  
    new_gen.append (first)
    return new_gen

def run_automata (gen:list , n_gen , rule):
    bin_rule = bin (rule)[2:]
    if (len (bin_rule) < 8):
      padding = ['0' for i in range (8 - len(bin_rule))]
      padding = ''.join(padding)
      bin_rule = padding + bin_rule 
    #print (f'Initial Generation: {gen}\n')
    history [0] = gen
    for i in range (n_gen):
        gen = generate (gen ,bin_rule)
        history [i+1] = gen
        # print (f'Genereation {i+1}: {gen}\n')


initial = [False for i in range (31)]
initial[15] = True  
run_automata (initial, 16 , 129)


#Visualization With P5
def setup():
    size(1550, 800)

def draw():
    width = 50
    for k , v in history.items():
        print (k)
        row = k * width
        for i in range (31):
            if v[i] == False:
                fill (255)
            else :
                fill (0)
            square (i*width , row , width)
run()