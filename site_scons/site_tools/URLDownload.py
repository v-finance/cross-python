#!python 
import urllib2, urlparse
import SCons.Builder, SCons.Node, SCons.Errors


# define an own node, for checking the data behind the URL,
# we must download only than, if the data is changed, the
# node derivates from the Python.Value node
class URLNode(SCons.Node.Python.Value) :

    # overload the get_csig (copy the source from the
    # Python.Value node and append the data of the URL header
    def get_csig(self, calc=None): 
        try: 
            return self.ninfo.csig 
        except AttributeError: 
            pass 
        
        # read URL header information
        try :
            response = urllib2.urlopen( str(self.value) ).info()
        except Exception, e :
            raise SCons.Errors.StopError( e )
            
        contents = ""
        # append the data from the URL header if exists
        # otherwise the returning data is equal to the Python.Value node
        if "Last-Modified" in response :
            contents = contents + response["Last-Modified"]
        if "Content-Length" in response :
            contents = contents + response["Content-Length"]
        if not contents :
            contents = self.get_contents() 
        self.get_ninfo().csig = contents 
        return contents 


# creates the downloading output message
# @param s original message
# @param target target name
# @param source source name
# @param env environment object
def __message( s, target, source, env ) :
    print "downloading [%s] to [%s] ..." % (source[0], target[0])



# the download function, which reads the data from the URL
# and writes it down to the file
# @param target target file on the local drive
# @param source URL
# @param env environment object
def __action( target, source, env ) :
    try :
        stream = urllib2.urlopen( str(source[0]) )
        file   = open( str(target[0]), "wb" )
        file.write(stream.read())
        file.close()
        stream.close()
    except Exception, e :
        raise SCons.Errors.StopError( e )


# defines the emitter of the builder
# @param target target file on the local drive
# @param source URL
# @param env environment object
def __emitter( target, source, env ) :
    # we need a temporary file, because the dependency graph
    # of Scons need a physical existing file - so we prepare it
    target[0].prepare()

    if not env.get("URLDOWNLOAD_USEURLFILENAME", False) :
        return target, source

    try :
        url = urlparse.urlparse( str(source[0]) )
    except Exception, e :
        raise SCons.Errors.StopError( e )
    return url.path.split("/")[-1], source



# generate function, that adds the builder to the environment,
# the value "DOWNLOAD_USEFILENAME" replaces the target name with
# the filename of the URL
# @param env environment object
def generate( env ) :
    env["BUILDERS"]["URLDownload"] = SCons.Builder.Builder( action = __action,  emitter = __emitter,  target_factory = SCons.Node.FS.File,  source_factory = URLNode,  single_source = True,  PRINT_CMD_LINE_FUNC = __message )
    env.Replace(URLDOWNLOAD_USEURLFILENAME =  True )


# existing function of the builder
# @param env environment object
# @return true
def exists(env) :
    return 1