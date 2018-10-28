"""
A SCons extension to extract a tarball
"""

import os,sys
import tarfile
   
from SCons.Script import *
import SCons.Builder

def UnpackString(target, source, env):
   return 'Unpack(%s,...)' % str(target[0])

def Unpack(target, source, env):
   print('Unpack', target, source)
   for s in source:
      tar = tarfile.open(env.GetBuildPath(s), mode='r:gz')
      for member in tar.getmembers():
         if member.isreg():  # skip if the TarInfo is not files
            member_path = os.path.join(*os.path.split(member.name)[1:])
            member.name = member_path
            tar.extract(member, str(target[0]))
            

def generate(env):
   """
   Add builders and construction variables for the Unpack builder.
   """

   env.Append(BUILDERS = {
      'Unpack': env.Builder(
         action = SCons.Action.Action(Unpack, UnpackString),
         source_factory = env.fs.Entry,
         target_factory = env.fs.Dir,
      ),
   })


def exists(env):
   return True
