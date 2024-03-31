import io as file
import json
import os
from google.protobuf import text_format, message, reflection
from striprtf.striprtf import rtf_to_text
import playlist_pb2
from PyRTF.Elements import Document, Section
import re

romanian_char_unicode = {
    'Ș':'\\u536\\\'e2',
    'ș':'\\u537\\\'e2',
    'Ț':'\\u538\\\'e2',
    'ț':'\\u539\\\'e2',
    'Â':'\\u194\\\'e2',
    'â':'\\u226\\\'e2',
    'Ă':'\\u258\\\'e2',
    'ă':'\\u259\\\'e2',
    'Î':'\\u206\\\'e2',
    'î':'\\u238\\\'e2',
    '\n':'\\\n'
}


def string_with_unicodes(text):
    def map_chars(chars):
        if(chars in romanian_char_unicode):
            return romanian_char_unicode.get(chars)
        else: return chars

    return str("".join(list(map(map_chars,[x for x in text]))))


def decode_pro_presenter_template():
    # decode propresenter here
    with open('propresenter_template.txt') as template:
        try:
            proto_obj: playlist_pb2.Playlist = text_format.Parse(template.read(),
                                          playlist_pb2.Playlist(), allow_unknown_field=True)
            return proto_obj
        except Exception as e:
            print(e)
            return None

def convert_sng_to_pro_file(cue_template):
    for (dirpath, dirnames, files) in os.walk('sng_files'):
        for f in files:
            if f.endswith('.sng'):
                with file.open(f'sng_files/{f}','r') as fl:
                    full_str = fl.read()
                    verses_str = full_str[full_str.find('---') + 4:].split('---')

                    cue = cue_template.cues[0]
                    rtf_data_text = cue.actions[0].slide.presentation.base_slide.elements[0].element.text.rtf_data.decode('cp1252')

                    # remove text from rtf
                    rtf_data_desc_end_idx = rtf_data_text.find('\n\n') + 1
                    rtf_data_desc = rtf_data_text[0:rtf_data_desc_end_idx]

                    verse_str_unicoded = string_with_unicodes(verses_str[0])

                    print(f'{rtf_data_desc}\n\\f0\\fs84{verse_str_unicoded}{"}"}')

def main():
    cue_template = decode_pro_presenter_template()

    convert_sng_to_pro_file(cue_template)

if __name__ == "__main__":
    main()