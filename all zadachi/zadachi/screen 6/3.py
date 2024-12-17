




def count_it(sequence):
    bibli = {}
    result = {}
    for item in sequence:
        bibli[item] = sequence.count(item)


    sorted_bibli = sorted(bibli.items(), key=lambda x :x[1])
    return dict(sorted_bibli[-3:])








print(count_it('122244445'))