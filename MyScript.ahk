^g::
 MouseGetPos, xpos, ypos, win
Loop, 46
{
Click %xpos% %ypos%
Send, {Backspace}{Backspace}%A_Index%{Enter}
Send, ^s 
sleep, 500
Send, Results %A_Index% {Enter}
sleep, 250
Send, {Enter}
sleep, 250
WinActivate, %win%
}
Esc::ExitApp