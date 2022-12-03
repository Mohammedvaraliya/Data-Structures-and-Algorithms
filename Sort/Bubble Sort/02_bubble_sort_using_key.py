def bubble_sort(elements, key=None):
    size = len(elements)

    for i in range(size - 1):
        swapped = False
        for j in range(size - 1 - i):
            X = elements[j][key]
            Y = elements[j + 1][key]

            if X > Y:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swapped = True

        if not swapped:
            break




if __name__ == '__main__':
    elements = [
        { 'name': 'varaliya',   'amount': 1000, 'device': 'iphone-14'},
        { 'name': 'mohammed', 'amount': 400,  'device': 'google pixel'},
        { 'name': 'sameer',  'amount': 200,  'device': 'vivo'},
        { 'name': 'subhashish',  'amount': 800,  'device': 'iphone-12'},
    ]

    bubble_sort(elements, key='amount') # This will sort elements by taking key as amount
    print(elements)
    print("\n")

    bubble_sort(elements, key='name') # This will sort elements by taking key as name
    print(elements)
    print("\n")

    bubble_sort(elements, key='device') # This will sort elements by taking key as device
    print(elements)

