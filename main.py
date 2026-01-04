from pyscript import display, document

def final_results(e):
    firstname = document.getElementById('firstname').value
    lastname = document.getElementById('lastname').value

    sci_unit = 5
    eng_unit = 5
    ict_unit = 2
    math_unit = 5
    fil_unit = 3
    pe_unit= 1

    science = float(document.getElementById('science').value)
    english = float(document.getElementById('english').value)
    ict = float(document.getElementById('ict').value)
    math = float(document.getElementById('math').value)
    filipino = float(document.getElementById('filipino').value)
    pe = float(document.getElementById('pe').value)

    total_units = 21

    gwa = (
        (science * sci_unit) + 
        (english * eng_unit) + 
        (ict * ict_unit) + 
        (math * math_unit) + 
        (filipino * fil_unit) + 
        (pe * pe_unit)
        ) / total_units

    display(f'Name: {firstname} {lastname}', target='name')
    document.getElementById('grades').innerHTML = f'''
Science: {science}<br>
English: {english}<br>
ICT: {ict}<br>
Math: {math}<br>
Filipino: {filipino}<br>
PE: {pe}<br>
'''
    display(f'Your general weighted average is {gwa:.2f}', target='gwa')