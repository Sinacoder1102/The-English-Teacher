def program():
        def hello():
            print('************************************************************************')
            print('The English text reader')
        hello()
        def reading():
            import pyttsx3
            tts = pyttsx3.init()
            tts.setProperty('volume',0.8)
            x = input('What do you want to say? : ')
            rate = int(input('Please determine the reading speed (the speed is between 1 and 200) : '))
            tts.setProperty('rate',rate)
            tts.say(x)
            tts.runAndWait()
            spell_question = input("Do you want your word's spell? (yes/no) : ").lower()
            if spell_question in ['yes','y']:
                spelled_out = "  ".join(x.upper())
                print('Spelling :',spelled_out)
                tts.setProperty('rate',95)
                tts.say(spelled_out)
                tts.runAndWait()
                tts.setProperty('rate',rate)
        reading()
        def question():
            while True:
                user_input = input('Do you want to continue? (yes/no) : ').lower()
                if user_input == 'yes' or user_input == 'y':
                    reading()
                elif user_input == 'no' or user_input == 'n':
                    print('************************************************************************')
                    break
                else:
                    print('Invalid input! Please enter yes or no')
        question()
# Program 2 is starting from here
def program2():
    def hello():
        print('Hello')
        print('Teaching fine details based on the notes of Professor Mohammad Amir Sinafar.')
    hello()
    def words():
        print('We have 4 types of word in English :')
        print('nouns (n)')
        print('verbs (v)')
        print('adjectives (adj)')
        print('adverbs (adv)')
    def numbers():
        print('We have 2 types of numbers in English : ')
        print('1.Cardinal numbers like : 1,2,3,4,5,78,12')
        print('2.ordinal numbers like : first(1st),second(2nd),third(3rd),etc.....')
        print('*Important point* : in the ordinal numbers,after 3,we must add Th after number.for example :')
        print('4th,5th,6th,10th...................')
    def adverds():
        print('According to the notes,we have 3 types of adverbs :')
        print('The adverbs of time like : now , yesterday , soon , *sentence : I will call you tomorrow*')
        print('The adverbs of place like : here , there , everywhere , *sentence : The cat is outside*')
        print('The adverbs of manner like : quickly , slowly , carefully , *sentence : He runs quickly*')
    def start():
        while True:
            start_question = input("What do you like to read? (types of words,types of numbers or types of adverbs),or you can type exit to finish : ").lower()
            if start_question == 'types of words' or start_question == 'words':
                words()
            elif start_question == 'types of numbers' or start_question == 'numbers':
                numbers()
            elif start_question == 'types of adverbs' or start_question == 'adverbs':
                adverds()
            elif start_question == 'exit' or start_question == 'e':
                print('************************************************************************')
                break
    start()                
# Starting program 3 from here
def program3():
    def hello():
        print('The grammer teacher')
        print("Acording mr Sinafar's notes")
    hello()
    def grammers():
        simple_present = """Simple present grammer:
Where is it used? : We use simple present grammer to speak about our habits.
------------------------------------------------------------------------------------------------
Grammar formula : positive (subject + verb),negetive (subject + does not,do not + verb),question (Do,does + subject + verb)
------------------------------------------------------------------------------------------------
examples : I play football , She doesn't play violin , Do They swim at 7:20?
------------------------------------------------------------------------------------------------
important Points : If you want to use this grammer for (he,she,it) You should add s or es In The last of your verb""".strip()
        present_continuous = """Present continuous or present prograssive :
Where is it used? : We use pesent continuous to speak about express actions that are currently being performed.
------------------------------------------------------------------------------------------------
Grammer formula : positive (Subject + tobe verb + ing),negetive (Subject + not + tobe verb + ing),question (Tobe verb + subject + verb + ing)
------------------------------------------------------------------------------------------------
examples : I'm playing football , She isn't swimming , Are you studying?
------------------------------------------------------------------------------------------------
Important points : If there's vowel sound in the last of a word,that word + ing but we add two of last letter.For Example :
run + ing = running"""
        simple_past = """Simple past grammer :
Where is it used? : We use simple past to express actions that have been completed in the past.
------------------------------------------------------------------------------------------------
Grammer point : For using this grammer,We have 2 types of verbs ; regular : We must add d or ed in last of our verb : played,lived
And iregular : These types are memorable : go = went , write = wrote
------------------------------------------------------------------------------------------------
Grammer formula : positive (Subject + past verb),negetive (Subject + did not + past verb),quetion (Did + subject + past verb)
------------------------------------------------------------------------------------------------
Important points : To express the exact time of an action, adverbs of time such as "yesterday," "last week," "in 2010," etc., are usually used.
In negative and interrogative sentences, the main verb is in its base form."""
        past_continuous = """Past continuous grammer :
Where is it used? : We use past continuous to describe actions that were ongoing at a specific time in the past.
------------------------------------------------------------------------------------------------
Grammer formula : positive (Subject + was/were + verb + ing),negetive (Subject + not + was/were + verb + ing),question (Was/were + subject + verb + ing)
------------------------------------------------------------------------------------------------
Examples : She was studying , They weren't watching TV , Were you sleeping?
------------------------------------------------------------------------------------------------
Important points : The Past Continuous tense emphasizes the duration or continuity of an action in the past.
This tense is formed using the verb "tobe" in the past (was/were) and adding -ing to the main verb."""
        simple_future = """Simple future (will) :
Where is it used? : We use simple future to describe actions that will be performed in the future.
------------------------------------------------------------------------------------------------
Grammer formula : positive (Subject + will + verb),negetive (Subject + won't + verb),questoin (Will + subject + verb)
------------------------------------------------------------------------------------------------
Examples : I will go tomorrow , He won't come , Will you come with us?
------------------------------------------------------------------------------------------------
Important points : The Simple Future tense is formed simply using "will" and the main verb.
In spoken language, "will" is usually shortened to 'll  (for example: I'll, you'll)."""
        present_perfect = """Present perfect grammer :
Where is it used? : We use present perfect to describe actions that have been completed in the past and have an effect or connection to the present.
------------------------------------------------------------------------------------------------
Grammer formula : positive (Subject + have/has + past verb),negetive (Subject + not + have/has + past verb),question (Have/has + subject + past verb)
------------------------------------------------------------------------------------------------
Examples : T have read a book , He hasn't eaten yet , Have you see this movie?
------------------------------------------------------------------------------------------------
Important points : The Present Perfect tense does not refer to the exact time of the action in the past; rather, it emphasizes the result or effect of that action on the present.
Some verbs (such as "know," "believe," "love") are usually used in the Present Perfect tense because they indicate a state or condition."""
        past_progressive = """Past progressive grammer :
Where is it used? : The past progressive tense is used to describe actions that were ongoing at a specific time in the past.
This tense is typically used to express activities that were in progress and may have been interrupted by another action.
------------------------------------------------------------------------------------------------
Grammer formula : positive (Subject + was/were + verb with ing),negetive (Subject + not + was/were + verb with ing),question (Was/were + subject + verb with ing).
------------------------------------------------------------------------------------------------
Examples : She was reading a book , We weren't talking , Was he working?
------------------------------------------------------------------------------------------------
Important points : The past progressive tense is usually accompanied by specific times in the past, such as *at 5 o'clock* or *yesterday*.
This tense is usually not used for verbs that indicate a state or condition (such as *know* or *believe*)."""
        def question():
            cs = input('Which grammer do you want to practice? : ').lower()
            if cs in ['simple present']:
                print('************************************************************************')
                print(simple_present)
            elif cs in ['present continuous']:
                print('************************************************************************')
                print(present_continuous)
            elif cs in ['simple past']:
                print('************************************************************************')
                print(simple_past)
            elif cs in ['past continuous']:
                print('************************************************************************')
                print(past_continuous)
            elif cs in ['simple future','will']:
                print('************************************************************************')
                print(simple_future)
            elif cs in ['present perfect']:
                print('************************************************************************')
                print(present_perfect)
            elif cs in ['past progressive']:
                print('************************************************************************')
                print(past_progressive)
            else:
                print('Sorry! This grammer is not defined')
        def start():
            while True:
                question()
                v1 = input('Do you want to continue? (y/n) : ').lower()
                if v1 in ['y','yes']:
                    question()
                elif v1 in ['n','no']:
                    print('****************************************************************************')
                    break
                else:
                    print('Please enter y or n')
        start()                    
    grammers()     
# Starting program 4 from here
def program4():
    def hello():
        print('Have got / Has got explaining :')
    hello()
    def have_got_and_has_got():
        has_have = """------------------------------------------------------------------------------------------------
Where is it used? : "Have got" and "has got" mean "to have" and are used informally in English.
------------------------------------------------------------------------------------------------
Have got : It is used for the first person (I and we), the second person (you), and plural.
------------------------------------------------------------------------------------------------
Has got : It is used for the third person (he, she, it).
------------------------------------------------------------------------------------------------
Examples for poditive sentences : I have got a new car , He has got a dog
------------------------------------------------------------------------------------------------
How to make negetive form? : For negative sentences, "haven't got" and "hasn't got" are used.
------------------------------------------------------------------------------------------------
How to make interrogative form? : For question sentences, "Have you got" and "Has he/she/it got" are used in that order.
------------------------------------------------------------------------------------------------
Examples for negetive and interrogative form : She hasn't got a bike , Have you got a pen?
------------------------------------------------------------------------------------------------
Important points : "Have got" and "has got" are used more in conversational and informal language. In more formal language, usually only "have" and "has" are used.
------------------------------------------------------------------------------------------------"""
        print(has_have)
    have_got_and_has_got()    

# Starting program 5 from here

def program5():
    def hello():
        print('----------------------------------------------------------------------------------------------')
        print('The history of English language :')
    hello()
    def History_EN():
        History = """
The English language is a Indo-European language that can be divided into several historical periods:
1. Old English (450 - 1150 AD)
Origins: After the arrival of the Angles, Saxons, and Jutes in Britain.
Characteristics: Old English was influenced by Scandinavian languages and Latin. Notable texts include "Beowulf."
------------------------------------------------------------------------------------------------
2. Middle English (1150 - 1500 AD)
Norman Influence: Following the Norman Conquest in 1066, French heavily influenced English.
Characteristics: Major changes in grammar and vocabulary. Important works include "The Canterbury Tales" by Chaucer.
-----------------------------------------------------------------------------------------------
3. Early Modern English (1500 - 1700 AD)
Literary Flourishing: The emergence of writers like William Shakespeare and translations of the Bible.
Characteristics: Changes in pronunciation and vocabulary. The language expanded due to colonization and trade.
-----------------------------------------------------------------------------------------------
4. Modern English (1700 - Present)
Global Development: English emerged as an international language in trade, science, and culture.
Characteristics: Expansion of vocabulary and influences from other languages, especially during the colonial era.
-----------------------------------------------------------------------------------------------"""        
        print(History)
    History_EN()

# Program 6 starts from here
def program6():
    def hello():
        print('----------------------------------------------------------------------------------------------')
        print("Explaining 'Can'")
    hello()
    def can_E():
        can = """
What's can? : 
The term "can" in English means "to be able to" or "to be capable of" and is used as a modal verb.
-----------------------------------------------------------------------------------------------
Where is it used? : 
Expressing ability : I can speak English.
-----------------------------------------------------------------------------------------------
Requesting permission : Can I go to the bathroom?
-----------------------------------------------------------------------------------------------
Expressing possibility: It can rain tomorrow."""
        print(can)
    can_E() 

#ُStarting program7
def program7():
    def hello():
        print('----------------------------------------------------------------------------------------------')
        print("Explaining 'Be'")
    hello()
    def be_e():
        be = """
What's be? :
The verb "to be": This verb means "to exist" and is used to express existence, state, or identification.
-----------------------------------------------------------------------------------------------  
Different forms: The verb "be" is conjugated in different ways in various tenses:  
Simple present: am, is, are  
Simple past: was, were  
Future: will be  
Present continuous: being
----------------------------------------------------------------------------------------------
Wher we can use it? :
Identification: Used to express the identity or identification of people or objects.  
Example: He is a teacher. 
---------------------------------------------------------------------------------------------- 
State and characteristic: Used to express the state or characteristic of people or objects.  
Example: The sky is blue.  
----------------------------------------------------------------------------------------------
Existence: Used to express existence or non-existence.  
Example: There are two apples on the table.
----------------------------------------------------------------------------------------------
Interrogative and negetive form :
Questions: To form questions, the verb "be" is used in reverse order.  
Example: Are you a student?
----------------------------------------------------------------------------------------------  
Negative sentences: To form negative sentences, "not" is placed after the verb "be."  
Example: She is not happy.
----------------------------------------------------------------------------------------------
Phrasal verb :
"Be" is used in combination with other verbs to form continuous and future tenses.  
Example: I am studying.
----------------------------------------------------------------------------------------------"""
        print(be) 
    be_e()

#Starting peogram 8
def program8():
    def hello():
        print('----------------------------------------------------------------------------------------------')
        print('Explaining Articles')
    hello()
    def Articles_e ():
        Articles = """
What's The Article? : 
Articles in English are divided into two main categories: Definite Articles and Indefinite Articles.
----------------------------------------------------------------------------------------------
Definite Articles : 
"the": This article is used to refer to a specific or particular noun.
Example: The book on the table is mine
----------------------------------------------------------------------------------------------
Indefinite Articles : 
"a" and "an": These articles are used to refer to a non-specific or general noun.
"a": Used before nouns that begin with a consonant sound.
Example: I saw a dog in the park.
"an": Used before nouns that begin with a vowel sound.
Example: She wants an apple
----------------------------------------------------------------------------------------------
Rules and iporatant points :
Correct Usage:
When using "a" and "an," pay attention to the initial sound of the word, not just the first letter.
If the word starts with a silent "h," do not use "an."
Example: an hour
No Article:
In some cases, articles are omitted, especially in general statements or when referring to concepts as a whole.
Example: Dogs are loyal animals
----------------------------------------------------------------------------------------------
Expentions :
Some proper nouns (like names of countries, cities, etc.) are usually used without an article.
Example: I live in Canada
----------------------------------------------------------------------------------------------"""
        print(Articles)
    Articles_e()    

#Starting program 9
def program9():
    def hello():
        print('----------------------------------------------------------------------------------------------')
        print('Explaining Countables and uncountables nouns')
    hello()
    def c_e():
        cou_uncou = """
Nouns in English can be categorized into two main types: countable nouns and uncountable nouns. Understanding the difference between them is essential for using articles, quantifiers, and verb agreements correctly.
----------------------------------------------------------------------------------------------
1. Countable Nouns
Countable nouns refer to items that can be counted as individual units. They have both singular and plural forms.
Characteristics:
Can be preceded by a number or quantifiers like "many," "few," "a few," etc.
Have a plural form (usually by adding -s or -es).
Examples:
Singular: apple, book, car
Plural: apples, books, cars
Usage:
Example: I have three apples. (You can count the apples.)
----------------------------------------------------------------------------------------------
2. Uncountable Nouns
Uncountable nouns refer to substances, concepts, or collective categories that cannot be counted as individual units. They do not have a plural form.
Characteristics:
Cannot be preceded by a number directly or quantifiers like "many." Instead, use "much," "some," or "a little."
Typically refer to materials, liquids, abstract ideas, or collective nouns.
Examples:
water, sugar, information, furniture, advice
Usage:
Example: I need some water. (You cannot count water in individual units.)
----------------------------------------------------------------------------------------------
3. Common Mistakes
Using Countable Nouns as Uncountable:
Incorrect: I have three informations.
Correct: I have three pieces of information.
Using Uncountable Nouns as Countable:
Incorrect: I would like a furniture.
Correct: I would like some furniture.
----------------------------------------------------------------------------------------------
4. Some Nouns Can Be Both
Certain nouns can be both countable and uncountable, depending on their meaning.
Examples:
Chicken:
Countable: I have three chickens. (referring to the animals)
Uncountable: I want chicken for dinner. (referring to the meat)
Hair:
Countable: She found three hairs on her shirt. (referring to individual strands)
Uncountable: Her hair is beautiful. (referring to hair as a whole)
----------------------------------------------------------------------------------------------"""
        print(cou_uncou)
    c_e()  

#progarm 10
def program10():
    def hello():
        print('----------------------------------------------------------------------------------------------')
        print('Explaining relative pronouns')
    hello()
    def reli():
        relative_pronouns = """
Relative pronouns are used to connect clauses or phrases to nouns, providing additional information about those nouns. They help in forming relative clauses, which describe or give more details about a noun.
----------------------------------------------------------------------------------------------
1. Common Relative Pronouns
Who: Refers to people.
Example: The teacher who teaches math is very helpful.
----------------------------------------------------------------------------------------------
Whom: Also refers to people but is used in more formal contexts or as the object of a verb or preposition.
Example: The person whom you met yesterday is my friend.
----------------------------------------------------------------------------------------------
Which: Refers to animals or things.
Example: The book which I borrowed was fascinating.
----------------------------------------------------------------------------------------------
That: Can refer to people, animals, or things. It is often used in restrictive clauses.
Example: The car that I bought is blue.
----------------------------------------------------------------------------------------------
Whose: Indicates possession and can refer to people or things.
Example: The student whose project won the award is very talented.
----------------------------------------------------------------------------------------------
2. Types of Relative Clauses
Defining (Restrictive) Relative Clauses: Provide essential information about the noun. These clauses are not set off by commas.
Example: The book that you lent me was amazing. (It specifies which book.)
----------------------------------------------------------------------------------------------
Non-defining (Non-restrictive) Relative Clauses: Provide additional information that is not essential to the meaning of the sentence. These clauses are set off by commas.
Example: My brother, who lives in New York, is visiting. (It adds extra information about my brother but is not essential.)
----------------------------------------------------------------------------------------------
3. Omitting Relative Pronouns
In some cases, the relative pronoun can be omitted, especially when it is the object of the relative clause.
Example:
With pronoun: The book that I read was great.
Without pronoun: The book I read was great.
----------------------------------------------------------------------------------------------
4. Examples of Relative Pronouns in Sentences
Who: The artist who painted this is famous.
Whom: The woman whom I called is my aunt.
Which: The movie which we watched was thrilling.
That: The house that we bought needs renovation.
Whose: The author whose book I enjoy is coming to town
----------------------------------------------------------------------------------------------"""
        print(relative_pronouns)
    reli()        

# Starting question
def starting():
    def hello():
        print('Hello,Dear teachers')
        print('This program is given as a gift to my dear teacher at Bammad Danesh School,Mr Sinafar')
        print('This app has many options : ')
        print(
            '1.Teaching (teach)\n'
            '2.Text reader (t)\n'
            '3.Grammer teacher (g)\n'
            '4.Have got / Has got explaining (hs)\n'
            '5.A history of English language (history)\n'
            '6.Explaining Can (c)\n'
            '7.Explaining be (be)\n'
            '8.Explaining Articles (ar)\n'
            '9.Explaining countables and uncountables (co)\n'
            '10.Explaining relative pronouns (rp)'
        )
    hello()
    def question():
        while True:
            question1 = input("Which option Do you like to use? (if you don't want to use any option,press enter) : ").lower()
            if question1 == 't' or question1 == 'text reader':
                program()
            elif question1 == 'teach': 
                program2()
            elif question1 in ['G','g']:
                program3()
            elif question1 in ['hs','HS']:
                program4() 
            elif question1 in ['history','HISTORY']:
                program5()
            elif question1 in ['c','C']:
                program6()
            elif question1 in ['be','Be']:
                program7() 
            elif question1 in ['Ar','ar']:
                program8()  
            elif question1 in ['co','CO']:
                program9() 
            elif question1 in ['rp','RP']:
                program10()                   
            elif question1 == "":
                print('Ok,Goodbye')
                break    
            else:
                print("Sorry! This option isn't defined")
                continue
    question()        
starting()  
