# User & Access Management

## 1. Overview

The User & Access Management component of the IT Support & Helpdesk Lab simulates how an internal IT team manages employee access to company systems and resources.

The system uses a group-based access model. Instead of assigning permissions individually to each employee, users are assigned to groups that represent the access required for their job responsibilities. Each group is then associated with specific systems and permissions.

The access model follows this structure:

User
  ↓
Group
  ↓
System + Permission

For example, an employee in the Reservations department may belong to the `CRM-Reservations` group. This group provides access to the CRM system with specific permissions such as `Login`, `Read`, `Create`, and `Edit`.

This approach makes access management easier to maintain and scale. When multiple employees require the same access, they can be assigned to the appropriate group instead of configuring each user's permissions individually.

The model follows the principle of **least privilege**, ensuring that users receive only the access required to perform their responsibilities. Permissions such as `Delete` and `Admin` are not granted by default and should only be assigned when there is a valid business or administrative requirement.

The component is implemented using SQLite and is integrated into the broader IT Support & Helpdesk Lab. It provides a foundation for user onboarding, offboarding, access requests, permission changes, and access-related support tickets.

## 2. Users and Departments

The system maintains a centralized directory of employees who interact with the company's IT environment.

Each user is associated with a department that represents their organizational area within Borealis Travel. Departments provide organizational context and help the IT team understand the user's business role when handling access requests, incidents, and support tickets.

The current departments are:

- Reservations
- Concierge
- Sales
- Marketing
- Operations
- Administration
- IT

Each user record contains information such as:

- User ID
- Full name
- Email address
- Department
- Job role
- Account status
- Creation date
- Deactivation date

The department assigned to a user does not directly determine their permissions. Instead, departments provide organizational context, while access to systems is managed through groups and permissions.

For example, Sarah Johnson belongs to the Reservations department. Her department indicates where she works within the organization, while her assigned groups determine which systems she can access and which actions she can perform.

This separation between organizational structure and access control makes the model more flexible. Users can change departments or responsibilities without requiring permissions to be directly tied to their department.

## 3. Groups

Groups are used to organize users according to the access they require to perform their job responsibilities.

Instead of assigning individual permissions directly to each user, the IT team assigns users to one or more groups. Each group represents a specific access profile and is associated with the systems and permissions required for that profile.

The current groups are:

- CRM-Reservations
- Microsoft365-Users
- Zoom-Users
- Front-Reservations
- SharedDrive-Reservations

For example, the `CRM-Reservations` group is designed for employees who need access to the CRM system as part of their responsibilities in the Reservations department.

Groups provide several advantages:

- Simplify access management.
- Reduce repetitive permission configuration.
- Make onboarding and offboarding easier.
- Provide a consistent access model for users with similar responsibilities.
- Support the principle of least privilege.
- Make access changes easier to audit and maintain.

A user can belong to multiple groups at the same time. For example, Sarah Johnson belongs to several groups because her role requires access to multiple company systems.

The relationship between users and groups is many-to-many. A user can belong to multiple groups, and a group can contain multiple users.

This relationship is implemented through the `user_groups` table.

## 4. Systems

The `systems` table contains the catalog of applications and resources that employees may need to access as part of their work.

Keeping systems in a separate table allows access management to remain flexible. Groups are not directly tied to individual applications in the user records. Instead, group permissions determine which systems a group can access and what actions members of that group can perform.

The current systems are:

- Microsoft 365
- CRM
- Front
- Zoom
- Company Portal
- Shared Drives

Each system represents a specific application, platform, or company resource.

For example, the `CRM` system represents the company's customer relationship management platform, while `Shared Drives` represents shared company storage resources.

Systems are connected to groups through the `group_permissions` table. This allows the same system to be used by multiple groups with different permission levels.

For example:

- `CRM-Reservations` → CRM → Login, Read, Create, Edit
- `Microsoft365-Users` → Microsoft 365 → Login, Read, Create, Edit
- `Zoom-Users` → Zoom → Login, Read, Create, Edit

This separation between users, groups, systems, and permissions makes the access model easier to expand as the organization introduces new applications or access requirements.

## 5. Permissions

Permissions define the actions that a user is allowed to perform within a specific system.

The project uses a predefined permission catalog:

- Login
- Read
- Create
- Edit
- Delete
- Admin

Each permission represents a type of action rather than a specific application.

For example, `Read` does not refer to a particular system. It represents the ability to view information within whichever system the permission is assigned to.

The same permission can therefore be associated with different systems.

For example:

- CRM → Read
- Microsoft 365 → Read
- Zoom → Read
- Shared Drives → Read

The `Admin` permission represents elevated administrative capabilities and should not be assigned as a default permission.

Similarly, `Delete` is considered a potentially destructive permission and should only be granted when required by the user's responsibilities.

Permissions are not assigned directly to users. Instead, they are associated with groups and systems through the `group_permissions` table.

This structure allows the IT team to define exactly what members of a group can do within each system while maintaining a consistent and scalable access model.

## 6. Group Permissions

The `group_permissions` table defines what actions members of a specific group are allowed to perform within a specific system.

It connects three elements:

Group → System → Permission

For example:

CRM-Reservations → CRM → Edit

This means that users belonging to the `CRM-Reservations` group are allowed to edit information within the CRM system.

The `group_permissions` table contains:

- `group_id` — Identifies the group.
- `system_id` — Identifies the system.
- `permission_id` — Identifies the permission.

The table also enforces a unique combination of group, system, and permission. This prevents the same permission from being assigned to the same group and system more than once.

The current access mappings include:

- CRM-Reservations → CRM → Login, Read, Create, Edit
- Microsoft365-Users → Microsoft 365 → Login, Read, Create, Edit
- Zoom-Users → Zoom → Login, Read, Create, Edit
- Front-Reservations → Front → Login, Read, Create, Edit
- SharedDrive-Reservations → Shared Drives → Login, Read, Create, Edit

This design allows a group to have different permissions depending on the system.

For example, a group could have `Read` access to one system while having `Create` and `Edit` access to another.

The model is therefore more flexible than assigning a fixed set of permissions to a group without considering the target system.

## 7. User Groups

The `user_groups` table defines which groups are assigned to each user.

Users can belong to multiple groups, and each group can contain multiple users. This creates a many-to-many relationship between users and groups.

The relationship is implemented using:

- `user_id` — Identifies the user.
- `group_id` — Identifies the assigned group.

For example, Sarah Johnson belongs to the following groups:

- CRM-Reservations
- Microsoft365-Users
- Zoom-Users
- Front-Reservations
- SharedDrive-Reservations

Her group memberships determine which systems and permissions she receives.

The user does not receive permissions directly from the `users` table. Instead, the system follows the relationship:

User → User Group → Group → Group Permission → System + Permission

This approach allows multiple employees with similar responsibilities to share the same access configuration.

For example, if several employees in the Reservations department require the same CRM access, they can all be assigned to the `CRM-Reservations` group. If the permissions of that group need to change, the change can be applied to the group rather than modifying every user individually.

The `user_groups` table also prevents duplicate group assignments for the same user by enforcing a unique combination of `user_id` and `group_id`.

## 8. Effective Access

Effective access represents the actual systems and permissions available to a user after evaluating their group memberships and the permissions assigned to those groups.

The system determines effective access by following the relationships between users, groups, systems, and permissions:

User → Group → System → Permission

A user's effective access is therefore not stored directly in the `users` table. It is calculated by combining the user's group memberships with the permissions assigned to those groups.

For example, Sarah Johnson belongs to the `CRM-Reservations` group.

The `CRM-Reservations` group is associated with the CRM system and the following permissions:

- Login
- Read
- Create
- Edit

As a result, Sarah's effective access to the CRM is:

CRM → Login, Read, Create, Edit

Sarah also belongs to additional groups, giving her access to Microsoft 365, Zoom, Front, and Shared Drives.

This model allows the IT team to answer practical access management questions such as:

- Which systems can a user access?
- What actions can a user perform within a system?
- Which group provides a specific permission?
- What access would be removed if a user were removed from a group?

Effective access can be retrieved using SQL queries that join the `users`, `user_groups`, `groups`, `group_permissions`, `systems`, and `permissions` tables.

This provides a clear and auditable way to determine a user's current access without storing duplicated permission information directly on the user record.

## 9. Least Privilege

The access model follows the principle of **least privilege**.

Least privilege means that users should receive only the permissions required to perform their assigned responsibilities. Users should not receive additional access simply because it is available.

In this project, permissions such as `Delete` and `Admin` are not assigned by default.

For example, members of the `CRM-Reservations` group currently have:

- Login
- Read
- Create
- Edit

They do not have:

- Delete
- Admin

This reflects a typical support and access management practice where users receive the minimum level of access required for their daily tasks.

Applying least privilege helps reduce the potential impact of:

- Accidental changes or deletion of data.
- Unauthorized access to systems or information.
- Misuse of elevated privileges.
- Security incidents involving compromised accounts.

Additional permissions should only be granted when there is a valid business requirement and, where applicable, the appropriate authorization.

The group-based access model makes this principle easier to enforce because permissions can be reviewed and modified at the group level instead of being managed independently for every user.

## 10. User Lifecycle

User access should be managed throughout the employee lifecycle, from onboarding to offboarding.

The main stages are:

- Onboarding
- Role or department changes
- Offboarding

### Onboarding

When a new employee joins the company, the IT team creates the user account and assigns the appropriate department and groups based on the employee's role and responsibilities.

Group membership then determines the systems and permissions available to the user.

This approach allows the IT team to provide consistent access without manually assigning individual permissions for every system.

### Role or Department Changes

When an employee changes responsibilities or moves to another department, their access should be reviewed.

The IT team may need to:

- Add new groups.
- Remove groups that are no longer required.
- Review existing permissions.
- Verify that the user's effective access matches their new responsibilities.

Access should be adjusted as part of the role change rather than allowing previous permissions to remain indefinitely.

### Offboarding

When an employee leaves the company, their account should be deactivated and their access revoked.

The user record is retained to preserve historical information related to tickets, incidents, and previous support activity.

The user record includes a `status` field and a `deactivated_at` field to distinguish inactive users from active users.

The offboarding process should include:

1. Deactivate the user's account.
2. Revoke access to assigned groups and systems.
3. Remove or disable access to company resources.
4. Preserve relevant historical records.
5. Record the access changes for auditing purposes.

This approach allows the organization to revoke access while maintaining historical information required for IT support, auditing, and reporting.

## 11. Example: Sarah Johnson

Sarah Johnson is an employee in the Reservations department at Borealis Travel.

Her user account is associated with the Reservations department and she is assigned to the following groups:

- CRM-Reservations
- Microsoft365-Users
- Zoom-Users
- Front-Reservations
- SharedDrive-Reservations

These group memberships provide Sarah with access to the systems required for her responsibilities.

Her effective access is:

| System | Permissions |
|---|---|
| CRM | Login, Read, Create, Edit |
| Microsoft 365 | Login, Read, Create, Edit |
| Zoom | Login, Read, Create, Edit |
| Front | Login, Read, Create, Edit |
| Shared Drives | Login, Read, Create, Edit |

Sarah does not have the `Delete` or `Admin` permissions in these systems because they are not required for the access profile defined in this lab.

The access is determined through the following relationships:

User → User Groups → Groups → Group Permissions → Systems + Permissions

For example:

Sarah Johnson
→ CRM-Reservations
→ CRM
→ Login, Read, Create, Edit

This example demonstrates how the access model can be used to determine a user's effective permissions without storing individual system permissions directly on the user record.

If Sarah changes roles or leaves the company, her group memberships can be reviewed and updated while preserving her historical user and support records.