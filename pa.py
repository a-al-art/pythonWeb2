import argparse





parser = argparse.ArgumentParser()

parser.add_argument('--cars', type=int, default=50)
parser.add_argument('--barbie', type=int, default=50)
parser.add_argument('--movie', choices=['melodrama', 'football', 'other'], default='other')
my_args = parser.parse_args()

if my_args.barbie > 100 or my_args.barbie < 0:
    my_args.barbie = 50

if my_args.cars > 100 or my_args.cars < 0:
    my_args.cars = 50

my_args.movie = (0 if my_args.movie == 'melodrama' else (100 if my_args.movie == 'football' else 50))

boy = int((100 - my_args.barbie + my_args.cars + my_args.movie) / 3)
girl = 100 - boy
print(f'''boy: {boy}
girl: {girl}''')
