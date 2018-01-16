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
@set _HS_HOME=%_HS_HOME:~-7%
@if "%1"=="debug" (
    echo on
    shift
    set _debug=debug
) else (
    echo off
    set _debug=
)

:: init variables
set _op=venv

:: get some argument
:label_getopt
if /i "%1"=="help" (
    goto label_help
) else if /i "%1"=="venv" (
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
echo Error! Target %_op% is not supported.
goto label_end

:label_venv
if "%VIRTUAL_ENV%"=="%_HS_HOME%\venv" (echo Already in venv.) & goto label_end
call denv py 2
if exist "venv" goto label_venv_activate
virtualenv venv
:label_venv_activate
call venv\Scripts\activate.bat
goto label_end

:label_start
goto label_end

:label_help
:: print help message
@echo Usage: %batch_name% [TARGET] [OPTION...]
@echo    Build LabManager project and copy files to local shared directory
@echo    Note: Appropriate dev environment needs to be setup before use.
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

