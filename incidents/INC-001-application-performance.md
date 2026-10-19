# INC-001 — Application Performance Incident

> **Scenario:** Fictional IT Support case study  
> **Company:** Borealis Travel  
> **Incident ID:** INC-001  
> **Category:** Application Performance  
> **Priority:** High  
> **Status:** Resolved

## 1. Incident Summary

Borealis Travel experienced an application performance incident affecting the Reservations and Sales departments.

Starting at approximately 09:00, users reported significant delays when loading reservations and searching for customer information. Some users also experienced temporary application freezes.

The issue affected multiple users across two departments. Initial investigation indicated that both applications relied on the same backend services, helping the IT Support team identify a potential common cause rather than treating each report as an isolated problem.

The incident was resolved after the Database team restored an unavailable database index. Subsequent technical checks and user validation confirmed that application performance returned to normal.

**Root cause:** A database change made at approximately 08:55 left an index required by customer and reservation queries unavailable, causing inefficient database queries and increased API response times.

## 2. Impact and Scope

### Affected Departments
- **Reservations:** Users experienced slow reservation loading times and temporary application freezes.
- **Sales:** Users experienced delays when searching for customer information.

### Affected Services
- Reservations application
- Sales Portal
- Travel API
- Customer Database

### User Impact
Multiple users were unable to use the affected application features at normal speed. This delayed reservation-related tasks and customer information searches.

### Scope of the Incident
The issue affected specific operations that retrieved customer and reservation data. Other Travel API operations continued to respond normally, and no widespread authentication failures were identified.

### Initial Assessment
Because both affected applications depended on the same backend services, the incident was investigated as a potential shared-service issue rather than as separate workstation problems.

## 3. Incident Timeline

| Time | Event | Findings / Actions |
|---|---|---|
| 08:55 | Database change | A database change was recorded shortly before the first user reports. |
| 09:00 | Initial user report | Sarah Johnson reported slow loading times and temporary freezes in the Reservations application. |
| 09:18 | Related incident reported | INC-001-T01 reported slow reservation loading in the Reservations department. |
| 09:26 | Related incident reported | INC-001-T02 reported application freezes when opening a reservation. |
| 09:34 | Additional department affected | INC-001-T03 reported delays when retrieving customer information in the Sales Portal. |
| Investigation | Service dependency analysis | The Helpdesk identified that Reservations and Sales depended on the Travel API and Customer Database. |
| Investigation | Application team consulted | The Applications team confirmed increased Travel API latency affecting customer and reservation operations. No widespread authentication failures were identified. |
| Investigation | Database team consulted | The Database team found unusually slow queries and identified a database change that coincided with the beginning of the incident. |
| Investigation | Execution plan reviewed | The query execution plan showed a full table scan instead of using the expected index. The index was confirmed unavailable after the database change. |
| Resolution | Database correction | The Database team restored the index through the approved change procedure. |
| Validation | Technical and user verification | Query performance and API latency returned to normal. Sarah Johnson and Sales confirmed that their applications were working correctly. |
| Closure | Related incidents documented | The main incident and related tickets were documented and prepared for closure after validation. |

> **Note:** Investigation, resolution, validation, and closure times were not specified in the simulation. They are therefore recorded as stages rather than assigned invented timestamps.

## 4. Troubleshooting and Evidence

### 4.1 Initial Symptom Assessment

**Reported symptoms**
- Reservations screens took approximately 20 seconds to load.
- The application temporarily froze when opening screens or reservations.
- Microsoft Word and Notepad continued to work normally on the affected workstation.
- Multiple users reported similar symptoms.

**Assessment:** The symptoms were concentrated in specific business applications rather than affecting all applications on the workstation.

### 4.2 Related Incident Review

The Helpdesk reviewed existing tickets and identified three related reports:

- **INC-001-T01:** Slow reservation loading.
- **INC-001-T02:** Application freezes when opening a reservation.
- **INC-001-T03:** Delays retrieving customer information in the Sales Portal.

**Assessment:** Reports from both Reservations and Sales suggested a shared backend dependency rather than an isolated workstation issue.

### 4.3 Service Dependency Analysis

The internal service catalog identified the following dependencies:

- Reservations application → Travel API → Customer Database
- Sales Portal → Travel API → Customer Database

**Assessment:** The shared Travel API and Customer Database were prioritized for investigation.

### 4.4 Application Team Findings

The Applications team reported increased Travel API latency beginning at approximately 09:05.

The latency was concentrated in customer search and reservation retrieval operations. Other API operations remained responsive, and no widespread authentication failures were identified.

**Assessment:** The evidence narrowed the investigation to the database operations used by the affected API endpoints.

### 4.5 Database Investigation

The Database team observed unusually slow queries involving customer and reservation data. Database CPU and memory utilization remained within normal ranges.

A database change had been recorded at approximately 08:55, shortly before the first reported symptoms.

**Assessment:** The timing of the change and the query-specific performance degradation justified further investigation.

### 4.6 Query Execution Plan Review

The Database team compared query execution behavior before and after the change.

- Before the change, the relevant queries used the expected index.
- After the change, the execution plan showed a full table scan.
- The team confirmed that the expected index was no longer available after the database change.

**Assessment:** The execution plan and index availability provided technical evidence explaining the increased query execution times.

### 4.7 Evidence Summary

| Evidence | Observation | Diagnostic Value |
|---|---|---|
| Related incident tickets | Multiple users and two departments affected | Suggested a shared issue |
| Service catalog | Both applications depended on the same backend services | Narrowed the investigation scope |
| Travel API metrics | Latency increased for customer and reservation operations | Identified affected API operations |
| Database performance metrics | No general CPU or memory saturation | Made overall resource exhaustion less likely |
| Query execution plan | Full table scan instead of the expected index | Supported the database performance diagnosis |
| Database change history | Change at approximately 08:55 preceded the symptoms | Connected the issue to a recent change |

> **Evidence note:** This is a fictional training case. The findings and metrics described above are simulated and are not screenshots or logs from a real production environment.

## 5. Root Cause and Resolution

### 5.1 Root Cause

A database change performed at approximately 08:55 left the index required by customer and reservation queries unavailable.

Without the expected index, the database performed full table scans for affected queries instead of locating the relevant records efficiently. This increased query execution times and contributed to elevated response times in the Travel API.

The issue affected specific operations used by the Reservations application and Sales Portal. Other API operations remained responsive, and the database did not show general CPU or memory saturation.

**Confirmed root cause:** The database change left the expected index unavailable, resulting in inefficient query execution for customer and reservation data.

### 5.2 Resolution

The Database team:

1. Reviewed the database change and the affected query execution plans.
2. Confirmed that the expected index was unavailable.
3. Evaluated the corrective action through the approved change procedure.
4. Restored the index.
5. Rechecked query execution behavior and performance after the correction.

The Helpdesk coordinated the investigation and communicated with the Applications and Database teams. The corrective database operation was performed by the authorized Database team.

### 5.3 Resolution Outcome

Following the correction:

- The affected queries used the expected index again.
- Query response times returned to their normal range.
- Travel API latency returned to normal.
- Sarah Johnson confirmed that Reservations was functioning correctly.
- Sales confirmed that customer searches were responding normally.

### 5.4 Incident Status

**Status:** Resolved

The incident was considered resolved after technical checks and user validation confirmed that the affected services had recovered.

> **Training note:** All systems, people, findings, and outcomes in this report are fictional and are provided for educational purposes.

## 6. Preventive Actions

The following actions are recommended to reduce the likelihood of similar incidents.

| Preventive Action | Purpose | Suggested Owner |
|---|---|---|
| Validate database indexes during schema changes | Ensure required indexes remain available after database modifications | Database Team |
| Include query performance checks in change validation | Detect unexpected query execution changes before deployment | Database Team |
| Monitor query latency for critical operations | Identify performance degradation affecting customer and reservation workflows | Database Team |
| Monitor Travel API response times by endpoint | Detect problems affecting specific operations before they impact more users | Applications Team |
| Review database change and rollback procedures | Ensure changes have appropriate validation, approval, and recovery plans | Database and Applications Teams |
| Document dependencies between business applications and backend services | Help Support teams identify shared failure points more quickly | IT Operations |

### Follow-up Recommendations

- Review whether the database change process adequately validates critical indexes.
- Establish appropriate performance baselines for customer search and reservation retrieval.
- Review alert thresholds for sustained increases in API and database query latency.
- Ensure future incidents can be correlated with recent changes through consistent timestamps and logs.

> **Implementation status:** These are recommendations only. The fictional case does not establish that these actions have been implemented.

## 7. Related Tickets and Closure

### Related Tickets

| Ticket ID | Reported Issue | Relationship to INC-001 | Closure Summary |
|---|---|---|---|
| INC-001-T01 | Slow reservation loading | Related to the same Reservations performance incident | Reservation loading returned to normal after the database index was restored. |
| INC-001-T02 | Application freezes when opening a reservation | Related to the same Reservations performance incident | Reservation screens were validated after the corrective action. |
| INC-001-T03 | Delays retrieving customer information in the Sales Portal | Related to the same shared backend performance incident | Customer searches returned to normal after the database correction. |

### Closure Checklist

- [x] Related reports reviewed and linked to the main incident.
- [x] Root cause documented.
- [x] Corrective action recorded.
- [x] Technical performance checks completed.
- [x] User validation completed with Reservations and Sales.
- [x] Resolution documented for the related tickets.
- [x] Incident closure criteria satisfied.

### Final Closure Summary

The incident affected customer and reservation operations across the Reservations and Sales departments. Investigation identified an unavailable database index following a database change, resulting in inefficient queries and elevated Travel API latency.

The Database team restored the index through the approved change procedure. Subsequent technical checks and user validation confirmed that the affected services returned to normal operation.

INC-001 and its related tickets were documented for closure after their individual records were updated and their resolution status was verified.

> **Training note:** This is a fictional case study. The ticket relationships, closure records, and outcomes are simulated.
