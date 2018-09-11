import re

JIRA_PROJECTS = (
    "JIRA-",
    "ES-",
)

issue_key_regex = re.compile("(%s)(\d+)" % ("|".join(JIRA_PROJECTS)))


def reposetup(ui, repo):

    class jirarepo(repo.__class__):
        """
        Automatically adds the Jira issue key to a
        commit message if not present already.

        To install
         - Place this file into your ./hg/ directory
         - Maybe edit the JIRA_PROJECTS tuple and add your Jira project key
         - Update your .hg/hgrc and add these lines :

            [extensions]
            jiraissue = ./.hg/jira_issue_hook.py

        """
        def commit(self, text, *args, **kwargs):
            branch_name = repo.dirstate.branch()
            has_bugid = issue_key_regex.match(text) is not None
            match = issue_key_regex.match(branch_name)
            if not has_bugid and match and len(match.groups()) > 1:
                issue_id = "".join(match.groups()[:2])
                text = " ".join([issue_id, text])
            return super(jirarepo, self).commit(text, *args, **kwargs)

    repo.__class__ = jirarepo


cmdtables = {}
