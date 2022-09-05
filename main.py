from filme import Filme
from playlist import Playlist
from serie import Serie


def main():
    vingadores = Filme('Vingadores - Guerra infinita', 2018, 160)
    vingadores.dar_like()

    atlanta = Serie('atlanta', 2017, 2)
    atlanta.dar_like()
    atlanta.dar_like()

    tmep = Filme('Todo mundo em pânico', 1999, 100)
    tmep.dar_like()
    tmep.dar_like()
    tmep.dar_like()
    tmep.dar_like()
    tmep.dar_like()

    demolidor = Serie('Demolidor', 2016, 3)
    demolidor.dar_like()
    demolidor.dar_like()
    demolidor.dar_like()

    filmes_e_series = [vingadores, atlanta, demolidor, tmep]
    playlist_fim_de_semana = Playlist('Fim de semana', filmes_e_series)

    print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}')

    for programa in playlist_fim_de_semana:
        print(programa)


if __name__ == '__main__':
    main()
