# README

## App Functionality

It is a software for tracking candidates (our product) across roles at various companies (aka clients).

### Application User Management

A user is either a client, a candidate, an agent, or other person authorized to view data within the application. The user management aspect of our application assigns roles to certain users and validates whether a user has access to the information they are attempting to retrieve or post.

#### Authentication

Authentication is a process in which the application validates a user exists within the system.

- [ ] Login
  - [ ] Username and password combo (username can [and should] be an email address for uniqueness.)
  - [ ] Generates an auth token with encoded user information.
- [ ] Logout
  - [ ] Invalidates the user token

#### Authorization

Authorization is a process that validates the logged in user's privileges on each access point in order to secure data properly.

- [ ] Role
  - [ ] Permission levels within the role.
    - [ ] Client
      - A representative of a specific company or master company.
        - [ ] Can post new jobs
        - [ ] Update current jobs (description, status)
    - [ ] Candidate
      - A person applying to a job or many different jobs at any company.
        - [ ] Can apply to job(s)
        - [ ] Update their profile
    - [ ] Admin
      - A superuser within the application who is authorized to see all data accross both client and candidates. Admins are the only users who can DELETE information.
    - [ ] Proxy
      - A proxy can represent a candidate or multiple candidates and submit to jobs at a number of (possibly all) clients.
  -

### Companies

A company is the parent to individual locations or instances of company branches. We have defined the parent company as `master_company` and all of the branches or locations are `companies`.

#### Features at the company level

- [x] Show a list of companies
  - [x] Get master company and all locations based on the parent co.
  - [x] Get an individual location
- [ ] Candidates matched to companies
  - [ ] The client should be able to view candidates (and their application status) who have applied:
    - [ ] to the company for any role/job
    - [ ] to a specific role/job
    - [ ] by job level
- [ ] The company should be able to update their status.
  - [ ] Active/Not-Active
  - [ ] Branch location
  - [ ] location point of contact

#### Features at the Job Level

- Update job openings/levels
  - Create a job posting (job)
  - Assign or Update job levels associated to a job

### Applicants

- See their information and update it
- See companies they are matched to
- See job levels they are matched to
- See job titles they are matched to
- Set themselves as active/not active
- See job placements
- View job placement history

### HR Agency

- Set companies and applicants to active/not active
- Add/Update/Delete master companies and sub-companies
- Add/Update/Delete applicants
- Add/Update/Delete job placement history
