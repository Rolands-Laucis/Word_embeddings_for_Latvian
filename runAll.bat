::runAll.bat
@echo off

::echo training all models 5 200...
::call trainAllModels.bat 5 200

::echo training all models 5 300...
::call trainAllModels.bat 5 300

::echo training all models 5 350...
::call trainAllModels.bat 5 350

echo evaluating all models 5 200
call analogyEval.bat 5 200 3cosmul

echo evaluating all models 5 300
call analogyEval.bat 5 300 3cosmul

echo evaluating all models 5 350
call analogyEval.bat 5 350 3cosmul

pause