

from collections import Counter


def top3(st):
    counter_top3 = Counter(st.replace(' ', '')).most_common(3)
    print(counter_top3)
    return ', '.join([f'{letter} - {cnt}' for letter, cnt in counter_top3])

top3("fdklsfjlsdfjdsfjdjfdsnfkndsfaskdkokwjqopjewqekqwjfuihplvkcxjnvbhfqwel;kdfldskfgjewjf;fdkljfd")
    