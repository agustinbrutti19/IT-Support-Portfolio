# INC-004 — Network Connectivity Incident

> **Scenario:** Fictional IT Support case study  
> **Company:** Borealis Travel  
> **Incident ID:** INC-004  
> **Category:** Network  
> **Priority:** Medium  
> **Status:** Resolved

## 1. Incident Summary

Daniel Wilson, an employee in the Reservations department at Borealis Travel, reported that he could not access the internal reservations application, Microsoft Outlook, or external websites from his workstation.

Initial troubleshooting revealed that the workstation had an Automatic Private IP Addressing (APIPA) address (`169.254.42.17`) and no default gateway. Attempts to renew the IP configuration failed because the workstation could not reach a DHCP server.

The investigation identified an incorrect switch port VLAN assignment. The port was assigned to a quarantine VLAN instead of the corporate Reservations VLAN. After the Network team corrected the configuration through the approved change management process, network connectivity was restored and Daniel confirmed that the affected services were working normally.

> **Note:** All technical findings, command outputs, and user confirmations documented in this report are simulated for portfolio demonstration purposes.

## 2. Impact and Scope

- **Affected user:** Daniel Wilson
- **Department:** Reservations
- **Affected device:** One corporate workstation
- **Affected services:** Internal reservations application, Microsoft Outlook, and external websites
- **Business impact:** Daniel was temporarily unable to access the systems required for his daily work.
- **Scope:** The incident was limited to one workstation. Other employees in the same area were able to access corporate services normally.
- **Priority justification:** Medium, because the incident significantly affected one user's productivity but did not cause a department-wide or company-wide outage.

## 3. Incident Timeline

| Time | Event | Result |
|---|---|---|
| 09:00 | Daniel reported loss of access to the reservations application, Outlook, and external websites. | Incident identified. |
| 09:05 | Checked the workstation's IP configuration using `ipconfig`. | APIPA address (`169.254.42.17`) and no default gateway detected. |
| 09:10 | Checked the Ethernet cable and attempted to renew the IP configuration. | Physical link appeared normal, but the DHCP renewal request timed out. |
| 09:15 | Checked another workstation in the same area. | The second workstation had a valid corporate IP configuration, suggesting the issue was isolated. |
| 09:20 | Contacted the Network team to investigate the affected switch port and VLAN assignment. | The port was found assigned to a quarantine VLAN. |
| 09:25 | Confirmed the correct Reservations VLAN and obtained change approval. | Network configuration change authorized. |
| 09:30 | The Network team assigned the switch port to the correct corporate VLAN. | The workstation obtained a valid IP address and default gateway. |
| 09:35 | Tested connectivity to the default gateway and an external IP address. | Both tests succeeded. |
| 09:40 | Tested DNS resolution using `nslookup www.microsoft.com`. | DNS resolution succeeded. |
| 09:45 | Asked Daniel to test the reservations application, Outlook, and an external website. | Daniel confirmed that all affected services were working. |
| 09:50 | Documented the findings and resolution. | Incident marked as resolved. |

## 4. Troubleshooting and Evidence

### 4.1 Initial IP Configuration

The `ipconfig` command showed that the workstation had an APIPA address and no default gateway.

```text
IPv4 Address: 169.254.42.17
Subnet Mask: 255.255.0.0
Default Gateway:
```

**Finding:** The workstation had not obtained a valid IP configuration from DHCP.

### 4.2 Physical Connection and DHCP Renewal

The Ethernet cable was connected at both ends, link lights were active, and no visible cable damage was found.

The technician then executed:

```cmd
ipconfig /release
ipconfig /renew
```

The renewal attempt timed out because the workstation could not contact a DHCP server.

**Finding:** The physical link appeared operational, but DHCP communication was unsuccessful.

### 4.3 Comparison with Another Workstation

A second workstation in the same area had the following configuration:

```text
IPv4 Address: 10.20.30.45
Subnet Mask: 255.255.255.0
Default Gateway: 10.20.30.1
```

**Finding:** Another workstation had valid corporate connectivity, making a broader DHCP outage less likely.

### 4.4 Switch Port and VLAN Investigation

The Network team confirmed that the affected switch port was assigned to a quarantine VLAN rather than the corporate Reservations VLAN.

The correct VLAN was verified, and the configuration change was approved through the internal change management process.

**Finding:** The incorrect VLAN assignment explained why the workstation could not obtain a corporate IP address or reach the required network services.

### 4.5 IP Configuration After the Change

After the Network team corrected the VLAN assignment, the technician executed:

```cmd
ipconfig /renew
```

The workstation obtained the following configuration:

```text
IPv4 Address: 10.20.30.67
Subnet Mask: 255.255.255.0
Default Gateway: 10.20.30.1
```

**Finding:** The workstation successfully obtained a valid corporate IP configuration.

### 4.6 Connectivity and DNS Validation

The technician tested connectivity to the default gateway:

```cmd
ping 10.20.30.1
```

The simulated test returned four replies with no packet loss.

External IP connectivity was then tested:

```cmd
ping 1.1.1.1
```

The simulated test also returned four replies with no packet loss.

Finally, DNS resolution was checked:

```cmd
nslookup www.microsoft.com
```

The query successfully returned IP address records.

**Finding:** Local network connectivity, external IP connectivity, and DNS resolution were working after the VLAN correction.

### 4.7 User Validation

Daniel tested the internal reservations application, Microsoft Outlook, and an external website. He confirmed that all three were working normally.

**Final finding:** The original connectivity issue was resolved, and the affected services were restored.

## 5. Root Cause and Resolution

### Root Cause

The affected workstation's switch port was incorrectly assigned to a quarantine VLAN instead of the corporate Reservations VLAN.

The quarantine VLAN did not provide access to the corporate network segment or its DHCP service. As a result, the workstation could not obtain a valid corporate IP address and instead configured itself with an APIPA address (`169.254.42.17`).

This prevented Daniel Wilson from accessing the internal reservations application, Microsoft Outlook, and external websites.

### Resolution

The issue was resolved through the following actions:

1. The Helpdesk technician identified the APIPA address and unsuccessful DHCP renewal as initial indicators of a network configuration issue.
2. A comparison with another workstation confirmed that the problem appeared isolated to the affected device or its network connection.
3. The Network team investigated the switch port and identified the incorrect VLAN assignment.
4. The correct Reservations VLAN was confirmed, and the change was approved through the internal change management process.
5. The Network team reassigned the switch port to the correct corporate VLAN.
6. The technician renewed the workstation's IP configuration and verified the default gateway, external IP connectivity, and DNS resolution.
7. Daniel confirmed that the reservations application, Outlook, and external websites were accessible again.

**Outcome:** Network connectivity was restored, and the incident was marked as resolved.

## 6. Preventive Actions

The following preventive actions are recommended to reduce the likelihood of similar incidents:

1. **Review VLAN assignment procedures:** Verify that corporate workstations are assigned to the correct VLAN during installation, relocation, and network configuration changes.
2. **Improve change validation:** Include a post-change connectivity check to confirm that affected devices receive a valid IP configuration and can access required network services.
3. **Maintain switch port documentation:** Keep network port assignments and their intended VLANs documented and up to date.
4. **Review quarantine VLAN procedures:** Ensure that devices assigned to the quarantine VLAN have a documented review and release process.
5. **Strengthen Helpdesk troubleshooting guidance:** Document how to recognize APIPA addresses (`169.254.x.x`) and investigate DHCP connectivity failures.
6. **Coordinate with the Network team:** Establish a clear escalation process for suspected switch port, VLAN, or DHCP issues.

These actions are recommendations. The simulation does not establish that they have been implemented.

## 7. Related Tickets and Closure

### Related Tickets

- **Network team escalation:** The Network team investigated the affected switch port, confirmed the incorrect VLAN assignment, and corrected the configuration after approval through the change management process.

### Closure Summary

The workstation's network connectivity was restored after the switch port was reassigned to the correct corporate Reservations VLAN.

The Helpdesk technician verified that the workstation received a valid IP configuration, could reach the default gateway and an external IP address, and could resolve DNS queries.

Daniel Wilson subsequently confirmed that the internal reservations application, Microsoft Outlook, and external websites were working normally.

- **Final status:** Resolved
- **Priority:** Medium
- **User confirmation:** Received
- **Closure reason:** Connectivity restored and affected services validated.
