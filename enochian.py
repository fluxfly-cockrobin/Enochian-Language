import sys
x = sys.argv[1]
n = ""
o = ""
v = ""
for i in x:
    if i.lower() == "a":
        n += "un"
        o += "taurus "
        v += "hierophant "
    if i.lower() == "b":
        n += "pe"
        o += "aries "
        v += "star "
    if i.lower() == "c" or i.lower() == "k":
        n += "veh"
        o += "fire "
        v += "judgement/aeon "
    if i.lower() == "d":
        n += "gal"
        o += "spirit "
        v += "empress "
    if i.lower() == "e":
        n += "graph"
        o += "virgo "
        v += "hermit "
    if i.lower() == "f":
        n += "orth"
        o += "cauda draconis "
        v += "juggler "
    if i.lower() == "g":
        n += "ged"
        o += "cancer "
        v += "chariot "
    if i.lower() == "h":
        n += "na-hath"
        o += "air "
        v += "fool "
    if i.lower() == "i" or i.lower() == "y" or i.lower() == "j":
        n += "gon"
        o += "sagittarius "
        v += "temperance/art "
    if i.lower() == "l":
        n += "ur"
        o += "cancer "
        v += "chariot "
    if i.lower() == "m":
        n += "tal"
        o += "aquarius "
        v += "emperor "
    if i.lower() == "n":
        n += "drun"
        o += "scorpio "
        v += "death "
    if i.lower() == "o":
        n += "med"
        o += "libra "
        v += "justice "
    if i.lower() == "p":
        n += "mals"
        o += "leo "
        v += "strength/lust "
    if i.lower() == "q":
        n += "ger"
        o += "water "
        v += "hanged man "
    if i.lower() == "r":
        n += "don"
        o += "pisces "
        v += "moon "
    if i.lower() == "s":
        n += "fam"
        o += "gemini "
        v += "lovers "
    if i.lower() == "t":
        n += "gisa"
        o += "leo "
        v += "strength/lust "
    if i.lower() == "u" or i.lower() == "v" or i.lower() == "w":
        n += "vau"
        o += "capricorn "
        v += "devil "
    if i.lower() == "x":
        n += "pal"
        o += "earth "
        v += "universe "
    if i.lower() == "z":
        n += "ceph"
        o += "leo "
        v += "strength/lust"
    if i == " ":
        n += " "

print(("word:"+n +"\r\nPlanetary/Element Correspondence:"+o+"\r\nTarot Correspondence:"+v))