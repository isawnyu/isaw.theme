## Script (Python) "robots.txt"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=*args,**kw
##title=

request = container.REQUEST
response = request.response
response.setHeader('Content-Type', 'text/plain')
response.setHeader('Cache-Control', 'public, max-age=86400')


if '//isaw.nyu.edu' in request.get('ACTUAL_URL'):
    return """Sitemap: /sitemap.xml.gz
User-agent: *
Disallow: /*sendto_form$
Disallow: /*folder_factories$
Disallow: /*-assets
return printed"""

else:
   return """User-agent: *
Disallow: /
"""
