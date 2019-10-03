from mycroft import MycroftSkill, intent_file_handler


class UnderwaterAdventure(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('adventure.underwater.intent')
    def handle_adventure_underwater(self, message):
        self.speak_dialog('adventure.underwater')


def create_skill():
    return UnderwaterAdventure()

