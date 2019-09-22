import requests

wd = '\x1b[90;1m'
GL = '\x1b[96;1m'
BB = '\x1b[34;1m'
YY = '\x1b[33;1m'
GG = '\x1b[32;1m'
WW = '\x1b[0;1m'
RR = '\x1b[31;1m'
CC = '\x1b[36;1m'
B  = '\x1b[34m'
Y  = '\x1b[33;1m'
G  = '\x1b[32m'
W  = '\x1b[0;1m'
R  = '\x1b[31m'
C  = '\x1b[36;1m'
P  = '\x1b[1;35m'
print GG + '      @@@@@@   @@@  @@@  @@@@@@@@  @@@  '
print '     @@@@@@@   @@@  @@@  @@@@@@@@  @@@  '
print '     !@@       @@!  @@@  @@!       @@!  '
print '     !@!       !@!  @!@  !@!       !@!  '
print '     !!@@!!    @!@  !@!  @!!!:!    !!@  '
print '      !!@!!!   !@!  !!!  !!!!!:    !!!  '
print G + '          !:!  !!:  !!!  !!:       !!:  '
print '         !:!   :!:  !:!  :!:       :!:  '
print '     :::: ::   ::::: ::   ::        ::  '
print '     :: : :     : :  :    :        :'
print YY + '\t      Subdomain Finder'
print ''
print WW + '  #########################################'
print '  #                                       #'
print '  #         Author : Nanda ID             #'
print '  #           Team : CLAY WHITE DARK      #'
print '  #      Thanks To : iExEi HD             #'
print '  #                : Akbar-Neotech        #'
print '  #                                       #'
print '  #########################################'
print wd + 'NOTE : Masukan Website Tanpa https:// Ataupun www'
print ''
target_url = raw_input(GG + 'Masukan Site : ' + P)

def rikues(url):
    try:
        return requests.get('http://' + url)
    except requests.exceptions.ConnectionError:
        pass


target_url
with open('heker.txt', 'r') as (wordlist_file):
    for line in wordlist_file:
        word = line.strip()
        test_url = word + '.' + target_url
        response = rikues(test_url)
        if response:
            print RR + 'Subdomain Ditemukan >> ' + WW + test_url
