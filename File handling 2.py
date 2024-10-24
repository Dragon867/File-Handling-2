#open the file in read mode
file_read=open('Codingal.txt','r')

#the file is in read mode
print("File in read mode")
print(file_read.read())
file_read.close()

#open the file in write mode
file_write=open('Codingal.txt','w')
#the file is in write mode
file_write.write("File in write mode")
file_write.write(" Hi I am a Hamza.")
file_write.close()

#open the file in append mode
file_append=open('Codingal.txt','a')
#the file is in append mode
file_append.write("File in append mode ")
file_append.write("Hi I am a Hamza.My age is 18")
file_append.close()