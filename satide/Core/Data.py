
links = []
project_path = ""
project_name = ""


def remove_links_by_id(block_id):
    for _ in range(2):
        for link in links:
            if link[0] == block_id:
                links.remove(link)
            if link[1] == block_id:
                links.remove(link)
