import requests
from bs4 import BeautifulSoup
import time

def extract_links(elements, base_url, max_results=100):
    links = []
    for e in elements:
        url = e["href"]
        if "https://" not in url:
            url = base_url + url
        if base_url in url:
            links.append(url)
    return set(links[:max_results])


def find_links(start_url, base_url, depth=2):
    if depth == 0:
        return set()

    page = requests.get(start_url)
    soup = BeautifulSoup(page.content, "html.parser")
    elements = soup.find_all("a", href=True)
    links = extract_links(elements, base_url)

    for url in links:
        new_links = find_links(url, base_url, depth-1)
        links = links.union(new_links)
    return links

base = "https://lshunters.eu/"
docs = base + ""


# Parallel search
"""import ray

@ray.remote
def find_links_task(start_url, base_url, depth=2):
    return find_links(start_url, base_url, depth)

links = [find_links_task.remote(docs,base)
         for lib in [""]]

for res in ray.get(links): print(len(res))"""

start_time = time.time()
print(find_links(docs, base))
end_time = time.time()
total_time = end_time - start_time
print(total_time)




