"""The CI shell scripts, run against throwaway git repos (a bare 'remote' stands in for GitHub)."""
import shutil
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
DATE = "2026-10-10"


def git(cwd, *args):
    return subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True, text=True).stdout.strip()


@pytest.fixture
def repo(tmp_path):
    remote, work = tmp_path / "remote.git", tmp_path / "work"
    git(tmp_path, "init", "-q", "--bare", "-b", "main", str(remote))
    git(tmp_path, "clone", "-q", str(remote), str(work))
    (work / "bin").mkdir()
    for f in ("ci-finish", "ci-paused"):
        shutil.copy(ROOT / "bin" / f, work / "bin" / f)
    (work / "portfolio").mkdir()
    (work / "portfolio" / "state.json").write_text('{"cash_usd": 100000}')
    (work / "portfolio" / "ledger.csv").write_text("date\n")
    git(work, "add", "-A")
    git(work, "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "-m", "init")
    git(work, "push", "-q", "origin", "main")
    return work, remote


def simulate_run(work, with_error_log=True):
    (work / "portfolio" / "state.json").write_text('{"cash_usd": 1}')           # a trade was applied
    (work / "portfolio" / "ledger.csv").write_text("date\n2026-10-10,X,BUY\n")
    (work / "research" / "X").mkdir(parents=True)
    (work / "research" / "X" / f"{DATE}.md").write_text("note")                  # new untracked file
    (work / "reports" / "weekly").mkdir(parents=True)
    (work / "reports" / "weekly" / f"{DATE}.md").write_text("report")
    if with_error_log:
        (work / "runs" / DATE).mkdir(parents=True)
        (work / "runs" / DATE / "error.log").write_text("Weekly run FAILED at step: decision log")


def finish(work, *args):
    return subprocess.run(["sh", "bin/ci-finish", *args], cwd=work, capture_output=True, text=True)


def test_success_commits_everything_with_message(repo):
    work, remote = repo
    simulate_run(work, with_error_log=False)
    r = finish(work, "success", "weekly", DATE)
    assert r.returncode == 0, r.stderr
    assert git(remote, "log", "-1", "--format=%s", "main") == f"Weekly run {DATE}"
    files = git(remote, "show", "--name-only", "--format=", "main").splitlines()
    assert set(files) == {"portfolio/state.json", "portfolio/ledger.csv", f"research/X/{DATE}.md",
                          f"reports/weekly/{DATE}.md"}


def test_failure_commits_only_error_log_and_fails(repo):
    work, remote = repo
    simulate_run(work)
    r = finish(work, "failure", "weekly", DATE)
    assert r.returncode == 1  # the run is marked failed
    assert git(remote, "log", "-1", "--format=%s", "main") == f"Weekly run {DATE} FAILED (error log only)"
    assert git(remote, "show", "--name-only", "--format=", "main").splitlines() == [f"runs/{DATE}/error.log"]
    # no trade from the run survives, locally or on the remote
    assert git(remote, "show", "main:portfolio/state.json") == '{"cash_usd": 100000}'
    assert (work / "portfolio" / "state.json").read_text() == '{"cash_usd": 100000}'
    assert not (work / "research" / "X").exists()
    assert "decision log" in git(remote, "show", f"main:runs/{DATE}/error.log")


def test_failure_before_run_log_still_commits_an_error_log(repo):
    work, remote = repo
    simulate_run(work, with_error_log=False)
    assert finish(work, "failure", "weekly", DATE).returncode == 1
    assert "FAILED before the run wrote its own log" in git(remote, "show", f"main:runs/{DATE}/error.log")


def test_paused(repo):
    work, _ = repo
    out = lambda: subprocess.run(["sh", "bin/ci-paused"], cwd=work, capture_output=True, text=True).stdout.strip()  # noqa: E731
    assert out() == "paused=false"
    (work / "PAUSED").write_text("")
    assert out() == "paused=true"


def test_workflows_wire_pause_failure_and_schedule():
    wf = (ROOT / ".github" / "workflows" / "weekly-review.yml").read_text()
    assert 'cron: "0 8 * * 6"' in wf and "contents: write" in wf and "group: paper-portfolio" in wf
    steps_after_pause = wf.split("bin/ci-paused", 1)[1]
    # every step after the pause check is skipped when paused
    assert steps_after_pause.count("- name:") + steps_after_pause.count("- uses:") == \
        steps_after_pause.count("steps.pause.outputs.paused != 'true'")
    assert "if: failure() && steps.pause.outputs.paused != 'true'" in wf and "bin/ci-finish failure weekly" in wf
    assert "ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}" in wf
    assert "CLAUDE_CODE_OAUTH_TOKEN: ${{ secrets.CLAUDE_CODE_OAUTH_TOKEN }}" in wf and "No ANTHROPIC_API_KEY or" in wf
    sc = (ROOT / ".github" / "workflows" / "screen.yml").read_text()
    assert "group: paper-portfolio" in sc and "bin/ci-finish failure screen" in sc
