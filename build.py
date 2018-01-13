#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import pygments.styles
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
  (foreground \"{fg}\")
  (background \"{bg}\")
{body})
"""

def parse(style_string):
    for s in  style_string.split():
        if s.startswith("#"):
            return "\"{}\"".format(s)
    return "nil"

def translate(style_dict):
    return dict((k, style_dict[v]) for k, v in translation_map.items())

def load_style(name):
    style =  pygments.styles.get_style_by_name(name)
    bg = style.background_color
    fg = style.styles[Text]
    if not fg:
        brightness = sum((int(bg[1:3],16),int(bg[3:5],16),int(bg[5:7],16))) / 3
        fg = "#000000" if brightness >= 128 else "#ffffff"
    style_dict = dict((str(k), parse(v)) for k, v in style.styles.items())
    return bg, fg, translate(style_dict)

def build_theme(name):
    bg, fg, attributes = load_style(name)

    body = "\n".join(
            "  ({}-attribute :foreground {} :background \"{}\")".format(*_, bg)
            for _ in attributes.items())
    with open("themes/{}.lisp".format(name), "w") as f:
        f.write(template.format(name=name, bg=bg, fg=fg, body=body))
 

if __name__ == "__main__":
    for name in pygments.styles.get_all_styles():
        build_theme(name)
