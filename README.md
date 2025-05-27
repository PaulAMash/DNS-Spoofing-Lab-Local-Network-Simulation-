# DNS Spoofing Lab (Local Network Simulation)

This lab simulates a MITM DNS spoofing attack.

## Components

- **spoof_dns.py**: Python script using dnslib to spoof DNS responses.

## Usage

1. Set up two Linux VMs (attacker and victim) on isolated network.
2. Redirect victim's DNS to attacker VM.
3. Run spoofing script on attacker:
   ```bash
   sudo python3 spoof_dns.py --map example.com 10.0.0.123 --map test.local 10.0.0.123
   ```
4. Use Ettercap for ARP spoofing if needed:
   ```bash
   sudo ettercap -T -M arp:remote /victim_ip/ /gateway_ip/
   ```
5. Verify spoofed responses on victim machine.
6. Mitigation: 
   - Add static DNS entries
   - Implement DNSSEC validation

## Requirements

- Python 3.6+
- dnslib (`pip install dnslib`)
- Ettercap (optional)
