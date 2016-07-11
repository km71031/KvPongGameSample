#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys

screen_size = (640, 480) # 画面サイズ
# Pygameを初期化
pygame.init()
# SCREEN_SIZEの画面を作成
screen = pygame.display.set_mode(screen_size)
# タイトルバーの文字列をセット
pygame.display.set_caption("ウィンドウの作成")

# ゲームループ
while True:
    screen.fill((0,0,255))   # 画面を青色で塗りつぶす
    pygame.display.update()  # 画面を更新
    # イベント処理
    for event in pygame.event.get():
        if event.type == QUIT:  # 終了イベント
            sys.exit()