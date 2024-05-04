import io as file
import json
import os
from google.protobuf import text_format, message, reflection
from striprtf.striprtf import rtf_to_text
import playlist_pb2
import applicationInfo_pb2
import propresenter_pb2
import presentation_pb2
import re
from copy import copy
import uuid
import subprocess
import codecs

from uuid_pb2 import UUID

romanian_char_unicode = {
    'Ș': '\\u536\\\'e2',
    'Ş': '\\u350\\\'e2',
    'ș': '\\u537\\\'e2',
    'Ț': '\\u538\\\'e2',
    'Ţ': '\\u354\\\'e2',
    'ț': '\\u539\\\'e2',
    'ţ': '\\u355\\\'e2',
    'Â': '\\u194\\\'e2',
    'â': '\\u226\\\'e2',
    'Ă': '\\u258\\\'e2',
    'ă': '\\u259\\\'e2',
    'Ȋ': '\\u206\\\'e2',
    'î': '\\u238\\\'e2',
    'ş': '\\u351\\\'e2',
    '\n': '\\\n '
}

rtf_font_size_100 = "{\\\\rtf1\\\\ansi\\\\ansicpg1252\\\\cocoartf2761\n\\\\cocoatextscaling0\\\\cocoaplatform0{\\\\fonttbl\\\\f0\\\\fswiss\\\\fcharset0 Helvetica;}\n{\\\\colortbl;\\\\red255\\\\green255\\\\blue255;}\n{\\\\*\\\\expandedcolortbl;;}\n\\\\pard\\\\tx560\\\\tx1120\\\\tx1680\\\\tx2240\\\\tx2800\\\\tx3360\\\\tx3920\\\\tx4480\\\\tx5040\\\\tx5600\\\\tx6160\\\\tx6720\\\\slleading700\\\\pardirnatural\\\\qc\\\\partightenfactor0\n\n\\\\f0\\\\fs200 \\\\cf1 \\\\kerning1\\\\expnd20\\\\expndtw100\n\\\\outl0\\\\strokewidth-50 \\\\strokec0"
rtf_font_size_82 = "{\\\\rtf1\\\\ansi\\\\ansicpg1252\\\\cocoartf2761\n\\\\cocoatextscaling0\\\\cocoaplatform0{\\\\fonttbl\\\\f0\\\\fswiss\\\\fcharset0 Helvetica;}\n{\\\\colortbl;\\\\red255\\\\green255\\\\blue255;}\n{\\\\*\\\\expandedcolortbl;;}\n\\\\pard\\\\tx560\\\\tx1120\\\\tx1680\\\\tx2240\\\\tx2800\\\\tx3360\\\\tx3920\\\\tx4480\\\\tx5040\\\\tx5600\\\\tx6160\\\\tx6720\\\\slleading700\\\\pardirnatural\\\\qc\\\\partightenfactor0\n\n\\\\f0\\\\fs164 \\\\cf1 \\\\kerning1\\\\expnd20\\\\expndtw100\n\\\\outl0\\\\strokewidth-50 \\\\strokec0"
rtf_font_size_64 = "{\\\\rtf1\\\\ansi\\\\ansicpg1252\\\\cocoartf2761\n\\\\cocoatextscaling0\\\\cocoaplatform0{\\\\fonttbl\\\\f0\\\\fswiss\\\\fcharset0 Helvetica;}\n{\\\\colortbl;\\\\red255\\\\green255\\\\blue255;}\n{\\\\*\\\\expandedcolortbl;;}\n\\\\pard\\\\tx560\\\\tx1120\\\\tx1680\\\\tx2240\\\\tx2800\\\\tx3360\\\\tx3920\\\\tx4480\\\\tx5040\\\\tx5600\\\\tx6160\\\\tx6720\\\\slleading700\\\\pardirnatural\\\\qc\\\\partightenfactor0\n\n\\\\f0\\\\fs128 \\\\cf1 \\\\kerning1\\\\expnd20\\\\expndtw100\n\\\\outl0\\\\strokewidth-50 \\\\strokec0"


def string_with_unicodes(text):
    def map_chars(chars):
        if (chars in romanian_char_unicode):
            return romanian_char_unicode.get(chars)
        else:
            return chars

    return str("".join(list(map(map_chars, [x for x in text]))))


def get_font_size(text: str):
    lines = text.split("\n")

    max_length = len(max(lines, key=len))

    if max_length > 50:
        return rtf_font_size_64
    elif 30 > max_length > 24:
        return rtf_font_size_82
    elif max_length < 24:
        return rtf_font_size_100

    return rtf_font_size_64


def get_encoding(f):
    f = open(f'sng_files/{f}', 'r', encoding='utf8')
    while True:
        try:
            line = f.readline()
        except UnicodeDecodeError:
            f.close()
            return'iso-8859-1'
            break
        if not line:
            f.close()
            return 'utf8'
            break

    return 'iso-8859-1'


def decode_pro_presenter_template():
    # decode propresenter here
    with open('./template/template.txt') as template:
        try:
            template = template.read()
            playlist: playlist_pb2.Playlist = text_format.Parse(template,
                                                                playlist_pb2.Playlist(), allow_unknown_field=True)
            playlist_doc: propresenter_pb2.PlaylistDocument = text_format.Parse(
                template,
                propresenter_pb2.PlaylistDocument(),
                allow_unknown_field=True
            )

            cue_groups: presentation_pb2.Presentation.CueGroup = text_format.Parse(
                template,
                presentation_pb2.Presentation.CueGroup(),
                allow_unknown_field=True
            )

            return playlist, playlist_doc, cue_groups
        except Exception as e:
            print(e)
            return None


def convert_sng_to_pro_file(cue_template):
    playlist_template, application_info_template, cue_group_template = cue_template

    application_info: propresenter_pb2.PlaylistDocument = application_info_template
    presentation: presentation_pb2.Presentation.CueGroup = cue_group_template
    playlist: playlist_pb2.Playlist = playlist_template

    for (dirpath, dirnames, files) in os.walk('sng_files'):
        for f in files:
            if f.endswith('.sng'):
                encoding = get_encoding(f)

                try:
                    with (file.open(f'sng_files/{f}', 'r', encoding=encoding) as fl):
                        full_str = fl.read()

                        full_str = full_str.replace('--', '---')

                        verses_str = full_str[full_str.find('---'):].split('---')[1:]

                        cue = playlist.cues[0]

                        cues = []

                        cue_group: presentation_pb2.Presentation.CueGroup = presentation_pb2.Presentation.CueGroup()
                        cue_group.group.uuid.string = str(uuid.uuid4()).upper()

                        for verse in verses_str:
                            cue_new = copy(cue)
                            rtf_data_text = cue_new.actions[0].slide.presentation.base_slide.elements[
                                0].element.text.rtf_data.decode('cp1252')

                            rtf_data_desc = get_font_size(verse[1:-1])

                            verse_str_unicoded = string_with_unicodes(verse[1:-1])

                            new_cue_uuid = str(uuid.uuid4()).upper()

                            cue_uuid = UUID()
                            cue_uuid.string = new_cue_uuid.upper()

                            cue_new.uuid.string = new_cue_uuid

                            # print("\n" + verse_str_unicoded)

                            rtf_data_encoded = (rtf_data_desc + ("\n" + verse_str_unicoded + "}")
                                                .replace("\\", "\\\\")
                                                ).encode("cp1252")




                            cue_new.actions[0].slide.presentation.base_slide.uuid.string = str(uuid.uuid4()).upper()

                            cues.append("\ncues {\n" + str(cue_new) + "\n}")

                            cue_group.cue_identifiers.append(cue_uuid)

                        output_uuid = UUID()
                        output_uuid.string = str(uuid.uuid4()).upper()

                        filename = fl.name.replace("sng_files/", "").replace(".sng", "")

                        output_filename = f"{f.replace('.sng', '')}"

                        file.open(f"./output/proto/{output_filename}.txt", "w").write(str(application_info)
                                                                                      + "".join(
                            "\nuuid {\n" + str(output_uuid) + "}\n")
                                                                                      + "".join(f"\nname: \"{filename}\"")
                                                                                      + "".join(
                            "\ncue_groups {\n" + str(cue_group) + "}\n")
                                                                                      + "".join(cues))

                        #subprocess.Popen(
                        #    f'protoc --encode=rv.data.Presentation ./propresenter.proto < "./../output/proto/{output_filename}.txt" > "./../output/propresenter/{output_filename}.pro"',
                        #    shell=True, cwd="./proto_7")
                except Exception as e:
                    print("Error in files: " + f + ": " + str(e))


def main():
    cue_template = decode_pro_presenter_template()

    convert_sng_to_pro_file(cue_template)


if __name__ == "__main__":
    main()
