from mycroft import MycroftSkill, intent_file_handler

from underwater_adventure import parse_input


class UnderwaterAdventure(MycroftSkill):
    def __init__(self):
        super().__init__()
        self.started = False

    @intent_file_handler('adventure.underwater.intent')
    def handle_adventure_underwater(self, message):
        self.speak_dialog('adventure.underwater')
        self.started = True
        self.speak(parse_input('look').replace('\n', '. '),
                   expect_response=True)

    def converse(self, utterances, lang):
        self.log.info('CONVERSE!!!!')
        self.log.info(utterances)
        utt = utterances[0] if utterances else ''
        if self.started:
            if utt != 'quit':
                self.speak(parse_input(utt), expect_response=True)
                return True
            else:
                self.started = False
                return True

        return False


def create_skill():
    return UnderwaterAdventure()
