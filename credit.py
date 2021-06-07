#def is_luhn_valid(cc):
#    num = list(map(int, str(cc)))
#    return sum(num[::-2] + [sum(divmod(d * 2, 10)) for d in num[-2::-2]]) % 10 == 0

from luhn import *

sigue = True;
while sigue:
    entrada = input("Number:");
    try:
        #if is_luhn_valid(entrada):
        if verify(entrada):
            longitud = len( entrada );
            if longitud == 15:
                if entrada[:2] == "34" or entrada[:2] == "37":
                    print("AMEX");
                    sigue = False;
                else:
                    print("INVALID");
                    sigue = False;
            elif longitud == 16:
                if entrada[:1] == "4":
                    print("VISA");
                    sigue = False;
                elif entrada[:2] == "51" or entrada[:2] == "52" or entrada[:2] == "53" or entrada[:2] == "54" or entrada[:2] == "55":
                    print("MASTER CARD");
                    sigue = False;
                else:
                    print("INVALID");
                    sigue = False;
            elif longitud == 13:
                print("VISA");
                sigue = False;
        else:
            print("INVALID");
            sigue = False;
    except:
        sigue = True;
