# TheoreticalFoundationofCS-DFA-project
The Program uses tkinter GUI and through input information it builds diagram of DFA and also has functionality to check input string on acceptance


## input example

Enter states        q0 q1 q2 d
Enter input symbols 0 1
Enter transitions   q0 0 d 1 q1
                    q1 0 q2 1 q1
                    q2 0 q2 1 q1
                    d 0 d 1 d
Enter initial state q0
Enter final states  q2

as you can see inputs need to be written in the style as provided in the example above. states and symbols have to be separated by space.
in transations, each line of input represents transition for first state in the line input. q0 takes 0 and goes to d state when q0 takes input of 1 it goes to q1 state. in this example there is only 1 final state however we can input more final states by simply separating them with space.

after clicking build button PDF file of visulised diagram will pop up then in
'Enter Input string' we can type input string and check if the inputed string is accpted by built DFA or not by cliking on check button
