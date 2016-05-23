# Collects issues and assorted information from a github page and return it in a Django-readable format
from github3 import login
from webapp import settings
from datetime import datetime
import os


def collect_issues():
    """
    :return: Tuple containing [0] open Issue and [1] closed Issue github3 objects.
    """
    gh = login(token=settings.GIT_TOKEN)  # Use your own GitAPI token here
    user = 'slin63'
    repo_name = 'django_NelsonDB'

    repo = gh.repository(user, repo_name)

    open_issues = []
    iterator_open = repo.iter_issues(state='open')
    [open_issues.append(issue) for issue in iterator_open.__iter__()]

    closed_issues = []
    iterator_closed = repo.iter_issues(state='closed', sort='closed')
    [closed_issues.append(issue) for issue in iterator_closed.__iter__()]

    issue_set = (open_issues, closed_issues[0:5])  # Only the last 5 closed issues

    return issue_set


def write_to_html(issue_set, output="issues.html"):
    """
    :param issue_set: Tuple containing Issue objects as generated by collect_issues.
    :return: Formatted .HTML file containing information about both closed and open Issue objects.
    """
    html_string = ''
    # Html header for open issues
    issue_open_header = """
        <!DOCTYPE html>
        <!-- GENERATED ON: {0} -->
        <ol>

        <div class="hero-unit">
            <h1>Current Changes and Issues:</h1>
        </div>

        <div class="bg-success" style="padding:15px">
            <ul>
        """.format(datetime.now())
    issue_open_body = generate_issue_html(issue_set[0])

    # Html header for closed issues
    issue_closed_header = """
        </br>
        <div class="hero-unit">
            <h1>Closed Changes and Issues:</h1>
        </div>

        <div class="bg-success" style="padding:15px">
            <ul>
        """
    issue_closed_body = generate_issue_html(issue_set[1])

    # Putting all the constructed HTML bits together
    html_string += issue_open_header + issue_open_body + \
        issue_closed_header + issue_closed_body

    # Outputting to our a newly opened html file
    html_file = open(output, "w")
    html_file.write(html_string)
    html_file.close()

    return html_string


def generate_issue_html(issue_list):
    """
    :param issue_list: A list of issues as generated by collect_issues().
    :return: An HTML formatted output containing a brief overview of the Issue's metadata.
    """
    html_string = ''

    for issue in issue_list:
        html_string += """
            <li> <h4> <a href={0.html_url}>{0.title}</a>
                <small>
                """.format(issue)
        if issue.labels:
            labels = []
            [labels.append(label.name.capitalize()) for label in issue.labels]
        else:
            html_string += "No labels!"
        html_string += """
                    - opened by <i><a href="https://github.com/{0.user}/">{0.user}</a></i>
                    on {0.created_at}
                </small>
            </h4>{1}</li>
            <hr>
        """.format(issue, issue.body_html.encode('utf-8'))

    # Html closers
    html_string += """
    </ul>
    </div>
    """

    return html_string


if __name__ == '__main__':
    issues = collect_issues()
    # Should return absolute path to output file
    html_output = os.path.dirname(os.path.abspath(__file__)) + '/templates/lab/index/issues.html'
    write_to_html(issues, html_output)


