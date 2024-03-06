from ovos_workshop.decorators import intent_handler
from ovos_workshop.skills import OVOSSkill
from underwater_adventure import parse_input


class UnderwaterAdventure(OVOSSkill):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.started = False

    @intent_handler('adventure.underwater.intent')
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
