import snapext
import os
user = os.path.expanduser('~')
from hashlib import md5
import time
streams = {}
@snapext.SnapHandler.route('/file/get')
def fileget(path):
    if os.path.isfile("%s/%s" % (user, path)):
        return open('%s/%s' % (user, path), 'r+').read()
    else:
        return False
@snapext.SnapHandler.route('/file/token')
def token(path):
    filetoken = md5(path + repr(round(time.time() * 1000))[-7:-2]).hexdigest()
    streams[filetoken] = open("%s/%s" % (user, path), 'r+')
    return filetoken
@snapext.SnapHandler.route('/file/stream')
def streamline(token): #haha
    line = streams[token].readline().strip('\n')
    if line == '':
        streams[token].close()
        return '***EOF***'
    else:
        return line
@snapext.SnapHandler.route('/file/write')
def filewrite(path, content):
    f = open("%s/%s" % (user, path), 'a')
    f.write(content)
    f.close()
@snapext.SnapHandler.route('/file/set')
def filewrite(path, content):
    f = open("%s/%s" % (user, path), 'w')
    f.write(content)
    f.close()


snapext.main(snapext.SnapHandler, 3131)
