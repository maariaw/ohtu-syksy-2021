from kps_io import PeliIO
from pelivalitsin import Pelivalitsin


def main():
    io = PeliIO()
    valitsin = Pelivalitsin(io)
    valitsin.suorita()


if __name__ == "__main__":
    main()
