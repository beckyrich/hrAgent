# README

## App Functionality

It is a software for tracking candidates (our product) across roles at various companies (aka clients). 

### Companies

A company is the parent to individual locations or instances of company branches. We have defined the parent company as `master_company` and all of the branches or locations and `companies`.

#### Features at the company level

- candidates matched to companies
  - The client should be able to view candidates who have applied:
    - to the company for any role/job
    - to a specific role/job 
    - by job level
- The company should be able to update their status. 
  - Active/Not-Active
  - Branch location
  - location point of contact

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
