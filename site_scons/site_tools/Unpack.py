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
   unpack = env['UNPACK']
   for s in source:
      tar = tarfile.open(env.GetBuildPath(s), mode='r:gz')
      for member in tar.getmembers():
         if member.isreg():  # skip if the TarInfo is not files
            split_name = member.name.split('/')[1:]
            member_path = os.path.join(*split_name)
            member.name = member_path
            tar.extract(member, unpack)
            
def emitter(target, source, env):
   new_target = []
   unpack = env['UNPACK']
   for t in target:
       new_target_path = env.GetBuildPath(os.path.join(unpack, str(t)))
       new_target.append(new_target_path)
   print(new_target, source)
   return new_target, source

def generate(env):
   """
   Add builders and construction variables for the Unpack builder.
   """

   env.Append(BUILDERS = {
      'Unpack': env.Builder(
         action = SCons.Action.Action(Unpack, UnpackString),
         emitter = emitter,
         source_factory = env.fs.Entry,
         target_factory = env.fs.Entry,
      ),
   })


def exists(env):
   return True
