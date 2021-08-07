from datetime import datetime


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("Hello", "Hi", "Ssup"):
        return "Hey, How is it going?"

    if user_message in ("who are you?", "who are you"):
        return "I am Munyao's bot"

    if user_message in ("time", "time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)

    if user_message in ("supplementary", "supplementary exams"):
        return "The supplementary examinations will be offered on the 13th of September"

    return "I don't understand you"
