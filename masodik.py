import csv
from pprint import pprint


def enumeratior(list1, list2):
    for number in enumerate(list2, 1):
        list1.append(number)
    return list1


def choose(list1):
    pprint(list1)
    choice = int(input('Válasszon egyet a fenti leheőségek közül!(Adja meg a sorszámát)! '))
    return choice


def getting_aspect():
    with open('sneakers.csv') as file:
        aspects = []
        base = file.readline().strip().split(',')
        enumeratior(aspects, base)
        aspect = aspects[choose(aspects)-1][1]
        return aspect


def main():
    with open('sneakers.csv') as sourcefile:
        csv_reader = csv.DictReader(sourcefile)
        data = [row for row in csv_reader]
        choosen = getting_aspect()
    pprint(sorted(data, key=lambda shoe: choosen))


main()
