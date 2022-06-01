from github import Github
import datetime
from optparse import OptionParser

parser = OptionParser()
parser.add_option('--repo', dest='repo_name', help='Mandatory. Takes repo name')
parser.add_option('--token', dest='token', help='Mandatory. Takes github access token')
(options, args) = parser.parse_args()

class Github_Utils():
    def __init__(self, repo_name, token):
        self.repo_name = repo_name
        self.token = token
        self.current_datetime = datetime.datetime.now()
    
    def get_repo(self):
        g = Github(self.token)
        repo = g.get_repo(self.repo_name)
        return repo
    
    def get_open_pull_details(self, status): # status='open'/'closed'/'all'
        repo = self.get_repo()
        pulls = repo.get_pulls(state=status, sort='created')
        return pulls
    
    def print_pull_details(self, status):
        pulls = self.get_open_pull_details(status)
        for pull in pulls:
            title = pull.title
            num = pull.number
            days_open = (self.current_datetime - pull.created_at).days
            user = pull.user.login
            print(f'{title}\n#{num} created {days_open} days ago by {user}\n')
        

some_repo = Github_Utils(options.repo_name, options.token)
some_repo.print_pull_details('open')