import snapext
import os
user = os.path.expanduser('~')
@snapext.SnapHandler.route('/file/get')
def fileget(path):
    if os.path.isfile("%s/%s" % (user, path)):
        return open('%s/%s' % (user, path), 'r+').read()
    else:
        return False

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
