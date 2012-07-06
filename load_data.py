import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'info.settings'

from web_resources.models import Resource, Keyword
from lxml import etree

parser = etree.XMLParser(ns_clean=True, recover=True)
xml = etree.parse('web_resources/web_resources.xml', parser)

for el in xml.getroot():
    id = el.get('id')
    
    keywords = []
    subresources = []

    for child in el:

        if child.tag == 'Title':
            title = child.text.encode("utf8")
        if child.tag == 'Description':
            for p in child.iter('p'):
                desc = p.text.encode("utf8")
        if child.tag == 'Link':
            link = child.text.encode("utf8")
        if child.tag == 'Keyword':
            keywords.append( child.text )
        if child.tag == 'Alternate':
            alt = {}
            alt['id'] = child.get('id')
            for element in child:
                if element.tag == 'Title':
                    alt['title'] = element.text.encode("utf8")
                if element.tag == 'Link':
                    alt['link'] = element.text.encode("utf8")
            subresources.append( alt )
            

    
    #print "id: %s\ntitle: %s\ndesc: %s\nlink: %s" % (id, title, desc, link)
    #print "Loading... %s" % title

    try:
        resource = Resource.objects.create(id=id, title=title, href=link, desc=desc)
    except Exception, err:
        #print "Resource error: %s, \n%s from id: %s" % (err, link, id)
        #print err
        print "Resource error: %s, \n%s\n from id: %s" % (err, link, id)

    #print keywords

    for keyword in keywords:
        k = resource.keyword_set.create(word = keyword)


    try: 
        for sub in subresources:
            s = resource.child.get_or_create(href=sub['link'], defaults={'title' : sub['title'], 'id' : sub['id'] })
    except Exception, err:
        #print err
        print "SubResource error: %s, \n%s\n from id: %s" % (err, sub['link'], sub['id'])
        #print err
        #import pdb; pdb.set_trace()
