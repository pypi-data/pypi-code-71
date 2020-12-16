# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['linear', 'linear.management.commands', 'linear.migrations']

package_data = \
{'': ['*'], 'linear': ['templates/admin/linear/*']}

install_requires = \
['django>=3.0,<4.0', 'requests']

setup_kwargs = {
    'name': 'django-linear',
    'version': '0.1.0',
    'description': 'Django app for importing Linear issues into the Django admin site.',
    'long_description': '# Django Linear\n\nReadonly access to Linear issues for users without a Linear account.\n\nThis app is designed to enable \'readonly\' user access to Linear issues via the Django admin site.\n\n### Motivation\n\nWe replaced our use of Jira with Linear a while back, and haven\'t looked back. However, one thing\nthat would improve it for our use case (small dev / design team, with many engaged internal\nstakeholders) would be the ability to share the status of issues more widely through the company.\n\nThis doesn\'t need to be sophisticated, we don\'t need to accept edits / comments - it\'s just a status\nupdate - for any issue, who is working on it, what its status is, which cycle / project it is part\nof.\n\n### Why bother?\n\nThe existing Google Sheets integration is almost good enough - but having the data in Django means\nwe can build additional functionality on top (custom notifications, alerts, reporting, etc.)\n\nThat said - this project is mainly an excuse to explore the GraphQL API.\n\n### Approach\n\nWe have a large "backoffice" project written in Django, and all our internal staff have accounts set\nup, and know their way around the Django admin site. Linear has a GraphQL API. Putting these two\ntogether, it ought to be simple to sync Linear updates to a Django model, and to surface those via\nthe admin site.\n\n![Screenshot of admin site](https://raw.githubusercontent.com/yunojuno/django-linear/master/screenshots/issue-list-view.png)\n\n### Principles\n\n1. Access is managed via existing Django authentication\n1. Data is readonly - if someone needs to edit an issue they should use Linear\n1. Users who require access to Linear should have a full ($) account\n\nNB this is **not** a tool to bypass Linear fees. Please respect their hard work.\n\n### How it works\n\nThe integration between Linear and the app occurs in two ways - via bulk import, and via webhook.\nThe data is readonly, so the principal is that all issues are imported once from Linear, and then\nmaintained via the webhook whenever they are updated. The webhook handler will pick up new Issues\ncreated after the import.\n\nThe integration doesn\'t go too deep into the data - we store the basics only - this is only intended\nfor use as simple dashboard for people who don\'t have / need access to Linear itself.\n\nYou can import the issues via the admin site itself (there is no "Add Linear issue" button), or if\nyou wish you can run the `import_issues` management command. If you don\'t have too many issues you\ncould even run the import on a schedule - start afresh each day.\n\n### Configuration\n\nIt\'s a standard Django app, so add it to `INSTALLED_APPS` as you would any other. The webhook URL is\n`/webook/`, so the recommended configuration is to add it to your main `urls.py` like this, making\nthe full url `/linear/webhook/`:\n\n```python\nurlpatterns = [\n    path("linear/", include("linear.urls")),\n]\n```\n\nYou should use this URL (with your fully-qualified domain name) when adding the webhook to Linear.\n\n#### Settings\n\nThe following Django settings are available:\n\n`LINEAR_API_KEY`\n\nThe only setting that is required is a valid API key, which is available from the Linear app, under\n"Workspace settings" > "API" > "Personal API keys".\n\n`LINEAR_API_PAGE_SIZE`\n\nThe page size to use when importing issues - defaults to 100, the max allowed by the API is 250.\n\n`LINEAR_WORKSPACE_NAME`\n\nYour workspace name is optional, but it is used in the admin site to provide a link from the object\npage to Linear - overriding the Django "View on site" link.\n',
    'author': 'YunoJuno',
    'author_email': 'code@yunojuno.com',
    'maintainer': 'YunoJuno',
    'maintainer_email': 'code@yunojuno.com',
    'url': 'https://github.com/yunojuno/django-linear',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
