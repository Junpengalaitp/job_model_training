from bs4 import BeautifulSoup


def clean_html_tags(job):
    desc_soup = BeautifulSoup(job['job_desc'], 'html.parser')
    cleaned_desc = desc_soup.get_text()
    job['job_desc'] = cleaned_desc


def clean_text(job):
    if 'description' in job:
        job['description'] = job['description'].replace('\n', ' ')
    if 'job_desc' in job:
        job['job_desc'] = job['job_desc'].replace('\\n', ' ')

