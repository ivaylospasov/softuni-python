from math import ceil

M_BRITISH_SHORTHAIR = 13
M_SIAMESE = 15
M_PERSIAN = 14
M_RAGDOLL = 16
M_AMERICAN_SHORTHAIR = 12
M_SIBERIAN = 11

F_BRITISH_SHORTHAIR = 14
F_SIAMESE = 16
F_PERSIAN = 15
F_RAGDOLL = 17
F_AMERICAN_SHORTHAIR = 13
F_SIBERIAN = 12

cat_breed = input()
cat_sex = input().lower() # m or f

def cat_months(cat_max_age):
    cat_life_in_months = cat_max_age * 12 / 6
    return ceil(cat_life_in_months)

if cat_breed == 'British Shorthair':
    if cat_sex == 'm':
        print(f'{cat_months(M_BRITISH_SHORTHAIR)} cat months')
    else:
        print(f'{cat_months(F_BRITISH_SHORTHAIR)} cat months')
elif cat_breed == 'Siamese':
    if cat_sex == 'm':
        print(f'{cat_months(M_SIAMESE)} cat months')
    else:
        print(f'{cat_months(F_SIAMESE)} cat months')
elif cat_breed == 'Persian':
    if cat_sex == 'm':
        print(f'{cat_months(M_PERSIAN)} cat months')
    else:
        print(f'{cat_months(F_PERSIAN)} cat months')
elif cat_breed == 'Ragdoll':
    if cat_sex == 'm':
        print(f'{cat_months(M_RAGDOLL)} cat months')
    else:
        print(f'{cat_months(F_RAGDOLL)} cat months')
elif cat_breed == 'American Shorthair':
    if cat_sex == 'm':
        print(f'{cat_months(M_AMERICAN_SHORTHAIR)} cat months')
    else:
        print(f'{cat_months(F_AMERICAN_SHORTHAIR)} cat months')
elif cat_breed == 'Siberian':
    if cat_sex == 'm':
        print(f'{cat_months(M_SIBERIAN)} cat months')
    else:
        print(f'{cat_months(F_SIBERIAN)} cat months')
else:
    print(f'{cat_breed} is invalid cat!')