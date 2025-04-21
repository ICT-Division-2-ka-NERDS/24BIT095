def text():
    
    f_r = open("C:\\Users\\admin\\Desktop\\Idiotic stuff (2nd sem)\\Python Assignments\\10\Input-8.txt", 'r')
    data = f_r.read()
    f_r.close()

    print("Original Text:", data)

    remove_words = [
        ' a ', ' an ', ' the ', ' A ', ' An ', ' The ', 
        'a ', 'an ', 'the ', 'A ', 'An ', 'The ',       
        ' a', ' an', ' the', ' A', ' An', ' The'        
    ]
    for word in remove_words:
        data = data.replace(word, ' ')  

    
    fw = open('Output-8.txt', 'w')
    fw.write(data)
    fw.close()

    print("Modified Text Written to Output-8.txt")

text()