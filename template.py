import glob
import os

cwd = os.getcwd()

f = open('index.html')
t = f.read()

template_top = t[:t.index("<maincontent>")]
template_bottom = t[t.index("</maincontent>")+len("</maincontent>"):]

all_htmls = glob.glob(cwd + '**\\**\\*.html', recursive = True)
all_htmls.remove(cwd + '\\index.html')

ot = "<maincontent>"
ct = "</maincontent>"

for html_path in all_htmls:
    file = open(html_path)
    content = file.read()
    file.close()
    if "<!--fancy-->" not in content:
        main_content = content[content.index(ot):content.index(ct)+len(ct)]
        file = open(html_path, "w")
        file.write(
            template_top +
            main_content +
            template_bottom
        )
        file.close()
