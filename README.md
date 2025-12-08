# What is this?
This is a simple CLI tool that allows to export mod ids from a `.html` file modpack to a whole list in `.txt` file. In summary, only thing that this program does is taking a `.html` file modpack as output extracting the `?id` query from the end of
each steam link to this mod and saving it all to specified output `.txt` file

# Future plans
I have in plans to not only make this a simple CLI tool, but I want to make whole GUI for this program. My goal is to make it easy to use, easy to install, cross-platform and most important open source so anyone can modify the program according to his needs. When 
I'll finish the program I'll provide whole documentation for the code. 

# Usage
The usage is very simple:
```bash
python3 main.py --input armamodpack.html --output out.txt
```
The `--input` option provides an input html file. <br>
The `--output` option provides an output txt file <br>
**IMPORTANT**: Provided output file needs to exist BEFORE the program is run. I'm currently in process of making it autocreate the file.

# Dependencies
The program uses:
- `BeautifulSoup4` for web scraping
- `argparse` for providing arguments
- `urllib` for searching for ids in links to the mods
