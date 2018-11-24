from mycroft import MycroftSkill, intent_file_handler


class History(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('history.intent')
    def handle_history(self, message):
        self.speak_dialog('history')


def create_skill():
    return History()

