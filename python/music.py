# equal temperation
eq_temp = [(2**(x/12)) for x in range(0,12)]

# just intonations
perfect = [1/1, 6/5, 5/4, 4/3, 3/2]

pythagorean_up = [1/1, 256/243, 9/8, 32/27, 81/64, 4/3, 1024/729, 3/2, 128/81, 27/16, 16/9, 243/128]
pythagorean_dn = [1/1, 256/243, 9/8, 32/27, 81/64, 4/3, 729/512, 3/2, 128/81, 27/16, 16/9, 243/128]

chinese = [1/1, 2187/2048, 9/8, 1968/1630, 81/64, 1771/1331, 729/512, 3/2, 6561/4096, 27/16, 5905/3277, 243/128]

sama_gana = [1/1, 9/8, 32/27, 4/3, 3/2, 27/16, 16/9]
sruti = [1/1, 25/24, 21/20, 
         256/243, 135/128, 16/15, 10/9, 
         9/8, 7/6, 32/27, 
         6/5,
         5/4, 81/64,
         4/3, 27/20, 45/32, 64/45, 
         729/512, 10/7, 
         3/2, 25/16, 
         128/81, 405/256, 8/5, 5/3,
         27/16, 7/4, 16/9, 9/5, 15/8,
         243/128, 40/21]

def make_octave(f0, ratios):
    return [round(f0*i, 1) for i in ratios]

print(make_octave(440, eq_temp))
print(make_octave(440, chinese))
print(make_octave(440, perfect))
print(make_octave(440, pythagorean_up))
print(make_octave(440, pythagorean_dn))
print(make_octave(440, sama_gana))
print(make_octave(440, sruti))