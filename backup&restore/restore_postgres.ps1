# Ruta al archivo .env
$envPath = "..\.env"

# Leer .env y establecer variables de entorno
Get-Content $envPath | ForEach-Object {
    if ($_ -match "^\s*([^#][^=]+)\s*=\s*(.+)$") {
        $key = $matches[1].Trim()
        $value = $matches[2].Trim().Trim("'").Trim('"')
        [System.Environment]::SetEnvironmentVariable($key, $value, "Process")
    }
}

# Pedir al usuario el nombre del archivo .sql
do {
    $filename = Read-Host "Ingresa el nombre del archivo .sql (ej: backup_20250722_1643.sql)"
    $backupFile = "C:\backups-basededatos\$filename"

    if (!(Test-Path -Path $backupFile)) {
        Write-Host "ERROR: El archivo '$filename' no existe en C:\backups-basededatos\" -ForegroundColor Red
    }
} while (!(Test-Path -Path $backupFile))

# Confirmar restauración
Write-Host "Restaurando la base de datos '$($env:POSTGRES_DB)' desde '$backupFile'..."

# Ejecutar restauración lógica
Get-Content $backupFile | docker exec -i grupo-6-db-1 psql -U $env:POSTGRES_USER -d $env:POSTGRES_DB

Write-Host "Restauración completada correctamente." -ForegroundColor Green
