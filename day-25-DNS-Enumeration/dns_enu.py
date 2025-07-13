#!/usr/bin/python3

# DNS Enumeration 

import dns.resolver

def dns_enum (target_domain,records):

    resolver = dns.resolver.Resolver()

    for dns_recods in records:
        try:
            answare_host = resolver.resolve(target_domain,dns_recods)
        except dns.resolver.NoAnswer:
            continue

        # records types

        print(f"-->> {dns_recods} recorde for {target_domain} ")
        for data in answare_host:
            print(f"-->> {data}\n")

if __name__ == "__main__":
    target_domain = "example.com"
    records = ["A","AAAA","CNAME","MX","SOA","TXT"]
    dns_enum(target_domain,records)

