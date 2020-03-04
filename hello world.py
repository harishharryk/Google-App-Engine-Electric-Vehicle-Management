import webapp2;
import os;
import jinja2;
import random;
from google.appengine.ext import ndb;
from google.appengine.api import users
from gpu import GPU
from myuser import MyUser
from gpufeatures import GPUFeatures
from display import Display
from edit import Edit
from refinedsearch import RefinedSearch
from datetime import datetime
from compare import Compare
from comparedevices import CompareDevices

JINJA_ENVIRONMENT = jinja2.Environment(
loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions = ['jinja2.ext.autoescape'],
autoescape = True
)

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        user = users.get_current_user()
        if user == None:
            template_values = {
            'login_url' : users.create_login_url(self.request.uri)
            }
            template = JINJA_ENVIRONMENT.get_template('mainpage_guest.html')
            self.response.write(template.render(template_values))
            return
        myuser_key = ndb.Key('MyUser', user.user_id())
        myuser = myuser_key.get()
        if myuser == None:
            myuser = MyUser(id=user.user_id(),username=user.email(),email_address=user.email())
            myuser.put()
        all_keys = GPU.query().fetch(keys_only = True)
        template_values = {
            'logout_url' : users.create_logout_url(self.request.uri),
            'all_keys' : all_keys,
            'message':"Add GPU"
            }

        template = JINJA_ENVIRONMENT.get_template('main.html')
        self.response.write(template.render(template_values))


        # for i in all_keys:
        #     self.response.write(i.gpuName + '<br/>')

    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        action = self.request.get('button')
        if action == 'Add GPU':
            gpuName = self.request.get('gpuName')
            gpuManufacturer = self.request.get('gpuManufacturer')
            gpuDateIssued = datetime.strptime(self.request.get('gpuDateIssued'),'%Y-%m-%d')
            geometryShader = True if self.request.get('geometryShader')=='on' else False
            tesselationShader = True if self.request.get('tesselationShader')=='on' else False
            shaderInt16 = True if self.request.get('shaderInt16')=='on' else False
            sparseBinding = True if self.request.get('sparseBinding')=='on' else False
            textureCompressionETC2 =True if self.request.get('textureCompressionETC2')=='on' else False
            vertexPipelineStoresAndAtomics =True if self.request.get('vertexPipelineStoresAndAtomics')=='on' else False
            new_gpu_features = GPUFeatures(geometryShader=geometryShader,tesselationShader=tesselationShader,shaderInt16=shaderInt16,sparseBinding=sparseBinding,textureCompressionETC2=textureCompressionETC2,vertexPipelineStoresAndAtomics=vertexPipelineStoresAndAtomics)

            mygpu_key = ndb.Key('GPU',gpuName)
            mygpu = mygpu_key.get()
            if mygpu == None:
                new_gpu = GPU(gpuName=gpuName, gpuManufacturer=gpuManufacturer, gpuDateIssued=gpuDateIssued,id=gpuName,gpuFeature=new_gpu_features)
                new_gpu.put()
                message = "GPU Added!!"
            else:
                message = "GPU already exists!!"

            template_values = {
                'message':message,
                'all_keys': GPU.query().fetch(keys_only=True)
                }
            template = JINJA_ENVIRONMENT.get_template('main.html')
            self.response.write(template.render(template_values))


app = webapp2.WSGIApplication([('/',MainPage),('/featureDisplay',Display),('/edit',Edit),('/refinedSearch',RefinedSearch),('/compare',Compare),('/compareDevices',CompareDevices)],debug = True)
