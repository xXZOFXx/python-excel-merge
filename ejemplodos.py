# importing the module
import pandas

# reading the files
f1 = pandas.read_excel("registro.xlsx")
f2 = pandas.read_excel("examresults.xlsx")

# merging the files
f3 = f1[["REGISTRATION NO",
		"STUDENT EMAIL ID "]].merge(f2[["REGISTRATION NO",
										"Name", "Marks Obtained",
										"Percentage"]],
									on = "REGISTRATION NO",
									how = "left")

# creating a new file
f3.to_excel("Results.xlsx", index = False)
