# KB-006 — Windows DNS Troubleshooting

**Category:** Network  
**System:** Windows / DNS / VPN  
**Audience:** IT Support / Helpdesk  
**Severity:** Medium  
**Last Updated:** 2026-10-12

## Overview

This article describes how to diagnose and troubleshoot DNS resolution issues on Windows devices. Incorrect or outdated DNS resolution may prevent users from reaching internal applications, VPN servers, or other network resources.

## Symptoms

- VPN client cannot connect to the VPN server.
- A hostname resolves to an unexpected IP address.
- A server hostname cannot be resolved.
- Network resources are inaccessible by hostname but may work by IP address.
- DNS-related errors appear when accessing internal applications.

## Troubleshooting Procedure

### 1. Verify Network Configuration

Open Command Prompt or PowerShell and run:

    ipconfig /all

**Purpose:** Displays network adapters, IP configuration, default gateways, and configured DNS servers.

**Check:**
- The active adapter has a valid IP address.
- The default gateway is correct for the network.
- The configured DNS servers match the approved network configuration.

Do not change DNS server settings without authorization.

### 2. Inspect the Local DNS Cache

Run:

    ipconfig /displaydns

**Purpose:** Displays entries currently stored in the Windows DNS resolver cache.

**Check:**
- Whether the target hostname has a cached entry.
- Whether the cached address appears inconsistent with the approved configuration.

Cached entries alone do not prove that DNS is the root cause. Compare results with an approved reference or a known-good device.

### 3. Test Hostname Resolution

Run:

    nslookup vpn-server.example.com

Replace `vpn-server.example.com` with the actual VPN server hostname.

**Purpose:** Queries DNS to determine which IP address is returned for the hostname.

**Check:**
- Whether the hostname resolves successfully.
- Which DNS server answered the query.
- Whether the returned address matches the expected configuration.

`nslookup` queries DNS directly and may return a different result from an entry currently stored in the local Windows DNS cache.

### 4. Compare Results with a Known-Good Device

If authorized, run the same `nslookup` command on another device connected to the same network and using the appropriate VPN configuration.

Compare:
- Resolved IP addresses.
- DNS servers used.
- Whether both devices can resolve the hostname.

Different results may indicate a DNS configuration or caching issue, but network segmentation and split-DNS configurations can also cause legitimate differences.

### 5. Test Network Reachability

To check hostname resolution and ICMP reachability, run:

    ping vpn-server.example.com

A failed ping does not necessarily mean the server is unavailable. Firewalls and servers may block ICMP traffic.

For a service that uses TCP, PowerShell can test the relevant port:

    Test-NetConnection vpn-server.example.com -Port 443

Replace port `443` with the actual TCP port required by the approved service configuration. A successful TCP test does not guarantee that VPN authentication or the tunnel will work.

### 6. Flush the Local DNS Cache

Only perform this step when the evidence supports a local DNS cache issue and you are authorized to troubleshoot the device.

Open Command Prompt or PowerShell and run:

    ipconfig /flushdns

**Purpose:** Clears the Windows DNS resolver cache so that subsequent lookups can obtain fresh DNS information.

Expected output typically confirms that the DNS Resolver Cache was successfully flushed.

This command does not change DNS server settings, repair incorrect DNS records on a server, or guarantee that a VPN connection will work.

### 7. Resolve the Hostname Again

Run:

    nslookup vpn-server.example.com

Then attempt the connection again using the approved VPN client and configuration.

If the result remains incorrect, investigate the configured DNS server, DNS records, VPN split-DNS settings, and relevant network policies. Escalate to the network team if the issue cannot be resolved within Helpdesk permissions.

## Additional Useful Commands

| Command | Purpose |
|---|---|
| `ipconfig` | Displays basic IP configuration. |
| `ipconfig /all` | Shows detailed adapter and DNS configuration. |
| `ipconfig /displaydns` | Displays the local DNS cache. |
| `ipconfig /flushdns` | Clears the local DNS resolver cache. |
| `nslookup hostname` | Queries DNS for a hostname. |
| `ping hostname` | Tests name resolution and ICMP reachability. |
| `Test-NetConnection hostname -Port 443` | Tests TCP connectivity to a specified port. |
| `route print` | Displays the local IP routing table. |

## Resolution Criteria

The issue can be considered resolved when:
- The VPN server hostname resolves to the expected address.
- The user successfully establishes the VPN connection.
- The user confirms access to the required internal resources.
- The troubleshooting actions and results are documented in the ticket.

## Escalation Criteria

Escalate to the Network or Infrastructure team when:
- The hostname continues resolving incorrectly after the local cache is cleared.
- Multiple devices experience the same DNS issue.
- The configured DNS server is unavailable or returns unexpected records.
- VPN split-DNS, routing, firewall, or server-side configuration requires investigation.

## Documentation Requirements

Record the following in the incident ticket:
- User, device, and network context.
- Symptoms and error messages.
- DNS server and hostname tested.
- Relevant `nslookup` results before and after troubleshooting.
- Commands executed and their results.
- Whether VPN connectivity and internal resource access were restored.

Avoid including passwords, authentication tokens, private keys, or other sensitive information in ticket notes.