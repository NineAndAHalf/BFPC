from sys import argv
from os import system

if __name__ == "__main__":
    
    file_path  = argv[1]
    output_file = argv[2]
    with open(file_path,"r") as file_brainfuck:
        with open(output_file+".c","w") as file_c:
            file_c.write("#include<stdio.h>\nint main(){char array[30000]={0};char *p=array;")
            
            for char in file_brainfuck.read():
                
                if char == ">":file_c.write("++p;")
                elif char == "<":file_c.write("--p;")
                elif char == "+":file_c.write("++(*p);")
                elif char == "-":file_c.write("--(*p);")    
                elif char == ".":file_c.write("putchar(*p);")    
                elif char == ",":file_c.write("*p=getchar();")   
                elif char == "[":file_c.write("while(*p){")   
                elif char == "]":file_c.write("}")   
            file_c.write("}")
            
system(f"gcc {output_file+'.c'} -o {output_file}; rm {output_file+'.c'}")