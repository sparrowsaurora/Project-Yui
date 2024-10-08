import wikipediaapi

def get_wikipedia_summary(query):
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page = wiki_wiki.page(query)
    if page.exists():
        return page.summary
    else:
        return "No information found on Wikipedia."

def define_query():
    query = voice_input.capture_voice()
    if query:
        summary = get_wikipedia_summary(query)
        speech_output.speak(summary)
        print("Wikipedia Summary: " + summary)


define_query()
