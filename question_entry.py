import pymongo
from pymongo import ReturnDocument

input_request_text = {
'question_type': '\nHello, What type of question are you inputting?\nPlease choose One of the following:\n(1) Multiple Choice\n(2) Fill in the blank\n(3) True or False\n(4) Best choices\n',
'question_text': '\nPlease enter your question text now:\n',
'set_single_answer': 'Please enter the correct answer below:\n',
'set_correct_choices': 'How many correct choices do you require?\n',
'set_incorrect_choices': 'How many incorrect choices do you require?\n',
'tag_choice': 'Would you like to enter question tags?\n(1) for YES\n(2) for NO\n',
'set_tags': 'Please enter all single word tags in the line below with a single space in between each.\n',
'set_bool': 'What is the answer:\n(1) True\n(2) False\n'
}

class QuestionObject(dict):
    def set_question_type(self):
        retry = True
        while retry == True:
            retry = False
            qtype = input(input_request_text['question_type'])
            if qtype == '1':
                self.type = 'mc'
            elif qtype == '2':
                self.type = 'fib'
            elif qtype == '3':
                self.type = 'bool'
            elif qtype == '4':
                self.type = 'bc'
            else:
                print('Input Error: That choice is not available.')
                retry = True
    def set_question_text(self):
        retry = True
        while retry == True:
            retry = False
            text = input(input_request_text['question_text'])
            self.text = text
    def set_single_answer(self):
        answer = input(input_request_text['set_single_answer'])
        self.answer = answer
    def set_bool_answer(self):
        retry = True
        while retry == True:
            retry = False
            answer = input(input_request_text['set_bool'])
            if answer == '1':
                self.answer = 'true'
            elif answer == '2':
                self.answer = 'false'
            else:
                print('Input Error: That choice is not available.')
                retry = True
    def set_right_choices(self):
        choices = []
        choice_quantity = input(input_request_text['set_correct_choices'])
        for num in range(1,int(choice_quantity)+1):
            choice = input(
            '''Please enter choice {} now:   '''.format(num))
            choices.append(choice)
            self.correct_choices = choices
    def set_wrong_choices(self):
        choices = []
        choice_quantity = input(input_request_text['set_incorrect_choices'])
        for num in range(1,int(choice_quantity)+1):
            choice = input(
            '''Please enter choice {} now:   '''.format(num))
            choices.append(choice)
            self.wrong_choices = choices
    def set_tags(self):
        retry = True
        while retry:
            retry = False
            response = input(input_request_text['tag_choice'])
            if response == '1':
                tags = input(input_request_text['set_tags'])
                tags_list = tags.split(' ')
                self.tags = tags_list
            elif response == '2':
                print('Okay no tags!\n')
            else:
                print('Not a valid choice please try again\n')
                retry = True
    def set_next_sequence(self, seq):
        self.questionID = seq

def run_program():
    Question = QuestionObject()

    Question.set_question_type()
    Question.set_question_text()
    if Question.__getattribute__('type') == 'mc':
        Question.set_single_answer()
        Question.set_wrong_choices()
    if Question.__getattribute__('type') == 'fib':
        Question.set_single_answer()
    if Question.__getattribute__('type') == 'bool':
        Question.set_bool_answer()
    if Question.__getattribute__('type') == 'bc':
         Question.set_right_choices()
         Question.set_wrong_choices()

    Question.set_tags()
    print(Question.__dict__)


    # establish a connection to the database
    connection = pymongo.MongoClient("mongodb://localhost:27017")
    db = connection.text2learn
    #db.drop_collection('questions')
    questions = db.questions

    def getNextSequence(name):
        counters = db.counters
        result = counters.find_one_and_update(
            { '_id': name },
            { '$inc': { 'seq': 1 }},
            projection={'seq': True, '_id': False},
            upsert=True,
            return_document=ReturnDocument.AFTER
        )
        return int(result['seq'])

    seq = getNextSequence("questionID")

    Question.set_next_sequence(seq)


    response = questions.insert_one(Question.__dict__)
    if response.acknowledged:
        print('\nYour question has been saved to the text2learn database\nObjectId: {}'.format(response.inserted_id))
    else:
        print('Something happened bad')

if __name__ == "__main__":
    run_program()
