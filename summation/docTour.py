# Underlying graphics for turtle is Tkinter

import turtle
import importlib

sc = turtle.Screen()
sc.delay(51)
sc.screensize(500,1300)
tu = turtle.Turtle()
tu.up() # penup
tu.shape('triangle')

def reInitialize():
    sc = turtle.Screen()
    sc.delay(5)
    tu = turtle.Turtle()
    tu.up() # penup
    tu.shape('triangle')

def exitScreen():
    sc = turtle.Screen()
    sc.bye()

msg = "the quick brown fox jumps over the lazy dog"

t = tu

# starting from start position (0,0)
def goToFirstTextSlot():
    t.bk(357)
    t.left(90)
    t.fd(315)
    t.right(90)

# Kind of generic fonts on my system (as of now)
genericFonts = [ 'Bitstream Vera Sans',
                 'Bitstream Vera Sans Mono',
                 'Nimbus Sans Narrow',
                 'URW Bookman',
                 'DejaVu Sans',
                 'DejaVu Sans Mono',
                 'DejaVu Serif',
                 'Nimbus Mono PS',
                 'Bitstream Vera Serif',
                 'Liberation Mono',
                 'Droid Serif',
                 'URW Gothic',
                 'Cantarell',
                 'Liberation Sans',
                 'DejaVu Serif',
                 'Droid Naskh Shift Alt',
                 'Droid Sans',
                 'Akaash',
                 'Mukti Narrow',
                 'Nimbus Sans',
                 'Nimbus Roman',
                 'Droid Sans Mono']

def padFontLst(fontLst=genericFonts):
    maxLen = 0
    for fontName in fontLst:
        maxLen = max(len(fontName))
    resFontLst = []
    for fontName in fontLst:
        resFontLst.append(fontName+ (''*(maxLen - len(fontName))))
    return resFontLst

def printFonts(message=msg, fontLst=genericFonts):
    for fontName in fontLst:
        t.write(fontName + " : " + message, font=(fontName, 13, 'bold'))
        t.right(90)
        t.fd(37)
        t.left(90)

restFonts = ['Serto Jerusalem Outline', 'Estrangelo Edessa', 'Estrangelo Quenneshrin',
             'Droid Arabic Kufi', 'orya', 'Source Code Pro', 'Serto Mardin',  'Estrangelo Talada', 
             'Pothana2000', 'Estrangelo TurAbdin', 'Cantarell', 'Likhan', 'Cascadia Mono',  'Gargi-1.2b',
             'Estrangelo Nisibin Outline', 'malayalam', 
              'Source Code Pro', 'Estrangelo Nisibin',
             'Inconsolata', 'TSCu_Times', 'Standard Symbols PS', 'DejaVu Math TeX Gyre', 
             'East Syriac Ctesiphon', 'Source Code Pro',  'PowerlineSymbols', 'Ligconsolata', 'Mukti Narrow',
             'Cascadia Code',  'Hack',  'C059', 'TAMu_Maduram',   'MalOtf',
             'AkrutiMal2', 'AkrutiMal1',  'Serto Urhoy', 'Sagar', 'AkrutiTml2', 'AkrutiTml1', 'Z003',
             'D050000L', 'TSCu_Comic',  'GurbaniBoliLite',   'Sampige',
             'Estrangelo Antioch',  'TSCu_Paranar', 'Cascadia Code PL',  'Mukti Narrow',  'Source Code Variable',
             'TAMu_Kalyani',  'Source Code Pro', 'Cascadia Mono PL',  'East Syriac Adiabene', 'Serto Malankara',
             'Source Code Pro',    'TAMu_Kadambri', 'Serto Jerusalem', 'P052', 'Serto Batnan', 'padmaa', 
             'Goha-Tibeb Zemen', 'Estrangelo Midyat', 'Serto Kharput']


