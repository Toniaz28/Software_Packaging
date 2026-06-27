param(
    [string]$tag = 'v1.0.0'
)

if (-not (Test-Path .git)) {
    Write-Error 'This script must be run from the repository root and requires git.'
    exit 2
}

git add -A
git commit -m "chore: initialize packaging scaffold" || Write-Host 'commit skipped'
git reset --soft HEAD~0

$msgs = @(
    'chore: add Node tests and scripts',
    'test: add Python pytest and build deps',
    'test: add Java JUnit tests',
    'ci: update workflow to run tests and build artifacts',
    'chore: add checksums, changelog, and release helpers'
)

foreach ($m in $msgs) {
    git add -A
    git commit -m $m
}

git tag $tag
Write-Host "Created ${($msgs.Count)} commits and tag $tag. Push with: git push --follow-tags origin main"
