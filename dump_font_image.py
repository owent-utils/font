#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os, platform
import pygame
from optparse import OptionParser
from pygame.locals import *

console_encoding = sys.getfilesystemencoding()

usage = "usage: %prog [options...] <format message> [format parameters...]"
parser = OptionParser(usage)

parser.add_option("-v", "--version", action="store_true", help="show version and exit", dest="version")
parser.add_option("-f", "--font", action="store", help="set font file path", metavar="<font file>", dest="font")
parser.add_option("-s", "--size", action="append", help="specify font sizes", metavar="<size>", dest="size", default=[])
parser.add_option("-c", "--color", action="store", help="set color", metavar="<color code>", dest="color", default="0,0,0")
parser.add_option("-g", "--background-color", action="store", help="set background color", metavar="<color code>", dest="background_color", default="255,255,255")
parser.add_option("-o", "--output-file", action="store", help="output file path", metavar="<output file>", dest="output", default='font_test.png')
parser.add_option("-i", "--italic", action="store_true", help="set font italic", dest="italic", default=False)
parser.add_option("-u", "--underline", action="store_true", help="set font underline", dest="underline", default=False)
parser.add_option("-b", "--bold", action="store_true", help="set font bold", dest="bold", default=False)
parser.add_option("-r", "--vertical-spacing", action="store", help="set vertical spacing", metavar="<vertical spacing>", dest="vertical_spacing", type='int',default=5)
parser.add_option("-m", "--smooth", action="store_true", help="set font smooth", dest="smooth", default=True)

(options, left_args) = parser.parse_args()

if options.version:
    print('1.0.0.0')
    exit(0)

if not options.font:
    print('font file is required.')
    parser.print_help()
    exit(-1)

if len(left_args) > 0:
    # pygame初始化
    pygame.init()
    all_size = options.size
    if len(all_size) == 0:
        all_size = [9, 12, 14, 16, 18, 22, 24, 28, 32, 36, 72, 96, 128]

    show_text = ' '.join(left_args)
    all_font_ftext = []
    sum_height = 0
    max_width = 0
    front_color = options.color.split(',')
    back_color = options.background_color.split(',')
    for font_size in all_size:
        # 设置字体和字号
        font = pygame.font.Font(options.font, font_size)
        # 渲染图片，设置背景颜色和字体样式,前面的颜色是字体颜色

        font.set_italic(options.italic)
        font.set_underline(options.underline)
        font.set_bold(options.bold)

        sum_height = sum_height + font.get_height() + options.vertical_spacing

        ftext = font.render('Size=' + str(font_size) + ': ' + show_text, options.smooth, (int(front_color[0]), int(front_color[1]), int(front_color[2])), (int(back_color[0]), int(back_color[1]), int(back_color[2])))
        all_font_ftext.append(ftext)
        max_width = max(max_width, ftext.get_width())

    root = pygame.Surface((max_width, sum_height))
    root.fill((int(back_color[0]), int(back_color[1]), int(back_color[2])))
    start_height = 0
    for ftext in all_font_ftext:
        root.blit(ftext, (0, start_height))
        start_height = start_height + ftext.get_height() + options.vertical_spacing

    # 保存图片
    pygame.image.save(root, options.output) # 图片保存地址
