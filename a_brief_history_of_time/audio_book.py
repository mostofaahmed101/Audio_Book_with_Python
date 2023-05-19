import pyttsx3
import PyPDF2


B_file = open('a_brief_history_of_time.pdf', "rb")

print("A Brief History of Time \n  by Stephen Hawking \n\n")

book = PyPDF2.PdfFileReader(B_file)
pages = book.numPages
print("The Total pages is", pages)

P_N = int(input("which page you want to listen: ")) - 1

Book_Audio = pyttsx3.init()

for x in range(P_N, pages):
    print("Page no:", x+1)
    page_Num = book.getPage(x)
    Book_Text = page_Num.extract_text()
    print(Book_Text)

    Book_Audio.say(Book_Text)
    Book_Audio.runAndWait()
    
    if x < pages:
        print("\n \n \n_NEXT PAGE /--> \n")
    else:
        print("ohhh... Done")
