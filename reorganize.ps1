# 🐍 PythonProgramsV3 - Reorganization Script
# Save this file as: reorganize.ps1 in your repo root
# Run from PowerShell: powershell -ExecutionPolicy Bypass -File reorganize.ps1

Write-Host "🚀 Starting PythonProgramsV3 Reorganization..." -ForegroundColor Green
Write-Host ""

# Get the current directory
$baseDir = Get-Location

# Step 1: Create new folder structure
Write-Host "📁 Creating new folder structure..." -ForegroundColor Cyan

$folders = @(
    'Games',
    'Math',
    'Utilities',
    'Validation',
    'Finance',
    'String_Processing',
    'Web_and_API',
    'Data_Analysis',
    'Conversions'
)

foreach ($folder in $folders) {
    $path = Join-Path $baseDir $folder
    if (-not (Test-Path $path)) {
        New-Item -ItemType Directory -Path $path | Out-Null
        Write-Host "✅ Created: $folder" -ForegroundColor Green
    } else {
        Write-Host "⏭️  Already exists: $folder" -ForegroundColor Yellow
    }
}

Write-Host ""
Write-Host "📋 Moving files to new categories..." -ForegroundColor Cyan
Write-Host ""

# Step 2: Define file movements
$moves = @(
    # Games
    @{ src = "Number\RollTheDice.py"; dst = "Games\RollTheDice.py" },
    @{ src = "Number\numbergame.py"; dst = "Games\numbergame.py" },
    @{ src = "Number\Monster_Duelz.py"; dst = "Games\Monster_Duelz.py" },
    @{ src = "Number\TerminalDriftGame.py"; dst = "Games\TerminalDriftGame.py" },
    @{ src = "Other Programs\TerminalQuizShowdown.py"; dst = "Games\TerminalQuizShowdown.py" },
    @{ src = "Other Programs\basketball.py"; dst = "Games\basketball.py" },
    @{ src = "Number\enhanced_snakes_and_ladders.py"; dst = "Games\enhanced_snakes_and_ladders.py" },
    @{ src = "Number\snakes_and_ladders_1p.py"; dst = "Games\snakes_and_ladders_1p.py" },
    @{ src = "Number\snakes_and_ladders_2p.py"; dst = "Games\snakes_and_ladders_2p.py" },
    
    # Math
    @{ src = "Number\Fibonacci.py"; dst = "Math\Fibonacci.py" },
    @{ src = "Number\DataTypes.py"; dst = "Math\DataTypes.py" },
    @{ src = "Number\times tables.py"; dst = "Math\times_tables.py" },
    @{ src = "Number\VolumeOfSphere.py"; dst = "Math\VolumeOfSphere.py" },
    @{ src = "Number\heart.py"; dst = "Math\heart.py" },
    @{ src = "Number\mathsquiz.py"; dst = "Math\mathsquiz.py" },
    
    # Finance
    @{ src = "Number\VAT.py"; dst = "Finance\VAT.py" },
    @{ src = "Number\discount.py"; dst = "Finance\discount.py" },
    @{ src = "Number\Waiter.py"; dst = "Finance\Waiter.py" },
    
    # Validation
    @{ src = "Number\Age.py"; dst = "Validation\Age.py" },
    @{ src = "Number\Month.py"; dst = "Validation\Month.py" },
    @{ src = "Number\YearGroups.py"; dst = "Validation\YearGroups.py" },
    @{ src = "Number\Hertz.py"; dst = "Validation\Hertz.py" },
    @{ src = "Other Programs\Name.py"; dst = "Validation\Name.py" },
    @{ src = "Other Programs\Security.py"; dst = "Validation\Security.py" },
    
    # String Processing
    @{ src = "Other Programs\Code.py"; dst = "String_Processing\Code.py" },
    @{ src = "Other Programs\Story.py"; dst = "String_Processing\Story.py" },
    
    # Utilities
    @{ src = "Number\time.py"; dst = "Utilities\time.py" },
    @{ src = "Number\Lucky.py"; dst = "Utilities\Lucky.py" },
    @{ src = "Number\float.py"; dst = "Utilities\float.py" },
    @{ src = "Number\FortuneTeller.py"; dst = "Utilities\FortuneTeller.py" },
    @{ src = "Number\heads vs tails.py"; dst = "Utilities\heads_vs_tails.py" }
)

# Step 3: Move files
$successCount = 0
$failCount = 0

foreach ($move in $moves) {
    $src = Join-Path $baseDir $move.src
    $dst = Join-Path $baseDir $move.dst
    
    if (Test-Path $src) {
        try {
            Move-Item -Path $src -Destination $dst -Force
            Write-Host "✅ Moved: $($move.src) → $($move.dst)" -ForegroundColor Green
            $successCount++
        } catch {
            Write-Host "❌ Failed to move: $($move.src)" -ForegroundColor Red
            Write-Host "   Error: $_" -ForegroundColor Red
            $failCount++
        }
    } else {
        Write-Host "⚠️  File not found: $($move.src)" -ForegroundColor Yellow
    }
}

Write-Host ""
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan

# Step 4: Rename files with spaces
Write-Host ""
Write-Host "🔄 Renaming files with spaces..." -ForegroundColor Cyan

$renames = @(
    @{ old = "Dice\Dice Part 2.py"; new = "Dice\Dice_Part_2.py" }
)

foreach ($rename in $renames) {
    $oldPath = Join-Path $baseDir $rename.old
    $newPath = Join-Path $baseDir $rename.new
    
    if (Test-Path $oldPath) {
        try {
            Move-Item -Path $oldPath -Destination $newPath -Force
            Write-Host "✅ Renamed: $($rename.old) → $($rename.new)" -ForegroundColor Green
            $successCount++
        } catch {
            Write-Host "⚠️  Could not rename: $($rename.old)" -ForegroundColor Yellow
        }
    }
}

Write-Host ""
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
Write-Host ""
Write-Host "📊 Summary:" -ForegroundColor Yellow
Write-Host "✅ Successfully moved: $successCount files" -ForegroundColor Green
Write-Host "⚠️  Failed/Not found: $failCount files" -ForegroundColor Red
Write-Host ""
Write-Host "🎉 Reorganization complete!" -ForegroundColor Green
Write-Host ""
Write-Host "📝 Next steps:" -ForegroundColor Cyan
Write-Host "1. Review the new structure with File Explorer"
Write-Host "2. Update README.md to reflect new structure"
Write-Host "3. Commit changes: git add . && git commit -m 'refactor: reorganize files into categories'"
Write-Host ""
Write-Host "Press Enter to exit..."
Read-Host
