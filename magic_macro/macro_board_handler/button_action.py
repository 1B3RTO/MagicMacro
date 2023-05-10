from magic_macro.utils.enums import TriggerType, RepetitionType


class ButtonAction:
    repetition_type: RepetitionType = None
    trigger_type: TriggerType = None
    combination = None

    def __init__(self, repetition_type, trigger_type, combination):
        self.repetition_type = repetition_type
        self.trigger_type = trigger_type
        self.combination = combination
