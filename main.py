from pyscript import document

def check_eligibility(e):
    output = document.getElementById("output")
    output.innerHTML = ""

    # Registered
    if document.getElementById("reg_yes").checked:
        registered = "yes"
    elif document.getElementById("reg_no").checked:
        registered = "no"
    else:
        registered = None

    # Medical
    if document.getElementById("med_yes").checked:
        medical = "yes"
    elif document.getElementById("med_no").checked:
        medical = "no"
    else:
        medical = None

    grade = document.getElementById("grade").value
    section = document.getElementById("section").value

    # Section → Team mapping + image
    section_team = {
        "Emerald": {"team": "Yellow Tigers", "img": "yellow.png"},
        "Ruby": {"team": "Blue Bears", "img": "blue.png"},
        "Sapphire": {"team": "Green Hornets", "img": "green.png"},
        "Topaz": {"team": "Red Bulldogs", "img": "red.png"}
    }

    # helper function for ineligible messages (red)
    def show_error(message):
        output.innerHTML = f'<div style="color: red; text-align: center;">{message}</div>'

    # ─────────── MISSING / INELIGIBLE ───────────
    if registered is None and medical is None and grade == "" and section == "":
        show_error("Please answer all questions: registration, medical clearance, grade level, and section.")

    elif registered is None and medical is None:
        show_error("Please answer both registration and medical clearance questions.")

    elif registered is None:
        show_error("Please answer the registration question.")

    elif medical is None:
        show_error("Please answer the medical clearance question.")

    elif registered == "no" and medical == "no":
        show_error("Please register online and secure a medical clearance before joining the Intramurals.")

    elif registered == "no" and grade == "" and section == "":
        show_error("Please register online and select your grade level and section.")

    elif registered == "no" and grade == "":
        show_error("Please register online and select your grade level.")

    elif registered == "no" and section == "":
        show_error("Please register online and select your section.")

    elif registered == "no":
        show_error("Please register online to join the Intramurals.")

    elif medical == "no" and grade == "" and section == "":
        show_error("Please secure a medical clearance and select your grade level and section.")

    elif medical == "no" and grade == "":
        show_error("Please secure a medical clearance and select your grade level.")

    elif medical == "no" and section == "":
        show_error("Please secure a medical clearance and select your section.")

    elif medical == "no":
        show_error("Please secure a medical clearance before joining.")

    elif grade == "" and section == "":
        show_error("Please select both your grade level and section.")

    elif grade == "":
        show_error("Please select your grade level.")

    elif section == "":
        show_error("Please select your section.")

    elif int(grade) < 7 or int(grade) > 10:
        show_error("Only students from Grades 7 to 10 are eligible.")

    # ─────────── ELIGIBLE ───────────
    else:
        team_info = section_team[section]
        team_name = team_info["team"]
        team_img = team_info["img"]

        output.innerHTML = f"""
            <div style="text-align: center; color: green;">
                <h3>🎉 Congratulations! You are eligible to join the Intramurals!</h3>
                <p>Grade {grade} - {section}</p>
                <img src="{team_img}" width="100" style="margin: 10px 0;">
                <p>Assigned Team: <strong>{team_name}</strong></p>
            </div>
        """
