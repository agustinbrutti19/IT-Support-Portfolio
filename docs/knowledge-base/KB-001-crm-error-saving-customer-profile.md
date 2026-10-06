# KB-001 — CRM Error When Saving Customer Profile

**Category:** CRM  
**System:** CRM  
**Audience:** Helpdesk  
**Severity:** High  
**Last Updated:** 2026-10-06

## Problem

Users may encounter an error when attempting to save changes
to an existing customer profile in the CRM.

The issue prevents customer information from being updated
successfully.

## Symptoms

- The user can access the CRM normally.
- The user can open an existing customer profile.
- The user can modify customer information.
- An error appears when the user attempts to save the changes.
- The updated information is not saved.
- The issue may prevent the Reservations team from completing
  customer-related tasks.

## Root Cause

The issue was caused by a backend validation error in the CRM.

The validation error prevented the application from successfully
processing changes made to an existing customer profile.

The user's Microsoft 365 account and CRM permissions were
verified and were working correctly, which ruled out an
authentication or access-related issue.

## Troubleshooting Steps

1. Confirm that the user can successfully log in to Microsoft 365.
2. Confirm that the user can successfully access the CRM.
3. Verify that the user's CRM permissions are correctly assigned.
4. Open an existing customer profile.
5. Modify one or more customer fields.
6. Attempt to save the changes.
7. If an error appears, record the exact error message.
8. Repeat the test to determine whether the issue is reproducible.
9. If the issue is consistently reproducible and permissions are confirmed to be correct, document the behavior and prepare a bug report.
10. Escalate the issue to the appropriate technical team with the reproduction steps, expected result, actual result, environment, and business impact.

## Resolution

The issue was escalated to the Engineering team after the
problem was reproduced and documented.

Engineering identified the backend validation error and
deployed a fix.

Helpdesk then reproduced the original scenario and verified
that customer profile changes could be saved successfully
without triggering the previous error.

The user confirmed that the CRM was working correctly and
that customer profile changes could be saved successfully.

## When to Escalate

The issue should be escalated when:

- The problem can be consistently reproduced.
- The user's account and permissions have been verified.
- Basic troubleshooting does not resolve the issue.
- The issue appears to be related to application behavior or
  backend processing.
- The problem affects an important business process.
- A software defect is suspected.

Helpdesk should avoid making changes to the application or
backend when the issue requires specialized technical access.

## Information Required for Escalation

The following information should be included when escalating
a CRM application issue:

- User name and department.
- Ticket number.
- Clear description of the issue.
- Exact error message, if available.
- Steps to reproduce the problem.
- Expected result.
- Actual result.
- Application and environment where the issue occurred.
- User impact and affected business process.
- Troubleshooting already performed.
- Confirmation that the issue is reproducible.
- Any relevant screenshots, logs, or supporting information.