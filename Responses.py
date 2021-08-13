from datetime import datetime

semester = 0
my_list = ["Football", "Basketball", "Rugby", "Table tennis"]
stud_leaders = ["Mama Yao - President", "Sheila Jelimo - Secretary General", "Noah Silot - Finance"]


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "ssup"):
        return "Hey, How is it going?"

    if user_message in ("who are you?", "who are you"):
        return "I am Munyao's bot"

    if user_message in ("time", "time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)

    if user_message in ("supplementary", "supplementary exams", "supplementaries"):
        return "The supplementary examinations will be offered on the 13th of September"

    if user_message in ("fees", "fees payable?"):
        return "semester you are in?"

    if user_message in ("bank account number", "bank", "whats the bank account number?"):
        return "For KCB, the bank account number is: 1104513447. For Equity bank, the account number is 0610262187946. "

    if user_message in ("lecturers contact", "lecturer"):
        return "Masau's contact is 0753660, Kiri's contact is 072660, Okuku's contact is 6789094", "Edith's contact " \
                                                                                                   "is 098989990 "

    if user_message in ("sports in the school", "sports?"):
        return "They include", my_list

    if user_message in ("library", "library opening hours", "when is the library open?"):
        return "The library is usually open on weekdays from 8 a.m to 10 p.m On weekends and public holidays it's " \
               "closed."

    if user_message in ("opening date", "when will the school open?", "when are we opening"):
        return "Hello, we will open on 2nd August 2021. Mark your calendar well."

    if user_message in ("closing date", "when will the school close?", "when are we closing?"):
        return "Hello, we will close on 11th November 2021. Mark your calendar."

    if user_message in ("exams", "examination", "when will the exams start", "exam period", "exam date"):
        return "The examinations will commence on 9th august and end on the 19th of the same month."

    if user_message in ("student leaders", "school leadership"):
        return "The student leaders are as follows", stud_leaders

    if user_message in ("scholarships", "do you offer scholarships?", "scholarship"):
        return "Currently there are no scholarship programs being offered, however, we'll notify you in the future."

    if user_message in ("missed an exam", "skipped an exam", "I missed an exam"):
        return "Contact your respective dean for more clarification"

    if user_message in ("contact", "contact information"):
        return "You can contact by call through; 0207252000, email; info@mmu.ac.ke, address: P.O Box 15653 - 00503"

    if user_message in ("faculties", "faculty", "faculties in mmu", "what faculties are in mmu?", "how many faculties"
                        "are in mmu?"):
        return "The faculties in the school are;\n 1. Faculty of Science and Technology\n 2. Faculty of Media & " \
               "Communication\n 3. Faculty of Engineering & Technology\n 4. Faculty of Business & Economics\n 5. " \
               "Faculty of Social Sciences & Technology\n 6. Faculty of Computing &Information Technology"

    if user_message in ("faculty of science and technology", "fost"):
        return "The dean is Dr Sitawa Wattanga. Her contact is: iwatanga@mmu.ac.ke. \nThere are three types of " \
               "courses offered by the faculty include;\n 1. Bridging \n 2. Undergraduate \n 3. Postgraduate\n\n" \
               "In BRIDGING, the programmes offered are \nMaths\nPhysics and\nChemistry\n\n" \
               "In UNDERGRADUATE, the programmes offered are;\n BSc Analytical Chemistry \nBSc Applied Optics & Lasers"\
               "\nBSc Maths & Computer Science \n BSc Applied Physics & Computer Science \nBSc Renewable Energy & " \
               "Technology \nBSc Industrial Chemistry \nBSc Instrumentation & Control \n \nIn POSTGRADUATE, " \
               "the courses offered are; \n MSc in Analytical Chemistry \n MSc in Applied Mathematics " \
               "\n MSc in Pure Mathematics \n MSc in Statistics \n MSc in Renewable Energy & Technology"\

    if user_message in ("faculty of media and communication", "fameco"):
        return "The dean is Dr Isaac Mutwiri, PhD.\nThere are 2 departments\nJournalism and Communication & Broadcast "\
               "Production. \nCourses offered by the faculty include; \n" \
               "1. Certificate\n2. Diploma\n3. Undergraduate\n4. Postgraduate\n\n "\
               "In CERTIFICATE, the programme offered is\nCertificate in Mass Communication\n\n"\
               "In DIPLOMA, the programmes offered are\nDiploma in Film & Production\nDiploma in Journalism\n"\
               "Diploma in Strategic Public Relations.\n\n"\
               "In UNDERGRADUATE, the programmes offered are\n Bachelor of Film Production & Animation\n "\
               "Bachelor of Journalism\n Bachelor of Applied Communication\n\n"\
               "In POSTGRADUATE, the programmes offered are\nMSc in Journalism & Media Studies\nMSc in Corporate "\
               "Communication"

    if user_message in ("faculty of engineering and technology", "fet"):
        return "The dean is Prof(Eng) Abel Mayaka (PhD). His contact is: amayaka@mmu.ac.ke \nThere are 2 departments\n"\
               "Department of Electrical and Information Engineering & Department of Mechanical and Manufacturing "\
               "Engineering.\nCourses offered by the faculty include; \n1. Diploma\n2. Undergraduate\n3. Postgraduate"\
               "\n\n In DIPLOMA, the programmes offered are;\nDiploma in Electrical & Telecommunication Engineering\n"\
               "Diploma in Mechanical Engineering\n\n"\
               "In UNDERGRADUATE, the programmes offered are; \nBSc in Electrical & Telecommunication Engineering\n"\
               "BSc in Mechanical & Manufacturing Engineering\nBSc in Civil Engineering\n\n"\
               "In POSTGRADUATE, the programmes offered are; \nMSc in Communication & Multimedia Engineering\n"\
               "MSc in Mechanical Engineering"

    if user_message in ("faculty of business and economics", "fobe"):
        return "The dean is Dr Mary Mugo, PhD. Her contact is: mmugo@mmu.ac.ke \nThere are 3 departments\n Department"\
               "of Marketing & Management \nDepartment of Finance & Accounting \nDepartment of Procurement & Logistics"\
               "\n Courses by the faculty include; \n1. Certificate\n2. Diploma\n3. Undergraduate\n4. Postgraduate\n\n"\
               "In CERTIFICATE, the programme offered is; \nCIPS Professional Courses\n\n"\
               "In DIPLOMA, the programmes offered are; \nDiploma in Business Administration\nDiploma in Human"\
               "Resource Management\nDiploma in Procurement & Logistics Management\nDiploma in Marketing\nDiploma in"\
               "Hospitality & Tourism Management\n\n"\
               "In UNDERGRADUATE, the programmes offered are; \nBachelor of Commerce\nBachelor of Procurement & "\
               "Logistics Management\nBSc in Actuarial Science\nBSc in Economics\n\n"\
               "In POSTGRADUATE, the programmes offered are; \nMSc in Supply Chain Management\nMSc in Economics\n"\
               "Masters in Business Administration(MBA)"

    if user_message in ("faculty of social sciences and technology", "fsst"):
        return "The dean is Dr Jonathan K Maweu, PhD. His contact is: jkathungu@mmu.ac.ke \nThere are 3 departments\n"\
               "Department of Sociology \nDepartment of Psychology \nDepartment of Political Science\n\n"\
               "The only course offered by the faculty is; \n1. Undergraduate\n\n"\
               "The programmes offered are; \n Bachelor of Arts in Political Science\nBachelor of Arts in Psychology &"\
               "Technology\nBachelor of Arts in Sociology & Technology"

    if user_message in ("faculty of computing and information technology", "cit"):
        return "The dean is Dr Moses O Odeo. His contact is: modeo@mmu.ac.ke \n There are 2 departments\nComputer "\
               "Science Department\nInformation Technology Department\n"\
               "Courses offered by the faculty include; \n1. Certificate\n2. Diploma\n3. Undergraduate\n4. Masters\n\n"\
               "In CERTIFICATE, the programmes offered are; \nCISCO CCNA\nICDL\n\n"\
               "In DIPLOMA, the programmes offered are; \nDiploma in ICT\nInternational Diploma in Computer Studies\n"\
               "International Advanced Diploma in Computer Studies\n\n"\
               "In UNDERGRADUATE, the programmes offered are; \nBSc in Computer Science\nBSc Information Technology\n"\
               "BSc in Computer Technology\nBSc in Software Engineering\n\n"\
               "In MASTERS, the programmes offered are; \nMSc in Information Technology\nMSc in Computer Science "

    return "I don't understand you"
