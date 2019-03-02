from string import ascii_lowercase

shift = 2
text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
shifted_ascii = 'yzabcdefghijklmnopqrstuvwx'
text = "map"
shifted_ascii = [ascii_lowercase]

out = ''
for l in text:
    if l in ascii_lowercase:
        i = shifted_ascii.index(l)
        out += ascii_lowercase[i]
    else:
        out += 1
