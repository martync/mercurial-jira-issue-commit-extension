# mercurial-jira-issue-commit-extension
Automatically adds the Jira issue key on a hg commit if not present already.

Installation
------------

* Place this file into your ./hg/ directory
* Maybe edit the `JIRA_PROJECTS` tuple and add your Jira project key
* Update your .hg/hgrc and add these lines :

```
[extensions]
jiraissue = ./.hg/jira_issue_hook.py
```
