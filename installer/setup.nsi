Name "Hello PyWinSparkle Updater"
OutFile "hello_pywinsparkle_setup.exe"
RequestExecutionLevel user
InstallDir $APPDATA\hello_pywinsparkle

Section
  SetOutPath $INSTDIR
  nsExec::Exec 'cmd /c taskkill /F /IM hello_pywinsparkle.exe'
  File ..\dist\hello_pywinsparkle.exe
  ;File /r *.*
  nsExec::Exec /TIMEOUT=10 $INSTDIR\hello_pywinsparkle.exe
SectionEnd