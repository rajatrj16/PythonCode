try:
    f = open('Textfile.txt','r')
    #f = open('Textfile.txt','w')
    f.write("Write something into the textfile")
#except IOError:
except:
    print("Error: Could not find file or Data")
finally:
#else:
    #print("File Found")
    print("********************************************************************")
    print("This is finally block which always execute except syntex error")
    print(3+9)
    f.close()
    print("********************************************************************")
print("This is something after exception")
