# XBASIC PROMO SYSTEMS TESTS

## Introduction

For more details on these tests please consult [Project Analysis](/doc/project-analysis.txt)

## Header

### Acceptance Criteria

The XBasic brand and a logo should appear at the top of each page

A menu set of page links should be presented toward the top of the page

![Header](./doc/screenshots/header-crop.webp)

On small screens the menu should appear as a drop-down menu

![Dropdown Menu](./doc/screenshots/dropdown-menu-crop.webp)

Each of the menu items is highlighted when hovered on and the links work:

Home

![Hover on Home](./doc/screenshots/hover-home-crop.webp)

Home Link

![Home Link Page](./doc/screenshots/home-link-crop.webp)

GUI-Design

![Hover on GUI-Design](./doc/screenshots/hover-gui-design-crop.webp)

GUI-Design Link

![GUI-Design Link Page](./doc/screenshots/gui-design-link-crop.webp)

Language

![Hover on Language](./doc/screenshots/hover-language-crop.webp)

Language Link

![Language Link Page](./doc/screenshots/language-link-crop.webp)

Functions

![Hover on Functions](./doc/screenshots/hover-functions-crop.webp)

Functions Link

![Functions Link Page](./doc/screenshots/functions-link-crop.webp)

Debugging

![Hover on Debugging](./doc/screenshots/hover-debugging-crop.webp)

Debugging Link

![Debugging Link Page](./doc/screenshots/debugging-link-crop.webp)

Issues

![Hover on Issues](./doc/screenshots/hover-issues-crop.webp)

Issues Link

![Issues Link Page](./doc/screenshots/issues-link-crop.webp)

Sign-in/up

![Hover on sign-in/up](./doc/screenshots/hover-sign-in-up-crop.webp)

Sign-in/up Link

![Sign-in/up Link Page](./doc/screenshots/sign-in-up-link-crop.webp)

Logout

![Hover on Logout](./doc/screenshots/hover-logout-crop.webp)

Logout Link

![Logout Link Page](./doc/screenshots/logout-link-crop.webp)

## Footer

### Acceptance Criteria

There is a link in the footer to the XBasic manual

Links to the sourceforge and github sites in the footer with text

Links to the groups.io and sourceforge sites

![Footer](./doc/screenshots/footer-crop.webp)

### Link Tests

XBasic Manual

![XBasic Manual Link](./doc/screenshots/xbasic-manual-link.webp)

Sourceforge Download

![Sourceforge Download Link](./doc/screenshots/sourceforge-link.webp)

GitHub Download

![GitHub Download Link](./doc/screenshots/github-link.webp)

Groups.io

![Groups.io Link](./doc/screenshots/groups-io-link.webp)

## User Adminitration, Registration, General

### Acceptance Criteria

There should be pages for Login, Sign-up and Logout

Registration details include a username

Register

![Register](./doc/screenshots/register.webp)

Login

![Login](./doc/screenshots/sign-in.webp)

Logout

![Logout](./doc/screenshots/logout.webp)

A message should be displayed after logout/login and register

The user should be returned to the home page after each action

The menu item for Logout should only be visible if the the user is logged-in

The menu item for Login/Sign-up should only be visible if the user is NOT logged-in

Register

![Register Details](./doc/screenshots/register-complete.webp)

![Register Done](./doc/screenshots/register-done.webp)

Login

![Login Details](./doc/screenshots/sign-in-complete.webp)

![Login Done](./doc/screenshots/sign-in-done.webp)

Logout

![Logout Done](./doc/screenshots/logout-done.webp)

### Data Tests

Registration:

omit username

Focus returned to username with focus message

![Register Username Omitted](./doc/screenshots/register-username-omitted.webp)

omit password

Focus returned to password with focus message

![Register Password Omitted](./doc/screenshots/register-password-omitted.webp)

poor password

![Register Password Poor](./doc/screenshots/register-password-poor.webp)

username already exists

![Register Username Exists](./doc/screenshots/register-username-exists.webp)

Login:

omit username

Focus set on username and option to view saved logins presented

![Sign-in Username Omitted](./doc/screenshots/sign-in-username-omitted.webp)

invalid username

![Sign-in Username Invalid](./doc/screenshots/sign-in-username-invalid.webp)

omit password

Focus set on password, message displayed

![Sign-in Password Omitted](./doc/screenshots/sign-in-password-omitted.webp)

invalid password

![Sign-in Invalid Password](./doc/screenshots/sign-in-password-invalid.webp)

## Administration Editor

### Acceptance Criteria

Feature Pages:

Editing of the feature pages is provided by the site/admin/ url

![Admin Editor Login](./doc/screenshots/admin-editor-login.webp)

There is provision for feature pages

![Admin Editor Main Page - Feature Pages](./doc/screenshots/admin-editor-main-page.webp)

The administrator can add feature pages

![Admin Editor Add Page](./doc/screenshots/admin-editor-add-page.webp)

The administrator can edit feature pages

The administrator can include a feature page introduction with an image

Site page contents are updated according to the feature page record

![Admin Editor make Change](./doc/screenshots/admin-editor-edit-page.webp)

![Admin Editor page displayed](./doc/screenshots/admin-editor-edit-change.webp)

The administrator can delete feature pages

Confirmation is required for feature page deletion

![Admin Editor feature page listed to delete](./doc/screenshots/admin-editor-delete-page-1.webp)

![Admin Editor feature page to be deleted](./doc/screenshots/admin-editor-delete-page-2.webp)

![Admin Editor feature page delete confirmation](./doc/screenshots/admin-editor-delete-page-3.webp)

![Admin Editor feature page delete done](./doc/screenshots/admin-editor-delete-page-4.webp)

Feature Sections:

There is provision for feature sections

![Admin Editor feature sections list](./doc/screenshots/admin-editor-features.webp)

The administrator can add feature sections

![Admin Editor add feature section](./doc/screenshots/admin-editor-add-section.webp)

The administrator can edit feature sections

![Admin Editor edit feature section select](./doc/screenshots/admin-editor-edit-section-1.webp)

![Admin Editor edit feature section page](/doc/screenshots/admin-editor-edit-section-2.webp)

Site page contents are updated according to changes to the feature sections

![Admin Editor display feature section](./doc/screenshots/admin-editor-add-section-display.webp)

![Admin Editor edit feature section display](./doc/screenshots/admin-editor-edit-section-3.webp)

The administrator can delete feature sections

Confirmation is required for section deletion

![Admin Editor delete section list](./doc/screenshots/admin-editor-delete-section-1.webp)

![Admin Editor delete section item](./doc/screenshots/admin-editor-delete-section-2.webp)

![Admin Editor delete section confirmation](./doc/screenshots/admin-editor-delete-section-3.webp)

![Admin Editor delete section deleted](./doc/screenshots/admin-editor-delete-section-4.webp)
As an administrator I can edit/add or delete Issues using the admin pages in order to 
ensure editorial standards

Issues:

Admin Pages Add Issue

Issues are updated accordingly on the Issues page of the website

![Admin Editor list issues](./doc/screenshots/admin-editor-add-issue-1.webp)

![Admin Editor add issue page](./doc/screenshots/admin-editor-add-issue-2.webp)

![Admin Editor add issue list updated](./doc/screenshots/admin-editor-add-issue-3.webp)

![Admin Editor add issue page updated](./doc/screenshots/admin-editor-add-issue-4.webp)

Admin Pages Edit Issue

![Admin Editor edit issue page](./doc/screenshots/admin-editor-edit-issue-1.webp)

![Admin Editor edit issue - issue page](./doc/screenshots/admin-editor-edit-issue-2.webp)

Admin Pages Delete Issue

Deletion requires confirmation

![Admin Editor delete issue - selection](./doc/screenshots/admin-editor-delete-issue-1.webp)

![Admin Editor delete issue - edit issue page](./doc/screenshots/admin-editor-delete-issue-2.webp)

![Admin Editor delete issue - confirmation](./doc/screenshots/admin-editor-delete-issue-3.webp)

![Admin Editor delete issue - item deleted](./doc/screenshots/admin-editor-delete-issue-4.webp)

Answers:

As an administrator I can edit/add or delete Answers using the admin pages in order to 
ensure editorial standards

Acceptance criteria:

Admin Pages Add Answer

Answers are updated accordingly on the Issues page of the website

![Admin Editor - Add Answe, list of answers](./doc/screenshots/admin-editor-add-answer-1.webp)

![Admin Editor - Add Answer page](./doc/screenshots/admin-editor-add-answer-2.webp)

![Admin Editor - Add Answer, list updated](./doc/screenshots/admin-editor-add-answer-3.webp)

![Admin Editor - Add Answer, Issue Page](./doc/screenshots/admin-editor-add-answer-4.webp)


Admin Pages Edit Answer

![Admin Editor - Edit Answer, list selection](./doc/screenshots/admin-editor-edit-answer-1.webp)

![Admin Editor - Edit Answer, edit page](./doc/screenshots/admin-editor-edit-answer-2.webp)

![Admin Editor - Edit Answer, list updated](./doc/screenshots/admin-editor-edit-answer-3.webp)

![Admin Editor - Edit Answer, Issue Page Updated](./doc/screenshots/admin-editor-edit-answer-4.webp)

Admin Pages Delete Answer

Deletion requires confirmation

![Admin Editor - Delete Answer, Select from list](./doc/screenshots/admin-editor-delete-answer-1.webp)

![Admin Editor - Delete Answer, record to delete](./doc/screenshots/admin-editor-delete-answer-2.webp)

![Admin Editor - Delete Answer, confirm deletion](./doc/screenshots/admin-editor-delete-answer-3.webp)

![Admin Editor - Delete Answer, list updated](./doc/screenshots/admin-editor-delete-answer-4.webp)

#### Data Tests

Duplicate Title - Should be Unique in all cases:

Add Feature Page

![Admin Editor - Add Page - Duplicate Title](./doc/screenshots/admin-editor-page-duplicate-1.webp)

![Admin Editor - Submit Page - Duplicate Title](./doc/screenshots/admin-editor-page-duplicate-2.webp)

Add Feature Section

![Admin Editor - Add Section - Duplicate Title](./doc/screenshots/admin-editor-section-duplicate-1.webp)

![Admin Editor - Submit Section - Duplicate Title](./doc/screenshots/admin-editor-section-duplicate-2.webp)

Add Issue

![Admin Editor - Add Issue - Duplicate Title](./doc/screenshots/admin-editor-issue-duplicate-1.webp)

![Admin Editor - Submit Issue - Duplicate Title](./doc/screenshots/admin-editor-issue-duplicate-2.webp)

Add Answer

![Admin Editor - Add Answer - Duplicate Title](./doc/screenshots/admin-editor-answer-duplicate-1.webp)

![Admin Editor - Submit Answer - Duplicate Title](./doc/screenshots/admin-editor-answer-duplicate-2.webp)

### XBasic Intro Page

As a new or existing programmer I can read a brief desciption of the 
XBasic PDE and Language in order to get an overview.

Acceptance Criteria

There is an introductory panel describing the site

![XBasic Site Introduction](./doc/screenshots/xb-intro-1.webp)

The opening page has a brief description of the XBasic system.

There is a screenshot of the PDE and console on the opening page

There is a screenshot example of some code which has been run

It should be clear what environments the language will operate in

There is a description of file handling capabilities

There is a description of database handling capabilities

There is a brief description of the GUI toolkit

![XBasic - General Introduction](./doc/screenshots/xb-intro-2.webp)


### GUI Design

As an existing programmer I can refer to a description of the GUI toolkit in order to determine
whether XBasic is suitable for my requirements

Acceptance Criteria:

GUI toolkit description and screenshots on own page

![GUI Design Intro](./doc/screenshots/gui-design-1.webp)

![GUI Design Code](./doc/screenshots/gui-design-2.webp)

### Language Features - Language page

As a user I can read a summary description of language features in order to gain more insight

Acceptance Criteria:

On a separate page there is a summary description of key language features

The description has associated screenshots

![Language - Data Types](./doc/screenshots/language-1.webp)

![Language - Program Structure](./doc/screenshots/language-2.webp)

### Built-in Functions - Functions Page

As a user I can read about built-in functions in order to gain more insight into language features

Acceptance Criteria

On a separate page there is a summary description of built-in functions

![Functions Page](./doc/screenshots/functions-1.webp)

### Debugging Features - Debugging Page

As a user I can read a description of debugging features in order to know about ease of coding

Acceptance Criteria:

On a separate page there is a summary description of debugging features

Debugging description is supported by screenshots

![Debugging - Compile Time Errors](./doc/screenshots/debugging-1.webp)

![Debugging - Runtime Errors](./doc/screenshots/debugging-2.webp)

### Issue Pages

As a user, I can discuss/read about issues and problems with XBasic, in order to further 
	my understanding or help to resolve a problem

Acceptance Criteria:

Error and problem discussion page/database

By default, the issue page presents the most recent issue

Issues can be scrolled through in date or search rank order

The problem page has a search input field at the top

There are next and previous buttons on the reply area

![Issue Page - start of set](./doc/screenshots/issue-page-1.webp)

![Issue Page - end of set](./doc/screenshots/issue-page-2.webp)

The search is conducted by description, title or keywords

![Issue Page - search 1](./doc/screenshots/issue-page-search-1.webp)

![Issue Page - search 2](./doc/screenshots/issue-page-search-2.webp)

When no user is logged-in an options message is displayed

![Issue Page - No Login](./doc/screenshots/issue-page-no-login.webp)

When a user's issue is displayed, the new and edit options are available

![Issue Page - User's issue](./doc/screenshots/issue-page-user-issue.webp)

When another user's issue is displayed, only the new option is available

![Issue Page - Different User](./doc/screenshots/issue-page-user-logged-in-1.webp)

When the user is an administrator the New, Edit and Delete buttons are available

![Issue Page - Admin Logged In](./doc/screenshots/issue-page-admin-logged-in.webp)

Add Issue:

As a user, I can raise an issue, in order to ask for help in resolving my problem/issue

Acceptance Criteria:

On the issues page there is an new issue button

![New Issue - New Button](./doc/screenshots/new-issue-1.webp)

When the user clicks on the new issue button a form area is presented, ready to enter text into 

When the new Issue button is clicked, the user is required to enter a title

When the user clicks the new Issue button, he is presented with a keywords field
along with the other fields.

The issue entry layout includes a feature to select an image using a file system browser

![New Issue - entry page](./doc/screenshots/new-issue-2.webp)

Images are recorded along with the issue description

The user is returned to the issues page after a submit, with the entry showing

A message appears at the top of the screen to indicate an issue added

![New Issue - issue added](./doc/screenshots/new-issue-3.webp)

Data Tests:

Title Left Blank

Focus is set on title field and hover message appears

![New Issue - title left blank](./doc/screenshots/new-issue-title-blank.webp)

Title Duplicated
![New Issue - title duplicated](./doc/screenshots/new-issue-duplicate-title.webp)

Edit Issue:

As an Owner/Administrator I can edit issues so that they conform to standards

Acceptance Criteria

If the user is an owner/administrator an edit button appears on an issue

![Edit Issue - edit facility](./doc/screenshots/edit-issue-1.webp)

Clicking the edit button enables editing of the current issue

When the edit button is clicked a submit button appears in the issue area

![Edit Issue - edit page](./doc/screenshots/edit-issue-2.webp)

The user is returned to the issue page with entry after an edit

A success message appears toward the top of the page

![Edit Issue - edit completed](./doc/screenshots/edit-issue-3.webp)

Data Tests

Image Deleted

![Edit Issue - image delete - clear](./doc/screenshots/edit-issue-image-deleted-1.webp)

![Edit Issue - image deleted](./doc/screenshots/edit-issue-image-deleted-2.webp)

Image Replaced

![Edit Issue - image replaced - page](./doc/screenshots/edit-issue-image-replaced-1.webp)

![Edit Issue - image replace - completed](./doc/screenshots/edit-issue-image-replaced-2.webp)

Title Blank

Focus set on title, hover message appears

![Edit Issue - title left blank](./doc/screenshots/edit-issue-title-left-blank.webp)

Title Duplicated

![Edit Issue - duplicate title](./doc/screenshots/edit-issue-title-duplicated.webp)

Delete Issue

As an Owner/Administrator, I can delete an issue, in order to remove unnecessary or offensive issues

Acceptance Criteria

![Delete Issue - delete option available](./doc/screenshots/delete-issue-1.webp)

There should be a confirmation before the delete is executed

![Delete Issue - confirmation](./doc/screenshots/delete-issue-2.webp)

There should be a message after the delete

![Delete Issue - message](./doc/screenshots/delete-issue-3.webp)

### Answers

Answer Edit Options Availability:

If user is super-user/owner/administrator

No Answers

Options: New

![No Answers](./doc/screenshots/answer-opts-owner-no-answers.webp)

Otherwise
                    
Options: New, Edit, Delete

![Has Answer](./doc/screenshots/answer-opts-owner-has-answer.webp)

Else If general user

No Answers:

Options: New

![General User - no answer](./doc/screenshots/answer-opts-gen-user-no-answers.webp)

If the user is the author:

Options: New, Edit

![General User - answer author](./doc/screenshots/answer-opts-gen-user-author-answer.webp)

If the user is NOT the author:

![General User - not author](./doc/screenshots/answer-opts-gen-user-not-author.webp)

Options: New

Else (NOT logged-in)

Options: None
                
Message to indicate how to add

![No User Logged-in - message](./doc/screenshots/answer-opts-no-user-1.webp)

![No User Logged-in - no answers](./doc/screenshots/answer-opts-no-user-2.webp)

![No User Logged-in - has answers](./doc/screenshots/answer-opts-no-user-3.webp)

Add Answer

As a logged-in user I can add a reply to an issue in order to inform other users and participate

Acceptance Criteria

There is a New button on the issues area, which raises an Answer entry form
on the issues page

The layout of the Answer form is very similar to the issue form

![Add Answer - form](./doc/screenshots/add-answer-1.webp)

When the new answer is submitted, the user is returned to the issues page with
the issue and answer displayed

A message appears when the form is successfully submitted

![Add Answer - submitted message](./doc/screenshots/add-answer-2.webp)

![Add Answer - page presented](./doc/screenshots/add-answer-3.webp)

Data Tests:
	
title blank

The focus is set on the title, with a hover message displayed

![Add Answer - title blank](./doc/screenshots/add-answer-title-blank.webp)

title duplicated

![Add Answer - title duplicated](./doc/screenshots/add-answer-duplicate-title.webp)

Edit Answer:

As an Administrator or the author I can edit answers so that they conform to standards

Acceptance Criteria:

If the user is an owner/administrator an edit button appears above the answer

![Edit Answer - Edit Button](./doc/screenshots/edit-answer-1.webp)

Clicking the edit button enables editing of the current answer

![Edit Answer - Edit Answer Page Top](./doc/screenshots/edit-answer-2.webp)

![Edit Answer - Edit Answer Page Form](./doc/screenshots/edit-answer-3.webp)

When the submit button is clicked the user is returned to the issues page with the 
appropriate issue and answer displayed

When the record is added a message appears on the relevant issues page

![Edit Answer - Submitted - Issue Page](./doc/screenshots/edit-answer-4.webp)

![Edit Answer - Submitted - Issue Page Answer](./doc/screenshots/edit-answer-5.webp)

Data Tests:

title blank

message appears in hover text with the focus on title

![Edit Answer - Title Blank](./doc/screenshots/edit-answer-title-blank.webp)

title duplicated

![Edit Answer - Title Duplicated](./doc/screenshots/edit-answer-title-duplicated.webp)

Delete Answers

As an Administrator I can delete answers in order to maintain standards

Acceptance Criteria:

![Delete Answer - Delete Button](./doc/screenshots/delete-answer-1.webp)

Clicking the delete button on the answer form of the issues page causes
the confirm option to appear

![Delete Answer - User Confirmation](./doc/screenshots/delete-answer-2.webp)

Once the deletion has been confirmed the answer record is deleted

When an answer deletion is done a message appears at the top of the page

![Delete Answer - Completed](./doc/screenshots/delete-answer-3.webp)

When an answer deletion is done the issue page displays the current issue

