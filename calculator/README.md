version:

markdown

# PowerShell Script for Creating a Scheduled Task

## Overview

This PowerShell script is designed to create a scheduled task in Windows that runs a specified PowerShell script weekly. The scheduled task will execute a script located at `C:\Users\mollo\OneDrive\Documents\Scripts\WindowsUpdates.ps1` every Sunday at 10:00 AM.

## Script Breakdown

### 1. Define the Action

```powershell
$Action = New-ScheduledTaskAction -Execute 'PowerShell.exe' -Argument '-File C:\Users\mollo\OneDrive\Documents\Scripts\WindowsUpdates.ps1'

    New-ScheduledTaskAction: This cmdlet creates an action for the scheduled task.
    -Execute: Specifies the program to run (in this case, PowerShell.exe).
    -Argument: Indicates the PowerShell script to be executed using -File followed by the script's full path.

2. Define the Trigger

powershell

$Trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Sunday -At 10:00AM

    New-ScheduledTaskTrigger: This cmdlet creates a trigger that specifies when the task should run.
    -Weekly: Indicates that the task will run on a weekly basis.
    -DaysOfWeek: Specifies the day(s) the task will run (in this case, Sunday).
    -At: Sets the exact time for the task to execute (10:00 AM).

3. Define the Settings

powershell

$Settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable -RunOnlyIfNetworkAvailable

    New-ScheduledTaskSettingsSet: Configures settings for the scheduled task.
    -AllowStartIfOnBatteries: The task can start even if the system is on battery power.
    -DontStopIfGoingOnBatteries: The task will continue running if the system switches to battery power.
    -StartWhenAvailable: If the scheduled time is missed (e.g., the computer was off), the task will start as soon as possible.

4. Combine Action, Trigger, and Settings

powershell

$Task = New-ScheduledTask -Action $Action -Trigger $Trigger -Settings $Settings

    New-ScheduledTask: Combines the previously defined action, trigger, and settings into a single task object.

5. Register the Scheduled Task

powershell

Register-ScheduledTask -TaskName 'Weekly Windows Updates' -InputObject $Task

    Register-ScheduledTask: Registers the new scheduled task in the Task Scheduler.
    -TaskName: Specifies the name of the scheduled task ("Weekly Windows Updates").
    -InputObject: Passes the task object created earlier to register it with the Task Scheduler.

Conclusion

This PowerShell script automates the process of creating a scheduled task that runs a specified script weekly. By using various cmdlets, the script sets up an action, a trigger, and appropriate settings, ensuring that the task runs reliably under specified conditions.
