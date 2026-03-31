from invoke import task
from sys import platform


@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)


@task
def test(ctx):
    ctx.run("pytest src/tests", pty=True)


@task
def coverage(ctx):
    ctx.run("coverage run -m pytest src/tests", pty=True)


@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)
    # tekoälyltä saatu idea
    if platform == "win32":
        ctx.run("start htmlcov/index.html", pty=True, warn=True)
    elif platform == "darwin":
        ctx.run("open htmlcov/index.html", pty=True, warn=True)
    else:
        ctx.run("xdg-open htmlcov/index.html", pty=True, warn=True)
    # tekoälyltä saatu idea loppuu