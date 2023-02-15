from magic_macro.utils.enums import TriggerType, RepetitionType


class ButtonAction:
    repetition_type: RepetitionType = None
    trigger_type: TriggerType = None
    method = None

    def __init__(self, repetition_type, trigger_type, method):
        self.repetition_type = repetition_type
        self.trigger_type = trigger_type
        self.method = method
