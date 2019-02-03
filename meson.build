project('cross-python', 'c')

python_source = get_option('source')
python_include = include_directories(join_paths(python_source, 'Include'))

#
# COMPILER OPTIONS
#


OPT = [
    '-DNDEBUG', '-fwrapv', '-O3', '-Wall', '-Wstrict-prototypes',
    # for mingw
    # '-mwindows', '-municode'
    # -gstabs : to be able to debug using wine
    # '-gstabs'
]

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

compiler = meson.get_compiler('c')

conf_data = configuration_data()

# configure.ac line 122

# The later defininition of _XOPEN_SOURCE disables certain features
# on Linux, so we need _GNU_SOURCE to re-enable them (makedev, tm_zone).
conf_data.set('_GNU_SOURCE', '1')  # Define on Linux to activate all library features

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