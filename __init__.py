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

    def handle_game_input(self, utterance):
        if utterance not in self.translate_list('quit'):
            game_response = parse_input(utterance)
            if game_response:
                self.speak(game_response, expect_response=True)
            else:
                self.speak_dialog("didnt.understand")
            return True
        else:
            self.started = False
            self.speak_dialog("leave.game")
            return True

    def converse(self, utterances, lang):
        self.log.debug(utterances)
        utt = utterances[0] if utterances else ''
        if self.started:
            return self.handle_game_input(utt)
        else:
            return False


def create_skill():
    return UnderwaterAdventure()
