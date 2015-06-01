# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'))

def cesar():
    import sys
import os

print ("")
print ("Script per a calcular la contrasenya d\'un ajuntament")
print ("El primer argument es el nom del municipi") 
print("")
print("")

dicc_vocals = {"a":5,"e":4,"i":3,"o":2,"u":1}

nom_municipi = sys.argv[1]
contrasenya = ""
i=0
while i < len(nom_municipi):
	if dicc_vocals.has_key(nom_municipi[i]):
		lletra = dicc_vocals[nom_municipi[i]]
		contrasenya = contrasenya + str(lletra)
	else:
		posicio = ord(nom_municipi[i])
		if posicio == 121:
			contrasenya = contrasenya + chr(97)
		elif posicio == 122:
			contrasenya = contrasenya + chr(98)	
		else: 
			contrasenya = contrasenya + chr(posicio + 2)
	i = i + 1

outfile = open(nom_municipi+'.txt', 'w') # Indicamos el valor 'w'
outfile.write("_"+contrasenya)
outfile.close()

print "_"+contrasenya




def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
