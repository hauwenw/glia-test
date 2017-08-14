import operator

# examples
urls = [
    "http://www.google/a.txt",
    "jdskladjalsk/a.txt",
    "dhasklhdaskl/dajsldjlas/dalkjsdjal/c.jpg",
    "http://www.google.co.jp/a.txt",
    "http://www.goog.cleomc/b.txt",
    "hhtp://facebook.coma/dasjdk/b.txt",
    "http://ayoo.com/asd/das1000/c.jpg",
    "http://gliacloud.com/haha.png",
]

def counting(urls):
    summary = {}
    for url in urls:
        filename = url.split('/')[-1]
        if (filename in summary):
            summary[filename] += 1
        else:
            summary[filename] = 1
    sorted_summary = sorted(summary.items(), key=operator.itemgetter(1), reverse=True)
    for item in sorted_summary[:3]:
        print(item[0], item[1])

counting(urls)