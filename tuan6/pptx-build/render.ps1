param(
  [string]$File = "C:\Users\Admin\Desktop\baitap\tuan6\pptx-build\presentation.pptx",
  [string]$OutDir = "C:\Users\Admin\Desktop\baitap\tuan6\pptx-build\render"
)
$ErrorActionPreference = "Stop"
New-Item -ItemType Directory -Force -Path $OutDir | Out-Null
Get-ChildItem $OutDir -Filter "slide-*.png" -ErrorAction SilentlyContinue | Remove-Item -Force
$app = New-Object -ComObject PowerPoint.Application
try {
  $pres = $app.Presentations.Open($File, $true, $false, $false)
  $count = $pres.Slides.Count
  Write-Output "slides=$count"
  for ($i = 1; $i -le $count; $i++) {
    $name = Join-Path $OutDir ("slide-{0:D2}.png" -f $i)
    $pres.Slides.Item($i).Export($name, "PNG", 1920, 1080)
  }
  $pres.Close()
  Write-Output "exported=$count"
} finally {
  $app.Quit()
  [System.Runtime.InteropServices.Marshal]::ReleaseComObject($app) | Out-Null
}
