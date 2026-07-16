#task ==== extract all number from paragraph
#para = """
#only digit.txt 
# only_alfabate.txt
# server jub jub errorb generate krega toh logs khud se nikal ke aa jaaye \\ sever 1000000 line me agar only digit ho logs generate ho usame se only numbrr rkhna h 
#usame total number of logs,
# 
# [[[iska main use logs generate krega system usko python se handle krenge withn the help of python]]]]]
# agar aapko python aaygi toh jindgi aasahn ho jaaygi(baar baaar kaam nhi krna hoga 
# {[this is cost optomization without tools use krke python ki code se filter kr skte hai}]]]])
# python se data bulk me inject kr skte hai, )  other wise postman tool use in end point data inject
# ec2 hume per hours log generate kr ke bheje wha bhi python script use hota hai,,
# , and yha error less code likhte hai [[[ek program aapko aati h toh aapki jingin aashan ho  jati h python se ip adress se stress test lga skte b hai ]]
#get and post dono python ki script se kr skte hai///
# //withut tools se hum python use kr skte hai
#hum sara kaam github action se kr skte hai]
# duniya ki puri kaam prograaming se ho skti hai in python 

#file handling----------------------------------------------------------

# 1.  File handling in python means reading from and writing to files/folder stored on 
# disk using python

# 2.  Your python code can open a file  , pull out data of it ,  put data into it and
# also close it properly.

#what is file-------------------(raw information ko data bolte hai)
#but file  me information and data both store
# files are store of data and information on the specific path of device


# type of files
# 1. text file (.txt,.csv,.json)
# 2. binary file (images, videos, audio) 

# Type of file path

#1. Absolute path : The complete path from the root of the filesystem.
#2. Relative path  : The path relative to where your current folder (current working directory)

#file mode
#1. a : append , a+ : append and read
#2. w : write  , w+ : write and read
#3. r : read   , r+ : read and write
#4. x : strictly create file

# python handling methods.
#1. open(file_name,mode) : open file
#2. close() : close file
#3. flush() : memory cleanup.

#4. read() :file read
#5. readlines() : file read line by line.
#6. write() : writes data in files only take string.
#7. writelines() : write data in file of any data types.

#8. tail() : cursor move
#9. seel() : specific position set of cursor

# in-built module
#os library
#shutil library
#subprocess library
# randam library
# string library

#-------------create file
# file=open("demo.txt","x")
# print("file created")

#---------------------------------------
#create a file in strict mode
# try:
#     file=open("demo.txt","x")
#     print("file created")
# except Exception as e:
#     print("Error:",e)

#2. write mode file creaction  // file jo create hoga write mode me
# file=open("new_demo.txt","w")  //open method use
# file.write("this is file content using file handling")
# print("file created in write mode...")
# // change directory
#// current working get directory


# import os  #os ke andar hum file bna skte h
# print(os.getcwd())  # cwd = current working directory
# path=r"C:\Users\ANNU SINGH\Desktop"        # r koi bhi specil charcter ko string ,me  convert krta h
# os.chdir(path)
# print(os.getcwd())   # yeh nbatata hai current directory kya g ex desktop yah c,d

# file=open("lms-app.zip.zip","r")
# print(os.getcwd())
# print(os.listdir())  # desktop ka sara file list form me dika dega

# #mtlb hum python .py filr bna ke python ki file ko handle kr skte hai

# file=open("data.py","w")
# file.write(f"print('File handling')")
# file.close()
# print(os.listdir())   not use industry because yha file ko oen and close ke liye coommnd dena pdta h es liye

# #context manager= yeh file ko securly open and close krega humko bina like file.close likhe
# yha with likhna hota = yeh khud file ko open and close secure tarike se krta h // also use in industry more use and its also work pore because yha file ko open close naa kr ke yeh 
# // and we always use with
#with open("demo.txt","r") as file:
# with open("demo.txt","w") as file: # in use our system log generate krega esi se
#     #r=file.read()
#     file.write("this is new content of file")
#     file.write("this is updated file")
#     #print(r) #file me jo lika h usko hum dekhn skte h terminal pur
# #     print("file")

# server_list=['prod_server' , "test_server" , "dev_server"]
# for i in server_list:
#     with open(f"{i}.txt","w") as file:    
#       print(i,"file created................")

      #server ka ;log generate hum append mode me krte h kyoki last hi record rkhta h fikle khi  
      #  pichle line dikkat ho toh pta nhi chula paayega 
      #   append mode me server piche aur aage dono ki log store kr ke rkhta h append in list mode

# with open("dev_server.txt","w") as file:
#     file.write("this is content of dev server")
         
with open("dev_server.txt","a") as file:
    file.write("\n")
    file.write("this is content of my server") # mtlb yeh append krne pe jitni
    #baar run hoga utni baar lig collect hogastorage me (you go and see dev_server file text)
         
        