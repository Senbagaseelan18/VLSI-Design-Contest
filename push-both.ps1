param(
  [string]$branch = "main"
)

Write-Host "Pushing branch $branch to origin..."
git push origin $branch
if ($LASTEXITCODE -ne 0) { Write-Error "push to origin failed"; exit $LASTEXITCODE }

Write-Host "Pushing branch $branch to senba..."
git push senba $branch
if ($LASTEXITCODE -ne 0) { Write-Warning "push to senba failed (check permissions)"; exit $LASTEXITCODE }

Write-Host "Done."
