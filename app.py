# coronasafe/care

# import sanic
# import sqlalchemy
#TO-DO: store token in env file
#TO-DO: organize code to find the certain bug label
#TO-DO: store the data
#TO-DO: schedule tasks
import github
import os
from collections import defaultdict
# github entity to access repo
    # find issues by label
    #
class Github:
    def __init__(self, repoPath=None):
        token = os.environ['GITHUB_TOKEN']
        github_client = github.Github(token)
        self.repo = github_client.get_repo("coronasafe/care")  # Replace with owner/repo name

    '''
    title(str), number(int)
    id(int): The GitHub - assigned ID for the issue(unique across all repositories). html_url(str): The URL of the issue on GitHub.
    body(str):, state(str): The current state of the issue(e.g., "open", "closed").
    created_at(datetime bject), updated_at(datetime object), closed_at(datetime object or None), assignee(User object or None), milestone(Milestone object or None), labels(list of Label objects):
    '''
    def getIssues(self, label='good_first_issue'):
        self.issues = self.repo.get_issues(state="open")  # Retrieve open issues

    def getLables(self):
        self.getIssues()
        issue_data = defaultdict(list)
        for issue in self.issues:
            issue_info = {
                "title": issue.title,
                "html_url": issue.html_url,
                "created_at": issue.created_at
                # Add more attributes as needed (e.g., "created_at, "updated_at")
            }
            labels = [label.name for label in issue.labels]
            if len(labels) == 0:
                issue_data['unlabled'].append(issue_info)
            for l in labels:
                issue_data[l].append(issue_info)
        print(issue_data.keys())

if __name__=="__main__":
    gitObj = Github()
    # gitObj.getIssues()
    gitObj.getLables()