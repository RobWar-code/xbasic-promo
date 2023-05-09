# xbasic-promo

## Introduction

This site provides the source and documentation for a website that
provides an introduction to the programming language and Program 
Development Environment (PDE) XBasic and an issue/problem reporting
reporting page for additional user support.

## Target Audience

The website is intended for programmers, both novice and established
to allow them access to the information required to make a decision
on choosing the XBasic programming language.

Additionally, the site provides for existing users to discuss issues
arising from their work.

## Development Methodology
Following from the UXD approach to design, the requirements are
established as a set of user stories and maintained as a list
in the Github issues set-up for project management.

Although the development approach is basically a Waterfall approach in the
sense that most of the design is done in advance, 
it borrows from the Agile approach, in terms of staging of work in order of priority, 
so that the project has flexible scope rather than trying to skip the deadlines for a 
completed work. 

The initial analysis has been conducted in [Project Analysis](/doc/project-analysis.txt).
High-level time recording and estimating is also maintained in this file.

Project Requirement items are listed in the project plan on GitHub 
xbasic-promo. [Project Planner](https://github.com/users/RobWar-code/projects/4)

Tasks in relation to user stories and other aspects of project work are recorded in
[Work Log](/doc/work-log.txt)

## Systems Tests

Systems Tests are in the file [SYSTEM_TESTS.md](./SYSTEMS_TESTS.md)

## Media Tests

Media Tests are in the file [MEDIA_TESTS.md](./SYSTEMS_TESTS.md)

## Code Quality Tests

### Python Quality
Using https://pep8ci.herokuapp.com

xb-promo/admin.py

![admin.py](./doc/code-test-shots/admin-py-test.png)

xb-promo/forms.py

![forms.py](./doc/code-test-shots/forms-py-test.png)

xb-promo/models.py

![models.py](./doc/code-test-shots/models-py-test.png)

xb-promo/views.py

![models.py](./doc/code-test-shots/views-py-test.png)

### CSS Code
Using: https://jigsaw.w3.org/css-validator/#validate_by_input

/static/css/style.css

![style.css](./doc/code-test-shots/style-css-test.png)

### HTML Templates
Using djlint (pip install djlint), djlint file-path --lint

templates directory

answer_panel

Note that the width for the image is set as 100% in the css file

![Answer Panel Test](./doc/code-test-shots/answer-panel-html-test.webp)

base

The duplicate attribute is a repeated href used also for the title logo

![djlint base.html](./doc/code-test-shots/base-html-test.webp)

edit_answer

The apparently orphan form tag is a part of a template
conditional if .. else

![djlint edit_answer.html](./doc/code-test-shots/edit-answer-html-test.webp)

edit_issue

The apparently orphan form tag is a part of a template
conditional if .. else

![djlint edit_issue.html](./doc/code-test-shots/edit-issue-html-test.webp)

index

![djlint index.html](./doc/code-test-shots/index-html-test.webp)

issue_control

![djlint issue_control.html](./doc/code-test-shots/issue-control-html-test.webp)

issue_panel

![djlint issue_panel.html](./doc/code-test-shots/issue-panel-html-test.webp)

issues

![djlint issues.html](./doc/code-test-shots/issues-html-test.webp)

## Errors / Bug Reports

### Due:
Problem: Admin Pages - Summernote editor fails to work once 
used elsewhere in site - needs investigation

Status: Ongoing

Priority: Medium

Temp fix - just use text editing on the content fields

Could be due to a dual reference to the summernote library in different modules

--------------------------
Problem: Admin Pages, Add Issue - Search Vector field not updated

Status: Ongoing

Priority: Low

When the entry is updated the search vector field IS updated.

### Fixed

Problem: Admin Pages, Model Data Editing:

Status: Fixed

The summernote presentation of the textfields had ceased to work after summernote
was used on the issues and answers pages. This may be a library usage problem.

Solution:

Withdraw the summernote presentation on the admin pages.

----------------------

Problem: Image not saved with add/edit issue and add/edit answer

Status: Fixed

Priority: High

The problem was caused by the cloudinary image field not being updated/connected
to the site using the ModelForm. This has to be done explicitly.

            # Upload the file to Cloudinary
            uploaded_file = cloudinary.uploader.\
                upload(request.FILES['screenshot_img'])

            # Assign the Cloudinary URL to the `image` field of the `Issue`
            # model instance
            instance.screenshot_img = uploaded_file['url']


-----------------
Problem: Add/Edit Issue - The submit button is too small for the text on small screens

Status: Fixed

Priority: High

Submit button div set to col-4 col-lg-2
------------------
Problem: Edit Issue Page - No error message reported to user when duplicate title field
submitted

Status: Fixed

It was necessary to detect the form error explicitly in the invalid form section
of the IssueEdit view:

message_text = issue_form.errors.get('title', None)

messages.warning(request, message_text)
 
------------------

Problem: Add Answer/Edit Answer - Image not uploaded

Status: Fixed

Priority: high

This is the same as the problem as it appeared in the issue form.
In this case solved by adding 

enctype="multipart/form-data"

to the template.
---------------------
Problem: Add Answer, When Title Duplicated - no message

Status: Fixed

Priority: High

Message displayed as warning
-------------------

Problem: Admin Pages, Delete Feature Section - Title not displayed on confirmation

Status: Fixed

Priority: Medium

The model FeatureSection required the function

def __str__(self):
    return self.title

![Admin Editor - Delete Section Confirmation](./doc/screenshots/admin-editor-debug-section-delete.webp)
--------------------
