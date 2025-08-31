import sys
x = sys.argv[1]
n = ""
o = ""
v = ""
g = 0
for i in x:
    if i.lower() == "a":
        n += "un"
        o += "taurus "
        v += "hierophant "
        g += 6
    if i.lower() == "b":
        n += "pe"
        o += "aries "
        v += "star "
        g += 5
    if i.lower() == "c" or i.lower() == "k":
        n += "veh"
        o += "fire "
        v += "judgement/aeon "
        g += 300
    if i.lower() == "d":
        n += "gal"
        o += "spirit "
        v += "empress "
        g += 4
    if i.lower() == "e":
        n += "graph"
        o += "virgo "
        v += "hermit "
        g += 10
    if i.lower() == "f":
        n += "orth"
        o += "cauda draconis "
        v += "juggler "
        g += 3
    if i.lower() == "g":
        n += "ged"
        o += "cancer "
        v += "chariot "
        g += 8
    if i.lower() == "h":
        n += "na-hath"
        o += "air "
        v += "fool "
        g += 1
    if i.lower() == "i" or i.lower() == "y" or i.lower() == "j":
        n += "gon"
        o += "sagittarius "
        v += "temperance/art "
        g += 60
    if i.lower() == "l":
        n += "ur"
        o += "cancer "
        v += "chariot "
        g += 8
    if i.lower() == "m":
        n += "tal"
        o += "aquarius "
        v += "emperor "
        g += 90
    if i.lower() == "n":
        n += "drun"
        o += "scorpio "
        v += "death "
        g += 50
    if i.lower() == "o":
        n += "med"
        o += "libra "
        v += "justice "
        g += 30
    if i.lower() == "p":
        n += "mals"
        o += "leo "
        v += "strength/lust "
        g += 9
    if i.lower() == "q":
        n += "ger"
        o += "water "
        v += "hanged man "
        g += 40
    if i.lower() == "r":
        n += "don"
        o += "pisces "
        v += "moon "
        g += 100
    if i.lower() == "s":
        n += "fam"
        o += "gemini "
        v += "lovers "
        g += 7
    if i.lower() == "t":
        n += "gisa"
        o += "leo "
        v += "strength/lust "
        g += 9
    if i.lower() == "u" or i.lower() == "v" or i.lower() == "w":
        n += "vau"
        o += "capricorn "
        v += "devil "
        g += 70
    if i.lower() == "x":
        n += "pal"
        o += "earth "
        v += "universe "
        g += 400
    if i.lower() == "z":
        n += "ceph"
        o += "leo "
        v += "strength/lust"
        g += 9
    if i == " ":
        n += " "

print(("word:"+n +"\r\nPlanetary/Element Correspondence:"+o+"\r\nTarot Correspondence:"+v+"\r\nGematria value:"+str(g)))
