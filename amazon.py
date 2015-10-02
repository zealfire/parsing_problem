countries=['com','co.uk','ca','de']
books=[
        '''http://www.amazon.%s/Glass-House-Climate-Millennium-ebook/dp/B005U3U69C''',
        '''http://www.amazon.%s/The-Japanese-Observer-ebook/dp/B0078FMYD6''',
        '''http://www.amazon.%s/Falling-Through-Water-ebook/dp/B009VJ1622''',
      ]
import urllib2;
import re

for book in books:
    print '-'*40
    print book.split('%s/')[1]
    for country in countries:
        asin=book.split('/')[-1]; title=book.split('/')[3]
        url='''http://www.amazon.%s/product-reviews/%s'''%(country,asin)
        print url
        #url='http://www.amazon.com/product-reviews/B0078FMYD6'
        try: f = urllib2.urlopen(url)
        except: page=""
        page=f.read().lower();
        #print page
        #print '%s=%s'%(country, page.count('member-review'))
        lists=re.findall(r'<span class="a-size-base review-text">.*?</span>',page,re.DOTALL)
        k=1
        for list in lists:
            print '''comment %d'''%(k)
            print list
            k+=1
        #break
    #break
print '-'*40
