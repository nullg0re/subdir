# subdir.py
Subdomain DNS Brute Forcer

Pretty self explanitory - Takes a wordlist of potential subdomains (www, vpn, email, etc) and a domain (example.com) and queries DNS for the full hostname (www.example.com, vpn.example.com, email.example.com).

If an IP address is returned by DNS, then the hostname and the IP address is saved in a python dict. If not, the hostname is thrown out.

This is a multi-threaded python script, so adding in the `-t #` switch will increase or decrease the speed at which the DNS requests are made. (Default Thread count is 10)

Once all the wordlist has been exhausted, the "live" or "hostnames with found IPs" will be printed to screen similar to the following:

```[+] site.example.com : 127.0.0.1```

Below will contain additional example output.

# Help Menu
```
./subdir.py --help
usage: subdir.py [-h] -d DOMAIN -w WORDLIST [-o OUTFILE] [-t THREADS]

DNS Subdomain Brute Forcer

optional arguments:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        domain.com
  -w WORDLIST, --wordlist WORDLIST
                        subdomain wordlist
  -o OUTFILE, --outfile OUTFILE
                        output file
  -t THREADS, --threads THREADS
                        concurrent threads
```
# Example Output
```
# ./subdir.py -d morainevalley.edu -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt -t 30 -o test-output.txt
[+] 41 Live Subdomains Found!
[+] vcse.morainevalley.edu : 64.107.14.13
[+] multimedia.morainevalley.edu : 64.107.14.212
[+] astra.morainevalley.edu : 64.107.12.247
[+] ldap1.morainevalley.edu : 64.107.14.213
[+] netlab.morainevalley.edu : 64.107.13.100
[+] www.apps.morainevalley.edu : 64.107.14.207
[+] pop3.morainevalley.edu : 64.107.14.203
[+] news.morainevalley.edu : 64.107.14.212
[+] webapps.morainevalley.edu : 64.107.14.212
[+] ist.morainevalley.edu : 64.107.14.5
[+] portfolio.morainevalley.edu : 64.107.14.138
[+] books.morainevalley.edu : 207.138.59.100
[+] smtp.morainevalley.edu : 64.107.14.203
[+] notes.morainevalley.edu : 64.107.14.6
[+] directory.morainevalley.edu : 64.107.14.205
[+] intranet.morainevalley.edu : 64.107.14.154
[+] autodiscover.morainevalley.edu : 52.96.79.216
[+] learn.morainevalley.edu : 64.107.14.202
[+] jobs.morainevalley.edu : 161.47.143.131
[+] www.library.morainevalley.edu : 64.107.14.30
[+] ldap2.morainevalley.edu : 64.107.14.218
[+] cit.morainevalley.edu : 64.107.14.155
[+] email.morainevalley.edu : 64.107.14.203
[+] ext.morainevalley.edu : 34.231.191.220
[+] wellness.morainevalley.edu : 64.107.14.212
[+] canvas.morainevalley.edu : 34.224.143.193
[+] remote.morainevalley.edu : 64.107.14.212
[+] library.morainevalley.edu : 64.107.14.30
[+] apps.morainevalley.edu : 64.107.14.208
[+] WWW.morainevalley.edu : 18.232.224.67
[+] lib.morainevalley.edu : 64.107.14.205
[+] moo.morainevalley.edu : 64.107.13.110
[+] moodle.morainevalley.edu : 64.107.13.110
[+] meeting.morainevalley.edu : 64.107.14.32
[+] ww2.morainevalley.edu : 64.107.8.51
[+] www.morainevalley.edu : 18.232.224.67
[+] dropbox.morainevalley.edu : 64.107.14.212
[+] online.morainevalley.edu : 64.107.14.205
[+] imap.morainevalley.edu : 64.107.14.203
[+] cube.morainevalley.edu : 64.107.11.246
[+] office.morainevalley.edu : 64.107.14.145
[*] Subdomains and IPs saved to test-output.txt.
```
# Screenshot
![Alt Text](Screenshots/subdir_mvcc.JPG "Execution")
