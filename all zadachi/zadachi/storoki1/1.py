


def search_substr(subst, st):
    if subst.lower in st.lower:
        print('Есть контакт!')
    else:
        print("Мимо!")