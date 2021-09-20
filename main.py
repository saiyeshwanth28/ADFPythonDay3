"""
importing the required packages
"""
import sys
import logging
import re
import uuid
from collections import Counter

logging.basicConfig(filename="sample.txt",filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

class Task:
    """
    parent class with read and write operations on files
    """
    def __init__(self,filename):
        """
        constructor for initialization
        """
        self.filename=filename
        self.words=[]
        self.un_fname= ""
        self.most_repeat=""


    def read(self):
        """
        this function is to read a file and slit the data into words and append to a list
        """
        try:
            with open(self.filename,'r+',encoding="UTF-8") as file:
                data=file.readlines()
        except IOError:
            logging.error("exception occurred")
        for i in data:
            self.words.extend(i.split())
        logging.info('file reading and splitting into words')
        logging.info(self.words)


    def write(self):
        """
        this funtion is to write an output file
        """
        try:
            with open('self.un_name','w',encoding="utf-8") as output_file:
                output_file.write("-".join(self.words)+'\n')
                logging.info('file written successfully')
        except IOError:
            logging.error("exception occurred")


class StringOperations(Task):
    """
    class used to perform various operation on the text present in the input file
    """
    def vowels_split(self):
        """
        this funtion is to split the words in the list based on vowels
        """
        list_vowels_split=[]
        try:
            for i in range(len(self.words)):
                list_vowels_split.extend(re.split('a|e|i|o|u|A|E|I|O|U',self.words[i]))
            logging.info("splitting based on vowels")
            logging.info(list_vowels_split)
            self.words=list_vowels_split[:]
        except:
            logging.error("exception occurred : ")


    def counter_index(self):
        """
        this funtion is to Create a Word dict with Key as counter
        index and value as the words present in file and print them on screen.
        """
        logging.info("counter index with data as values")
        return dict(enumerate(self.words))


    def unique_list(self):
        """
        this funtion is to Convert all words into unique list and print in command line
        """
        logging.info("unique list by removing duplicates")
        return list(set(self.words))


    def maximum_repeated(self):
        """
        this funtion is to Print the word that was repeated maximum number of times.
        """
        try:
            logging.info("most repeated word in the input file")
            self.most_repeat=Counter(self.words)
            return self.most_repeat.most_common(1)[0][0]
        except:
            logging.error("exception occurred : ")


    def caps_third_letter(self):
        """
        this funtion is to Capitalize 3rd letter of every word
        """
        try:
            for i in range(len(self.words)):
                if len(self.words[i])>=3:
                    flag=list(self.words[i])
                    flag[2]=flag[2].upper()
                    self.words[i]=''.join(flag)
            logging.info("capitalizing every 3rd letter of a word")
            logging.info(self.words)
        except:
            logging.error("exception occurred : ")

    def caps_fith_word(self):
        """
        this funtion is to Capitalize all characters of every 5th word in the file.
        """
        try:
            for i in range(4,len(self.words),5):
                self.words[i]=self.words[i].upper()
            logging.info("capitalizing every fifth word")
            logging.info(self.words)
        except:
            logging.error("exception occurred : ")

    def semi_colon_replace(self):
        """
        this funtion is to Use ; (semi-colon) for new line
        """
        try:
            logging.info("replacing the new line character with semi colon")
            for i in range(len(self.words)):
                self.words[i]=self.words[i].replace('\n',';')
        except :
            logging.error("exception occurred : ")



    def starts_with_to(self):
        """
        this funtion is to Print the number of words having prefix with “To” in the input file.
        """
        count=0
        try:
            for i in self.words:
                if i.startswith("to") or i.startswith("To"):
                    count+=1
        except:
            logging.error("exception occurred : ")

        return count


    def ends_with_ing(self):
        """
        Print the number of words ending with “ing” in the input file
        """
        count=0
        try:
            for i in self.words:
                if i.endswith("ing"):
                    count+=1
        except:
            logging.error("exception occurred : ")
        return count


    def palindrome(self):
        """
        this funtion is to Print the palindrome present in the file.
        """
        list_palindromes=[]
        try:
            for i in self.words:
                if i==i[::-1] and len(i)>1:
                    list_palindromes.append(i)
        except:
            logging.error("exception occurred : ")
        return list_palindromes



    def unique_file_name(self):
        """
        this funtion is to Output file name should be generated with unique name.
        """
        try:
            logging.info("creating an unique file")
            self.words=' '.join(self.words).split()
            self.un_fname=str(uuid.uuid4())
            self.un_fname+='.txt'
            self.write()
        except:
            logging.error("exception occurred : ")



if __name__=="__main__":
    x=StringOperations(sys.argv[1])
    x.read()
    print("prefix with 'to' : ",x.starts_with_to())
    print("suffix with 'ing' : ",x.ends_with_ing())
    print("max repeated : ",x.maximum_repeated())
    print("palindromes : ",x.palindrome())
    print("unique words : ",x.unique_list())
    print("counter index : ",x.counter_index())
    x.vowels_split()
    x.caps_third_letter()
    x.caps_fith_word()
    x.semi_colon_replace()
    x.unique_file_name()
