def build_profile(first, last, **user_info):
    """Строит словарь с информацией о пользователе."""

    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('sergei', 'reshetniak',
                             weight=10,
                             height=15,
                             size='S')
print(user_profile)