import datetime
import os
from os import listdir
from os.path import isfile, join

import matplotlib
import matplotlib.pyplot as plt
from art import *
from colorama import Fore



#opening screen
ascii_art = text2art(text='File  Stats') #declare ascii art
os.system('title File Stats') #title
os.system('cls') #clear the screen
print(f"{Fore.MAGENTA}{ascii_art}{Fore.RESET}") #show ascii art
print(f"{Fore.RED}Type exit at any point to close the window.{Fore.RESET}") #exit message



#functions
def convert_bytes(num): #convert any bytes into appropriate format
    step_unit = 1000.0

    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < step_unit:
            return "%3.1f %s" % (num, x)
        num /= step_unit

def display_pie_chart(title, labels, sizes): #display the pie chart
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, autopct='%1.1f%%', shadow=True, startangle=90, normalize=True)
    ax1.axis('equal')

    plt.legend(labels)
    plt.title(title)
    plt.show()



#folder functions
def compare_folder_linecount(folder_path):
    total_linecount, line_count, folder_total_linecount = 0, 0, 0

    files = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
    for filee in files:
        try:
            with open(f"{folder_path}\\{filee}", 'r', encoding='UTF-8') as file:
                print(f"Counting the lines for: {filee}")
                for line in file.readlines():
                    line_count += 1
                    
                filename = os.path.basename(file.name)
                    
            folder_total_linecount += line_count
                
        except Exception as e:
            print(f"Couldn't linecount {filee} | {e}")
            pass
        
    sizes.append(folder_total_linecount)
    labels.append(f"{os.path.basename(folder_path)} - {folder_total_linecount:,}")

def compare_folder_file_sizes(folder_path):
    file_size, total_file_size = 0, 0
    
    files = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
    
    for filee in files:
        try:
            print(f"Getting the size of: {filee}")
            file = f"{folder_path}\\{filee}"
            file_size = os.path.getsize(f"{file}")
            total_file_size += file_size
                
        except Exception as e:
            print(f"Couldn't get the size of {filee} | {e}")
            pass
        
    name = os.path.basename(folder_path)
    sizes.append(total_file_size)
    labels.append(f"{name}: {total_file_size:,} bytes")

def folder_line_count(folder_path):
    total_linecount, line_count = 0, 0

    files = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
    for filee in files:
        try:
            with open(f"{folder_path}\\{filee}", "r", encoding="UTF-8") as file:
                print(f"Counting the lines for: {filee}")
                for line in file.readlines():
                    line_count += 1
                    
                filename = os.path.basename(file.name)
                    
                labels.append(f"{filename} - {line_count:,}")
                sizes.append(line_count)
                
        except Exception as e:
            print(f"Couldn't linecount {filee} | {e}")
            pass

def folder_file_sizes(folder_path):
    file_size, total_file_size = 0, 0
    
    files = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
    for filee in files:
        print(f"Getting the size of: {filee}")
        try:
            file = f"{folder_path}\\{filee}"
            file_size = os.path.getsize(f"{file}")
            total_file_size += file_size
                    
            labels.append(f"{filee}: {file_size:,} bytes")
            sizes.append(file_size)
                
        except Exception as e:
            print(f"Couldn't linecount {filee} | {e}")
            pass
               
    total_file_size = convert_bytes(float(total_file_size))
    display_pie_chart(f"Total: {total_file_size}", labels, sizes)

def folder_extensions(folder_path):
    file_types = {}
    
    files = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
    for filee in files:
        try:
            with open(f"{folder_path}\\{filee}", "r", encoding="UTF-8") as file:
                print(f"Getting the file extension for: {filee}")
                file_name, file_extension = os.path.splitext(filee)
                        
                if file_extension in file_types.keys():
                    file_types[file_extension] += 1
                    
                else:
                    file_types[file_extension] = 1
                
        except Exception as e:
            print(f"Couldn't linecount {filee} | {e}")
            pass
        
    for element in file_types:
        labels.append(f"{element} - {file_types[element]}")
        sizes.append(file_types[element])
        
    display_pie_chart('Most common file types', labels, sizes)



#file functions
def compare_linecount(user_file):
    linecount = 0

    try:
        print(f"Counting the lines for: {os.path.basename(user_file)}")
        file = open(f"{user_file}", 'r', encoding='UTF-8')
        for line in file.readlines():
            linecount += 1
                
    except Exception as e:
        print(f"Couldn't linecount {file} | {e}")
        
    labels.append(f"File {os.path.basename(user_file)}: {linecount:,} lines")
    sizes.append(linecount)

def compare_file_sizes(user_file):
    file_size, total_file_size = 0, 0

    try:
        print(f"Getting the size for: {os.path.basename(user_file)}")
        file = open(f"{user_file}", 'r', encoding='UTF-8')
        file_size = os.path.getsize(f"{user_file}")
        total_file_size += file_size
                
    except Exception as e:
        print(f"Couldn't calculate size of {file} | {e}")
        
    filename = os.path.basename(user_file)
    labels.append(f"{filename}: {file_size:,} bytes")
    sizes.append(file_size)

def file_linecount(user_file):
    total_line_count, pure_line_count, empty_line_count = 0, 0, 0
    print('Calculating line count!')

    try:
        with open(f"{user_file}", 'r', encoding='UTF-8') as file:
            for line in file.readlines():
                
                if line != "\n":
                    pure_line_count += 1
                else:
                    empty_line_count += 1
                
                total_line_count += 1
                
    except Exception as e:
        print(f"Couldnt linecount {file} | {e}")
    
    print(f" Total lines: {total_line_count:,} \n Pure lines: {pure_line_count:,} \n Empty lines: {empty_line_count:,}")
    
    labels.append(f"Pure line count: {pure_line_count:,}")
    sizes.append(pure_line_count)
    labels.append(f"Empty lines: {empty_line_count:,}")
    sizes.append(empty_line_count)
    
    display_pie_chart(f"File {os.path.basename(user_file)}: {total_line_count:,} lines", labels, sizes)



#main loop
while True:
    try: 
        path_or_file = str(input('Would you like the stats for a folder or a specific file: ').lower())
        
        if path_or_file == 'folder':
            try:
                compare = str(input('Would you like to compare paths(Y/N): ').lower())
                
                if compare == 'y':
                    user_option = str(input('Which option would you like: \n Option 1 = compare total lines \n Option 2 = compare file sizes \n Option: ').lower())
                
                    if user_option == '1' or user_option == 'option 1':
                        labels, sizes = [], []
                        amount = int(input('Amount of directories to compare: '))
                        
                        for i in range(amount):
                            total_linecount, line_count, folder_total_linecount = 0, 0, 0
                            folder_path = str(input(f"Folder Path {i+1}: "))
                            
                            compare_folder_linecount(folder_path)
                            
                            for element in sizes: 
                                total_linecount += element                            

                        display_pie_chart(f"Total lines: {total_linecount:,}", labels, sizes)
                        continue
                        
                    if user_option == '2' or user_option == 'option 2':
                        labels, sizes = [], []
                        amount = int(input('Amount of directories to compare: '))
                        
                        for i in range(amount):
                            total, file_size, total_file_size = 0, 0, 0
                            folder_path = str(input(f"Folder Path {i+1}: "))
                            
                            compare_folder_file_sizes(folder_path)
                            
                        for element in sizes:
                            total += element   

                        total = convert_bytes(total)
                        display_pie_chart(f"Total: {total}", labels, sizes)
                        continue
                
                    if user_option == 'exit':
                        break
                    
                    else:
                        raise Exception('Invalid option, please try again.')
                        continue
                
                if compare == 'n':
                    user_option = str(input('Which option would you like: \n Option 1 = total line count \n Option 2 = file sizes \n Option 3 = file types \n Option: ').lower())
                    
                    if user_option == '1' or user_option == 'option 1':
                        labels, sizes, line_count, total_linecount = [], [], 0, 0
                        folder_path = str(input('Folder Path: '))
                        
                        folder_line_count(folder_path)
                        
                        for element in sizes:
                            total_linecount += element
                        
                        display_pie_chart(f"Total lines: {total_linecount:,}", labels, sizes)
                        continue
                          
                    if user_option == '2' or user_option == 'option 2':
                        labels, sizes, file_size, total_file_size = [], [], 0, 0
                        folder_path = str(input('Folder Path: '))
                        
                        folder_file_sizes(folder_path)
                        continue
                    
                    if user_option == '3' or user_option == 'option 3':
                        labels, sizes = [], []
                        folder_path = str(input('Folder Path: '))
                        
                        folder_extensions(folder_path)
                        continue
                          
                    if user_option == 'exit':
                        break
                            
                    else:
                        raise Exception('Invalid option, please try again.')
                        continue
                
                if compare == 'exit':
                    break
                
                else:
                    raise Exception('Invalid option, please try again.')
                    continue
                
            except Exception as e:
                print(f"Error: {e}")
                continue
                
        if path_or_file == 'file':
            try:
                compare = str(input('Would you like to compare files(Y/N): ').lower())
            
                if compare == 'y':
                    
                    try:
                        user_option = str(input('Which option would you like: \n Option 1 = compare line count \n Option 2 = compare file sizes \n Option: ').lower())
                        
                        if user_option == '1' or user_option == 'option 1':
                            labels, sizes, linecount, total_linecount = [], [], 0, 0
                            amount = int(input('Amount of files to compare: '))
                            
                            for i in range(amount):
                                linecount = 0
                                user_file = str(input(f'File directory {i+1}: '))
                                filename = os.path.basename(user_file)
                                
                                compare_linecount(user_file)
                                
                            for element in sizes:
                                total_linecount += element
                                
                            display_pie_chart(f"Total lines: {total_linecount:,}", labels, sizes)
                            continue
                            
                        if user_option == '2' or user_option == 'option 2':
                            labels, sizes, file_size, total_file_size = [], [], 0, 0
                            amount = int(input('Amount of files to compare: '))
                            
                            for i in range(amount):
                                file_size = 0
                                user_file = str(input(f"File directory {i+1}: "))
                                
                                compare_file_sizes(user_file)
                                
                            for element in sizes:
                                total_file_size += element
                                
                            display_pie_chart(f"Total: {total_file_size:,}", labels, sizes)
                            continue
                            
                        if user_option == 'exit':
                            break
                            
                        else:
                            raise Exception('Invalid option, please try again.')
                    
                    except Exception as e:
                        print(f"Error: {e}")
                        continue
                
                if compare == 'n':
                    
                    try:
                        user_option = str(input('Which option would you like: \n Option 1 = line stats \n Option 2 = file size \n Option: ').lower())
                        
                        if user_option == '1' or user_option == 'option 1':
                            labels, sizes, linecount = [], [], 0
                            
                            user_file = str(input('File directory: '))
                            
                            file_linecount(user_file)
                            continue
                            
                        if user_option == '2' or user_option == 'option 2':
                            user_file = str(input('File directory: '))
                            
                            file_size = os.path.getsize(f"{user_file}")
                            
                            file_size = convert_bytes(file_size)
                            
                            print(f"{os.path.basename(user_file)} is {file_size}")
                            continue
                            
                        if user_option == 'exit':
                            break
                            
                        else:
                            raise Exception('Invalid option, please try again.')
                            continue
                    
                    except Exception as e:
                        print(f"Error: {e}")
                        
                if compare == 'exit':
                    break
                        
                else:
                    raise Exception('Invalid option, please try again.')
                    continue
                    
            except Exception as e:
                print(f"Error: {e}")
                
        if path_or_file == 'exit':
            break
            
        else:
            raise Exception('Invalid option, please try again.')
            continue
        
    except Exception as e:
        print(f"Error: {e}")