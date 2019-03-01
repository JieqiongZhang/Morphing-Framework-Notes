import os
import re
import sys
import glob
import base64

RE_MARCHER = re.compile(r"data:image/(?P<ext>[A-Za-z]+);base64,(?P<b64>.*)")

def img2txt(img_filename):
    print("img2txt({})".format(img_filename))
    filename, ext = os.path.splitext(img_filename)
    ret, ext = None, ext[1:]
    with open(img_filename, 'rb') as fin:
        ret = str(base64.b64encode(fin.read()), encoding='utf-8')
    with open("{}.base64{}".format(filename, ext), 'w') as fout:
        print("data:image/{};base64,{}".format(ext, ret), file=fout)
    

def txt2img(txt_filename):
    print("txt2img({})".format(txt_filename))
    ret = None
    with open(txt_filename, 'r', encoding='utf-8') as fin:
        ret = RE_MARCHER.match(fin.read())
    ext, b64 = [ret.groupdict()[some] for some in ["ext", "b64"]]
    with open("{}.{}".format(os.path.splitext(txt_filename)[0], ext), 'wb') as fout:
        fout.write(base64.b64decode(b64))


def main():
    r"""

      ___           ___           ___       ___           ___           ___           ___     
     /\  \         /\  \         /\__\     /\  \         /\  \         /\  \         /\__\    
    /::\  \       /::\  \       /:/  /    /::\  \       /::\  \       /::\  \       /:/  /    
   /:/\:\  \     /:/\:\  \     /:/  /    /:/\:\  \     /:/\ \  \     /:/\ \  \     /:/__/     
  /::\~\:\  \   /:/  \:\  \   /:/  /    /:/  \:\  \   _\:\~\ \  \   _\:\~\ \  \   /::\__\____ 
 /:/\:\ \:\__\ /:/__/ \:\__\ /:/__/    /:/__/ \:\__\ /\ \:\ \ \__\ /\ \:\ \ \__\ /:/\:::::\__\
 \/__\:\/:/  / \:\  \ /:/  / \:\  \    \:\  \ /:/  / \:\ \:\ \/__/ \:\ \:\ \/__/ \/_|:|~~|~   
      \::/  /   \:\  /:/  /   \:\  \    \:\  /:/  /   \:\ \:\__\    \:\ \:\__\      |:|  |    
       \/__/     \:\/:/  /     \:\  \    \:\/:/  /     \:\/:/  /     \:\/:/  /      |:|  |    
                  \::/  /       \:\__\    \::/  /       \::/  /       \::/  /       |:|  |    
                   \/__/         \/__/     \/__/         \/__/         \/__/         \|__|     
     ____________________________________________________________________ 
    |                                                                    | 
    | @filename: base64img.py                                            ||
    | @author:   polossk                                                 ||
    | @date:     2019-02-27                                              ||
    | @version:  1.0                                                     ||
    |____________________________________________________________________||
     |____________________________________________________________________|

Convert a single or multiple image files into conresponding base64 text files,
or reverse this process.

The extension filename will be `base64`-prefixed. For example `a.png` will
convert into `a.base64png`, and `b.base64jpg` will reverse into `b.jpg`.

Usage:
    > python base64img.py <filename> [<filename> ...]
    filename: the file you want to convert

Example:
    > python base64img.py figure_01.png
    > python base64img.py figure_01.base64png figure_02.png
    """
    if len(sys.argv) <= 1:
        help(main)
        return
    worklist = [_ for __ in sys.argv[1:] for _ in glob.glob(__) if os.path.isfile(_)]
    worklist = list(set(worklist))
    calllist = [txt2img if _.find("base64") >= 0 else img2txt for _ in worklist]
    for _, __ in zip(calllist, worklist): _(__)

    
if __name__ == "__main__":
    main()