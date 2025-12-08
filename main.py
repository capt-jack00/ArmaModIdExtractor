import argparse
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs

def main():
    # TODO: Add error handling for cases where the input file isn't a html file or the program cannot find any ids
    # TODO: Allow user to enter a name of a output file that doesn't exist. In this case let the program create the output txt file
    parser = argparse.ArgumentParser(description="This program extracts mod id's from a html file to txt file")
    parser.add_argument("--input", type=str, required=True, help="Provides input modpack file")
    parser.add_argument("--output", type=str, required=True, help="Provides output .txt file")

    args = parser.parse_args()

    with open(args.input, "r", encoding="utf-8") as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, "html.parser")

    with open(args.output, "w", encoding="utf-8") as f:
        for a in soup.find_all("a"):
            href = a.get("href")
            if href:
                parsed_url = urlparse(href)
                query_params = parse_qs(parsed_url.query)
                id_value = query_params.get("id", [None])[0]
                print(id_value)
                f.write(id_value + "\n") 


if __name__ == "__main__":
    main()
