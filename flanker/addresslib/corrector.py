# coding:utf-8
"""
Spelling corrector library, used to correct common typos in domains like
gmal.com instead of gmail.com.

The spelling corrector uses difflib which in turn uses the
Ratcliff-Obershelp algorithm [1] to compute the similarity of two strings.
This is a very fast an accurate algorithm for domain spelling correction.

The (only) public method this module has is suggest(word), which given
a domain, suggests an alternative or returns the original domain
if no suggestion exists.

[1] http://xlinux.nist.gov/dads/HTML/ratcliffObershelp.html
"""

import difflib


def suggest(word, cutoff=0.77):
    """
    Given a domain and a cutoff heuristic, suggest an alternative or return the
    original domain if no suggestion exists.
    """
    if word in LOOKUP_TABLE:
        return LOOKUP_TABLE[word]

    guess = difflib.get_close_matches(word, MOST_COMMON_DOMAINS, n=1, cutoff=cutoff)
    if guess and len(guess) > 0:
        return guess[0]
    return word


MOST_COMMON_DOMAINS = [
    # mailgun :)
    'mailgun.net',
    # big esps
    '163.com',
    'aim.com',
    'alice.it',
    'aol.co.uk',
    'aol.com',
    'att.net',
    'azet.sk',
    'bell.net',
    'bellsouth.net',
    'bigpond.com',
    'bigpond.com.au',
    'bigpond.net.au',
    'bluewin.ch',
    'blueyonder.co.uk',
    'bol.com.br',
    'btinternet.com',
    'btopenworld.com',
    'cableone.net',
    'centrum.sk',
    'centurylink.net',
    'centurytel.net',
    'charter.net',
    'comcast.net',
    'cox.net',
    'cs.com',
    'earthlink.net',
    'email.com',
    'email.cz',
    'email.it',
    'embarqmail.com',
    'excite.com',
    'fastwebnet.it',
    'free.fr',
    'freemail.hu',
    'freenet.de',
    'frontier.com',
    'frontiernet.net',
    'fuse.net',
    'gmail.com',
    'gmx.at',
    'gmx.ch',
    'gmx.com',
    'gmx.de',
    'gmx.net',
    'google.com',
    'googlemail.com',
    'hanmail.net',
    'home.nl',
    'hotmail.be',
    'hotmail.ca',
    'hotmail.co.jp',
    # 'hotmail.co.nz',
    'hotmail.co.uk',
    'hotmail.com',
    'hotmail.com.ar',
    'hotmail.com.au',
    'hotmail.de',
    'hotmail.es',
    'hotmail.fr',
    'hotmail.gr',
    'hotmail.it',
    'hotmail.nl',
    'hotmail.no',
    'hotmail.se',
    'hughes.net',
    'icloud.com',
    'iinet.net.au',
    'inbox.lv',
    'inbox.ru',
    'interia.pl',
    'juno.com',
    'laposte.net',
    'libero.it',
    'list.ru',
    'live.be',
    'live.ca',
    'live.co.uk',
    'live.com',
    'live.com.ar',
    'live.com.au',
    'live.com.mx',
    'live.de',
    'live.dk',
    'live.fr',
    'live.it',
    'live.nl',
    'live.no',
    'live.se',
    'mac.com',
    'mail.com',
    'mail.ru',
    'me.com',
    'microsoft.com',
    'mindspring.com',
    'msn.com',
    'naver.com',
    # 'nc.rr.com',
    'netscape.net',
    'netspace.net.au',
    'netzero.com',
    'netzero.net',
    'neuf.fr',
    'nhs.net',
    'ntlworld.com',
    'o2.pl',
    'online.no',
    'optimum.net',
    'optonline.net',
    'optusnet.com.au',
    'orange.fr',
    'ostrovok.ru',
    'outlook.com',
    'outlook.com.au',
    'outlook.de',
    'outlook.es',
    'outlook.fr',
    'outlook.it',
    'pacbell.net',
    'planet.nl',
    'prodigy.net',
    'prodigy.net.mx',
    'protonmail.com',
    'q.com',
    'qq.com',
    'rambler.ru',
    'reagan.com',
    'rediffmail.com',
    'roadrunner.com',
    'rocketmail.com',
    'rogers.com',
    'sbcglobal.net',
    'seznam.cz',
    'sfr.fr',
    'shaw.ca',
    'sky.com',
    'skynet.be',
    'suddenlink.net',
    'swbell.net',
    'sympatico.ca',
    't-online.de',
    'talktalk.net',
    'telefonica.net',
    'telenet.be',
    'telfort.nl',
    'telia.com',
    'telus.net',
    'telusplanet.net',
    'tiscali.co.uk',
    'tiscali.it',
    'ukr.net',
    'uol.com.br',
    'usa.net',
    'vepl.com',
    'verizon.net',
    'videotron.ca',
    'virgilio.it',
    'virgin.net',
    'virginmedia.com',
    'wanadoo.fr',
    'web.de',
    'windowslive.com',
    'windstream.net',
    'wp.pl',
    'xs4all.nl',
    'xtra.co.nz',
    'y7mail.com',
    'ya.ru',
    'yahoo.ca',
    'yahoo.co.id',
    # 'yahoo.co.in',
    'yahoo.co.jp',
    # 'yahoo.co.nz',
    'yahoo.co.uk',
    'yahoo.com',
    'yahoo.com.ar',
    'yahoo.com.au',
    'yahoo.com.br',
    'yahoo.com.hk',
    'yahoo.com.mx',
    'yahoo.com.my',
    'yahoo.com.ph',
    'yahoo.com.sg',
    'yahoo.com.tw',
    'yahoo.de',
    'yahoo.es',
    'yahoo.fr',
    'yahoo.gr',
    'yahoo.ie',
    'yahoo.in',
    'yahoo.it',
    'yahoo.no',
    'yahoo.se',
    'yandex.com',
    'yandex.ru',
    'ymail.com',
    'ziggo.nl',
    'zoominternet.net'
]

# domains that the corrector doesn't fix that we should fix
LOOKUP_TABLE = {
    u'yahoo':       u'yahoo.com',
    u'gmail':       u'gmail.com',
    u'hotmail':     u'hotmail.com',
    u'live':        u'live.com',
    u'outlook':     u'outlook.com',
    u'msn':         u'msn.com',
    u'googlemail':  u'googlemail.com',
    u'aol':         u'aol.com',
    u'aim':         u'aim.com',
    u'icloud':      u'icloud.com',
    u'me':          u'me.com',
    u'mac':         u'mac.com',
    u'facebook':    u'facebook.com',
    u'comcast':     u'comcast.net',
    u'sbcglobal':   u'sbcglobal.net',
    u'bellsouth':   u'bellsouth.net',
    u'verizon':     u'verizon.net',
    u'earthlink':   u'earthlink.net',
    u'cox':         u'cox.net',
    u'charter':     u'charter.net',
    u'shaw':        u'shaw.ca',
    u'bell':        u'bell.net'
}
