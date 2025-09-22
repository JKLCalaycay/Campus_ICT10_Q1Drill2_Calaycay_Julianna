from pyscript import document, display

def getting_info (e): #e for COMPUTATION
    Name = str(document.getElementById("name1").value)
    Age = str(document.getElementById("age2").value)
    School = str(document.getElementById("school3").value)

    display(f"""Student information: 
        \tName: {Name}. 
        \nAge: {Age} years old. 
        \nCampus: {School} campus.""", target="message")
   
