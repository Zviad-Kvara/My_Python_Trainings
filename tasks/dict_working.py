# working with dictionary 7kuy 

# In this kata we have to create a function that will give us some specific information of a data base. We have a sequence of 
# postive integers that is registered by OEIS with the code 001055. This sequence give us the amount of ways that a number may be 
# expressed as a product of its factors (including the number itself multiplied by one.)

# The first terms of this sequence are shown below:

# n-th term    a(n)
# 1             1
# 2             1
# 3             1
# 4             2
# 5             1
# 6             2
# 7             1
# 8             3
# 9             2
# 10            2
# 11            1
# 12            4
# 13            1
# 14            2
# 15            2
# 16            5

# In the preloaded section you are given a hash table named A001055, 
# where keys are the numbers from 1 to 1006, and the values are the respective terms of the aforementioned sequence.

# You have to create the function that receives three arguments:

# An array with 2 elements that represent the numbers in range [a, b] to be considered.
# A string with five possible valid values: "equals to", "higher than", "lower than", "higher and equals to", 
# and "lower and equals to" (any other value is considered invalid).
# The element of the A001055 sequence.
# The function should return the amount of numbers that fulfill our conditions and a sorted list of these numbers.

# Examples
# We want to know about the numbers between 10 and 21 (included) that have more than 1 multiplicative partition:
# range = [10, 21]
# str = "higher than"
# val = 1
# result = (8, [10, 12, 14, 15, 16, 18, 20, 21])

# We want to know the numbers between 25 and 75 that have more than or equals to 5 multiplicative partitions:
# range = [25, 75]
# str = "higher and equals to"
# val = 5
# result = (13, [30, 32, 36, 40, 42, 48, 54, 56, 60, 64, 66, 70, 72])

# If the string command is wrong, the function will return "wrong constraint":
# range = [25, 75]
# str = "qwerty"
# val = 5

# result = "wrong constraint"

A001055 = {1: 1, 2: 1, 3: 1, 4: 2, 5: 1, 6: 2, 7: 1, 8: 3, 9: 2, 10: 2, 11: 1, 12: 4, 13: 1, 14: 2, 15: 2, 16: 5, 17: 1, 18: 4, 19: 1, 20: 4, 21: 2, 22: 2, 23: 1, 24: 7, 25: 2, 26: 2, 27: 3, 28: 4, 29: 1, 30: 5, 31: 1, 32: 7, 33: 2, 34: 2, 35: 2, 36: 9, 37: 1, 38: 2, 39: 2, 40: 7, 41: 1, 42: 5, 43: 1, 44: 4, 45: 4, 46: 2, 47: 1, 48: 12, 49: 2, 50: 4, 51: 2, 52: 4, 53: 1, 54: 7, 55: 2, 56: 7, 57: 2, 58: 2, 59: 1, 60: 11, 61: 1, 62: 2, 63: 4, 64: 11, 65: 2, 66: 5, 67: 1, 68: 4, 69: 2, 70: 5, 71: 1, 72: 16, 73: 1, 74: 2, 75: 4, 76: 4, 77: 2, 78: 5, 79: 1, 80: 12, 81: 5, 82: 2, 83: 1, 84: 11, 85: 2, 86: 2, 87: 2, 88: 7, 89: 1, 90: 11, 91: 2, 92: 4, 93: 2, 94: 2, 95: 2, 96: 19, 97: 1, 98: 4, 99: 4, 100: 9, 101: 1, 102: 5, 103: 1, 104: 7, 105: 5, 106: 2, 107: 1, 108: 16, 109: 1, 110: 5, 111: 2, 112: 12, 113: 1, 114: 5, 115: 2, 116: 4, 117: 4, 118: 2, 119: 2, 120: 21, 121: 2, 122: 2, 123: 2, 124: 4, 125: 3, 126: 11, 127: 1, 128: 15, 129: 2, 130: 5, 131: 1, 132: 11, 133: 2, 134: 2, 135: 7, 136: 7, 137: 1, 138: 5, 139: 1, 140: 11, 141: 2, 142: 2, 143: 2, 144: 29, 145: 2, 146: 2, 147: 4, 148: 4, 149: 1, 150: 11, 151: 1, 152: 7, 153: 4, 154: 5, 155: 2, 156: 11, 157: 1, 158: 2, 159: 2, 160: 19, 161: 2, 162: 12, 163: 1, 164: 4, 165: 5, 166: 2, 167: 1, 168: 21, 169: 2, 170: 5, 171: 4, 172: 4, 173: 1, 174: 5, 175: 4, 176: 12, 177: 2, 178: 2, 179: 1, 180: 26, 181: 1, 182: 5, 183: 2, 184: 7, 185: 2, 186: 5, 187: 2, 188: 4, 189: 7, 190: 5, 191: 1, 192: 30, 193: 1, 194: 2, 195: 5, 196: 9, 197: 1, 198: 11, 199: 1, 200: 16, 201: 2, 202: 2, 203: 2, 204: 11, 205: 2, 206: 2, 207: 4, 208: 12, 209: 2, 210: 15, 211: 1, 212: 4, 213: 2, 214: 2, 215: 2, 216: 31, 217: 2, 218: 2, 219: 2, 220: 11, 221: 2, 222: 5, 223: 1, 224: 19, 225: 9, 226: 2, 227: 1, 228: 11, 229: 1, 230: 5, 231: 5, 232: 7, 233: 1, 234: 11, 235: 2, 236: 4, 237: 2, 238: 5, 239: 1, 240: 38, 241: 1, 242: 4, 243: 7, 244: 4, 245: 4, 246: 5, 247: 2, 248: 7, 249: 2, 250: 7, 251: 1, 252: 26, 253: 2, 254: 2, 255: 5, 256: 22, 257: 1, 258: 5, 259: 2, 260: 11, 261: 4, 262: 2, 263: 1, 264: 21, 265: 2, 266: 5, 267: 2, 268: 4, 269: 1, 270: 21, 271: 1, 272: 12, 273: 5, 274: 2, 275: 4, 276: 11, 277: 1, 278: 2, 279: 4, 280: 21, 281: 1, 282: 5, 283: 1, 284: 4, 285: 5, 286: 5, 287: 2, 288: 47, 289: 2, 290: 5, 291: 2, 292: 4, 293: 1, 294: 11, 295: 2, 296: 7, 297: 7, 298: 2, 299: 2, 300: 26, 301: 2, 302: 2, 303: 2, 304: 12, 305: 2, 306: 11, 307: 1, 308: 11, 309: 2, 310: 5, 311: 1, 312: 21, 313: 1, 314: 2, 315: 11, 316: 4, 317: 1, 318: 5, 319: 2, 320: 30, 321: 2, 322: 5, 323: 2, 324: 29, 325: 4, 326: 2, 327: 2, 328: 7, 329: 2, 330: 15, 331: 1, 332: 4, 333: 4, 334: 2, 335: 2, 336: 38, 337: 1, 338: 4, 339: 2, 340: 11, 341: 2, 342: 11, 343: 3, 344: 7, 345: 5, 346: 2, 347: 1, 348: 11, 349: 1, 350: 11, 351: 7, 352: 19, 353: 1, 354: 5, 355: 2, 356: 4, 357: 5, 358: 2, 359: 1, 360: 52, 361: 2, 362: 2, 363: 4, 364: 11, 365: 2, 366: 5, 367: 1, 368: 12, 369: 4, 370: 5, 371: 2, 372: 11, 373: 1, 374: 5, 375: 7, 376: 7, 377: 2, 378: 21, 379: 1, 380: 11, 381: 2, 382: 2, 383: 1, 384: 45, 385: 5, 386: 2, 387: 4, 388: 4, 389: 1, 390: 15, 391: 2, 392: 16, 393: 2, 394: 2, 395: 2, 396: 26, 397: 1, 398: 2, 399: 5, 400: 29, 401: 1, 402: 5, 403: 2, 404: 4, 405: 12, 406: 5, 407: 2, 408: 21, 409: 1, 410: 5, 411: 2, 412: 4, 413: 2, 414: 11, 415: 2, 416: 19, 417: 2, 418: 5, 419: 1, 420: 36, 421: 1, 422: 2, 423: 4, 424: 7, 425: 4, 426: 5, 427: 2, 428: 4, 429: 5, 430: 5, 431: 1, 432: 57, 433: 1, 434: 5, 435: 5, 436: 4, 437: 2, 438: 5, 439: 1, 440: 21, 441: 9, 442: 5, 443: 1, 444: 11, 445: 2, 446: 2, 447: 2, 448: 30, 449: 1, 450: 26, 451: 2, 452: 4, 453: 2, 454: 2, 455: 5, 456: 21, 457: 1, 458: 2, 459: 7, 460: 11, 461: 1, 462: 15, 463: 1, 464: 12, 465: 5, 466: 2, 467: 1, 468: 26, 469: 2, 470: 5, 471: 2, 472: 7, 473: 2, 474: 5, 475: 4, 476: 11, 477: 4, 478: 2, 479: 1, 480: 64, 481: 2, 482: 2, 483: 5, 484: 9, 485: 2, 486: 19, 487: 1, 488: 7, 489: 2, 490: 11, 491: 1, 492: 11, 493: 2, 494: 5, 495: 11, 496: 12, 497: 2, 498: 5, 499: 1, 500: 16, 501: 2, 502: 2, 503: 1, 504: 52, 505: 2, 506: 5, 507: 4, 508: 4, 509: 1, 510: 15, 511: 2, 512: 30, 513: 7, 514: 2, 515: 2, 516: 11, 517: 2, 518: 5, 519: 2, 520: 21, 521: 1, 522: 11, 523: 1, 524: 4, 525: 11, 526: 2, 527: 2, 528: 38, 529: 2, 530: 5, 531: 4, 532: 11, 533: 2, 534: 5, 535: 2, 536: 7, 537: 2, 538: 2, 539: 4, 540: 52, 541: 1, 542: 2, 543: 2, 544: 19, 545: 2, 546: 15, 547: 1, 548: 4, 549: 4, 550: 11, 551: 2, 552: 21, 553: 2, 554: 2, 555: 5, 556: 4, 557: 1, 558: 11, 559: 2, 560: 38, 561: 5, 562: 2, 563: 1, 564: 11, 565: 2, 566: 2, 567: 12, 568: 7, 569: 1, 570: 15, 571: 1, 572: 11, 573: 2, 574: 5, 575: 4, 576: 77, 577: 1, 578: 4, 579: 2, 580: 11, 581: 2, 582: 5, 583: 2, 584: 7, 585: 11, 586: 2, 587: 1, 588: 26, 589: 2, 590: 5, 591: 2, 592: 12, 593: 1, 594: 21, 595: 5, 596: 4, 597: 2, 598: 5, 599: 1, 600: 52, 601: 1, 602: 5, 603: 4, 604: 4, 605: 4, 606: 5, 607: 1, 608: 19, 609: 5, 610: 5, 611: 2, 612: 26, 613: 1, 614: 2, 615: 5, 616: 21, 617: 1, 618: 5, 619: 1, 620: 11, 621: 7, 622: 2, 623: 2, 624: 38, 625: 5, 626: 2, 627: 5, 628: 4, 629: 2, 630: 36, 631: 1, 632: 7, 633: 2, 634: 2, 635: 2, 636: 11, 637: 4, 638: 5, 639: 4, 640: 45, 641: 1, 642: 5, 643: 1, 644: 11, 645: 5, 646: 5, 647: 1, 648: 57, 649: 2, 650: 11, 651: 5, 652: 4, 653: 1, 654: 5, 655: 2, 656: 12, 657: 4, 658: 5, 659: 1, 660: 36, 661: 1, 662: 2, 663: 5, 664: 7, 665: 5, 666: 11, 667: 2, 668: 4, 669: 2, 670: 5, 671: 2, 672: 64, 673: 1, 674: 2, 675: 16, 676: 9, 677: 1, 678: 5, 679: 2, 680: 21, 681: 2, 682: 5, 683: 1, 684: 26, 685: 2, 686: 7, 687: 2, 688: 12, 689: 2, 690: 15, 691: 1, 692: 4, 693: 11, 694: 2, 695: 2, 696: 21, 697: 2, 698: 2, 699: 2, 700: 26, 701: 1, 702: 21, 703: 2, 704: 30, 705: 5, 706: 2, 707: 2, 708: 11, 709: 1, 710: 5, 711: 4, 712: 7, 713: 2, 714: 15, 715: 5, 716: 4, 717: 2, 718: 2, 719: 1, 720: 98, 721: 2, 722: 4, 723: 2, 724: 4, 725: 4, 726: 11, 727: 1, 728: 21, 729: 11, 730: 5, 731: 2, 732: 11, 733: 1, 734: 2, 735: 11, 736: 19, 737: 2, 738: 11, 739: 1, 740: 11, 741: 5, 742: 5, 743: 1, 744: 21, 745: 2, 746: 2, 747: 4, 748: 11, 749: 2, 750: 21, 751: 1, 752: 12, 753: 2, 754: 5, 755: 2, 756: 52, 757: 1, 758: 2, 759: 5, 760: 21, 761: 1, 762: 5, 763: 2, 764: 4, 765: 11, 766: 2, 767: 2, 768: 67, 769: 1, 770: 15, 771: 2, 772: 4, 773: 1, 774: 11, 775: 4, 776: 7, 777: 5, 778: 2, 779: 2, 780: 36, 781: 2, 782: 5, 783: 7, 784: 29, 785: 2, 786: 5, 787: 1, 788: 4, 789: 2, 790: 5, 791: 2, 792: 52, 793: 2, 794: 2, 795: 5, 796: 4, 797: 1, 798: 15, 799: 2, 800: 47, 801: 4, 802: 2, 803: 2, 804: 11, 805: 5, 806: 5, 807: 2, 808: 7, 809: 1, 810: 38, 811: 1, 812: 11, 813: 2, 814: 5, 815: 2, 816: 38, 817: 2, 818: 2, 819: 11, 820: 11, 821: 1, 822: 5, 823: 1, 824: 7, 825: 11, 826: 5, 827: 1, 828: 26, 829: 1, 830: 5, 831: 2, 832: 30, 833: 4, 834: 5, 835: 2, 836: 11, 837: 7, 838: 2, 839: 1, 840: 74, 841: 2, 842: 2, 843: 2, 844: 4, 845: 4, 846: 11, 847: 4, 848: 12, 849: 2, 850: 11, 851: 2, 852: 11, 853: 1, 854: 5, 855: 11, 856: 7, 857: 1, 858: 15, 859: 1, 860: 11, 861: 5, 862: 2, 863: 1, 864: 97, 865: 2, 866: 2, 867: 4, 868: 11, 869: 2, 870: 15, 871: 2, 872: 7, 873: 4, 874: 5, 875: 7, 876: 11, 877: 1, 878: 2, 879: 2, 880: 38, 881: 1, 882: 26, 883: 1, 884: 11, 885: 5, 886: 2, 887: 1, 888: 21, 889: 2, 890: 5, 891: 12, 892: 4, 893: 2, 894: 5, 895: 2, 896: 45, 897: 5, 898: 2, 899: 2, 900: 66, 901: 2, 902: 5, 903: 5, 904: 7, 905: 2, 906: 5, 907: 1, 908: 4, 909: 4, 910: 15, 911: 1, 912: 38, 913: 2, 914: 2, 915: 5, 916: 4, 917: 2, 918: 21, 919: 1, 920: 21, 921: 2, 922: 2, 923: 2, 924: 36, 925: 4, 926: 2, 927: 4, 928: 19, 929: 1, 930: 15, 931: 4, 932: 4, 933: 2, 934: 2, 935: 5, 936: 52, 937: 1, 938: 5, 939: 2, 940: 11, 941: 1, 942: 5, 943: 2, 944: 12, 945: 21, 946: 5, 947: 1, 948: 11, 949: 2, 950: 11, 951: 2, 952: 21, 953: 1, 954: 11, 955: 2, 956: 4, 957: 5, 958: 2, 959: 2, 960: 105, 961: 2, 962: 5, 963: 4, 964: 4, 965: 2, 966: 15, 967: 1, 968: 16, 969: 5, 970: 5, 971: 1, 972: 47, 973: 2, 974: 2, 975: 11, 976: 12, 977: 1, 978: 5, 979: 2, 980: 26, 981: 4, 982: 2, 983: 1, 984: 21, 985: 2, 986: 5, 987: 5, 988: 11, 989: 2, 990: 36, 991: 1, 992: 19, 993: 2, 994: 5, 995: 2, 996: 11, 997: 1, 998: 2, 999: 7, 1000: 31, 1001: 5, 1002: 5, 1003: 2, 1004: 4, 1005: 5, 1006: 2}

def inf_database(range_, str_, val):
    result = ()
    if str_ not in ["equals to", "higher than", "lower than", "higher and equals to", "lower and equals to"]:
            return "wrong constraint"
    
    keys = []                                      
    for key in range(range_[0], range_[1] + 1):
        values = A001055.get(key)
        if  str_ == "higher than" and values > val:                        
            keys.append(key)
        if str_ == "higher and equals to" and values >= val:
             keys.append(key)
        if str_ == "equals to" and values == val:
             keys.append(key)
        if str_ == "lower than" and values < val:
             keys.append(key)
        if str_ == "lower and equals to" and values <= val:
            keys.append(key)
        
    result = len(keys), keys
    
    return result

print(inf_database([10, 21], "higher than", 1))                # result = (8, [10, 12, 14, 15, 16, 18, 20, 21])
print(inf_database([25, 75], "higher and equals to", 5))         # (13, [30, 32, 36, 40, 42, 48, 54, 56, 60, 64, 66, 70, 72])
