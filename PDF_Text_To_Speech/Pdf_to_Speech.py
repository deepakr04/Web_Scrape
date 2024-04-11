# importing the modules
import PyPDF2
import pyttsx3


def Text_To_Speech(txt):
    print("Text to Speech: Hello")
    # reading the text
    speak = pyttsx3.init()
    speak.say(txt)
    speak.runAndWait()


def main():
    try:
        # Open the PDF file in read-binary mode
        with open("6-7-week1-math-geometry1_free.pdf", 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            num_pages = pdf_reader.numPages
            text = ''

            # Iterate through each page and extract text
            for page_num in range(num_pages):
                page = pdf_reader.getPage(page_num)
                text += page.extractText()

            Text_To_Speech(text)
    except Exception as e:
        print(f"An error occurred while reading the PDF file: {e}")


if __name__ == '__main__':
    main()
