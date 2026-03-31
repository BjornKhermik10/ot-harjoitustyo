from invoke import task
from sys import platform

@task
def coverage(ctx):
    ctx.run("coverage run -m pytest src/tests", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage report -m", pty=True)