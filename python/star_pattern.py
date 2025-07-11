def print_3x3_grid(num):
    print(f'star pattern for {num}:')
    star_pattern = { 'A':'*', 'B':'**', 'C':'***'}
    digits_star_pattern = { 1 : 'A', 2 : 'B', 3 : 'C', 4 :'CA', 5 :'CB', 6:'CC', 7:'CCA',8:'CCB', 9:'CCC'}

    string_code = digits_star_pattern.get(num)
    for s in string_code:
        print(star_pattern.get(s))

for i in range(1,10):
  print_3x3_grid(i)

'''
    star pattern for 1:
    *
    star pattern for 2:
    **
    star pattern for 3:
    ***
    star pattern for 4:
    ***
    *
    star pattern for 5:
    ***
    **
    star pattern for 6:
    ***
    ***
    star pattern for 7:
    ***
    ***
    *
    star pattern for 8:
    ***
    ***
    **
    star pattern for 9:
    ***
    ***
    ***
'''
