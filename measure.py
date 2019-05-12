from krawedz import run
from helpers import save_measurements

elements = [n*10 for n in range(1,11)]

clear_measurements = lambda: {e: [] for e in elements}

measurements = {
    'sort_top': clear_measurements(),
    'sort_top_dfs': clear_measurements(),
}

for e in elements:
    for _ in range(5):
        pomiary = run(e)
        while not pomiary:
            pomiary = run(e)
        measurements['sort_top_del'][e].append(pomiary['sort_top_del'])
        measurements['sort_top_dfs'][e].append(pomiary['sort_top_dfs'])

save_measurements('sort_top', measurements['sort_top'])
save_measurements('sort_top_dfs', measurements['sort_top_dfs'])

