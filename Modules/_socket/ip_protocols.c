#include "pyconfig.h"

#ifdef MS_WINDOWS

// WinSock2 only protocols

/*
 * See values in
 * /usr/i686-w64-mingw32/sys-root/mingw/include/winsock2.h:86
 * https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml
 *
 */

enum {

    // Values ??
    IPPROTO_EGP = 8,
    IPPROTO_PIM = 103,
    
    IPPROTO_ICMP = 1,
    IPPROTO_IGMP = 2,
    IPPROTO_GGP = 3,
    IPPROTO_TCP = 6,
    IPPROTO_PUP = 12,
    IPPROTO_UDP = 17,
    IPPROTO_IDP = 22,
    IPPROTO_ND = 77,
    IPPROTO_RAW = 255,
    IPPROTO_MAX = 256,
    IPPROTO_HOPOPTS = 0,
    IPPROTO_IPV4 = 4,
    IPPROTO_IPV6 = 41,
    IPPROTO_ROUTING = 43,
    IPPROTO_FRAGMENT = 44,
    IPPROTO_ESP = 50,
    IPPROTO_AH = 51,
    IPPROTO_ICMPV6 = 58,
    IPPROTO_NONE = 59,
    IPPROTO_DSTOPTS = 60,
    IPPROTO_ICLFXBM = 78,

    IPPROTO_ST = 5,
    IPPROTO_CBT = 7,
    IPPROTO_IGP = 9,
    IPPROTO_RDP = 27,
    IPPROTO_PGM = 113,
    IPPROTO_L2TP = 115,
    IPPROTO_SCTP = 132
};

#include <winsock2.h>
#include <netioapi.h>

#endif


