project('cross-python', 'c')

python_source = get_option('source')

#
# COMPILER DETECTION
#

compiler = meson.get_compiler('c')
mingw = compiler.get_id()=='gcc' and host_machine.system()=='windows'

#
# COMPILER OPTIONS
#

SOABI=		'cpython-36m-x86_64-linux-gnu'
VPATH=          'sourcedir'

LIBS=		[
    dependency('threads'),
]
LIBM=		[compiler.find_library('m', required : false)]
LIBC=		[]
SYSLIBS=	LIBM + LIBC

THREADOBJ = join_paths(python_source, 'Python', 'thread.c')

# include paths

host_includes = []
if host_machine.system()=='windows'
    host_includes += join_paths(python_source, 'PC')
endif

python_include = include_directories([
    join_paths(python_source, 'Include'),
    join_paths(python_source, 'Include', 'internal'),
    ] + host_includes
)

OPT = [
    '-DNDEBUG', '-fwrapv', '-O3', '-Wall', '-Wstrict-prototypes',
    # -gstabs : to be able to debug using wine
    # '-gstabs'
]

if mingw
    OPT += ['-mwindows', '-municode']
endif

if host_machine.system()=='windows'
    MACHDEP = 'win32'
else
    MACHDEP = host_machine.system()
endif

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


#
# CONFIGURATION
#
# This is a replacement of configure.ac in the CPython source.
# Check the configuration of the target system and write the results to
# 'pyconfig.h'.  This differs from the autotools setup, in that no
# 'pyconfig.h.in' template file is used.
#

LIBRARY = 'python'

conf_data = configuration_data()

# configure.ac line 122

# The later defininition of _XOPEN_SOURCE disables certain features
# on Linux, so we need _GNU_SOURCE to re-enable them (makedev, tm_zone).
conf_data.set('_GNU_SOURCE', '1')  # Define on Linux to activate all library features
conf_data.set('_PYTHONFRAMEWORK', '""')

# check size of data types

conf_data.set('SIZEOF_WCHAR_T', compiler.sizeof('wchar_t', prefix : '#include <sys/types.h>'))
conf_data.set('SIZEOF_DOUBLE', compiler.sizeof('double'))
conf_data.set('SIZEOF_FLOAT', compiler.sizeof('float'))
conf_data.set('SIZEOF_FPOS_T', compiler.sizeof('fpos_t'))
conf_data.set('SIZEOF_INT', compiler.sizeof('int'))
conf_data.set('SIZEOF_LONG', compiler.sizeof('long'))
conf_data.set('SIZEOF_LONG_DOUBLE', compiler.sizeof('long double'))
conf_data.set('SIZEOF_LONG_LONG', compiler.sizeof('long long'))
conf_data.set('SIZEOF_OFF_T', compiler.sizeof('off_t'))
conf_data.set('SIZEOF_PID_T', compiler.sizeof('pid_t', prefix : '#include <sys/types.h>'))
conf_data.set('SIZEOF_PTHREAD_T', compiler.sizeof('pthread_t'))
conf_data.set('SIZEOF_SHORT', compiler.sizeof('short'))
conf_data.set('SIZEOF_SIZE_T', compiler.sizeof('size_t'))
conf_data.set('SIZEOF_TIME_T', compiler.sizeof('time_t'))
conf_data.set('SIZEOF_UINTPTR_T', compiler.sizeof('uintptr_t'))
conf_data.set('SIZEOF_VOID_P', compiler.sizeof('void *'))
conf_data.set('SIZEOF__BOOL', compiler.sizeof('_Bool'))

# check availability of types

conf_data.set('HAVE_SSIZE_T', compiler.has_header_symbol('sys/types.h', 'ssize_t'))
conf_data.set('HAVE_GCC_UINT128_T', compiler.has_type('__uint128_t'))
    
# check availability of headers

conf_data.set('HAVE_SYSEXITS_H', compiler.check_header('sys/exits.h'))
conf_data.set('HAVE_SYS_AUDIOIO_H', compiler.check_header('sys/audioio.h'))
conf_data.set('HAVE_SYS_BSDTTY_H', compiler.check_header('sys/bsdtty.h'))
conf_data.set('HAVE_SYS_DEVPOLL_H', compiler.check_header('sys/devpoll.h'))
# Define to 1 if you have the <> header file, and it defines `DIR'.
conf_data.set('HAVE_SYS_DIR_H', compiler.check_header('sys/dir.h'))
conf_data.set('HAVE_SYS_ENDIAN_H', compiler.check_header('sys/endian.h'))
conf_data.set('HAVE_SYS_EPOLL_H', compiler.check_header('sys/epoll.h'))
conf_data.set('HAVE_SYS_EVENT_H', compiler.check_header('sys/event.h'))
conf_data.set('HAVE_SYS_FILE_H', compiler.check_header('sys/file.h'))
conf_data.set('HAVE_SYS_IOCTL_H', compiler.check_header('sys/ioctl.h'))
conf_data.set('HAVE_SYS_KERN_CONTROL_H', compiler.check_header('sys/kern_control.h'))
conf_data.set('HAVE_SYS_LOADAVG_H', compiler.check_header('sys/loadavg.h'))
conf_data.set('HAVE_SYS_LOCK_H', compiler.check_header('sys/lock.h'))
conf_data.set('HAVE_SYS_MKDEV_H', compiler.check_header('sys/mkdev.h'))
conf_data.set('HAVE_SYS_MODEM_H', compiler.check_header('sys/modem.h'))
conf_data.set('HAVE_SYS_NDIR_H', compiler.check_header('sys/ndir.h'))
conf_data.set('HAVE_SYS_PARAM_H', compiler.check_header('sys/param.h'))
conf_data.set('HAVE_SYS_POLL_H', compiler.check_header('sys/poll.h'))
conf_data.set('HAVE_SYS_RANDOM_H', compiler.check_header('sys/random.h'))
conf_data.set('HAVE_SYS_RESOURCE_H', compiler.check_header('sys/resource.h'))
conf_data.set('HAVE_SYS_SELECT_H', compiler.check_header('sys/select.h'))
conf_data.set('HAVE_SYS_SENDFILE_H', compiler.check_header('sys/sendfile.h'))
conf_data.set('HAVE_SYS_SOCKET_H', compiler.check_header('sys/socket.h'))
conf_data.set('HAVE_SYS_STATVFS_H', compiler.check_header('sys/statvfs.h'))
conf_data.set('HAVE_SYS_STAT_H', compiler.check_header('sys/stat.h'))
conf_data.set('HAVE_SYS_SYSCALL_H', compiler.check_header('sys/syscall.h'))
conf_data.set('HAVE_SYS_SYSMACROS_H', compiler.check_header('sys/sysmacros.h'))
conf_data.set('HAVE_SYS_SYS_DOMAIN_H', compiler.check_header('sys/sys_domain.h'))
conf_data.set('HAVE_SYS_TERMIO_H', compiler.check_header('sys/termio.h'))
conf_data.set('HAVE_SYS_TIMES_H', compiler.check_header('sys/times.h'))
conf_data.set('HAVE_SYS_TIME_H', compiler.check_header('sys/time.h'))
conf_data.set('HAVE_SYS_TYPES_H', compiler.check_header('sys/types.h'))
conf_data.set('HAVE_SYS_UIO_H', compiler.check_header('sys/uio.h'))
conf_data.set('HAVE_SYS_UN_H', compiler.check_header('sys/un.h'))
conf_data.set('HAVE_SYS_UTSNAME_H', compiler.check_header('sys/utsname.h'))
conf_data.set('HAVE_SYS_WAIT_H', compiler.check_header('sys/wait.h'))
conf_data.set('HAVE_SYS_XATTR_H', compiler.check_header('sys/xattr.h'))
conf_data.set('HAVE_STDLIB_H', compiler.check_header('stdlib.h'))
conf_data.set('HAVE_STDINT_H', compiler.check_header('stdint.h'))
conf_data.set('HAVE_ERRNO_H', compiler.check_header('errno.h'))
conf_data.set('HAVE_UNISTD_H', compiler.check_header('unistd.h'))
conf_data.set('HAVE_STDDEF_H', compiler.check_header('stddef.h'))
conf_data.set('HAVE_ALLOCA_H', compiler.check_header('alloca.h'))
conf_data.set('HAVE_ASM_TYPES_H', compiler.check_header('asm/types.h'))
conf_data.set('HAVE_BLUETOOTH_BLUETOOTH_H', compiler.check_header('bluetooth/bluetooth.h'))
conf_data.set('HAVE_BLUETOOTH_H', compiler.check_header('bluetooth.h'))
conf_data.set('HAVE_CONIO_H', compiler.check_header('conio.h'))
conf_data.set('HAVE_CURSES_H', compiler.check_header('curses.h'))
conf_data.set('HAVE_DIRECT_H', compiler.check_header('direct.h'))
conf_data.set('HAVE_DIRENT_H', compiler.check_header('dirent.h'))
conf_data.set('HAVE_DLFCN_H', compiler.check_header('dlfcn.h'))
conf_data.set('HAVE_ENDIAN_H', compiler.check_header('endian.h'))
conf_data.set('HAVE_FCNTL_H', compiler.check_header('fcntl.h'))
conf_data.set('HAVE_GRP_H', compiler.check_header('grp.h'))
conf_data.set('HAVE_IEEEFP_H', compiler.check_header('ieeefp.h'))
conf_data.set('HAVE_INTTYPES_H', compiler.check_header('inttypes.h'))
conf_data.set('HAVE_IO_H', compiler.check_header('io.h'))
conf_data.set('HAVE_LANGINFO_H', compiler.check_header('langinfo.h'))
conf_data.set('HAVE_LIBINTL_H', compiler.check_header('libintl.h'))
conf_data.set('HAVE_LIBUTIL_H', compiler.check_header('libutil.h'))
conf_data.set('HAVE_LINUX_CAN_BCM_H', compiler.check_header('linux/can/bcm.h'))
conf_data.set('HAVE_LINUX_CAN_H', compiler.check_header('linux/can.h'))
conf_data.set('HAVE_LINUX_CAN_RAW_H', compiler.check_header('linux/can/raw.h'))
conf_data.set('HAVE_LINUX_NETLINK_H', compiler.check_header('linux/netlink.h'))
conf_data.set('HAVE_LINUX_RANDOM_H', compiler.check_header('linux/random.h'))
conf_data.set('HAVE_LINUX_TIPC_H', compiler.check_header('linux/tipc.'))
conf_data.set('HAVE_MEMORY_H', compiler.check_header('memory.h'))
conf_data.set('HAVE_NCURSES_H', compiler.check_header('ncurses.h'))
conf_data.set('HAVE_NDIR_H', compiler.check_header('ndir.h'))
conf_data.set('HAVE_STRINGS_H', compiler.check_header('strings.h'))
conf_data.set('HAVE_STRING_H', compiler.check_header('string.h'))
conf_data.set('HAVE_WCHAR_H', compiler.check_header('wchar.h'))
conf_data.set('HAVE_SIGNAL_H', compiler.check_header('signal.h'))
conf_data.set('HAVE_UTIME_H', compiler.check_header('utime.h'))
conf_data.set('HAVE_DIRECT_H', compiler.check_header('direct.h'))
conf_data.set('HAVE_IO_H', compiler.check_header('io.h'))
conf_data.set('HAVE_PROCESS_H', compiler.check_header('process.h'))
conf_data.set('MS_WINDOWS', compiler.check_header('windows.h'))
    
# @todo : more complex checks in configure.ac
conf_data.set('HAVE_STD_ATOMIC', compiler.check_header('stdatomic.h')) # line 5397
conf_data.set('HAVE_BUILTIN_ATOMIC', compiler.check_header('stdatomic.h'))
conf_data.set('HAVE_STDARG_PROTOTYPES', compiler.check_header('stdarg.h')) # line 4057
conf_data.set('TM_IN_SYS_TIME', 0)
conf_data.set('SYS_SELECT_WITH_SYS_TIME', compiler.check_header('sys/select.h') and compiler.check_header('sys/time.h'))
conf_data.set('TIME_WITH_SYS_TIME', compiler.check_header('time.h') and compiler.check_header('sys/time.h'))
conf_data.set('HAVE_DYNAMIC_LOADING', 0)
# According to the POSIX spec, a pthreads implementation must
# define _POSIX_THREADS in unistd.h. This does not seems to be the case
# for mingw
conf_data.set('_POSIX_THREADS', compiler.check_header('pthread.h'))
    
if host_machine.system()=='windows'
    conf_data.set('MAX_PATH', 260)
endif

if mingw
    # these appear to be missing from mingw
    conf_data.set('MEM_COMMIT', '0x00001000')
    conf_data.set('MEM_RESERVE', '0x00002000')
    conf_data.set('PAGE_READWRITE', '0x04')
    conf_data.set('MEM_RELEASE', '0x8000')
endif

configure_file(
    output : 'pyconfig.h',
    configuration : conf_data,
)
               
#
# PARSER GENERATOR
#

POBJS = []
foreach s : [
    'acceler.c',
    'grammar1.c',
    'listnode.c',
    'node.c',
    'parser.c',
    'bitset.c',
    'metagrammar.c',
    'firstsets.c',
    'grammar.c',
    'token.c',
    'pgen.c',
    ]
    POBJS += join_paths(python_source, 'Parser', s)
endforeach

PARSER_OBJS = POBJS
foreach s : [
    'myreadline.c',
    'parsetok.c',
    'tokenizer.c',
    ]
    PARSER_OBJS += join_paths(python_source, 'Parser', s)
endforeach

PGOBJS = []
foreach s : [
    join_paths('Objects', 'obmalloc.c'),
    join_paths('Python', 'dynamic_annotations.c'),
    join_paths('Python', 'mysnprintf.c'),
    join_paths('Python', 'pyctype.c'),
    join_paths('Parser', 'tokenizer_pgen.c'),
    join_paths('Parser', 'printgrammar.c'),
    join_paths('Parser', 'parsetok_pgen.c'),
    join_paths('Parser', 'pgenmain.c'),
    ]
    PGOBJS += join_paths(python_source, s)
endforeach

PGENOBJS = POBJS + PGOBJS

executable(
    'pgen',
    PGENOBJS,
    include_directories : python_include,
    c_args : PY_CORE_CFLAGS,
    install : true
)

#
# Python Library
#

OBJECT_OBJS = []
foreach s : [
    'abstract.c',
    'accu.c',
    'boolobject.c',
    'bytes_methods.c',
    'bytearrayobject.c',
    'bytesobject.c',
    'call.c',
    'cellobject.c',
    'classobject.c',
    'codeobject.c',
    'complexobject.c',
    'descrobject.c',
    'enumobject.c',
    'exceptions.c',
    'genobject.c',
    'fileobject.c',
    'floatobject.c',
    'frameobject.c',
    'funcobject.c',
    'iterobject.c',
    'listobject.c',
    'longobject.c',
    'dictobject.c',
    'odictobject.c',
    'memoryobject.c',
    'methodobject.c',
    'moduleobject.c',
    'namespaceobject.c',
    'object.c',
    'obmalloc.c',
    'capsule.c',
    'rangeobject.c',
    'setobject.c',
    'sliceobject.c',
    'structseq.c',
    'tupleobject.c',
    'typeobject.c',
    'unicodeobject.c',
    'unicodectype.c',
    'weakrefobject.c',
    ]
    OBJECT_OBJS += join_paths(python_source, 'Objects', s)
endforeach

platform_obj = static_library(
    'getplatform',
    join_paths(python_source, 'Python', 'getplatform.c'),
    include_directories : python_include,
    c_args : PY_CORE_CFLAGS + ['-DPLATFORM="' + MACHDEP + '"'],
    pic : true,
)

PYTHON_OBJS = []
foreach s : [
    '_warnings.c',
    'Python-ast.c',
    'asdl.c',
    'ast.c',
    'ast_opt.c',
    'ast_unparse.c',
    'bootstrap_hash.c',
    'bltinmodule.c',
    'coreconfig.c',
    'ceval.c',
    'compile.c',
    'context.c',
    'codecs.c',
    'dynamic_annotations.c',
    'errors.c',
    'frozenmain.c',
    'future.c',
    'getargs.c',
    'getcompiler.c',
    'getcopyright.c',
    'getversion.c',
    'graminit.c',
    'hamt.c',
    'import.c',
    'importdl.c',
    'marshal.c',
    'modsupport.c',
    'mystrtoul.c',
    'mysnprintf.c',
    'pathconfig.c',
    'peephole.c',
    'pyarena.c',
    'pyctype.c',
    'pyfpe.c',
    'pyhash.c',
    'pylifecycle.c',
    'pymath.c',
    'pystate.c',
    'pythonrun.c',
    'pytime.c',
    'structmember.c',
    'symtable.c',
    'sysmodule.c',
    'traceback.c',
    'getopt.c',
    'pystrcmp.c',
    'pystrtod.c',
    'pystrhex.c',
    'dtoa.c',
    'formatter_unicode.c',
    'fileutils.c',
    #os.path.join(dynload_obj),
    #os.path.join('$(LIBOBJS'),
    #os.path.join('$(MACHDEP_OBJS'),
    #os.path.join('$(DTRACE_OBJS'),
    ]
    PYTHON_OBJS += join_paths(python_source, 'Python', s)
endforeach

PYTHON_OBJS += [THREADOBJ]

# 
# STATIC MODULES
#
# Builds minimum needed static modules
#

MODULE_OBJS = [
#    config_c,
    join_paths(python_source, 'Modules', 'main.c'),
    join_paths(python_source, 'Modules', 'gcmodule.c'),
]

# The modules listed here can't be built as shared libraries for
# various reasons; therefore they are listed here instead of in the
# normal order.

# This only contains the minimal set of modules required to run the
# setup.py script in the root of the Python source tree.

#posix -DPy_BUILD_CORE -I$(srcdir)/Include/internal posixmodule.c # posix (UNIX) system calls
#errno errnomodule.c			# posix (UNIX) errno values
#pwd pwdmodule.c				# this is needed to find out the user's home dir
    ## if $HOME is not set
#_sre _sre.c				# Fredrik Lundh's new regular expressions
#_codecs _codecsmodule.c			# access to the builtin codecs and codec registry
#_weakref _weakref.c			# weak references
#_functools -DPy_BUILD_CORE -I$(srcdir)/Include/internal _functoolsmodule.c   # Tools for working with functions and callable objects
#_operator _operator.c	        	# operator.add() and similar goodies
#_collections _collectionsmodule.c	# Container types
#_abc _abc.c				# Abstract base classes
#itertools itertoolsmodule.c		# Functions creating iterators for efficient looping
#atexit atexitmodule.c			# Register functions to be run at interpreter-shutdown
#_signal -DPy_BUILD_CORE -I$(srcdir)/Include/internal signalmodule.c
#_stat _stat.c				# stat.h interface
#time -DPy_BUILD_CORE -I$(srcdir)/Include/internal timemodule.c	# -lm # time operations and variables
#_thread -DPy_BUILD_CORE -I$(srcdir)/Include/internal _threadmodule.c	# low-level threading interface

## access to ISO C locale support
#_locale -DPy_BUILD_CORE _localemodule.c  # -lintl

## Standard I/O baseline
#_io -DPy_BUILD_CORE -I$(srcdir)/Include/internal -I$(srcdir)/Modules/_io _io/_iomodule.c _io/iobase.c _io/fileio.c _io/bytesio.c _io/bufferedio.c _io/textio.c _io/stringio.c

## faulthandler module
#faulthandler faulthandler.c

## debug tool to trace memory blocks allocated by Python
##
## bpo-35053: The module must be builtin since _Py_NewReference()
## can call _PyTraceMalloc_NewReference(). hashtable.c
_tracemalloc = static_library(
    '_tracemalloc', [
        join_paths(python_source, 'Modules', '_tracemalloc.c'),
        join_paths(python_source, 'Modules', 'hashtable.c'),
    ],
    include_directories : python_include,
    c_args : PY_CORE_CFLAGS,
    pic : true,
)

MODULE_OBJS_objs = _tracemalloc.extract_objects()
#if host_machine.system()=='windows'
    #MODULE_OBJS += [join_paths(python_source, 'PC', 'getpathp.c')]
    #MODULE_OBJS += [join_paths(python_source, 'PC', 'dl_nt.c')]
#else
    #MODULE_OBJS += [join_paths(python_source, 'Modules', 'getpath.c')]
#endif

MODOBJS = []

LIBRARY_OBJS_OMIT_FROZEN = [
    join_paths(python_source, 'Modules', 'getbuildinfo.c')
]
LIBRARY_OBJS_OMIT_FROZEN += PARSER_OBJS
LIBRARY_OBJS_OMIT_FROZEN += OBJECT_OBJS
LIBRARY_OBJS_OMIT_FROZEN += PYTHON_OBJS
LIBRARY_OBJS_OMIT_FROZEN += MODULE_OBJS
LIBRARY_OBJS_OMIT_FROZEN += MODOBJS

LIBRARY_OBJS = LIBRARY_OBJS_OMIT_FROZEN + [
    join_paths(python_source, 'Python', 'frozen.c')
]

static_library(
    LIBRARY,
    LIBRARY_OBJS,
    include_directories : python_include,
    objects: platform_obj.extract_objects(),
    c_args : PY_CORE_CFLAGS,
    pic : true,
    install : true,
)

#shared_library(
#    LIBRARY,
#    LIBRARY_OBJS,
#    include_directories : python_include,
#    objects: MODULE_OBJS_objs,
#    c_args : PY_CORE_CFLAGS,
#    install : true,
#    dependencies : SYSLIBS + LIBS
#)
