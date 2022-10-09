from serpapi import GoogleSearch
import Token


def search(query):

    params = {
        "device": "desktop",
        "engine": "google",
        "q": query,
        "location": "Germany",
        "google_domain": "google.de",
        "gl": "de",
        "hl": "de",
        "tbm": "isch",
        "nfpr": "1",
        "safe": "active",
        "api_key": Token.SERP_TOKEN,
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    for results in results["images_results"]:
        if "source" == "chefkoch.de":
            return results["thumbnail"]
