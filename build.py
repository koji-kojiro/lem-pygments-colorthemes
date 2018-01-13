#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import pygments.styles
from x256 import x256
from pygments.token import Text

translation_map = {
    "syntax-warning": "Token.Error",
    "syntax-string": "Token.Literal.String",
    "syntax-comment": "Token.Comment",
    "syntax-keyword": "Token.Keyword",
    "syntax-constant": "Token.Name.Constant",
    "syntax-function-name": "Token.Name.Function",
    "syntax-variable": "Token.Name.Variable",
    "syntax-type": "Token.Keyword.Type",
    "syntax-builtin": "Token.Name.Builtin",
}

template = """\
(in-package :lem-user)

(define-color-theme \"{name}\" ()
  (foreground {fg})
  (background {bg})
{body})
"""

def parse(style_string):
    for s in  style_string.split():
        if s.startswith("#"):
            ix = s[1:] if len(s) == 7 else "".join(_ * 2 for _ in s[1:])
            c = x256.to_rgb(x256.from_hex(ix))
            return "\"#{:02x}{:02x}{:02x}\"".format(*c)
    return "nil"

def translate(style_dict):
    return dict((k, style_dict[v]) for k, v in translation_map.items())

def load_style(name):
    style =  pygments.styles.get_style_by_name(name)
    bg = parse(style.background_color)
    fg = parse(style.styles[Text])
    if fg == "nil":
        brightness =  sum(x256.to_rgb(x256.from_hex(bg[2:-1]))) / 3
        fg = "\"#000000\"" if brightness >= 128 else "\"#FFFFFF\""
    style_dict = dict((str(k), parse(v)) for k, v in style.styles.items())
    return bg, fg, translate(style_dict)

def build_theme(name):
    bg, fg, attributes = load_style(name)
    body = "  (cursor :foreground {} :background {})\n".format(bg, fg)
    body += "\n".join(
            "  ({}-attribute :foreground {} :background {})".format(*_, bg)
            for _ in attributes.items())
    with open("themes/{}.lisp".format(name), "w") as f:
        f.write(template.format(name=name, bg=bg, fg=fg, body=body))
 

if __name__ == "__main__":
    for name in pygments.styles.get_all_styles():
        build_theme(name)
