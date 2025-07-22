# Ruta al rchivo .env
$envPath = "..\.env"

# Lee el .env y crea las variables de entorno
Get-Content $envPath | ForEach-Object {
    if ($_ -match "^\s*([^#][^=]+)\s*=\s*(.+)$") {
        $key = $matches[1].Trim()
        $value = $matches[2].Trim().Trim("'").Trim('"')
        [System.Environment]::SetEnvironmentVariable($key, $value, "Process")
    }
}

$backupFolder = "C:\backups-basededatos"
if (!(Test-Path -Path $backupFolder)) {
    New-Item -ItemType Directory -Path $backupFolder | Out-Null
}

$fecha = Get-Date -Format "yyyyMMdd_HHmm"
$backupFile = "$backupFolder\backup_$fecha.sql"

docker exec grupo-6-db-1 pg_dump -U $env:POSTGRES_USER $env:POSTGRES_DB > $backupFile