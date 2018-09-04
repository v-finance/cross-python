"""
A SCons extension to do a recursive zip of a source folder
"""

import os,sys
import zipfile
   
from SCons.Script import *
import SCons.Builder

def ZipDirString(target, source, env):
   return 'ZipDir(%s,...)' % str(target[0])

def ZipDir(target, source, env):
   """zip archive builder"""

   excludeexts = env.Dictionary().get('ZIPDIR_EXCLUDEEXTS',[])
   excludedirs = env.Dictionary().get('ZIPDIR_EXCLUDEDIRS',['__pycache__'])

   # split the target directory, filename, and stuffix
   base_name = str(target[0]).split('.zip')[0]
   (target_dir, dir_name) = os.path.split(base_name)

   # create the target directory if it does not exist
   if target_dir and not os.path.exists(target_dir):
      os.makedirs(target_dir)

   # open our zip file for writing
   sys.stderr.write("ZipDir: write " + str(target[0]))
   zf = zipfile.ZipFile(str(target[0]), "w")

   for item in source:
      a_path = item.rdir().get_abspath()
      for root, dirs, files in os.walk(a_path):
         for name in files:
            ext = os.path.splitext(name)
            if not ext[1] in excludeexts:         
               zf.write(
                  os.path.join(root, name),
                  os.path.join(os.path.relpath(root, a_path), name),
                  zipfile.ZIP_DEFLATED
               )
         for d in excludedirs:
            if d in dirs:
               dirs.remove(d)

   sys.stderr.write("\n")
   zf.close()

def generate(env):
   """
   Add builders and construction variables for the ZipDir builder.
   """

   env.Append(BUILDERS = {
      'ZipDir': env.Builder(
         action = SCons.Action.Action(ZipDir, ZipDirString),
         suffix = '.zip',
         target_factory = env.fs.Entry,
         source_factory = env.fs.Dir,
      ),
   })


def exists(env):
   return True
