import io as file
import json
import os
from google.protobuf import text_format, message, reflection
from striprtf.striprtf import rtf_to_text

import playlist_pb2


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
                with file.open(f'sng_files/{f}') as fl:
                    full_str = fl.read()
                    verses_str = full_str[full_str.find('---') + 3:].split('---')

                    cue = cue_template.cues[0]
                    rtf_data_text = cue.actions[0].slide.presentation.base_slide.elements[0].element.text.rtf_data.decode('utf-8')

                    text = rtf_to_text(rtf_data_text)

                    print(text)

def main():
    cue_template = decode_pro_presenter_template()

    convert_sng_to_pro_file(cue_template)

if __name__ == "__main__":
    main()