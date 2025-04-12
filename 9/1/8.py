def whitespace():
    def convert(st:str):
        words = set(st.split())  
        sorted_words = sorted(words)  
        return " ".join(sorted_words)  

    string = "JOJO's bizzare adventure is a manga and anime series created by Hirohiko Araki. It has been serialized in Weekly Shōnen Jump since 1987, and has been adapted into several anime series, video games, and other media. The story follows the adventures of the Joestar family, who are often involved in supernatural battles against various villains. The series is known for its unique art style, creative storytelling, and memorable characters."
    print(convert(string)) 
    
whitespace() 