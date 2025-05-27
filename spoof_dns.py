#!/usr/bin/env python3

import argparse
import time
from dnslib import DNSRecord, QTYPE, RR, A
from dnslib.server import DNSServer, BaseResolver

class SpoofResolver(BaseResolver):
    def __init__(self, spoof_map):
        self.spoof_map = spoof_map

    def resolve(self, request, handler):
        reply = request.reply()
        qname = str(request.q.qname).rstrip('.')
        if qname in self.spoof_map:
            ip = self.spoof_map[qname]
            reply.add_answer(RR(request.q.qname, QTYPE.A, rdata=A(ip), ttl=60))
        return reply

def main():
    parser = argparse.ArgumentParser(description="DNS Spoofing Resolver")
    parser.add_argument('--map', nargs=2, action='append', metavar=('domain','ip'),
                        required=True, help='Domain and spoofed IP')
    parser.add_argument('--port', type=int, default=53, help='Port to listen on')
    args = parser.parse_args()

    spoof_map = {domain: ip for domain, ip in args.map}
    resolver = SpoofResolver(spoof_map)
    server = DNSServer(resolver, port=args.port, address='0.0.0.0')
    print(f"Starting DNS spoofing on port {args.port} for: {spoof_map}")
    server.start_thread()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping DNS spoofing.")

if __name__ == '__main__':
    main()
