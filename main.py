# main.py
from modules import voice_input, speech_output, emailer, code_writer, time_and_date, note_taker
ended = False
def main():
    global ended
    speech_output.speak("Hello, I am Youi. What would you like me to do?")
    
    while True:
        user_command = voice_input.capture_voice()
        
        if user_command:
            if "end session" in user_command:
                ended = True
                break
            elif "email" in user_command:
                emailer.send_email()
            elif "write code" in user_command:
                code_writer.write_code_file()
            elif "date" in user_command or "time" in user_command:
                time_and_date.print_wa_time()
            elif "note" in user_command or "notes" in user_command:
                note_taker.write_code_file()
            # Add more commands here...

if __name__ == "__main__":
    if ended == True:
        pass
    else:
        main()