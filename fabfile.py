from fabric.api import runs_once, lcd, local, task

@task
@runs_once
def register_deployment(git_path):
    with(lcd(git_path)):
        revision = local('git log -n 1 --pretty="format:%H"', capture=True)
        branch = local('git rev-parse --abbrev-ref HEAD', capture=True)
        local('curl https://intake.opbeat.com/api/v1/organizations/05436e12b988423f8cfde74512dbfd78/apps/5743335261/releases/'
              ' -H "Authorization: Bearer b0fdba56b0243d6959d5b866bfe845bc9b8ffbf1"'
              ' -d rev="{}"'
              ' -d branch="{}"'
              ' -d status=completed'.format(revision, branch))