::./runAll.bat
@echo off

echo training all models 5 200...
./trainAllModels.bat 5 200

echo training all models 5 300...
./trainAllModels.bat 5 200

echo training all models 5 350...
./trainAllModels.bat 5 350

echo evaluating all models 5 200
./analogyEval.bat 5 200 3cosmul

echo evaluating all models 5 300
./analogyEval.bat 5 300 3cosmul

echo evaluating all models 5 350
./analogyEval.bat 5 350 3cosmul