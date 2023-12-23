from mycroft import MycroftSkill, intent_file_handler


class DeconzControl(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('control.deconz.intent')
    def handle_control_deconz(self, message):
        device = ''
        status = ''

        self.speak_dialog('control.deconz', data={
            'device': device,
            'status': status
        })


def create_skill():
    return DeconzControl()

