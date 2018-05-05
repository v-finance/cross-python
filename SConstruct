# Use :
#   scons --srcdir=/home/tw55413/test/python/Python-3.6.4/
#

import os.path
import os

env = Environment(
    PATH = os.environ['PATH'],
    tools = ['default', 'textfile'],
    #CC   = "x86_64-w64-mingw32-gcc",
    #CXX  = "x86_64-w64-mingw32-gcc",
)

#env.Append(CPPDEFINES = '-DPYLONG_BITS_IN_DIGIT=30')
#env.Append(CPPDEFINES = '-DPY_FORMAT_SIZE_T="z"')

#have_ssize=conf.CheckType('ssize_t')
#conf.env.Append(CPPDEFINES = '-DHAVE_SSIZE_T={0}'.format(int(have_ssize)))

#void_p_size = conf.CheckTypeSize('void*')
#conf.env.Append(CPPDEFINES = '-DSIZEOF_VOID_P={0}'.format(void_p_size))
#
#conf.env.Append(CPPDEFINES = '-DSIZEOF_WCHAR_T={0}'.format(wchar_t_size))
#int_size = conf.CheckTypeSize('int')
#conf.env.Append(CPPDEFINES = '-DSIZEOF_INT={0}'.format(int_size))
#long_size = conf.CheckTypeSize('long')
#conf.env.Append(CPPDEFINES = '-DSIZEOF_LONG={0}'.format(long_size))
#long_double_size = conf.CheckTypeSize('long double')
#conf.env.Append(CPPDEFINES = '-DSIZEOF_LONG_DOUBLE={0}'.format(long_double_size))
#long_long_size = conf.CheckTypeSize('long long')
#conf.env.Append(CPPDEFINES = '-DSIZEOF_LONG_LONG={0}'.format(long_long_size))

#env = conf.Finish()

#
# Replacement of configure.ac
#

conf = Configure(env)

subst_dict = dict()

# Type availability checks : line 2202

#AC_TYPE_MODE_T
#AC_TYPE_OFF_T
#AC_TYPE_PID_T
#AC_DEFINE_UNQUOTED([RETSIGTYPE],[void],[assume C89 semantics that RETSIGTYPE is always void])
#AC_TYPE_SIZE_T
#AC_TYPE_UID_T

have_dict = {

    "HAVE_SSIZE_T": conf.CheckType('ssize_t'),
    "HAVE_GCC_UINT128_T": conf.CheckType('__uint128_t'),
  
    "HAVE_SYSEXITS_H": conf.CheckHeader('sys/exits.h'),
    "HAVE_SYS_AUDIOIO_H": conf.CheckHeader('sys/audioio.h'),
    "HAVE_SYS_BSDTTY_H": conf.CheckHeader('sys/bsdtty.h'),
    "HAVE_SYS_DEVPOLL_H": conf.CheckHeader('sys/devpoll.h'),
    # Define to 1 if you have the <> header file, and it defines `DIR'.
    "HAVE_SYS_DIR_H": conf.CheckHeader('sys/dir.h'),
    "HAVE_SYS_ENDIAN_H": conf.CheckHeader('sys/endian.h'),
    "HAVE_SYS_EPOLL_H": conf.CheckHeader('sys/epoll.h'),
    "HAVE_SYS_EVENT_H": conf.CheckHeader('sys/event.h'),
    "HAVE_SYS_FILE_H": conf.CheckHeader('sys/file.h'),
    "HAVE_SYS_IOCTL_H": conf.CheckHeader('sys/ioctl.h'),
    "HAVE_SYS_KERN_CONTROL_H": conf.CheckHeader('sys/kern_control.h'),
    "HAVE_SYS_LOADAVG_H": conf.CheckHeader('sys/loadavg.h'),
    "HAVE_SYS_LOCK_H": conf.CheckHeader('sys/lock.h'),
    "HAVE_SYS_MKDEV_H": conf.CheckHeader('sys/mkdev.'),
    "HAVE_SYS_MODEM_H": conf.CheckHeader('sys/modem.h'),
    "HAVE_SYS_NDIR_H": conf.CheckHeader('sys/ndir.h'),
    "HAVE_SYS_PARAM_H": conf.CheckHeader('sys/param.h'),
    "HAVE_SYS_POLL_H": conf.CheckHeader('sys/poll.h'),
    "HAVE_SYS_RANDOM_H": conf.CheckHeader('sys/random.h'),
    "HAVE_SYS_RESOURCE_H": conf.CheckHeader('sys/resource.h'),
    "HAVE_SYS_SELECT_H": conf.CheckHeader('sys/select.h'),
    "HAVE_SYS_SENDFILE_H": conf.CheckHeader('sys/sendfile.h'),
    "HAVE_SYS_SOCKET_H": conf.CheckHeader('sys/socket.h'),
    "HAVE_SYS_STATVFS_H": conf.CheckHeader('sys/statvfs.h'),
    "HAVE_SYS_STAT_H": conf.CheckHeader('sys/stat.h'),
    "HAVE_SYS_SYSCALL_H": conf.CheckHeader('sys/syscall.h'),
    "HAVE_SYS_SYSMACROS_H": conf.CheckHeader('sys/sysmacros.h'),
    "HAVE_SYS_SYS_DOMAIN_H": conf.CheckHeader('sys/sys_domain.h'),
    "HAVE_SYS_TERMIO_H": conf.CheckHeader('sys/termio.h'),
    "HAVE_SYS_TIMES_H": conf.CheckHeader('sys/times.h'),
    "HAVE_SYS_TIME_H": conf.CheckHeader('sys/time.h'),
    "HAVE_SYS_TYPES_H": conf.CheckHeader('sys/types.h'),
    "HAVE_SYS_UIO_H": conf.CheckHeader('sys/uio.h'),
    "HAVE_SYS_UN_H": conf.CheckHeader('sys/un.h'),
    "HAVE_SYS_UTSNAME_H": conf.CheckHeader('sys/utsname.h'),
    "HAVE_SYS_WAIT_H": conf.CheckHeader('sys/wait.h'),
    "HAVE_SYS_XATTR_H": conf.CheckHeader('sys/xattr.h'),
}

for k, v in have_dict.items():
    if v:
        subst_dict["#undef {0}".format(k)] = "#define {0} 1".format(k)

typesize_dict = {
    "SIZEOF_WCHAR_T": conf.CheckTypeSize('wchar_t'),
    "SIZEOF_DOUBLE": conf.CheckTypeSize('double'),
    "SIZEOF_FLOAT": conf.CheckTypeSize('float'),
    "SIZEOF_FPOS_T": conf.CheckTypeSize('fpos_t'),
    "SIZEOF_INT": conf.CheckTypeSize('int'),
    "SIZEOF_LONG": conf.CheckTypeSize('long'),
    "SIZEOF_LONG_DOUBLE": conf.CheckTypeSize('long double'),
    "SIZEOF_LONG_LONG": conf.CheckTypeSize('long long'),
    "SIZEOF_OFF_T": conf.CheckTypeSize('off_t'),
    "SIZEOF_PID_T": conf.CheckTypeSize('pid_t'),
    "SIZEOF_PTHREAD_T": conf.CheckTypeSize('pthread_t'),
    "SIZEOF_SHORT": conf.CheckTypeSize('short'),
    "SIZEOF_SIZE_T": conf.CheckTypeSize('size_t'),
    "SIZEOF_TIME_T": conf.CheckTypeSize('time_t'),
    "SIZEOF_UINTPTR_T": conf.CheckTypeSize('uintptr_t'),
    "SIZEOF_VOID_P": conf.CheckTypeSize('void *'),
    "SIZEOF_WCHAR_T": conf.CheckTypeSize('wchar_t'),
    "SIZEOF__BOOL": conf.CheckTypeSize('_Bool'),
}

for k, v in typesize_dict.items():
    subst_dict["#undef {0}\n".format(k)] = "#define {0} {1}\n".format(k, v)

type_dict = {
    "off_t": conf.CheckType('off_t', '#include <sys/types.h>'),
    "clock_t": conf.CheckType('clock_t', '#include <sys/types.h>'),
}

for k, v in type_dict.items():
    if v:
        subst_dict["#undef {0}".format(k)] = "/* #undef {0} */".format(k)

env.Substfile('pyconfig.h.in', SUBST_DICT=subst_dict)

#env.Command('pyconfig.h', , Copy('$TARGET', '$SOURCE'))

#
# Replacement of makesetup
#
# This part replaces the shell script in Modules/makesetup
#

env.Append(CPPPATH = ['Include', '.'])

# === Variables set by makesetup ===

MODNAMES=       []
MODOBJS=        [
    os.path.join('Modules', '_threadmodule.c'),
    os.path.join('Modules', 'posixmodule.c'),
    os.path.join('Modules/errnomodule.c'),
    os.path.join('Modules/pwdmodule.c'),
    os.path.join('Modules/_sre.c'),
    os.path.join('Modules/_codecsmodule.c'),  
    os.path.join('Modules/_weakref.c'),
    os.path.join('Modules/_functoolsmodule.c'),  
    os.path.join('Modules/_operator.c'),
    os.path.join('Modules/_collectionsmodule.c'),  
    os.path.join('Modules/itertoolsmodule.c'),
    os.path.join('Modules/atexitmodule.c'), 
    os.path.join('Modules/signalmodule.c'),
    os.path.join('Modules/_stat.c'),
    os.path.join('Modules/timemodule.c'),  
    os.path.join('Modules/_localemodule.c'),  
    os.path.join('Modules/_io/_iomodule.c'),
    os.path.join('Modules/_io/iobase.c'),
    os.path.join('Modules/_io/fileio.c'),
    os.path.join('Modules/_io/bytesio.c'),
    os.path.join('Modules/_io/bufferedio.c'), 
    os.path.join('Modules/_io/textio.c'),
    os.path.join('Modules/_io/stringio.c'), 
    os.path.join('Modules/zipimport.c'),
    os.path.join('Modules/faulthandler.c'),  
    os.path.join('Modules/_tracemalloc.c'),
    os.path.join('Modules/hashtable.c'),
    os.path.join('Modules/symtablemodule.c'),  
    os.path.join('Modules/xxsubtype.c'),
]

MODLIBS=        []

# === Variables set by configure

VERSION=        '3.6'
SOABI=		'cpython-36m-x86_64-linux-gnu'
VPATH=          'sourcedir'

LIBS=		['pthread', 'dl', 'util',]
LIBM=		['m']
LIBC=		[]
SYSLIBS=	LIBM + LIBC

THREADOBJ=	os.path.join('Python', 'thread.c')
DYNLOADFILE=	'dynload_shlib.o'
BUILDPYTHON=    'python'
LIBRARY=	'python'

# Install prefix for architecture-independent files
prefix=		'.'

# Install prefix for architecture-dependent files
exec_prefix=	prefix

# Compiler options
OPT=		['-DNDEBUG', '-g', '-fwrapv', '-O3', '-Wall', '-Wstrict-prototypes']
BASECFLAGS=	['-Wno-unused-result', '-Wsign-compare']
BASECPPFLAGS=	[]
CONFIGURE_CFLAGS= []	
# CFLAGS_NODIST is used for building the interpreter and stdlib C extensions.
# Use it when a compiler flag should _not_ be part of the distutils CFLAGS
# once Python is installed (Issue #21121).
CONFIGURE_CFLAGS_NODIST= ['-std=c99', '-Wextra', '-Wno-unused-result', '-Wno-unused-parameter', '-Wno-missing-field-initializers']
CONFIGURE_CPPFLAGS=	 []
CONFIGURE_LDFLAGS=	 []
# Avoid assigning CFLAGS, LDFLAGS, etc. so users can use them on the
# command line to append to these values without stomping the pre-set
# values.
PY_CFLAGS=	BASECFLAGS + OPT + CONFIGURE_CFLAGS
PY_CFLAGS_NODIST= CONFIGURE_CFLAGS_NODIST
# Both CPPFLAGS and LDFLAGS need to contain the shell's value for setup.py to
# be able to build extension modules using the directories specified in the
# environment variables
PY_CPPFLAGS=	BASECPPFLAGS + CONFIGURE_CPPFLAGS
# Extra C flags added for building the interpreter object files.
CFLAGSFORSHARED=[]
# C flags used for building the interpreter object files
PY_CORE_CFLAGS = PY_CFLAGS + PY_CFLAGS_NODIST + PY_CPPFLAGS + CFLAGSFORSHARED + ['-DPy_BUILD_CORE']

# === Definitions added by makesetup ===

PYTHONPATH=''

##########################################################################
# Modules
MODULE_OBJS = [
    os.path.join('Modules', 'config.c'),
    os.path.join('Modules', 'getpath.c'),
    os.path.join('Modules', 'main.c'),
    os.path.join('Modules', 'gcmodule.c'),
]

IO_H = [
    os.path.join('Modules', '_io', '_iomodule.h'),
]

IO_OBJS = [
    os.path.join('Modules', '_io', '_iomodule.c'),
    os.path.join('Modules', '_io', 'iobase.c'),
    os.path.join('Modules', '_io', 'fileio.c'),
    os.path.join('Modules', '_io', 'bufferedio.c'),
    os.path.join('Modules', '_io', 'textio.c'),
    os.path.join('Modules', '_io', 'bytesio.c'),
    os.path.join('Modules', '_io', 'stringio.c'),
]
                
##########################################################################
# Parser

POBJS = [
    os.path.join('Parser', 'acceler.c'),
    os.path.join('Parser', 'grammar1.c'),
    os.path.join('Parser', 'listnode.c'),
    os.path.join('Parser', 'node.c'),
    os.path.join('Parser', 'parser.c'),
    os.path.join('Parser', 'bitset.c'),
    os.path.join('Parser', 'metagrammar.c'),
    os.path.join('Parser', 'firstsets.c'),
    os.path.join('Parser', 'grammar.c'),
    os.path.join('Parser', 'pgen.c'),
]

PARSER_OBJS = POBJS + [
    os.path.join('Parser', 'myreadline.c'),
    os.path.join('Parser', 'parsetok.c'),
    os.path.join('Parser', 'tokenizer.c'),
]

PGOBJS = [
    os.path.join('Objects', 'obmalloc.c'),
    os.path.join('Python', 'dynamic_annotations.c'),
    os.path.join('Python', 'mysnprintf.c'),
    os.path.join('Python', 'pyctype.c'),
    os.path.join('Parser', 'tokenizer_pgen.c'),
    os.path.join('Parser', 'printgrammar.c'),
    os.path.join('Parser', 'parsetok_pgen.c'),
    os.path.join('Parser', 'pgenmain.c'),
]

PGENOBJS = POBJS + PGOBJS

##########################################################################
# Python

PYTHON_OBJS = [
    os.path.join('Python', '_warnings.c'),
    os.path.join('Python', 'Python-ast.c'),
    os.path.join('Python', 'asdl.c'),
    os.path.join('Python', 'ast.c'),
    os.path.join('Python', 'bltinmodule.c'),
    os.path.join('Python', 'ceval.c'),
    os.path.join('Python', 'compile.c'),
    os.path.join('Python', 'codecs.c'),
    os.path.join('Python', 'dynamic_annotations.c'),
    os.path.join('Python', 'errors.c'),
    os.path.join('Python', 'frozenmain.c'),
    os.path.join('Python', 'future.c'),
    os.path.join('Python', 'getargs.c'),
    os.path.join('Python', 'getcompiler.c'),
    os.path.join('Python', 'getcopyright.c'),
    os.path.join('Python', 'getplatform.c'),
    os.path.join('Python', 'getversion.c'),
    os.path.join('Python', 'graminit.c'),
    os.path.join('Python', 'import.c'),
    os.path.join('Python', 'importdl.c'),
    os.path.join('Python', 'marshal.c'),
    os.path.join('Python', 'modsupport.c'),
    os.path.join('Python', 'mystrtoul.c'),
    os.path.join('Python', 'mysnprintf.c'),
    os.path.join('Python', 'peephole.c'),
    os.path.join('Python', 'pyarena.c'),
    os.path.join('Python', 'pyctype.c'),
    os.path.join('Python', 'pyfpe.c'),
    os.path.join('Python', 'pyhash.c'),
    os.path.join('Python', 'pylifecycle.c'),
    os.path.join('Python', 'pymath.c'),
    os.path.join('Python', 'pystate.c'),
    os.path.join('Python', 'pythonrun.c'),
    os.path.join('Python', 'pytime.c'),
    os.path.join('Python', 'random.c'),
    os.path.join('Python', 'structmember.c'),
    os.path.join('Python', 'symtable.c'),
    os.path.join('Python', 'sysmodule.c'),
    os.path.join('Python', 'traceback.c'),
    os.path.join('Python', 'getopt.c'),
    os.path.join('Python', 'pystrcmp.c'),
    os.path.join('Python', 'pystrtod.c'),
    os.path.join('Python', 'pystrhex.c'),
    os.path.join('Python', 'dtoa.c'),
    os.path.join('Python', 'formatter_unicode.c'),
    os.path.join('Python', 'fileutils.c'),
    os.path.join('Python', DYNLOADFILE),
    #os.path.join('$(LIBOBJS'),
    #os.path.join('$(MACHDEP_OBJS'),
    THREADOBJ,
    #os.path.join('$(DTRACE_OBJS'),
]

##########################################################################
# Objects
OBJECT_OBJS = [
    os.path.join('Objects', 'abstract.c'),
    os.path.join('Objects', 'accu.c'),
    os.path.join('Objects', 'boolobject.c'),
    os.path.join('Objects', 'bytes_methods.c'),
    os.path.join('Objects', 'bytearrayobject.c'),
    os.path.join('Objects', 'bytesobject.c'),
    os.path.join('Objects', 'cellobject.c'),
    os.path.join('Objects', 'classobject.c'),
    os.path.join('Objects', 'codeobject.c'),
    os.path.join('Objects', 'complexobject.c'),
    os.path.join('Objects', 'descrobject.c'),
    os.path.join('Objects', 'enumobject.c'),
    os.path.join('Objects', 'exceptions.c'),
    os.path.join('Objects', 'genobject.c'),
    os.path.join('Objects', 'fileobject.c'),
    os.path.join('Objects', 'floatobject.c'),
    os.path.join('Objects', 'frameobject.c'),
    os.path.join('Objects', 'funcobject.c'),
    os.path.join('Objects', 'iterobject.c'),
    os.path.join('Objects', 'listobject.c'),
    os.path.join('Objects', 'longobject.c'),
    os.path.join('Objects', 'dictobject.c'),
    os.path.join('Objects', 'odictobject.c'),
    os.path.join('Objects', 'memoryobject.c'),
    os.path.join('Objects', 'methodobject.c'),
    os.path.join('Objects', 'moduleobject.c'),
    os.path.join('Objects', 'namespaceobject.c'),
    os.path.join('Objects', 'object.c'),
    os.path.join('Objects', 'obmalloc.c'),
    os.path.join('Objects', 'capsule.c'),
    os.path.join('Objects', 'rangeobject.c'),
    os.path.join('Objects', 'setobject.c'),
    os.path.join('Objects', 'sliceobject.c'),
    os.path.join('Objects', 'structseq.c'),
    os.path.join('Objects', 'tupleobject.c'),
    os.path.join('Objects', 'typeobject.c'),
    os.path.join('Objects', 'unicodeobject.c'),
    os.path.join('Objects', 'unicodectype.c'),
    os.path.join('Objects', 'weakrefobject.c'),
]

##########################################################################
# objects that get linked into the Python library
LIBRARY_OBJS_OMIT_FROZEN = [
    os.path.join('Modules', 'getbuildinfo.c'),
] + \
    PARSER_OBJS + \
    OBJECT_OBJS + \
    PYTHON_OBJS + \
    MODULE_OBJS + \
    MODOBJS

LIBRARY_OBJS = \
    LIBRARY_OBJS_OMIT_FROZEN + [
    os.path.join('Python', 'frozen.c'),
]

##########################################################################
# DTrace

# On some systems, object files that reference DTrace probes need to be modified
# in-place by dtrace(1).
DTRACE_DEPS = [
    os.path.join('Python', 'ceval.o'),
]

# XXX: should gcmodule, etc. be here, too?

# Scons Defines

env.Append(CPPDEFINES = '-DPYTHONPATH=\'"{0}"\''.format(PYTHONPATH))
env.Append(CPPDEFINES = '-DPREFIX=\'"{0}"\''.format(prefix))
env.Append(CPPDEFINES = '-DEXEC_PREFIX=\'"{0}"\''.format(exec_prefix))
env.Append(CPPDEFINES = '-DVERSION=\'"{0}"\''.format(VERSION))
env.Append(CPPDEFINES = '-DVPATH=\'"{0}"\''.format(VPATH))
for f in PY_CORE_CFLAGS:
    env.Append(CFLAGS = f)

dynload_env = env.Clone()
dynload_env.Append(CPPDEFINES = '-DSOABI=\'"{0}"\''.format(SOABI))
dynload_env.Object(os.path.join('Python', 'dynload_shlib.c'))
        
env.Program('pgen', PGENOBJS)

# Build static library
# avoid long command lines, same as LIBRARY_OBJS

library = env.Library(LIBRARY, LIBRARY_OBJS)
        
# Build the interpreter

interpreter_env = env.Clone()
interpreter_env.Append(LIBPATH = '.')
interpreter_env.Append(LIBS = [LIBRARY]+LIBS+SYSLIBS+MODLIBS)

interpreter_env.Program(BUILDPYTHON, [os.path.join('Programs', 'python.c')])


        #$(LDLIBRARY) $(PY3LIBRARY)
        #$(LINKCC) $(PY_LDFLAGS) $(LINKFORSHARED) -o $@ Programs/python.o $(BLDLIBRARY) $(LDLAST)
        
#env.Object('Objects/abstract.c')
object_sources = Glob('Objects/*.c')
for objects_src in object_sources:
    env.Object(objects_src)

#libpython = env.SharedLibrary('python3', object_sources)
#env.Program(os.path.join('Programs', 'python.c'), LIBS=libpython)



#for parser_src in Glob('Parser/*.c'):
    #env.Object(parser_src)
#for python_src in Glob('Python/*.c'):
    #env.Object(python_src)