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

omit password

poor password

valid

Login:

omit username

invalid username

omit password

invalid password
