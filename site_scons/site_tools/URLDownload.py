"""
A SCons extension to download a url
"""

import os,sys
import urllib2
   
from SCons.Script import *
import SCons.Builder

def URLDownloadString(target, source, env):
   return 'URLDownload(%s,...)' % str(target[0])

def URLDownload(target, source, env):
   """zip archive builder"""

   print('download', target, source)
   
   for s in source:
      source_path = env.GetBuildPath(s)
      with open(source_path, 'r') as source_file:
         url = source_file.read()
      
      sys.stderr.write("URLDownload: " + url + "\n")
      
      try :
         stream = urllib2.urlopen(url)
         file   = open( str(target[0]), "wb" )
         file.write(stream.read())
         file.close()
         stream.close()
      except Exception, e:
         raise SCons.Errors.StopError( e )

def emitter(target, source, env):
   print('emitter', target, source)
   new_source = []
   for s in source:
      new_source = str(s).split('/')[-1] + '.url'
      new_source_path = env.GetBuildPath(new_source)
      print  new_source_path
      old_url = ''
      if os.path.exists(new_source_path):
         with open(new_source_path, 'r') as new_source_file:
            old_url = new_source_file.read()
      if old_url != str(s):
         with open(new_source_path, 'w') as new_source_file:
            new_source_file.write(str(s))       
   return target, new_source

def generate(env):
   """
   Add builders and construction variables for the URLDownload builder.
   """

   env.Append(BUILDERS = {
      'URLDownload': env.Builder(
         action = SCons.Action.Action(URLDownload, URLDownloadString),
         emitter = emitter,
         source_factory = SCons.Node.Python.Value,
      ),
   })


def exists(env):
   return True
