file=open("abc.txt","r")
read_data=file.read()
per_word=read_data.split()
print("Total words:",len(per_word))