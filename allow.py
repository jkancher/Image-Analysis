from dropbox.client import DropboxOAuth2FlowNoRedirect
from dropbox import client
import dropbox
from docx import Document
from PIL import Image
from watson_developer_cloud import VisualRecognitionV3 as vr

#Authorize dropbox connection
#app_key = 'ais6zkfckgjw4t5'
app_key = raw_input("Enter app key: ")
#app_secret = 'ahetrgp97p5by0p'
app_secret = raw_input("Enter secret key: ")

flow = DropboxOAuth2FlowNoRedirect(app_key, app_secret)

authorize_url = flow.start()
print '1. Go to: ' + authorize_url
print '2. Click "Allow" (you might have to log in first)'
print '3. Copy the authorization code.'
code = raw_input("Enter the authorization code here: ").strip()

client = dropbox.client.DropboxClient(code)
print 'linked account: ', client.account_info()

#view folders
folder_metadata = client.metadata('/')
print 'metadata: ', folder_metadata

#download first image file
filelocation = raw_input("Enter file location: (example: /Home/13-15-00.jpg) ") 
f, metadata = client.get_file_and_metadata(filelocation)
print metadata
im = Image.open(f)
im.show()
print client.share(filelocation, short_url = False)
fileurl = client.share(filelocation, short_url = False)
print fileurl.get('url')
lasturl = fileurl.get('url')

#examine image file
instance = vr(api_key='c7e97f739c7a61949b71ef6c34993e94de53181a', version='2016-05-20')

img = instance.classify(images_url = lasturl)

a = 0
for things in img['images'][0]['classifiers'][0]['classes']:
    if((things['score']*100) > a):
        a = things['score']*100
        first = things['class']
    print('\n There is a ' + str(things['score']*100) + ' percent chance the image contains: '+ things['class'])

print first

#second image file retrieved
filelocation2 = raw_input("Enter file location to compare to: (example: /Home/13-15-00.jpg) ") 
c, metadata = client.get_file_and_metadata(filelocation2)
#print metadata
im2 = Image.open(c)
im2.show()
print client.share(filelocation2, short_url = False)
fileurl2 = client.share(filelocation2, short_url = False)
print fileurl2.get('url')
lasturl2 = fileurl2.get('url')

    
#analyze second image
img2 = instance.classify(images_url = lasturl2)

h = 0
for thing in img2['images'][0]['classifiers'][0]['classes']:
    if((thing['score']*100) > h):
        h = thing['score']*100
        z = thing['class']
    print('\n There is a ' + str(thing['score']*100) + ' percent chance the image contains: '+ thing['class'])

try:
    print z
except:
    print("You are comparing the same file!")
    
#results
print " "
if (z == first):
    print "PRODUCT NOT TAKEN"
else:
    print "PRODUCT IS TAKEN"
    