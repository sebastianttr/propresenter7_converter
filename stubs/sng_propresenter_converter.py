import io as file
import json
import os
from google.protobuf import text_format, message, reflection
from striprtf.striprtf import rtf_to_text
import playlist_pb2
import applicationInfo_pb2
import propresenter_pb2
import re
from copy import copy
import uuid


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
            template = template.read()
            playlist: playlist_pb2.Playlist = text_format.Parse(template,
                                          playlist_pb2.Playlist(), allow_unknown_field=True)
            
            playlist_doc: propresenter_pb2.PlaylistDocument = text_format.Parse(
                template,
                propresenter_pb2.PlaylistDocument(),
                allow_unknown_field=True
            )

            return playlist, playlist_doc
        except Exception as e:
            print(e)
            return None

def convert_sng_to_pro_file(cue_template):
    playlist, application_info = cue_template

    for (dirpath, dirnames, files) in os.walk('sng_files'):
        for f in files:
            if f.endswith('.sng'):
                with file.open(f'sng_files/{f}','r') as fl:
                    full_str = fl.read()
                    verses_str = full_str[full_str.find('---'):].split('---')

                    cue = playlist.cues[0]

                    cues = []

                    for verse in verses_str:
                        cue_new = copy(cue)
                        rtf_data_text = cue_new.actions[0].slide.presentation.base_slide.elements[0].element.text.rtf_data.decode('cp1252')

                        rtf_data_desc_end_idx = rtf_data_text.find('\n\n') + 1
                        rtf_data_desc = rtf_data_text[0:rtf_data_desc_end_idx]

                        verse_str_unicoded = string_with_unicodes(verse[1:-1])

                        cue_new.uuid.string = str(uuid.uuid4())
                        
                        rtf_data_encoded = (rtf_data_desc + "\n\\f0\\fs84" + verse_str_unicoded + "\n}").replace("\\","\\\\").encode("cp1252")

                        cue_new.actions[0].slide.presentation.base_slide.elements[0].element.text.rtf_data = rtf_data_encoded

                        cues.append("\ncues {\n" + str(cue_new) + "\n}")

                        #print("".join(cues))
                        

                    # print(cue_template)

                    # print(str(application_info) + "".join(cues))
                    
                    file.open("./output_1.txt", "w").write(str(application_info) + "".join(cues))

                    # cues_string = 
                    # print()

def main():
    cue_template = decode_pro_presenter_template()

    convert_sng_to_pro_file(cue_template)

if __name__ == "__main__":
    main()