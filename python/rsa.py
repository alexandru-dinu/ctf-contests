from gmpy2 import *
import copy

def t(k,accum,index,arr):
    #print accum,k
    if index == len(arr):
        if(k==0):
            return accum;
        else:
            return [];

    element = arr[index];
    result = []

    for set_i in range(len(accum)):
        if k>0:
            clone_new = copy.deepcopy(accum);
            clone_new[set_i].append([element]);
            result.extend( t(k-1,clone_new,index+1,arr) );

        for elem_i in range(len(accum[set_i])):
            clone_new = copy.deepcopy(accum);
            clone_new[set_i][elem_i].append(element)
            result.extend( t(k,clone_new,index+1,arr) );

    return result



n = 330927995485552243963798761388850162942165506877102576331679078292597846851877884041550348995315153007979606605827812629599330095352430915128718543807359969975367481173851226598032784993297282117425621592147206704941385155581723802041661497895530170903938942091910656754050143157823301935719969929331343816207
e = 65537
c = 137854857736896385085134501896413014044178419904651200686252188922913933236844769415389281902246959417937761270594408361846272317163966851378907278115407432934568839256355153295694371086166079515447979424370642496462788603449529777662596521126648833604443078644698683287982177585033446308612080664980363941217
dp = 397904053847709771663823352598257460224987023836661712446170547620184148333564117267829882998646084047415156259969266081040100592514889662695038159966729


# factors of (e * dp - 1)
f1 = 8
f2 = 3
f3 = 331
f4 = 245747
f5 = 23599612367
f6 = 566021061240068376094977314156722634269017646734957727658181658072499136407594886001847349511629201400830461413367668567812335754730093237

factors = [f1, f2, f3, f4, f5, f6]

# f1 * f2 * f3 * f4 * f5 * f6 = k * (p -1)
s = t(2, [[]], 0, factors)

print s