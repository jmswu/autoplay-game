def is_even_items(qmark_box):
    count = 0
    for x in qmark_box:
        count += 1
    return (count % 2 == 0) and (count > 1)


def duplicate(qmark_box):
    data = []
    for x in qmark_box:
        data.append(x)
    return data
