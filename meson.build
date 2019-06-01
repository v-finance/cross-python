project('cross-python', 'c')

python_source = get_option('source')

#
# COMPILER DETECTION
#
compiler = meson.get_compiler('c')
mingw = compiler.get_id()=='gcc' and host_machine.system()=='windows'

#
# PROGRAM DETECTION
#

cat = find_program('cat')
echo = find_program('echo')
version = find_program('version.sh')
zip = find_program('zip')

#
# Dependencies
#
# Can be found in PCBuild/get_externals.bat
#

zlib_subproject = subproject('zlib')
zlib_dep = zlib_subproject.get_variable('zlib_dep')

#
# COMPILER OPTIONS
#

# PLAFORM TRIPLET


#elif defined(__linux__)
# if defined(__x86_64__) && defined(__LP64__)
#        x86_64-linux-gnu

        
VERSION = run_command(
    version, [join_paths(python_source, 'configure.ac')],
  ).stdout()

warning(VERSION)

SOABI=		'cpython-36m-x86_64-linux-gnu'
VPATH=          'sourcedir'

LIBS=		[]
if host_machine.system() != 'windows'
    LIBS += [dependency('threads'),]
endif
LIBM=		[compiler.find_library('m', required : false)]
LIBC=		[]
SYSLIBS=	LIBM + LIBC

THREADOBJ = join_paths(python_source, 'Python', 'thread.c')
if host_machine.system()=='windows'
    DYNLOADFILE = 'dynload_win.c' #'dynload_stub.c' # dynload_shlib
else
    DYNLOADFILE = 'dynload_shlib.c'
    SYSLIBS += [compiler.find_library('dl', required : true)]
endif

# Install prefix for architecture-independent files
prefix=		'.'

# Install prefix for architecture-dependent files
exec_prefix=	prefix

PYTHONPATH='Lib'

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
    add_project_link_arguments('-municode', '-mwindows', language:'c')
    SYSLIBS += [
        compiler.find_library('mingw32', required : true),
        compiler.find_library('version', required : true), 
        compiler.find_library('ws2_32', required : true), 
        compiler.find_library('shlwapi', required : true), 
        compiler.find_library('iphlpapi', required : true),
    ]
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

#conf_data.set('SIZEOF_WCHAR_T', compiler.sizeof('wchar_t', prefix : '#include <sys/types.h>') or compiler.sizeof('wchar_t', prefix : '#include <wchar.h>'))
conf_data.set('SIZEOF_WCHAR_T', compiler.sizeof('wchar_t', prefix : '#include <wchar.h>'))
conf_data.set('SIZEOF_DOUBLE', compiler.sizeof('double'))
conf_data.set('SIZEOF_FLOAT', compiler.sizeof('float'))
conf_data.set('SIZEOF_FPOS_T', compiler.sizeof('fpos_t'))
conf_data.set('SIZEOF_INT', compiler.sizeof('int'))
conf_data.set('SIZEOF_LONG', compiler.sizeof('long'))
conf_data.set('SIZEOF_LONG_DOUBLE', compiler.sizeof('long double'))
conf_data.set('SIZEOF_LONG_LONG', compiler.sizeof('long long'))
conf_data.set('SIZEOF_OFF_T', compiler.sizeof('off_t'))
conf_data.set('SIZEOF_PID_T', compiler.sizeof('pid_t', prefix : '#include <sys/types.h>'))
conf_data.set('SIZEOF_PTHREAD_KEY_T', compiler.sizeof('pthread_key_t', prefix : '#include <pthread.h>'))
conf_data.set('SIZEOF_PTHREAD_T', compiler.sizeof('pthread_t', prefix : '#include <pthread.h>'))
conf_data.set('SIZEOF_SHORT', compiler.sizeof('short'))
conf_data.set('SIZEOF_SIZE_T', compiler.sizeof('size_t'))
conf_data.set('SIZEOF_TIME_T', compiler.sizeof('time_t', prefix : '#include <time.h>'))
conf_data.set('SIZEOF_UINTPTR_T', compiler.sizeof('uintptr_t', prefix: '#include <stdint.h>,'))
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

conf_data.set('HAVE_TIMEGM', compiler.has_function('timegm'))
conf_data.set('HAVE_TIMES', compiler.has_function('times'))
conf_data.set('HAVE_CLOCK_GETTIME', compiler.has_function('clock_gettime'))
conf_data.set('HAVE_CLOCK', compiler.has_function('clock'))
conf_data.set('HAVE_LSTAT', compiler.has_function('lstat'))
conf_data.set('HAVE_LUTIMES', compiler.has_function('lutimes'))
conf_data.set('HAVE_COPYSIGN', compiler.has_function('copysign'))
conf_data.set('HAVE_ACOSH', compiler.has_function('acosh'))
conf_data.set('HAVE_ASINH', compiler.has_function('asinh'))
conf_data.set('HAVE_ATANH', compiler.has_function('atanh'))
conf_data.set('HAVE_ERF', compiler.has_function('erf'))
conf_data.set('HAVE_ERFC', compiler.has_function('erfc'))
conf_data.set('HAVE_EXPM1', compiler.has_function('expm1'))
conf_data.set('HAVE_FINITE', compiler.has_function('finite'))
conf_data.set('HAVE_GAMMA', compiler.has_function('gamma'))
conf_data.set('HAVE_HYPOT', compiler.has_function('hypot'))
conf_data.set('HAVE_LGAMMA', compiler.has_function('lgamma'))
conf_data.set('HAVE_LOG1P', compiler.has_function('log1p'))
conf_data.set('HAVE_LOG2', compiler.has_function('log2'))
conf_data.set('HAVE_ROUND', compiler.has_function('round'))
conf_data.set('HAVE_TGAMMA', compiler.has_function('tgamma'))
    
conf_data.set('HAVE_WMEMCMP', compiler.has_function('wmemcmp'))
conf_data.set('HAVE_REALPATH', compiler.has_function('realpath'))
conf_data.set('HAVE_GETPPID', compiler.has_function('getppid') or compiler.has_function('getpid'))
conf_data.set('HAVE_GETLOGIN', compiler.has_function('getlogin'))
conf_data.set('HAVE_SPAWNV', compiler.has_function('spawnv'))
conf_data.set('HAVE_EXECV', compiler.has_function('execv'))
conf_data.set('HAVE_WSPAWNV', compiler.has_function('_wspawnv'))
conf_data.set('HAVE_WEXECV', compiler.has_function('_wexecv'))
conf_data.set('HAVE_PIPE', compiler.has_function('CreatePipe'))
conf_data.set('HAVE_SYSTEM', compiler.has_function('system'))
conf_data.set('HAVE_CWAIT', compiler.has_function('cwait'))
conf_data.set('HAVE_FSYNC', compiler.has_function('fsync') or compiler.has_function('_commit'))
conf_data.set('HAVE_COMMIT', compiler.has_function('_commit'))
conf_data.set('HAVE_FORK', compiler.has_function('fork') and not mingw)
conf_data.set('HAVE_DLOPEN', compiler.has_function('dlopen', prefix: '#include <dlfcn.h>', args: ['-ldl']))

conf_data.set('MS_WINDOWS', compiler.check_header('windows.h'))
conf_data.set('NT_THREADS', compiler.check_header('windows.h'))
    
# @todo : more complex checks in configure.ac
conf_data.set('HAVE_STD_ATOMIC', compiler.check_header('stdatomic.h')) # line 5397
conf_data.set('HAVE_BUILTIN_ATOMIC', compiler.check_header('stdatomic.h'))
conf_data.set('HAVE_STDARG_PROTOTYPES', compiler.check_header('stdarg.h')) # line 4057
conf_data.set('TM_IN_SYS_TIME', 0)
conf_data.set('SYS_SELECT_WITH_SYS_TIME', compiler.check_header('sys/select.h') and compiler.check_header('sys/time.h'))
conf_data.set('TIME_WITH_SYS_TIME', compiler.check_header('time.h') and compiler.check_header('sys/time.h'))
conf_data.set('HAVE_DECL_TZNAME', compiler.check_header('time.h'))
conf_data.set('HAVE_TZNAME', compiler.check_header('time.h'))
conf_data.set('HAVE_DYNAMIC_LOADING', 0)


#
# Windows specific configuration from PC/pyconfig.h
#
if host_machine.system()=='windows'
    conf_data.set('MAX_PATH', 260)
    # set the version macros for the windows headers
    # Python 3.5+ requires Windows Vista or greater
    conf_data.set('Py_WINVER', 0x0601) # _WIN32_WINNT_VISTA 
    conf_data.set('Py_NTDDI', 'NTDDI_VISTA')
    # We only set these values when building Python - we don't want to force
    # these values on extensions, as that will affect the prototypes and
    # structures exposed in the Windows headers. Even when building Python, we
    # allow a single source file to override this - they may need access to
    # structures etc so it can optionally use new Windows features if it
    # determines at runtime they are available.

    conf_data.set('NTDDI_VERSION', 'Py_NTDDI')
    conf_data.set('WINVER', 'Py_WINVER')
    conf_data.set('_WIN32_WINNT', 'Py_WINVER')
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
# list off files can be found in Makefile.pre.in

POBJS = []
foreach s : [
    'acceler.c',
    'grammar1.c',
    'listnode.c',
    'node.c',
    'parser.c',
    'token.c',
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

#executable(
#    'pgen',
#    PGENOBJS,
#    include_directories : python_include,
#    c_args : PY_CORE_CFLAGS,
#    install : true
#)

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
    'interpreteridobject.c',
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
    'picklebufobject.c',
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

#
# Python
#
# list off files can be found in Makefile.pre.in

PYTHON_OBJS = []
foreach s : [
    '_warnings.c',
    'Python-ast.c',
    'asdl.c',
    'ast.c',
    'ast_opt.c',
    'ast_unparse.c',
    'bltinmodule.c',
    'ceval.c',
    'compile.c',
    'context.c',
    'codecs.c',
    'dynamic_annotations.c',
    'errors.c',
    #'frozenmain.c',
    'future.c',
    'getargs.c',
    'getcompiler.c',
    'getcopyright.c',
    'getversion.c',
    'graminit.c',
    'hamt.c',
    'import.c',
    'importdl.c',
    'initconfig.c',
    'marshal.c',
    'modsupport.c',
    'mystrtoul.c',
    'mysnprintf.c',
    'pathconfig.c',
    'peephole.c',
    'preconfig.c',
    'pyarena.c',
    'pyctype.c',
    'pyfpe.c',
    'pyhash.c',
    'pylifecycle.c',
    'pymath.c',
    'pystate.c',
    'context.c',
    'hamt.c',
    'pythonrun.c',
    'pytime.c',
    'bootstrap_hash.c',
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

# The modules listed here can't be built as shared libraries for
# various reasons; therefore they are listed here instead of in the
# normal order.

# This only contains the minimal set of modules required to run the
# setup.py script in the root of the Python source tree.

# a list of pairs (static_library, module name) to ease inclusion
# in config.c
MODOBJS = []

# posix (UNIX) system calls
if host_machine.system()=='windows'
    posix = static_library(
        'nt', [
            join_paths(python_source, 'Modules', 'posixmodule.c'),
        ],
        include_directories : python_include,
        c_args : PY_CORE_CFLAGS + ['-D_MSC_VER', '-DWINVER=0x0601', '-D_WIN32_WINNT=0x0601'],
    )
    MODOBJS += [[posix, 'nt']]
    winreg = static_library(
        'winreg', [
            join_paths(python_source, 'PC', 'winreg.c'),
        ],
        include_directories : python_include,
        c_args : PY_CORE_CFLAGS,# + ['-D_MSC_VER', '-DWINVER=0x0601', '-D_WIN32_WINNT=0x0601'],
    )
    MODOBJS += [[winreg, 'winreg']]
else
    posix = static_library(
        'posix', [
            join_paths(python_source, 'Modules', 'posixmodule.c'),
        ],
        include_directories : python_include,
        c_args : PY_CORE_CFLAGS,
    )
    MODOBJS += [[posix, 'posix']]
endif

zlib_includes = []
zlib_includes += zlib_subproject.get_variable('incdir')
zlib_includes += python_include

zlib = static_library(
    'zlib', [
        join_paths(python_source, 'Modules', 'zlibmodule.c'),
    ],
    include_directories : zlib_includes,
    link_with: zlib_subproject.get_variable('zlib'),
    c_args : PY_CORE_CFLAGS,
)
MODOBJS += [[zlib, 'zlib']]

# a list of pairs (module name, module sources) to ease the creation
# of MODOBJS
MODSOURCES = []

#errno errnomodule.c			# posix (UNIX) errno values
MODSOURCES += [['errno', ['errnomodule.c'],]]
# this is needed to find out the user's home dir
## if $HOME is not set
if compiler.check_header('pwd.h')
    MODSOURCES += [['pwd', ['pwdmodule.c'],]]
endif

# Fredrik Lundh's new regular expressions
MODSOURCES += [['_sre', ['_sre.c'],]]
# access to the builtin codecs and codec registry
MODSOURCES += [['_codecs', ['_codecsmodule.c'],]]
# weak references
MODSOURCES += [['_weakref', ['_weakref.c'],]]
# Tools for working with functions and callable objects
MODSOURCES += [['_functools', ['_functoolsmodule.c'],]]
# operator.add() and similar goodies
MODSOURCES += [['_operator', ['_operator.c'],]]
# Container types
MODSOURCES += [['_collections', ['_collectionsmodule.c'],]]
# Abstract base classes
MODSOURCES += [['_abc', ['_abc.c'],]]
# Functions creating iterators for efficient looping
MODSOURCES += [['itertools', ['itertoolsmodule.c'],]]
# Register functions to be run at interpreter-shutdown
MODSOURCES += [['atexit', ['atexitmodule.c'],]]
MODSOURCES += [['_signal', ['signalmodule.c'],]]
# stat.h interface
MODSOURCES += [['_stat', ['_stat.c'],]]
#time -DPy_BUILD_CORE -I$(srcdir)/Include/internal timemodule.c	# -lm # time operations and variables
MODSOURCES += [['time', ['timemodule.c'],]]
# low-level threading interface
MODSOURCES += [['_thread', ['_threadmodule.c'],]]
## access to ISO C locale support
#_locale -DPy_BUILD_CORE _localemodule.c  # -lintl
MODSOURCES += [['_locale', ['_localemodule.c'],]]
MODSOURCES += [['unicodedata', ['unicodedata.c'],]]
## faulthandler module
MODSOURCES += [['faulthandler', ['faulthandler.c'],]]
## debug tool to trace memory blocks allocated by Python
##
## bpo-35053: The module must be builtin since _Py_NewReference()
## can call _PyTraceMalloc_NewReference(). hashtable.c
MODSOURCES += [['_tracemalloc', ['_tracemalloc.c', 'hashtable.c'],]]

IO_SRC = [
    join_paths('_io', '_iomodule.c'),
    join_paths('_io', 'iobase.c'),
    join_paths('_io', 'fileio.c'),
    join_paths('_io', 'bytesio.c'),
    join_paths('_io', 'bufferedio.c'),
    join_paths('_io', 'textio.c'),
    join_paths('_io', 'stringio.c'),
]
if host_machine.system()=='windows'
    IO_SRC += [
        join_paths('_io', 'winconsoleio.c'),
    ]
endif

## Standard I/O baseline
MODSOURCES += [['_io', IO_SRC,]]

# convert MODSOURCES into MODOBJS
foreach modsource:MODSOURCES
    sources = []
    foreach s:modsource[1]
        sources += [join_paths(python_source, 'Modules', s)]
    endforeach
    modlib = static_library(
        modsource[0], sources,
        include_directories : python_include,
        c_args : PY_CORE_CFLAGS,
    )
    MODOBJS += [[modlib, modsource[0]]]
endforeach

dynload = static_library(
    'dynload', [
        join_paths(python_source, 'Python', DYNLOADFILE),
    ],
    include_directories : python_include,
    c_args : PY_CORE_CFLAGS + ['-DSOABI="'+SOABI+'"'],
    pic : true,
)

GETPATH_SRC = []
if host_machine.system()=='windows'
    GETPATH_SRC += [join_paths(python_source, 'PC', 'getpathp.c')]
    GETPATH_SRC += [join_paths(python_source, 'PC', 'dl_nt.c')]
else
    GETPATH_SRC += [join_paths(python_source, 'Modules', 'getpath.c')]
endif

GETPATH_C_ARGS = []
GETPATH_C_ARGS += ['-DPREFIX="' + prefix + '"']
GETPATH_C_ARGS += ['-DEXEC_PREFIX="' + exec_prefix + '"']
GETPATH_C_ARGS += ['-DVERSION="' + VERSION + '"']
GETPATH_C_ARGS += ['-DVPATH="' + VPATH + '"']
GETPATH_C_ARGS += ['-DPYTHONPATH="' + PYTHONPATH + '"']

getpath = static_library(
    'getpath', GETPATH_SRC,
    include_directories : python_include,
    c_args : PY_CORE_CFLAGS + GETPATH_C_ARGS,
    pic : true,
)

#
# this is a replacement for the makesetup script, to manipulate 'config.c.in'
# and replace the markers with references to the build in modules
#

config_c_in = run_command(
    cat, [join_paths(python_source, 'Modules', 'config.c.in')],
  ).stdout()
  
config_c_in_lines = config_c_in.split('\n')
config_c_out_lines = []

foreach line: config_c_in_lines
    config_c_out_lines += [line, '\n']
    if line.startswith('/* -- ADDMODULE MARKER 1')
        foreach mod:MODOBJS
            config_c_out_lines += ['extern PyObject* PyInit_@0@(void);\n'.format(mod[-1])]
        endforeach
    endif
    if line.startswith('/* -- ADDMODULE MARKER 2')
        foreach mod:MODOBJS
            config_c_out_lines += ['{ "@0@", PyInit_@0@ },\n'.format(mod[-1])]
        endforeach
    endif        
endforeach

config_c_generator = generator(
    echo,
    output  : '@BASENAME@.c',
    arguments : config_c_out_lines,
    capture: true,
)

MODULE_OBJS = [
    config_c_generator.process(join_paths(python_source, 'Modules', 'config.c.in')),
    join_paths(python_source, 'Modules', 'main.c'),
    join_paths(python_source, 'Modules', 'gcmodule.c'),
]

LIBRARY_OBJS_OMIT_FROZEN = [
    join_paths(python_source, 'Modules', 'getbuildinfo.c')
]
LIBRARY_OBJS_OMIT_FROZEN += PARSER_OBJS
LIBRARY_OBJS_OMIT_FROZEN += OBJECT_OBJS
LIBRARY_OBJS_OMIT_FROZEN += PYTHON_OBJS
LIBRARY_OBJS_OMIT_FROZEN += MODULE_OBJS

LIBRARY_OBJS = LIBRARY_OBJS_OMIT_FROZEN + [
    join_paths(python_source, 'Python', 'frozen.c')
]
if host_machine.system()=='windows'
    LIBRARY_OBJS += [
        #join_paths(python_source, 'PC', 'frozen_dllmain.c'),
    ]
endif
        
MODLIBS = []
foreach mod:MODOBJS
    MODLIBS += mod[0]
endforeach

libpython = both_libraries(
    LIBRARY,
    LIBRARY_OBJS ,
    include_directories : python_include,
    c_args : PY_CORE_CFLAGS,
    install : true,
    link_with : MODLIBS + [dynload, getpath, platform_obj],
    dependencies : SYSLIBS + LIBS,
)

PYTHON_SRC = [join_paths(python_source, 'Programs', 'python.c')]
if host_machine.system()=='windows'
    PYTHON_SRC += [
        join_paths(python_source, 'PC', 'WinMain.c'),
    ]
endif

python_exe = executable(
    'python',
    PYTHON_SRC,
    include_directories : python_include,
    c_args : PY_CORE_CFLAGS,
    install : true,
    link_with : [libpython.get_shared_lib()],
    dependencies : SYSLIBS + LIBS,
)

#
# Install the standard library
#

install_subdir(
    join_paths(python_source, 'Lib'),
    install_dir: join_paths(get_option('bindir'), 'Lib'),
    strip_directory : true
)

custom_target(
    'python._pth',
    command : [echo, '-e', 'Lib\n.'],
    output  : 'python._pth',
    capture: true,
    install_dir: get_option('bindir'),
    install: true
)

#
# Now the core python interpreter works.
# The next step is to build various extension modules, these steps are
# described in setup.py
#
    
extension_includes = include_directories([
    join_paths(python_source, 'Modules'),
    join_paths(python_source, 'Include'),
] + host_includes)
extension_prefix = ''
extension_suffix = 'pyd'

socketmodule_c_generator = generator(
    cat,
    output  : '@BASENAME@.c',
    arguments : [join_paths('@SOURCE_DIR@', 'Modules', '_socket', 'ip_protocols.c'), '@INPUT@'],
    capture: true,
)

socket_module_objs = [
    socketmodule_c_generator.process(
        join_paths(python_source, 'Modules', 'socketmodule.c')
    )
]

shared_library(
    '_socket',
    socket_module_objs,
    include_directories : extension_includes,
    c_args: PY_CFLAGS + PY_CFLAGS_NODIST,
    install : true,
    link_with :[libpython.get_shared_lib()],
    dependencies : SYSLIBS + LIBS,
    name_prefix : extension_prefix,
    name_suffix : extension_suffix,
)

# from detect_simple_extensions

#
# The following modules are all pretty straightforward, and compile
# on pretty much any POSIXish platform.
#

# array objects
shared_library(
    'array',
    join_paths(python_source, 'Modules', 'arraymodule.c'),
    include_directories : extension_includes,
    c_args: PY_CFLAGS + PY_CFLAGS_NODIST,
    install : true,
    link_with :[libpython.get_shared_lib()],
    dependencies : SYSLIBS + LIBS,
    name_prefix : extension_prefix,
    name_suffix : extension_suffix,
)


# Context Variables
shared_library(
    '_contextvars',
    join_paths(python_source, 'Modules', '_contextvarsmodule.c'),
    include_directories : extension_includes,
    c_args: PY_CFLAGS + PY_CFLAGS_NODIST,
    install : true,
    link_with :[libpython.get_shared_lib()],
    dependencies : SYSLIBS + LIBS,
    name_prefix : extension_prefix,
    name_suffix : extension_suffix,
)

shared_math = join_paths(python_source, 'Modules', '_math.c')
m_library = [compiler.find_library('m', required : true)]

## math library functions, e.g. sin()
shared_library(
    'math',
    [join_paths(python_source, 'Modules', 'mathmodule.c'), shared_math],
    include_directories : extension_includes,
    c_args: PY_CFLAGS + PY_CFLAGS_NODIST,
    install : true,
    link_with :[libpython.get_shared_lib()],
    dependencies : SYSLIBS + LIBS + m_library,
    name_prefix : extension_prefix,
    name_suffix : extension_suffix,
)

## complex math library functions
shared_library(
    'cmath',
    [join_paths(python_source, 'Modules', 'cmathmodule.c'), shared_math],
    include_directories : extension_includes,
    c_args: PY_CFLAGS + PY_CFLAGS_NODIST,
    install : true,
    link_with :[libpython.get_shared_lib()],
    dependencies : SYSLIBS + LIBS + m_library,
    name_prefix : extension_prefix,
    name_suffix : extension_suffix,
)

# select(2); not on ancient System V
shared_library(
    'select',
    [join_paths(python_source, 'Modules', 'selectmodule.c')],
    include_directories : extension_includes,
    c_args: PY_CFLAGS + PY_CFLAGS_NODIST,
    install : true,
    link_with :[libpython.get_shared_lib()],
    dependencies : SYSLIBS + LIBS,
    name_prefix : extension_prefix,
    name_suffix : extension_suffix,
)

# Fred Drake's interface to the Python parser
shared_library(
    'parser',
    [join_paths(python_source, 'Modules', 'parsermodule.c')],
    include_directories : extension_includes,
    c_args: PY_CFLAGS + PY_CFLAGS_NODIST,
    install : true,
    link_with :[libpython.get_shared_lib()],
    dependencies : SYSLIBS + LIBS,
    name_prefix : extension_prefix,
    name_suffix : extension_suffix,
)

# Memory-mapped files (also works on Win32).
#shared_library(
    #'mmap',
    #[join_paths(python_source, 'Modules', 'mmapmodule.c')],
    #include_directories : extension_includes,
    #c_args: PY_CFLAGS + PY_CFLAGS_NODIST,
    #install : true,
    #link_with :[libpython.get_shared_lib()],
    #dependencies : SYSLIBS + LIBS,
    #name_prefix : extension_prefix,
    #name_suffix : extension_suffix,
#)

# Lance Ellinghaus's syslog module
# syslog daemon interface
#shared_library(
    #'syslog',
    #[join_paths(python_source, 'Modules', 'syslogmodule.c')],
    #include_directories : extension_includes,
    #c_args: PY_CFLAGS + PY_CFLAGS_NODIST,
    #install : true,
    #link_with :[libpython.get_shared_lib()],
    #dependencies : SYSLIBS + LIBS,
    #name_prefix : extension_prefix,
    #name_suffix : extension_suffix,
#)

# Python interface to subinterpreter C-API.
shared_library(
    '_xxsubinterpreters',
    [join_paths(python_source, 'Modules', '_xxsubinterpretersmodule.c')],
    include_directories : extension_includes,
    c_args: PY_CFLAGS + PY_CFLAGS_NODIST,
    install : true,
    link_with :[libpython.get_shared_lib()],
    dependencies : SYSLIBS + LIBS,
    name_prefix : extension_prefix,
    name_suffix : extension_suffix,
)

shared_library(
    '_overlapped',
    [join_paths(python_source, 'Modules', 'overlapped.c')],
    include_directories : extension_includes,
    c_args: PY_CFLAGS + PY_CFLAGS_NODIST,
    install : true,
    link_with :[libpython.get_shared_lib()],
    dependencies : SYSLIBS + LIBS,
    name_prefix : extension_prefix,
    name_suffix : extension_suffix,
)

shared_library(
    '_struct',
    [join_paths(python_source, 'Modules', '_struct.c')],
    include_directories : extension_includes,
    c_args: PY_CFLAGS + PY_CFLAGS_NODIST,
    install : true,
    link_with :[libpython.get_shared_lib()],
    dependencies : SYSLIBS + LIBS,
    name_prefix : extension_prefix,
    name_suffix : extension_suffix,
)

if host_machine.system()=='windows'
    shared_library(
        'msvcrt',
        [join_paths(python_source, 'PC', 'msvcrtmodule.c')],
        include_directories : extension_includes,
        c_args: PY_CORE_CFLAGS + ['-D_MSC_VER=1600'],
        install : true,
        link_with :[libpython.get_shared_lib()],
        dependencies : SYSLIBS + LIBS,
        name_prefix : extension_prefix,
        name_suffix : extension_suffix,
    )
    shared_library(
        '_winapi',
        [join_paths(python_source, 'Modules', '_winapi.c')],
        include_directories : extension_includes,
        c_args: PY_CORE_CFLAGS + ['-D_MSC_VER=1600'],
        install : true,
        link_with :[libpython.get_shared_lib()],
        dependencies : SYSLIBS + LIBS,
        name_prefix : extension_prefix,
        name_suffix : extension_suffix,
    )
endif
