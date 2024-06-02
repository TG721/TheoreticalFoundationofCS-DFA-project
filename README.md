# TheoreticalFoundationofCS-DFA-project
The Program uses tkinter GUI and through input information it builds diagram of DFA and also has functionality to check input string on acceptance


## input example

Enter states: q0 q1 q2 d

Enter input symbols: 0 1

Enter transitions:

q0 0 d
q0 1 q1
q1 0 q2
q1 1 q1
q2 0 q2
q2 1 q1
d 0 d
d 1 d
Enter initial state: q0

Enter final states: q2

As you can see, inputs need to be written in the style provided in the example above. States and symbols must be separated by spaces. In transitions, each line of input represents the transition for the first state in the line. For example, q0 takes 0 and goes to the d state. When q0 takes an input of 1, it goes to the q1 state. In this example, there is only one final state; however, we can input more final states by simply separating them with spaces.

After clicking the build button, a PDF file of the visualized diagram will pop up. Then, in 'Enter Input string,' we can type the input string and check if the inputted string is accepted by the built DFA or not by clicking the check button.
## Screenshot

<img width="359" alt="screenshot" src="https://user-images.githubusercontent.com/85778941/211063314-71242293-fe5c-49a1-94dc-b5e9d8e7b37d.png">
