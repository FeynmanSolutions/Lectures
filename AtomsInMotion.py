#!/usr/bin/env python

"""
This is the source code for the video "Atoms in Motion".
Developed by @Feynman.

Render Command:
manim -p -qh [Filename].py [class_name]

-p          PREVIEW
-a          RENDER ALL SCENES
            IN THE FILE
            (DON'T USE IT WITH -p FLAG)
-ql         LOW QUALITY         480p    15 fps
-qm         MEDIUM QUALITY      720p    30 fps
-qh         HIGHT QUALITY       1080p   60 fps
-qp         PRODUCTION QUALITY  1440p   60 fps
-qk         4K                  2160p   60 fps
-s          RENDER PNG OF THE
            LAST FRAME
-t          TRANSPARENT RENDER
Shorts:
    -pql    PREVIEW IN LOW QUALITY
    -pqm    PREVIEW IN MEDIUM QUALITY
    -pqh    PREVIEW IN HIGHT QUALITY
    -pqp    PREVIEW IN PRODUCTION QUALITY
    -pqk    PREVIEW IN 4K QUALITY
    -ps     RENDER LAST FRAME AS PNG
"""

from manim import *

class DrawBeaker(Scene):
    def construct(self):
        svg = SVGMobject("SVG/beaker.svg")
        self.play(Write(svg), run_time=5)
        self.wait()

class PhysEq(Scene):
    def construct(self):
        physics = Tex("Physics")
        nabla = MathTex(r"curlF\ =\ \nabla\ x\ F")
        nablas = MathTex(r"\nabla^2\ =\ \nabla\ \cdot\ \nabla")
        vector = MathTex(r"\overrightarrow{\text{A}}")
        einstein = MathTex("E = mc^2")
        self.play(Write(vector), run_time = 2)
        self.wait(3)
