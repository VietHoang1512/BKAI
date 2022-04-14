$files = @(Get-ChildItem -Path $PSScriptRoot -Recurse -Force -Include *.sh).fullname
$countSuccess = 0
foreach ($file in $files) {
    try {
        [IO.File]::WriteAllText($file, $([IO.File]::ReadAllText($file) -replace "`r`n", "`n"))
        $fileStatus = 'Fix ' + $file + ' done'
        echo $fileStatus
        $countSuccess += 1
    }
    catch {}
}
$finishStatus = 'Fix ' + $countSuccess + '/' + $files.Count + ' *.sh files in this directory and its subdirectories.'
echo $finishStatus
