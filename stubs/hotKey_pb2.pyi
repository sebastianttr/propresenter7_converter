from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HotKey(_message.Message):
    __slots__ = ("code", "control_identifier")
    class KeyCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        KEY_CODE_UNKNOWN: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_A: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_B: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_C: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_D: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_E: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_F: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_G: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_H: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_I: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_J: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_K: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_L: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_M: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_N: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_O: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_P: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_Q: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_R: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_S: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_T: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_U: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_V: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_W: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_X: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_Y: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_Z: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_0: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_1: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_2: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_3: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_4: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_5: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_6: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_7: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_8: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_9: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_EQUAL: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_MINUS: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_RIGHT_BRACKET: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_LEFT_BRACKET: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_QUOTE: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_SEMICOLON: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_BACKSLASH: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_COMMA: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_SLASH: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_PERIOD: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_GRAVE: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_KEYPAD_DECIMAL: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_KEYPAD_PLUS: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_KEYPAD_CLEAR: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_KEYPAD_DIVIDE: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_KEYPAD_ENTER: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_KEYPAD_MINUS: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_KEYPAD_EQUALS: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_KEYPAD_0: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_KEYPAD_1: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_KEYPAD_2: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_KEYPAD_3: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_KEYPAD_4: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_KEYPAD_5: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_KEYPAD_6: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_KEYPAD_7: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_KEYPAD_8: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ANSI_KEYPAD_9: _ClassVar[HotKey.KeyCode]
        KEY_CODE_F1: _ClassVar[HotKey.KeyCode]
        KEY_CODE_F2: _ClassVar[HotKey.KeyCode]
        KEY_CODE_F3: _ClassVar[HotKey.KeyCode]
        KEY_CODE_F4: _ClassVar[HotKey.KeyCode]
        KEY_CODE_F5: _ClassVar[HotKey.KeyCode]
        KEY_CODE_F6: _ClassVar[HotKey.KeyCode]
        KEY_CODE_F7: _ClassVar[HotKey.KeyCode]
        KEY_CODE_F8: _ClassVar[HotKey.KeyCode]
        KEY_CODE_F9: _ClassVar[HotKey.KeyCode]
        KEY_CODE_F10: _ClassVar[HotKey.KeyCode]
        KEY_CODE_F11: _ClassVar[HotKey.KeyCode]
        KEY_CODE_F12: _ClassVar[HotKey.KeyCode]
        KEY_CODE_F13: _ClassVar[HotKey.KeyCode]
        KEY_CODE_F14: _ClassVar[HotKey.KeyCode]
        KEY_CODE_F15: _ClassVar[HotKey.KeyCode]
        KEY_CODE_F16: _ClassVar[HotKey.KeyCode]
        KEY_CODE_F17: _ClassVar[HotKey.KeyCode]
        KEY_CODE_F18: _ClassVar[HotKey.KeyCode]
        KEY_CODE_F19: _ClassVar[HotKey.KeyCode]
        KEY_CODE_F20: _ClassVar[HotKey.KeyCode]
        KEY_CODE_FUNCTION: _ClassVar[HotKey.KeyCode]
        KEY_CODE_RETURN: _ClassVar[HotKey.KeyCode]
        KEY_CODE_TAB: _ClassVar[HotKey.KeyCode]
        KEY_CODE_SPACE: _ClassVar[HotKey.KeyCode]
        KEY_CODE_DELETE: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ESCAPE: _ClassVar[HotKey.KeyCode]
        KEY_CODE_COMMAND: _ClassVar[HotKey.KeyCode]
        KEY_CODE_SHIFT: _ClassVar[HotKey.KeyCode]
        KEY_CODE_CAPS_LOCK: _ClassVar[HotKey.KeyCode]
        KEY_CODE_OPTION: _ClassVar[HotKey.KeyCode]
        KEY_CODE_CONTROL: _ClassVar[HotKey.KeyCode]
        KEY_CODE_RIGHT_SHIFT: _ClassVar[HotKey.KeyCode]
        KEY_CODE_RIGHT_OPTION: _ClassVar[HotKey.KeyCode]
        KEY_CODE_RIGHT_CONTROL: _ClassVar[HotKey.KeyCode]
        KEY_CODE_VOLUME_UP: _ClassVar[HotKey.KeyCode]
        KEY_CODE_VOLUME_DOWN: _ClassVar[HotKey.KeyCode]
        KEY_CODE_MUTE: _ClassVar[HotKey.KeyCode]
        KEY_CODE_HELP: _ClassVar[HotKey.KeyCode]
        KEY_CODE_HOME: _ClassVar[HotKey.KeyCode]
        KEY_CODE_PAGE_UP: _ClassVar[HotKey.KeyCode]
        KEY_CODE_FORWARD_DELETE: _ClassVar[HotKey.KeyCode]
        KEY_CODE_END: _ClassVar[HotKey.KeyCode]
        KEY_CODE_PAGE_DOWN: _ClassVar[HotKey.KeyCode]
        KEY_CODE_LEFT_ARROW: _ClassVar[HotKey.KeyCode]
        KEY_CODE_RIGHT_ARROW: _ClassVar[HotKey.KeyCode]
        KEY_CODE_DOWN_ARROW: _ClassVar[HotKey.KeyCode]
        KEY_CODE_UP_ARROW: _ClassVar[HotKey.KeyCode]
        KEY_CODE_ISO_SELECTION: _ClassVar[HotKey.KeyCode]
        KEY_CODE_JIS_YEN: _ClassVar[HotKey.KeyCode]
        KEY_CODE_JIS_UNDERSCORE: _ClassVar[HotKey.KeyCode]
        KEY_CODE_JIS_KEYPAD_COMMA: _ClassVar[HotKey.KeyCode]
        KEY_CODE_JIS_EISU: _ClassVar[HotKey.KeyCode]
        KEY_CODE_JIS_KANA: _ClassVar[HotKey.KeyCode]
    KEY_CODE_UNKNOWN: HotKey.KeyCode
    KEY_CODE_ANSI_A: HotKey.KeyCode
    KEY_CODE_ANSI_B: HotKey.KeyCode
    KEY_CODE_ANSI_C: HotKey.KeyCode
    KEY_CODE_ANSI_D: HotKey.KeyCode
    KEY_CODE_ANSI_E: HotKey.KeyCode
    KEY_CODE_ANSI_F: HotKey.KeyCode
    KEY_CODE_ANSI_G: HotKey.KeyCode
    KEY_CODE_ANSI_H: HotKey.KeyCode
    KEY_CODE_ANSI_I: HotKey.KeyCode
    KEY_CODE_ANSI_J: HotKey.KeyCode
    KEY_CODE_ANSI_K: HotKey.KeyCode
    KEY_CODE_ANSI_L: HotKey.KeyCode
    KEY_CODE_ANSI_M: HotKey.KeyCode
    KEY_CODE_ANSI_N: HotKey.KeyCode
    KEY_CODE_ANSI_O: HotKey.KeyCode
    KEY_CODE_ANSI_P: HotKey.KeyCode
    KEY_CODE_ANSI_Q: HotKey.KeyCode
    KEY_CODE_ANSI_R: HotKey.KeyCode
    KEY_CODE_ANSI_S: HotKey.KeyCode
    KEY_CODE_ANSI_T: HotKey.KeyCode
    KEY_CODE_ANSI_U: HotKey.KeyCode
    KEY_CODE_ANSI_V: HotKey.KeyCode
    KEY_CODE_ANSI_W: HotKey.KeyCode
    KEY_CODE_ANSI_X: HotKey.KeyCode
    KEY_CODE_ANSI_Y: HotKey.KeyCode
    KEY_CODE_ANSI_Z: HotKey.KeyCode
    KEY_CODE_ANSI_0: HotKey.KeyCode
    KEY_CODE_ANSI_1: HotKey.KeyCode
    KEY_CODE_ANSI_2: HotKey.KeyCode
    KEY_CODE_ANSI_3: HotKey.KeyCode
    KEY_CODE_ANSI_4: HotKey.KeyCode
    KEY_CODE_ANSI_5: HotKey.KeyCode
    KEY_CODE_ANSI_6: HotKey.KeyCode
    KEY_CODE_ANSI_7: HotKey.KeyCode
    KEY_CODE_ANSI_8: HotKey.KeyCode
    KEY_CODE_ANSI_9: HotKey.KeyCode
    KEY_CODE_ANSI_EQUAL: HotKey.KeyCode
    KEY_CODE_ANSI_MINUS: HotKey.KeyCode
    KEY_CODE_ANSI_RIGHT_BRACKET: HotKey.KeyCode
    KEY_CODE_ANSI_LEFT_BRACKET: HotKey.KeyCode
    KEY_CODE_ANSI_QUOTE: HotKey.KeyCode
    KEY_CODE_ANSI_SEMICOLON: HotKey.KeyCode
    KEY_CODE_ANSI_BACKSLASH: HotKey.KeyCode
    KEY_CODE_ANSI_COMMA: HotKey.KeyCode
    KEY_CODE_ANSI_SLASH: HotKey.KeyCode
    KEY_CODE_ANSI_PERIOD: HotKey.KeyCode
    KEY_CODE_ANSI_GRAVE: HotKey.KeyCode
    KEY_CODE_ANSI_KEYPAD_DECIMAL: HotKey.KeyCode
    KEY_CODE_ANSI_KEYPAD_PLUS: HotKey.KeyCode
    KEY_CODE_ANSI_KEYPAD_CLEAR: HotKey.KeyCode
    KEY_CODE_ANSI_KEYPAD_DIVIDE: HotKey.KeyCode
    KEY_CODE_ANSI_KEYPAD_ENTER: HotKey.KeyCode
    KEY_CODE_ANSI_KEYPAD_MINUS: HotKey.KeyCode
    KEY_CODE_ANSI_KEYPAD_EQUALS: HotKey.KeyCode
    KEY_CODE_ANSI_KEYPAD_0: HotKey.KeyCode
    KEY_CODE_ANSI_KEYPAD_1: HotKey.KeyCode
    KEY_CODE_ANSI_KEYPAD_2: HotKey.KeyCode
    KEY_CODE_ANSI_KEYPAD_3: HotKey.KeyCode
    KEY_CODE_ANSI_KEYPAD_4: HotKey.KeyCode
    KEY_CODE_ANSI_KEYPAD_5: HotKey.KeyCode
    KEY_CODE_ANSI_KEYPAD_6: HotKey.KeyCode
    KEY_CODE_ANSI_KEYPAD_7: HotKey.KeyCode
    KEY_CODE_ANSI_KEYPAD_8: HotKey.KeyCode
    KEY_CODE_ANSI_KEYPAD_9: HotKey.KeyCode
    KEY_CODE_F1: HotKey.KeyCode
    KEY_CODE_F2: HotKey.KeyCode
    KEY_CODE_F3: HotKey.KeyCode
    KEY_CODE_F4: HotKey.KeyCode
    KEY_CODE_F5: HotKey.KeyCode
    KEY_CODE_F6: HotKey.KeyCode
    KEY_CODE_F7: HotKey.KeyCode
    KEY_CODE_F8: HotKey.KeyCode
    KEY_CODE_F9: HotKey.KeyCode
    KEY_CODE_F10: HotKey.KeyCode
    KEY_CODE_F11: HotKey.KeyCode
    KEY_CODE_F12: HotKey.KeyCode
    KEY_CODE_F13: HotKey.KeyCode
    KEY_CODE_F14: HotKey.KeyCode
    KEY_CODE_F15: HotKey.KeyCode
    KEY_CODE_F16: HotKey.KeyCode
    KEY_CODE_F17: HotKey.KeyCode
    KEY_CODE_F18: HotKey.KeyCode
    KEY_CODE_F19: HotKey.KeyCode
    KEY_CODE_F20: HotKey.KeyCode
    KEY_CODE_FUNCTION: HotKey.KeyCode
    KEY_CODE_RETURN: HotKey.KeyCode
    KEY_CODE_TAB: HotKey.KeyCode
    KEY_CODE_SPACE: HotKey.KeyCode
    KEY_CODE_DELETE: HotKey.KeyCode
    KEY_CODE_ESCAPE: HotKey.KeyCode
    KEY_CODE_COMMAND: HotKey.KeyCode
    KEY_CODE_SHIFT: HotKey.KeyCode
    KEY_CODE_CAPS_LOCK: HotKey.KeyCode
    KEY_CODE_OPTION: HotKey.KeyCode
    KEY_CODE_CONTROL: HotKey.KeyCode
    KEY_CODE_RIGHT_SHIFT: HotKey.KeyCode
    KEY_CODE_RIGHT_OPTION: HotKey.KeyCode
    KEY_CODE_RIGHT_CONTROL: HotKey.KeyCode
    KEY_CODE_VOLUME_UP: HotKey.KeyCode
    KEY_CODE_VOLUME_DOWN: HotKey.KeyCode
    KEY_CODE_MUTE: HotKey.KeyCode
    KEY_CODE_HELP: HotKey.KeyCode
    KEY_CODE_HOME: HotKey.KeyCode
    KEY_CODE_PAGE_UP: HotKey.KeyCode
    KEY_CODE_FORWARD_DELETE: HotKey.KeyCode
    KEY_CODE_END: HotKey.KeyCode
    KEY_CODE_PAGE_DOWN: HotKey.KeyCode
    KEY_CODE_LEFT_ARROW: HotKey.KeyCode
    KEY_CODE_RIGHT_ARROW: HotKey.KeyCode
    KEY_CODE_DOWN_ARROW: HotKey.KeyCode
    KEY_CODE_UP_ARROW: HotKey.KeyCode
    KEY_CODE_ISO_SELECTION: HotKey.KeyCode
    KEY_CODE_JIS_YEN: HotKey.KeyCode
    KEY_CODE_JIS_UNDERSCORE: HotKey.KeyCode
    KEY_CODE_JIS_KEYPAD_COMMA: HotKey.KeyCode
    KEY_CODE_JIS_EISU: HotKey.KeyCode
    KEY_CODE_JIS_KANA: HotKey.KeyCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    CONTROL_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    code: HotKey.KeyCode
    control_identifier: str
    def __init__(self, code: _Optional[_Union[HotKey.KeyCode, str]] = ..., control_identifier: _Optional[str] = ...) -> None: ...
