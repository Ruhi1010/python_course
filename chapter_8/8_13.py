#8.13
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

my_profile = build_profile('Ruhi', 'Tahmidul',
                           profession='student',
                           hobby='sleeping',
                           interested_in='AI')

print(my_profile)
