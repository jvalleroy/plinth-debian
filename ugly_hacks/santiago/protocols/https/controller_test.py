"""The HTTPS Santiago listener and sender.

TODO: Build out /consuming too.
TODO: build out the rest of the actions.

"""


from Cheetah.Template import Template
import cherrypy
import httplib, urllib, urlparse
import sys
import logging
import wsgiref.handlers


mykey = str(8)
hosting_data = { mykey: { "santiago": set( ["https://localhost:8080"] )}}
consuming_data = { "santiago": { mykey: set( ["https://localhost:8080"] )}}


def setup(santiago):
    # TODO call this bugger to prep the dispatcher, objects, etc.
    pass

class RestController(object):

    def PUT(self, *args, **kwargs):
        raise NotImplemented("RestController.PUT")

    def GET(self, *args, **kwargs):
        raise NotImplemented("RestController.GET")

    def POST(self, *args, **kwargs):
        raise NotImplemented("RestController.POST")

    def DELETE(self, *args, **kwargs):
        raise NotImplemented("RestController.DELETE")


class Hosting(RestController):
    exposed = True

    def __init__(self, data):
        self.hosting = data

    def GET(self):
        try:
            clients = [x for x in self.hosting]
            message = "success"
        except KeyError:
            clients = []
            message = "Error."
        finally:
            return [str(Template(
                        file="templates/hosting-get.tmpl",
                        searchList=[{
                                "clients": clients,
                                "message": message }]))]

class Client(object):
    exposed = True

    def __init__(self, data):
        self.hosting = data

    def GET(self, client=0):
        try:
            services = [x for x in self.hosting[client]]
            message = "success"
        except KeyError:
            services = []
            message = "Error."
        finally:
            return [str(Template(
                        file="templates/client-get.tmpl",
                        searchList=[{
                                "client": client,
                                "services": services,
                                "message": message }]))]

class HostedService(object):
    exposed = True

    def __init__(self, data):
        self.hosting = data

    def GET(self, client=0, service=""):
        try:
            locations = [x for x in self.hosting[client][service]]
            message = "success"
        except KeyError:
            locations = []
            message = "Error."
        finally:
            return [str(Template(
                        file="templates/hostedService-get.tmpl",
                        searchList=[{
                                "client": client,
                                "service": service,
                                "locations": locations,
                                "message": message }]))]

class Location(object):
    exposed = True

    def __init__(self, data):
        self.hosting = data

    def GET(self, client=0, service=0, location=0):
        try:
            location = self.hosting[client][service].find(location)
            message = "success"
        except KeyError:
            location = ""
            message = "error"
        return [str(Template(
                    file="templates/location-get.tmpl",
                    searchList=[{
                                "client": client,
                                "service": service,
                                "location": location,
                                "message": message, }]))]

def rest_connect(dispatcher, location, controller, trailing_slash=True):
    """Simple REST connector for object/location mapping."""

    if trailing_slash:
        location = location.rstrip("/")
        location = [location, location + "/"]
    else:
        location = [location]

    for place in location:
        for a_method in ("PUT", "GET", "POST", "DELETE"):
            dispatcher.connect(controller.__class__.__name__ + a_method,
                               place, controller=controller, action=a_method,
                               conditions={ "method": [a_method] })

    return dispatcher


if __name__ == "__main__":

    hosting = Hosting(hosting_data)
    client = Client(hosting_data)
    service = HostedService(hosting_data)
    location = Location(hosting_data)
    d = cherrypy.dispatch.RoutesDispatcher()

    rest_connect(d, '/hosting/:client/:service/:location', location)
    rest_connect(d, '/hosting/:client/:service', service)
    rest_connect(d, '/hosting/:client', client)
    rest_connect(d, '/hosting/', hosting)

    cherrypy.config.update({"server.socket_host": "0.0.0.0"})

    cherrypy.quickstart(hosting, "/", { "/": {'request.dispatch': d, }})
