# Ticket 014 — Microsoft 365 Email Delivery Issue

## Ticket Information

- **Ticket ID:** 014
- **User:** Emily Davis
- **Department:** Reservations
- **Issue Type:** Microsoft 365
- **Priority:** High
- **Status:** Pending
- **Assigned To:** Helpdesk
- **Escalated To:** Engineering

## User Report

Emily Davis from the Reservations department reports that she has not been
receiving customer emails since 09:00. Several customers confirm that they
sent messages needed to confirm reservations.

The issue occurs in both Outlook desktop and Outlook on the web. Emily can
open both clients, but the expected messages are not visible.

## Initial Assessment

The issue may involve Exchange Online message delivery or mailbox processing.

Because the user can access Outlook and the issue appears to affect incoming
messages, the investigation should focus on message delivery, mailbox folders,
inbox rules, quarantine, and other possible mailbox-level causes.

The root cause has not yet been identified.

## Troubleshooting Steps

1. Checked Microsoft 365 service health. No relevant service incident was found.
2. Reviewed Exchange Online Message Trace for three expected customer emails.
3. Confirmed that all three messages appeared as Delivered in Message Trace.
4. Checked Inbox, Junk Email, Deleted Items, Archive, and Other.
5. Searched for the expected messages by sender and subject.
6. Reviewed inbox rules. No relevant rule was found.
7. Checked mailbox quota, forwarding settings, and receiving restrictions.
8. Checked quarantine and relevant mail flow rules.
9. Confirmed that other Reservations employees were receiving emails normally.
10. Checked Deleted Items and available recoverable items. No matching messages were found.
11. Confirmed that the issue appeared to be isolated to one user.

## Diagnostic Findings

The expected messages appeared as Delivered in Message Trace, but Emily could
not locate them in her mailbox.

The investigation did not identify a relevant service incident, inbox rule,
forwarding configuration, quota issue, quarantine entry, or mail flow rule
that explained the problem.

The root cause remains unidentified.

## Escalation

The incident was escalated from Helpdesk to Engineering for further investigation.

**Reason for Escalation:**

The initial investigation did not identify the cause of the missing emails.
Message Trace showed the expected messages as Delivered, but the user could
not locate them in the mailbox.

**Requested Investigation:**

Engineering should coordinate with an Exchange Online administrator to
investigate message-level delivery and mailbox processing using authorized
administrative tools.

The investigation should determine whether the messages were moved, deleted,
retained, or affected by another mailbox process.

## Current Status

The incident remains unresolved and is pending further investigation.

- **Root Cause:** Unknown
- **Resolution:** No confirmed resolution
- **Next Action:** Continue investigation with Engineering and an Exchange Online administrator.
- **Follow-up Required:** Yes