from pprint import pprint


def getting_aspect():
    aspects = ['title', 'color', 'full_price', 'current_price', 'publish_date']
    print('Válassz, melyik szempont alapján rendezzem a cipőket!')
    for number in range(1, 6):
        print(f'{number} - {aspects[number-1]}')
    choice = int(input('Válasszon egyet a fenti leheőségek közül!(Adja meg a sorszámát)! '))
    return aspects[choice-1]


def main():
    with open('sneakers.csv') as sourcefile:
        sourcefile.readline()
        lines = []
        for line in sourcefile:
            data = line.strip().split(',')
            categories = {'title': data[0],
                          'color': data[1],
                          'full_price': float(data[2]),
                          'current_price': float(data[3]),
                          'publish_date': data[4]
                          }
            lines.append(categories)
        choosen = getting_aspect()
    pprint(sorted(lines, key=lambda shoes: shoes[choosen]))


main()
