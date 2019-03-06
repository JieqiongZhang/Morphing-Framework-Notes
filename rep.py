import os
import glob

def main():
    works = glob.glob("*.html")
    for e in works:
        text_data = []
        with open(e, 'r', encoding="utf-8") as fin:
            text_data = fin.readlines()
        text_data = [_.rstrip() for _ in text_data]
        text_data = [_ for _ in text_data if len(_) > 0]
        del text_data[6:8]
        with open(e, 'w', encoding="utf-8") as fout:
            for line in text_data:
                line = line.replace("<body>", '<body><div class="content"><div class="container">')
                line = line.replace("</body>", '</body></div></div>')
                line = line.replace(r"<p><img", r'<p align="center"><img')
                print(line, file=fout)
            print(file=fout)
        print("{} done.".format(e))


if __name__ == "__main__":
    main()

