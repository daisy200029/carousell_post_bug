
# carousell_post_bug
Use JIRA API to post bugs and user story.Ｔo start with:
1. Ｎeed jira name and jira password. If you forget JIRA password, you can go to jira to reset password.(Note: this password is not gmail password)
https://id.atlassian.com/login/resetpassword?email=daisy.liu%40thecarousell.com
and it will send email with reset password link.
2. You put photos you want to upload on your desktop
3. start script with >>python main.py


In bug.txt each ticket contains 4  mandatoryparts, @des, @assignee, @summary, @photos
If this ticket does not need to upload photo, this ticekt should specify like this -->

>>@photos

>>NULL

If this ticket need to upload two photos and make it merges to one , this ticekt should specify like this.

>>@photos

>>TEST1.PNG,TEST2.PNG

Then it will auto generate a merged one on desktop with file name "OUT.PNG". If this file already exists, it will name it "OUT-1.PNG" etc.. And then it will upload on the newly created ticket

So that we can start command as below and it will post bugs to CS project

>>create_bug {user_name} {password} CS bug.txt

or we can start command as below and it will post bugs to ISSUERPTS project

>>create_bug {user_name} {password} ISSUERPTS bug.txt

it will post bugs to ISSUERPTS project
