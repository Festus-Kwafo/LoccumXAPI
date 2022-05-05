# DCIT 307 - MINI PROJECT, GROUP 12 
# LOCUM PRO - SRS DOCUMENT
## 1. INTRODUCTION
### 1.1 Purpose and Product Scope
Shift work is a type of work scheduling in which workers succeed each other at the same workplace to perform the same operations. Most of the working hours during the shift system fall outside the standard workday such as evening, night or weekend shifts. On-call shift is a special form of shift work where in case of emergency particular workers are called for their duties. This variety of shift work is the most appropriate to employ the services of locums.
Locums are workers hired on a temporary basis to fill vacancies in full-time positions. They have become a common career option especially among the physician workforce dating back to 1985 and continue to be an increasingly utilised employment option to cope with short-term vacancies. Locums are essential for maintaining continuity of service, filling service gaps in rotas due to absence or recruitment and retention problems, maintaining appropriate staffing levels and allowing staffing flexibility. Our locum online and digital service connects validated professionals to clients requiring their expertise for temporary, short-term and one-time jobs.
### 1.2 Intended audience of the document and software
This software is intended for organisations or individuals to fill the gaps left by their workers due to planned vacations as well as unplanned working leave, for example when the worker falls sick. Organisations or individuals that have registered on the system will get access to this feature. This software is also intended for people that don’t like the idea of working at one place for a long time. People who want to deliver service to its client in a short period of time.

## 2. OVERALL DESCRIPTION
### 2.1 Product Functions
- Sign up as an institution
- Sign up as an individual
- Add a proof of identity to qualification during setting up of account profile (for both institution & individual)
- Institutions can put an open shift job for a locum
- Individuals can accept or reject locum offer from companies 
- Locum jobs put up by institutions set to expire after set date if not registered by a locum or individual
- Ratings and reviews feature.

### 2.2 User classes and stories
#### Actors of the system:
#### An Institution (e.g., Pharmacy, Clinic, Community Health Centre etc.)
Pharmacies, clinics, and health centres will be using the locum app to find locums for an open shift. Heads and members of these institutions will have the chance to request for a locum. The locum then makes the decision to either accept or reject the job. Institutions can also place an offer on the app for a locum to apply for. Important documents will be checked to verify if the locum is qualified enough for the shift. Locums may also be shown how much they will earn from a specific shift.

#### A locum (individual user)
The locum will set up his profile with a little background information to ease tracking in case of any emergencies. 
Locums can add their area of expertise in their profile to ease finding a job from an institution.
Locums have the choice to accept or reject a locum request. They will then have a full schedule on what days they must work, and at what time.

#### User Stories
#### An Institution
1. As an institution I want to be able to sign up with my company's email account.
2. As an institution I want to be able to set up a profile for my locum account.
3. As an institution I want to be able to put up an offer for a locum to apply.
4. As an institution I want my offer put up to expire if no locum accepts an hour before the set date and time.
5. As an institution I want to be able to delete a locum offer I put up in some circumstances.
6. As an institution I want to be able to put up permanent job offers as well.
7. As an institution I want to be notified when a locum accepts an offer.
8. As an institution I want to be able to search for locums I want and send them offers directly.
#### An Individual(Locum)
1. As an individual I want to be able to sign up with my email.
2. As an individual I want to be able to set up a profile with a little background information.
3. As an individual I want to be linked with specific job offers based on my profile.
4. As an individual I want to be notified on open shifts or offers set up by institutions in my geographical area.
5. As an individual I want to be able to either accept or reject offers (requests) from institutions.
6. As an individual I want to be able to cancel a shift I have initially accepted at least 12hrs before the due time based on a mutual agreement between myself and the institution. 
7. As an individual I want to be able to know how much I will be paid per shift.

### 2.3 Operating Environment
Since an operating system manages the hardware and software resources, provides a platform for application programs and system programs to run as well, Locum Pro mobile app will be supported by operating systems such as android and ios. Whilst the web obviously needs no specific operating system to run on, the web version would be able to function everywhere, anywhere.

### 2.4 Design and Implementation constraints
During the signup phase, we should be able to verify that the user is actually a certified locum(health worker) or a certified health institution. In our case, getting access or rights to such resources, say, an api, or a database to fetch original information would be very difficult.
Availability of APIs for some essential features such as scanning your surrounding to determine locums or institution available for service

### 2.5 User Documentation
We would be providing guidelines for usage to users both on the mobile app and on the web app. Here, we would show our users, step-by-step the paths and processes they should go through to accomplish a task in the software. Say, Employers adding jobs for locums, locums selling themselves out for jobs, booked jobs    and any other vital feature of the software.

## 3. SYSTEM FEATURES
### 3.1 Features (Functional Requirements)
#### The Sign up section
The product will have a **sign up section where all users** will have to sign up to create an account and be properly added to the system to allow them to use it .
In case the details entered for the account are wrong, the system will alert them to check and correct all mistakes in order to be able to continue.
This is of high priority  since every user has to be added to the system database and we would like to prevent people who are not registered into the system from accessing the information of the people who are registered in the system. This helps in a way to prevent fraudulence.
**Sign up as an institution** section will allow institutions to sign up with the company details and make them available for locum services.
In case the details entered for the account are wrong, the system will alert them to check and correct all mistakes in order to be able to continue.
This is of high priority since every institution has to be added to the system database for proper management.
For both individuals and institutions, a system of verification will be set up to make sure the account is authentic.  Proofs of identity will be required where they can upload documents to be verified.
This is highly recommended in order to make sure that all users and institutions qualify to offer such services and locum spaces and not just any ordinary person login on to be registered. 

#### Putting up a Locum job offer or Availability.
In this feature, the locum agency will be able to display a locum job vacancy which will be visible to the available individuals. The exact job that is available will be described in this feature. This feature will also allow individuals to present themselves as being available to take any locum job in their specific area of expertise.
Notification Feature
This will help notify all locums of available job offers. This feature will work as an in-app feature that will pop-up whenever an available job is offered by any institution. 
Accept or Reject Locum job offer
This feature will allow the individual (Locum) to either accept or reject the offer proposed to them on the application.  Buttons will be made and the freedom given to  individuals to audit or scan through the available offers and or Locum jobs offered and to either accept or reject such offers. 

#### GPS location of Locum jobs
This option will display the location using the GPS system to make tracking and location of job offers easy for both individuals and institutions.  The google maps feature will be embedded in the system to allow live tracking and easy location identification of jobs and institutions. 
This is of average imp	ortance due to the fact that Locums can still use the contact feature in the system to get location of jobs being offered. 
Job Expiry Feature
This feature will allow a smooth sail in job put up, and to avoid losing track of jobs and job offers being clumsy.
This feature will set a time frame for jobs that have been offered. Each job is set to expire after some time when the locum refuses to accept the job offer. This is to filter the system and to provide a clear difference  between available jobs and expired jobs. 
This is of high priority or importance since it will filter and avoid wasting time to accept already expired or unavailable jobs. 

#### Job Expiry Feature
This feature will allow a smooth sail in job put up, and to avoid losing track of jobs and job offers being clumsy.
This feature will set a time frame for jobs that have been offered. Each job is set to expire after some time when the locum refuses to accept the job offer. This is to filter the system and to provide a clear difference  between available jobs and expired jobs. 
This is of high priority or importance since it will filter and avoid wasting time to accept already expired or unavailable jobs. 

## 4. NON FUNCTIONAL REQUIREMENTS
#### Scalability:
There would be room for expansion of our scope to suit our increasing market, that is, the growth of institutions(Employers) and Locums  should be able to be accommodated in and to meet the rising demand for Locum Pro’s services offered.
Usability:
A simple UI will be implemented for the user(both the Employer and the locum) so that they will be able to quickly access the software and navigate through the pages and services of the software with ease. 
#### Performance:
To improve the performance of our software, best practices and standards for coding will be adopted in the development stage. This is because when the code is poorly structured it could lead to slower systems, but with a structured method of coding future improvements could even be made without making changes to the entire code.
UX optimization will also be adopted to achieve the best user experience. UX optimization methods such as the implementation of “lazy loading” whereby during the loading of a page, the top of the page displays first before the rest of the page would allow the user to start reading the content of the page even before the page is fully loaded.
Application performance tools such as Azure Monitor, Seq, etc. will be used to help optimise our software by alerting the team when performance boundaries have been crossed giving us time to troubleshoot before the problem becomes serious.
Security:
A firewall will be used to deny access to unauthorised users, protecting the database of locums. Account security procedures such as enforcing the use of strong passwords or locking the account after making a few unsuccessful attempts will be implemented..
SSL encryption will also be used to prevent hackers from accessing user’s login credentials. Website scanners such as Sitelock, Securi Sitecheck, etc. will be used to scan the website at least once a month for any malware.
Reliability and Maintainability
Availability: Heroku will host the system API so that it will be available 24/7 

#### Recoverability
Users will receive an error message on the system when an error is incurred. And when the maintenance time surpasses 6hours, an email will be deployed to inform the users about the speculated time the maintenance will be completed. 
We will have a spare hard disk drive where we will store the codes in case of any faults. 
Storage media for backup: 
Hard Copy backup: Krofuas PC will be used as hard backup for the programs 
Soft-copy backup:  Icedrive 
Aws Amplify's database
Common Errors we might encounter. 
Communication Errors from software to end-user. Example, No Help instructions/menu provided, features that are part of the release but are not documented in the help menu. 
Fault tolerance:
The System's pressure limit is set to 100 users. The number of users on the system should not exceed 100. 
Runtime streak: 2 weeks after development. 
Fault repair time: within 24hours
Maintainability costs in terms of workmanship:
5 developers plus project manager
