import matplotlib.pyplot as plt
from helpers import get_measurements, save_measurements
import numpy as np
import statistics
import itertools


def error_data(measurements, label=''):
    x = measurements.keys()
    y = list(map(lambda x: statistics.mean(x), measurements.values()))
    e = list(map(lambda x: np.std(x), measurements.values()))
    plt.errorbar(x, y, e, solid_capstyle='projecting', capsize=5, linestyle='-', fmt='o', label=label)


def error_plot(title, xlabel='Liczba elementów', ylabel="Czas", y_scale=None):
    plt.legend()

    plt.grid(True)

    plt.title(title)
    if y_scale:
        plt.yscale(y_scale)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.savefig('plots/' + title)
    plt.clf()


measurements = get_measurements('pomiary.json')

error_data(measurements['krawedz_sort_top_del'], 'Usuwanie')
error_data(measurements['krawedz_sort_top_dfs'], 'DFS')
error_plot('Sortowanie Topologiczne Listy krawędzi')

error_data(measurements['macierz_sort_top_del'], 'Usuwanie')
error_data(measurements['macierz_sort_top_dfs'], 'DFS')
error_plot('Sortowanie Topologiczne Macierz')

error_data(measurements['nastepnik_sort_top_del'], 'Usuwanie')
error_data(measurements['nastepnik_sort_top_dfs'], 'DFS')
error_plot('Sortowanie Topologiczne Lista Następników')


error_data(measurements['krawedz_sort_top_dfs'], 'Krawędź')
error_data(measurements['macierz_sort_top_dfs'], 'Macierz')
error_data(measurements['nastepnik_sort_top_dfs'], 'Następniki')
error_plot('Sortowanie Topologiczne DFS')

error_data(measurements['krawedz_sort_top_del'], 'Krawędź')
error_data(measurements['macierz_sort_top_del'], 'Macierz')
error_data(measurements['nastepnik_sort_top_del'], 'Następniki')
error_plot('Sortowanie Topologiczne przez usuwanie')

