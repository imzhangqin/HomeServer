::
:: DOS batch file
::    this script is used for running HomeServer
::
:: Author : Qin Zhang
:: Date   : 01/16/18
::
:: Release note:
:: V001  Initial version, 01/16/18
::
::

:: add script folder to PATH if not added already
@pushd \
@which %~n0 > nul 2>&1
@if %ERRORLEVEL% NEQ 0 set PATH=%PATH%;%~dp0
@popd

:: set local
@if "%OS%"=="Windows_NT" setlocal

@set batch_name=%~n0
@set _HS_HOME=%~dp0
@set _HS_HOME=%_HS_HOME:~0,-8%
@if "%1"=="debug" (
    echo on
    shift
    set _debug=debug
) else (
    echo off
    set _debug=
)

:: init variables
set _op=start

:: get some argument
:label_getopt
if /i "%1"=="help" (
    goto label_help
) else if /i "%1"=="venv" (
    set _op=%1
) else if /i "%1"=="start" (
    set _op=%1
) else if "%1"=="" (
   goto label_init_param
)
shift
goto label_getopt

:label_init_param
pushd %_HS_HOME%
if /i "%_op%"=="venv" goto label_venv
if /i "%_op%"=="start" goto label_start
echo Error: Operation %_op% is not supported.
goto label_end

:label_venv
if "%VIRTUAL_ENV%"=="%_HS_HOME%\venv" (echo Already in venv.) & goto label_venv_reqirements
call denv py 2
if exist "venv" goto label_venv_activate
:: create new venv
virtualenv venv
if %ERRORLEVEL% NEQ 0 (echo Error: Failed to create venv.) & goto label_end
call .\venv\Scripts\activate.bat
if /i "%USERDOMAIN%"=="BASLERDOM" (set _opt_proxy=--proxy 108.171.131.129:8080) else (set _opt_proxy=)
pip install %_opt_proxy% -r requirements.txt
goto label_end
:label_venv_activate
endlocal
call venv\Scripts\activate.bat
goto label_end
:label_venv_reqirements
pip freeze > requirements.txt
for /f %%p in ('git diff requirements.txt') do set _t=%%p
if not "%_t%"=="" echo Info: requirments.txt updated.
goto label_end

:label_start
python hs.py
goto label_end

:label_help
:: print help message
@echo Usage: %batch_name% [operation]
@echo    Script to help running home server.
@echo.
@echo    [operation:]
@echo       help    :   print this help message.
@echo       venv    :   Setup virtual enviroment.
@echo       start   :   Start server.
@echo.
@echo    Bug report to: imzhangqin@yahoo.com
@echo    Version : V001
goto label_end

:label_end
popd
if "%OS%"=="Windows_NT" endlocal

