import os

env_name = os.path.basename(os.path.normpath(os.path.dirname(os.path.abspath(__file__))))
env_settings = env_name + ".settings"

print env_settings

os.environ['DJANGO_SETTINGS_MODULE'] = env_settings 

from web_resources.models import PrimaryResource, Resource, Keyword, Category
from lxml import etree


def searchXML(el, keywords, subresources, categories):
    title = desc = link = primcat = None 
    shortdesc = longdesc = ''
    for child in el:

        if child.tag == 'Title':
            title = child.text.encode("utf8")
        if child.tag == 'Description':
            desc = child.text.encode("utf8").strip()
        if child.tag == 'Link':
            link = child.text.encode("utf8")
        if child.tag == 'Keyword':
            keywords.append( child.text )
        if child.tag == 'shortDesc':
            if child.text:    
                shortdesc = child.text.encode('utf8').strip()
            else: 
                shortdesc = ''
        if child.tag == 'longDesc':
            if child.text:
                longdesc = child.text.encode('utf8').strip()
            else: 
                longdesc = ''

        if child.tag == 'categories':
            for element in child:
                if element.tag == 'primary-category':
                    primcat = element.text.encode('utf8')
                if element.tag == 'category':
                    categories.append( element.text.encode('utf8'))

        if child.tag == 'Alternate':
            alt = {}
            alt['id'] = child.get('id')
            for element in child:
                if element.tag == 'Title':
                    alt['title'] = element.text.encode("utf8")
                if element.tag == 'Link':
                    alt['link'] = element.text.encode("utf8")
            subresources.append( alt )
    
    return (title, desc, link, shortdesc, longdesc, primcat)



parser = etree.XMLParser(ns_clean=True, recover=True)
xml = etree.parse('data/sitemap_and_resources.xml', parser)

for el in xml.getroot():
    id = el.get('id')
   
    title = desc = link = shortdesc = longdesc = primcat = None
    keywords = []
    subresources = []
    categories = []

    title, desc, link, shortdesc, longdesc, primcat = searchXML(el, keywords, subresources, categories)         

    
    #print "id: %s\ntitle: %s\ndesc: %s\nlink: %s" % (id, title, desc, link)
    #print "Loading... %s" % title

    try:
        if primcat is not None:
            pcat = Category.objects.get(display_name = primcat )
            resource = PrimaryResource.objects.create(id=id, name=title, url=link, desc=desc, 
                                                      shortdesc=shortdesc,longdesc=longdesc,
                                                      primary_category=pcat
                                                     )  
        else: 
            resource = PrimaryResource.objects.create(id=id, name=title, url=link, desc=desc, 
                                                      shortdesc=shortdesc,longdesc=longdesc
                                                     )
    except Exception, err:
        #print "Resource error: %s, \n%s from id: %s" % (err, link, id)
        #print err
        print "Resource error: %s, \n%s\n from id: %s\nprimarycat: %s" % (err, link, id, primcat)

    #print keywords

    for keyword in keywords:
        k = resource.keyword_set.create(word = keyword)

    try:
        for cat in categories:
            #add the m2m relationship
            c = Category.objects.get(display_name = cat)
            resource.categories.add( c )
    except Exception, err:
        print "Category Error: %s" % err

    try: 
        for sub in subresources:
            s = resource.subresources.get_or_create(url=sub['link'], defaults={'name' : sub['title'], 'id' : sub['id'] })
    except Exception, err:
        #print err
        print "SubResource error: %s, \n%s\n from id: %s" % (err, sub['link'], sub['id'])
        #print err
        #import pdb; pdb.set_trace()


#now for the dump file 
#dump = etree.parse('data/dump_out.xml', parser)

#for el in dump.getroot():
#    id = el.get('dbname')
#    featured = el.get('featured')


