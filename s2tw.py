import opencc
import glob
converter = opencc.OpenCC('s2tw')
for eachfaqfile in glob.glob('content.chs/faq/*'):
    with open(eachfaqfile, 'r', encoding='utf-8') as istream:
        with open('content.cht/faq/' + eachfaqfile.split('\\')[-1], 'w', encoding='utf-8') as ostream:
            ostream.write(converter.convert(istream.read()))
