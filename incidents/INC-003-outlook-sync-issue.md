# INC-003 — Outlook Email Synchronization Issue

> **Scenario:** Fictional IT Support case study  
> **Company:** Borealis Travel  
> **Incident ID:** INC-003  
> **Category:** Microsoft 365 / Email Synchronization  
> **Priority:** Medium  
> **Status:** Resolved
> **Affected User:** Daniel Wilson 

## 1. Incident Summary

Borealis Travel experienced an email synchronization incident affecting Daniel Wilson, a member of the Reservations department.

Daniel reported that new emails were not appearing in his Microsoft Outlook desktop Inbox. Initial troubleshooting confirmed that the issue also occurred in Outlook on the web, while other users continued receiving emails normally.

The investigation found that incoming messages had been delivered to Daniel's mailbox but were being moved to a secondary folder by a mailbox rule. The rule was disabled, and subsequent testing confirmed that new emails appeared correctly in both Outlook desktop and Outlook on the web.

The incident was resolved after the corrective action was applied and Daniel confirmed that email delivery to his Inbox had returned to normal. A simulated audit review identified the rule's origin and found no suspicious activity.

**Root cause:** A mailbox rule was configured to move incoming messages to a secondary folder instead of leaving them in the Inbox. The rule was disabled, restoring the expected email organization and visibility.

## 2. Impact and Scope

The incident affected one user in the Reservations department. Daniel Wilson was unable to see new incoming emails in his Outlook desktop Inbox or in Outlook on the web.

The issue was isolated to Daniel's mailbox. Other users continued receiving emails normally, and the simulated Exchange Online message trace indicated that incoming messages had been delivered successfully.

Although email delivery was functioning, the misplaced messages could have delayed Daniel's access to reservation-related communications and affected his ability to respond to customers in a timely manner.

No evidence of a wider Microsoft 365 service outage or unauthorized mailbox access was identified during the simulated investigation.

## 3. Incident Timeline

> **Note:** All timestamps below are simulated for this fictional case study.

- **09:15** — Daniel Wilson reported that new emails were not appearing in his Outlook desktop Inbox.
- **09:20** — IT Support confirmed that the issue also occurred in Outlook on the web and that other users were not affected.
- **09:30** — A simulated Exchange Online message trace indicated that incoming messages had been delivered to Daniel's mailbox.
- **09:40** — Investigation of mailbox folders and rules identified a rule moving incoming messages to a secondary folder.
- **09:50** — IT Support disabled the rule after confirming the situation with Daniel.
- **10:00** — A simulated test message appeared correctly in the Inbox in both Outlook desktop and Outlook on the web.
- **10:10** — Daniel confirmed that the issue was resolved and that he could access his previous emails.
- **10:15** — A simulated audit review identified the rule's origin and found no suspicious activity. The incident was marked as resolved.

## 4. Troubleshooting and Evidence

### 4.1 Email Client Verification

The technician verified whether Daniel Wilson could see new emails in Outlook desktop and Outlook on the web.

Both clients showed the same issue. Other users continued receiving emails normally.

**Finding:** The issue was isolated to Daniel's mailbox rather than being a general Outlook client problem or a wider Microsoft 365 service outage.

### 4.2 Message Delivery Check

The technician reviewed a simulated Exchange Online message trace to determine whether incoming messages had reached Daniel's mailbox.

The trace indicated that the messages had been delivered successfully.

**Finding:** Email delivery was functioning normally. The investigation needed to determine why delivered messages were not appearing in the Inbox.

### 4.3 Mailbox Rule Investigation

The technician reviewed Daniel's mailbox folders and configured rules to identify whether messages were being redirected or moved automatically.

The investigation identified a rule configured to move incoming messages to a secondary folder. Daniel confirmed that he had not intentionally configured the rule and wanted new messages to appear in his Inbox.

**Finding:** The mailbox rule explained why incoming messages were not visible in the Inbox despite being delivered to the mailbox.

### 4.4 Rule Change and Security Review

After confirming the issue with Daniel, the technician disabled the identified rule without deleting it, preserving the possibility of reviewing it later.

A simulated audit review identified the rule's origin and found no suspicious activity.

**Finding:** Disabling the rule was an appropriate corrective action for the simulated incident. The audit review did not identify evidence of suspicious activity.

### 4.5 Post-Resolution Validation

The technician sent a simulated test message and verified that it appeared in the Inbox in both Outlook desktop and Outlook on the web.

Daniel confirmed that new emails were visible and that he could access his previous messages.

**Finding:** Email visibility returned to normal, and the user confirmed that the issue was resolved.

### 4.6 Evidence-Based Assessment

The investigation established the following:

- Daniel's issue occurred in both Outlook desktop and Outlook on the web.
- Other users continued receiving emails normally.
- Simulated message trace results indicated successful delivery to Daniel's mailbox.
- A mailbox rule was moving incoming messages to a secondary folder.
- The rule was disabled, and subsequent testing was successful.
- The simulated audit review found no suspicious activity.
- Daniel confirmed that the issue was resolved.

**Conclusion:** The findings supported a mailbox rule as the cause of the incident, rather than an authentication failure, an email delivery failure, or a general Microsoft 365 service outage.

**Evidence Note:** All checks, findings, message trace results, audit results, and user validation described in this section are simulated for portfolio demonstration purposes.

## 5. Root Cause and Resolution

The incident was caused by a mailbox rule configured to move incoming messages to a secondary folder instead of leaving them in Daniel Wilson's Inbox.

The simulated Exchange Online message trace indicated that messages were being delivered successfully. The investigation confirmed that the mailbox rule was responsible for the unexpected behavior.

After confirming the situation with Daniel, the technician disabled the rule rather than deleting it. This corrective action restored the expected behavior while preserving the possibility of reviewing the rule later.

A simulated audit review identified the rule's origin and found no suspicious activity. However, the rule's origin and configuration should remain documented for any future review.

Following the change, a test message appeared correctly in both Outlook desktop and Outlook on the web. Daniel confirmed that new emails were visible in his Inbox and that he could access his previous emails.

**Resolution:** The mailbox rule was disabled, email visibility was restored, and the user confirmed that the issue was resolved.

**Root cause:** A mailbox rule moved incoming messages to a secondary folder, preventing them from appearing in the Inbox as expected.

## 6. Preventive Actions

The following actions are recommended to reduce the likelihood of similar email visibility and mailbox rule incidents. These are recommendations and have not been implemented as part of this simulated case study.

| Recommended Action | Purpose | Suggested Owner |
|---|---|---|
| Review mailbox rules periodically | Identify unexpected rules that move, forward, or redirect incoming messages. | IT Operations |
| Improve user awareness | Help employees recognize unfamiliar mailbox rules and report unexpected email behavior. | IT Support |
| Document mailbox rule changes | Maintain records of relevant rule changes, their justification, and the responsible technician. | IT Operations |
| Review mailbox audit records | Investigate the origin of unexpected rules and identify potential signs of unauthorized activity. | Security / IT Operations |
| Standardize missing-email troubleshooting | Ensure technicians check message delivery, mailbox folders, and rules before escalating an incident. | IT Support |
| Maintain incident and resolution records | Preserve investigation findings, corrective actions, audit results, and user validation. | IT Support |

### Preventive Review

The incident highlights the importance of distinguishing email delivery failures from mailbox organization issues, reviewing unexpected mailbox rules, and preserving audit records to support security investigations.

**Implementation Status:** Recommendations documented; implementation not verified.

## 7. Related Tickets and Closure

**Related Tickets:** No related incidents or service requests were identified in this simulated case study.

### Closure Checklist

- [x] User's reported email visibility issue documented.
- [x] Outlook desktop and Outlook on the web checked.
- [x] Scope of the issue confirmed to be limited to one user.
- [x] Simulated message trace reviewed.
- [x] Mailbox rule responsible for moving incoming messages identified.
- [x] Rule disabled as the corrective action.
- [x] Simulated audit review completed.
- [x] New email successfully tested in both Outlook clients.
- [x] User confirmed access to new and previous emails.
- [x] Resolution and preventive recommendations documented.

### Final Closure Statement

Incident INC-003 was resolved after the mailbox rule responsible for moving incoming messages to a secondary folder was identified and disabled. Successful testing and confirmation from Daniel Wilson established that new emails were visible in the Inbox in both Outlook desktop and Outlook on the web.

The simulated audit review identified the rule's origin and found no suspicious activity. The rule remained disabled pending any further review.

The case demonstrates a structured IT Support troubleshooting workflow covering email delivery verification, mailbox rule investigation, corrective action, security review, user validation, and incident documentation.

**Final Status:** Resolved  
**Closure Basis:** Successful validation by the affected user  
**Case Type:** Fictional IT Support portfolio case study