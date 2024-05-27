letter = " \n\nDear <NAME> \n\t We are informing you that \n\t your application for job \n\t is selected Congratulation! \n\t you sould report to the office on \n     <DATE>\n   H.R"
name = input("Enter the name of Candidate here:- ")
date = input("Enter the date in dd/mm/yyyy :- ")
letter = letter.replace("<NAME>",name)
letter = letter.replace("<DATE>",date)
print(letter)