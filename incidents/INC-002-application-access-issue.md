# INC-002 — Application Access Issue

## 1. Incident Summary

> **Incident ID:** INC-002  
> **Incident Type:** Identity and Access Management (IAM)  
> **Priority:** Medium  
> **Status:** Closed  
> **Affected User:** Emily Davis  
> **Department:** Sales  
> **Affected Application:** Customer Relationship Management (CRM)  
> **Related Access Request:** AR-002

### Incident Description

Emily Davis reported that she could successfully sign in to her corporate account but received an "Access Denied" message when attempting to open the CRM application.

The initial investigation confirmed that her account was active and that authentication was successful. However, her account was not a member of the required security group, `CRM-Sales-Users`.

After confirming the business need with her manager, the IT Support team verified the group's purpose, recorded the approval, and followed the authorized access-management procedure to grant the required permissions.

The user subsequently confirmed that she could access the CRM and perform her normal tasks.

**Documentation Note:** This is a fictional incident created for an IT Support portfolio case study. All users, records, approvals, and actions described in this report are simulated.

## 2. Impact and Scope

### User Impact

Emily Davis was unable to access the CRM application, which prevented her from performing CRM-related tasks, including searching customer records and reviewing assigned sales opportunities.

### Scope

- **Confirmed affected users:** One — Emily Davis.
- **Affected department:** Sales.
- **Affected service:** CRM application access.
- **Authentication:** Working normally.
- **Authorization:** Missing required security group membership.
- **Other users affected:** No additional affected users were identified during this investigation.

### Business Impact

The access issue temporarily prevented Emily from completing assigned CRM-related work. No broader application outage or widespread authentication issue was identified.

### Scope Assessment

The available evidence indicates an individual access-permission issue rather than a general CRM service outage.

**Evidence Limitation:** The scope reflects the findings of this simulated investigation. It does not establish that no other users could have experienced similar issues outside the investigated case.

## 3. Incident Timeline

| Stage | Activity | Outcome |
|---|---|---|
| 1. Initial report | Emily Davis reported an "Access Denied" message when opening the CRM. | Incident recorded as INC-002. |
| 2. Identity verification | The support technician verified that Emily's account was active and sign-in was successful. | Authentication issues were ruled out as the primary cause. |
| 3. Permission review | The technician checked the user's current CRM group memberships. | Required group membership was missing. |
| 4. Manager confirmation | The Sales manager confirmed Emily's business need for CRM access. | Business justification documented. |
| 5. Group validation | The technician verified the purpose and permissions of `CRM-Sales-Users`. | The group was confirmed as appropriate for the requested access. |
| 6. Access request | Request AR-002 was documented with the manager's approval. | Request prepared for authorized execution. |
| 7. Access change | An authorized technician added Emily to `CRM-Sales-Users` and recorded the change. | Group membership updated. |
| 8. User validation | Emily signed in and tested the CRM functions required for her role. | Access and required tasks were confirmed to work. |
| 9. Closure | The technician documented the cause, approval, change, and validation. | Incident closed. |

**Timeline Note:** This timeline describes the sequence of events in a fictional simulation. Exact timestamps were not recorded and have therefore been omitted.

## 4. Troubleshooting and Evidence

### 4.1 Authentication Check

The technician verified that Emily Davis's corporate account was active and that she could successfully sign in.

**Finding:** Authentication was working normally. The issue occurred when the user attempted to access the CRM application.

### 4.2 Authorization Check

The technician reviewed Emily's current security group memberships and confirmed that she was not a member of the required `CRM-Sales-Users` group.

**Finding:** The missing group membership was consistent with the "Access Denied" message.

### 4.3 Business Need and Approval

The technician contacted Emily's Sales manager to confirm that CRM access was required for her assigned responsibilities.

The manager confirmed the business need and approved the request. The approval was documented in the simulated access request, AR-002.

### 4.4 Security Group Validation

Before making any access change, the technician reviewed the purpose and permissions of `CRM-Sales-Users`.

The group was confirmed to provide standard CRM access for eligible Sales employees, including the ability to search customer records and view or manage assigned sales opportunities. It did not grant administrative privileges.

### 4.5 Evidence-Based Assessment

The investigation established the following:

- Emily's account was active.
- Authentication was successful.
- The required CRM security group membership was missing.
- The manager confirmed the business need and approved the request.
- The selected group matched the user's job responsibilities.

**Conclusion:** The available findings supported a missing authorization assignment as the cause of the incident, rather than an authentication failure or a general CRM outage.

**Evidence Note:** All checks, findings, and approval records described in this section are simulated for portfolio demonstration purposes.

## 5. Root Cause and Resolution

### 5.1 Root Cause

The incident was caused by missing membership in the `CRM-Sales-Users` security group.

Emily Davis's corporate account was active and authentication was successful, but the required authorization assignment was absent. As a result, the CRM denied access.

### 5.2 Resolution

After confirming the business need and recording the Sales manager's approval in access request AR-002, an authorized technician followed the simulated access-management procedure.

The technician added Emily to `CRM-Sales-Users` and recorded the change in the simulated access record.

Only the standard CRM permissions required for her Sales responsibilities were granted. No administrative privileges were assigned.

### 5.3 Validation

Following the change, Emily signed in again and tested the CRM application.

The validation confirmed that she could:

- Open the CRM successfully.
- Search and view customer records.
- Access and manage her assigned sales opportunities.

The user confirmed that the required tasks were working as expected.

### 5.4 Resolution Outcome

**Resolution Status:** Successful  
**Incident Status:** Closed  
**Root Cause:** Missing required security group membership  
**Access Approval:** Sales manager approval documented in AR-002  
**Validation:** Successful user testing

The incident was closed after the access change and user validation were documented.

**Simulation Note:** The access change, approval, validation, and closure described above are fictional. No real user account or directory was modified.

## 6. Preventive Actions

The following actions are recommended to reduce the likelihood of similar access incidents. These are recommendations and have not been implemented as part of this simulated case study.

| Recommended Action | Purpose | Suggested Owner |
|---|---|---|
| Standardize access requests | Ensure requests include a business justification and the required approval before access is granted. | IT Support / Access Management |
| Maintain role-based access | Assign permissions through approved security groups aligned with each department's responsibilities. | Access Management |
| Review group membership changes | Periodically verify that security group memberships remain appropriate for users' current roles. | IT Operations |
| Strengthen joiner, mover, and leaver procedures | Ensure access is provisioned, modified, or revoked when employees join, change roles, or leave the organization. | IT Operations / Human Resources |
| Improve access-denied guidance | Provide clear instructions for reporting access issues and identifying the application involved. | IT Support |
| Preserve audit records | Document approvals, access changes, the responsible technician, and validation results. | Access Management |

### Preventive Review

The incident highlights the importance of separating authentication from authorization, validating business requirements before granting access, and maintaining an auditable access-management process.

**Implementation Status:** Recommendations documented; implementation not verified.

## 7. Related Tickets and Closure

### Related Records

| Record ID | Record Type | Description | Status |
|---|---|---|---|
| AR-002 | Access Request | Manager-approved request for standard CRM access for Emily Davis. | Completed in simulation |

No additional related incidents or escalations were identified as necessary for this case.

### Closure Checklist

- [x] User identity and account status verified.
- [x] Authentication confirmed to be working.
- [x] Missing security group membership identified.
- [x] Business need confirmed with the Sales manager.
- [x] Approval documented in access request AR-002.
- [x] Required access granted through the authorized procedure.
- [x] User successfully tested the CRM.
- [x] Resolution and access change documented.
- [x] Preventive recommendations recorded.

### Final Closure Statement

Incident INC-002 was closed after the missing CRM authorization was identified, the required approval was documented, the appropriate security group membership was granted, and the user confirmed successful access.

The case demonstrates a controlled IAM support workflow covering identity verification, authorization troubleshooting, approval handling, least-privilege access, validation, and documentation.

**Final Status:** Closed  
**Closure Basis:** Successful validation by the affected user  
**Case Type:** Fictional IT Support portfolio case study
