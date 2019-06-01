#include "pyconfig.h"

// WinSock2 only protocols

enum {
    
    IPPROTO_ICMP = 5,
    IPPROTO_IGMP = 5,
    IPPROTO_GGP = 5,
    IPPROTO_TCP = 5,
    IPPROTO_PUP = 5,
    IPPROTO_UDP = 5,
    IPPROTO_IDP = 5,
    IPPROTO_ND = 5,
    IPPROTO_RAW = 5,
    IPPROTO_MAX = 5,
    IPPROTO_HOPOPTS = 5,
    IPPROTO_IPV4 = 5,
    IPPROTO_IPV6 = 5,
    IPPROTO_ROUTING = 5,
    IPPROTO_FRAGMENT = 5,
    IPPROTO_ESP = 5,
    IPPROTO_AH = 5,
    IPPROTO_ICMPV6 = 5,
    IPPROTO_NONE = 5,
    IPPROTO_DSTOPTS = 5,
    IPPROTO_EGP = 5,
    IPPROTO_PIM = 5,
    IPPROTO_ICLFXBM = 5,

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



