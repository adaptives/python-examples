import os
import re

"""
def find_msg_files(d):
    msg_files = []
    for f in os.listdir(d):
        if f.endswith('.msg'):
            msg_files.append(f)
    return msg_files
"""

def get_all_msgs():
    msgs = []
    msg_file_names = find_msg_files('c:/temp')
    for msg_file_name in msg_file_names:
        msgs.append(parse_msg_file(msg_file_name))
    return msgs
    
def find_msg_files(d):
    return [f for f in os.listdir(d) if f.endswith('.msg')]

def parse_msg_file(fname):
    fp = open(fname, 'r')
    reading_body = False
    ffrom = ""
    to = ""
    cc = ""
    tstamp = ""
    mime = ""
    body = ""
    for line in fp.readlines():
        if reading_body:
            body += line
        else:
            if line.startswith('to: '):
                to = line[len('to: '):]
                to = __remove_newline_chars(to)
            elif line.startswith('from: '):
                ffrom = line[len('from: '):]
                ffrom = __remove_newline_chars(ffrom)
            elif line.startswith('cc: '):
                cc = line[len('cc: '):]
                cc = __remove_newline_chars(cc)
            elif line.startswith('tstamp: '):
                tstamp = line[len('tstamp: '):]
                tstamp = __remove_newline_chars(tstamp)
            elif line.startswith('mime: '):
                mime = line[len('mime: '):]
                mime = __remove_newline_chars(mime)
            elif line.startswith('body:'):
                reading_body = True
                
    return Msg(to=to, ffrom=ffrom, cc=cc, tstamp=tstamp, mime=mime, body=body)

def __remove_newline_chars(s):
    s = s.replace('\n','')
    s = s.replace('\r', '')
    return s

class Msg(object):
    def __init__(self, ffrom="", to="", cc="", tstamp="", mime="", body=""):
        self.ffrom = ffrom
        self.to = []
        self.cc = []
        self.tstamp = tstamp
        self.mime = mime
        self.body = body
        self.to = re.split(',\s*', to)
        if '' in self.to:
            self.to.remove('')
        self.cc = re.split(',\s*', cc)
        if '' in self.cc:
            self.cc.remove('')

    def __str__(self):
        return """
from: %s
to: %s
cc: %s
mime: %s
tstamp: %s
body: %s""" % (self.ffrom, self.to, self.cc, self.mime, self.tstamp, self.body)


        
    
if "__main__" == __name__:
    print find_msg_files('c:/temp')
