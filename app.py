
import github
import redis

import os
from collections import defaultdict
# TODO - think of cron jobs too if its cheaper
class Github:
    # fixme - parametrize reop
    # fixme - make token private?
    # TODO - singleton github client
    # TODO - filter issues based on not stores or newly created
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
    def getIssues(self):
        '''
        :param
        :return: None
        '''
        self.issues = self.repo.get_issues(state="open")  # Retrieve open issues

    def getLables(self):
        '''
        :return: None
        '''
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

class Scheduler:
    # TODO - install Airflow
    # TODO - intigrate DAG into this to schedule jobs and call all other class objects in this
    # TODO - add this a seperate file

    def __int__(self):
        pass

class Database:
    # TODO - fix the function to save data accoring to the format I have
    # TODO - add functions to query the db
    def __init__(self, host, port):
        '''
        :param host:address of the db
        :param port: post of the db
        '''
        self.redis_client = redis.Redis(host=host, port=port)

    def store_issue(self, issue_id, issue_data):
        key = f"issue_{issue_id}"
        self.redis_client.set(key, issue_data)


if __name__=="__main__":
    # gitObj = Github()
    # # gitObj.getIssues()
    # gitObj.getLables()
    redisDB = Database('localhost', '7979')
    redisDB.store_issue('1234', 'test')