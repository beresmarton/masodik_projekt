from pprint import pprint


def getting_aspect():
    aspects = ['title', 'color', 'full_price', 'current_price', 'publish_date']
    print('Válassz, melyik szempont alapján rendezzem a cipőket!')
    for number in range(1, 6):
        print(f'{number} - {aspects[number-1]}')
    choice = int(input('Válasszon egyet a fenti leheőségek közül!(Adja meg a sorszámát)! '))
    return choice


def main():
    with open('sneakers.csv') as sourcefile:
        sourcefile.readline()
        lines = []
        for line in sourcefile:
            categories = {'title': line.strip().split(',')[0],
                          'color': line.strip().split(',')[1],
                          'full_price': line.strip().split(',')[2],
                          'current_price': line.strip().split(',')[3],
                          'publish_date': line.strip().split(',')[4]
                          }
            lines.append(categories)
        choosen = getting_aspect()
    pprint(sorted(lines, key=lambda shoe: choosen))


main()
