#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


class HTML(object):

    tagRe = re.compile(r'''<(?:"[^"]*"['"]*|'[^']*'['"]*|[^'">])+>''')
    attrRe = re.compile(r'''([\w-]+)|['"]{1}([^'"]*)['"]{1}''')

    def __init__(self):
        super(HTML, self).__init__()

    @classmethod
    def parse(cls, htmlString):
        start = 0
        end = 0
        tree = {}
        for tag in cls.tagRe.finditer(htmlString):
            if end >= tag.end():
                continue
            start = tag.start()
            end = tag.end()
            string = tag.group(0)
            if string[1] == "/":
                if string == "</html>":
                    return tree
                return tree, start, end
            tagName = string[1:].split()[0].strip(">")
            if tagName.lower() == "!doctype":
                continue
            tagAttr = cls.parseTag(string)
            if "</%s>" % tagName in htmlString:
                if tagName == "script":
                    ret = cls.parseScript(htmlString[end:])
                else:
                    ret = cls.parse(htmlString[end:])
                if ret[0]:
                    tagAttr[tagName]["children"] = ret[0]
                else:
                    tagAttr[tagName]["content"] = htmlString[end:end+ret[1]]
                end += ret[2]
            tree[tagName] = tagAttr[tagName]
        return tree

    @classmethod
    def parseScript(cls, scriptString):
        return [], scriptString.index("</script>"), scriptString.index("</script>")

    @classmethod
    def parseTag(cls, tagString):
        tag = {}
        index = 0
        key = "tagname"
        for attr in cls.attrRe.finditer(tagString):
            if index % 2 == 0:
                tag[key] = attr.group(0)
            else:
                key = attr.group(0)
            index += 1
        tagname = tag["tagname"]
        del tag["tagname"]
        return {tagname: tag}


if __name__ == '__main__':
    from pprint import pprint
    with open("test\\sample0.html", "rb") as fh:
        pprint(HTML.parse(fh.read()))
