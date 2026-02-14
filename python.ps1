# python.ps1
while ($true) {
    # Ensure that all packages are installed and updated
    py -m pip install --upgrade pip ruff tco customtkinter
    
    # Run Ruff Formatting and Linting on the current directory
    py -m ruff format .
    py -m ruff check --fix .
    
    # Wait for 1 hour
    Write-Host "Ruff completed at $(Get-Date). Waiting 1 hour..."
    Start-Sleep -Seconds 3600
}