#!/usr/bin/python
import dns.resolver
import argparse
from colorama import Fore,Style
import concurrent.futures

def get_args():
	p = argparse.ArgumentParser(description="DNS Subdomain Brute Forcer")
	p.add_argument('-d','--domain',type=str,help='domain.com',required=True)
	p.add_argument('-w','--wordlist',type=argparse.FileType('r'),help='subdomain wordlist', required=True)
	p.add_argument('-o','--outfile',type=str,help='output file',required=False)
	p.add_argument('-t','--threads',type=int,default=10,help='concurrent threads',required=False)

	args = p.parse_args()

	return args

def a_lookup(record):
	ip = ""
	try:
		answers = dns.resolver.query(record,'A')
		for ip in answers:
			return ip
	except Exception as e:
		return "0.0.0.0"

def main():
	args = get_args()

	subdomains = []
	for line in args.wordlist:
		subdomains.append(line.strip()+"."+args.domain)
	
	records = {}

	with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads) as executor:
		future_to_ip = {executor.submit(a_lookup, record): record for record in subdomains}
		for future in concurrent.futures.as_completed(future_to_ip):
			record = future_to_ip[future]
			try:
				records[record] = future.result()
			except Exception as exc:
				print(Fore.RED+"[!] ERROR: %s" % exc+Style.RESET_ALL)

	actual_records = {}

	for k,v in records.iteritems():
		if "0.0.0.0" in str(v):
			continue
		else:
			actual_records[k] = v

	print(Fore.GREEN+Style.BRIGHT+"[+] %s Live Subdomains Found!" % str(len(actual_records))+Style.RESET_ALL)

	for k,v in actual_records.iteritems():
		print(Fore.GREEN+Style.BRIGHT+'[+]'+Style.RESET_ALL+' %s : %s' % (k,v))

	if args.outfile:
		f = open(args.outfile, 'w')
		for k,v in records.iteritems():
			if "0.0.0.0" in str(v):
				continue
			else:
				f.write("%s : %s\r\n" % (k,v))
		f.close()
		print(Fore.YELLOW+"[*] Subdomains and IPs saved to %s." % args.outfile + Style.RESET_ALL)

if __name__ == '__main__':
	main()
