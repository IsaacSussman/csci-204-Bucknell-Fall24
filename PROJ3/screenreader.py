import pyttsx3
from webaccess import *

''' DO NOT CHANGE THIS FILE'''

def screen_reader(site, site_file):
    '''
    Parameters:
        site; AccessHTML object
    '''

    
    site.sort_by("PAGE_ORDER")
    elements = site.elements
    print(site)
    cur_type = "ALL"
    cur_idx = -1


    
    engine = pyttsx3.init()
    engine.say("Hello")
    engine.runAndWait()

    print("Screen reader on")
    engine.say("Screen reader on")
    engine.runAndWait()

    print("Reading "+site_file)
    engine.say("Reading "+site_file)
    engine.runAndWait()

    prompt = "Enter Next Command or ? to see command options."
    engine.say("Enter Next Command or question mark to see command options.")
    engine.runAndWait()
    help = \
    "=== Commands ===\n" +\
    " -- Navigation --\n" + \
    " f - move forward an element\n" +\
    " s - move backard an element\n" +\
    "\n-- Change Navigation Settings --\n" +\
    " h - by heading\n" +\
    " i - by images\n"+\
    " l - by links\n"+\
    " a - by all three elements \n" +\
    "\n -- Other -- \n" +\
    " q - quit \n" +\
    " ? - help menu\n" +\
    " p - print whole site to screen \n"
    print(help)
    while True:
       
        #engine.startLoop(False)
        command = input(prompt)
        match command:
            
            case 'f':
              cur_idx += 1
              if cur_idx == len(elements):
                print("bottom of page. returning to top")

                engine.say("bottom of page. returning to top")
                engine.runAndWait()
                cur_idx = 0
            case 's':
                cur_idx -= 1
                if cur_idx <= -1:
                    print("top of page. going to bottom")
                    engine.say("top of page. going to bottom")
                    engine.runAndWait()
                    cur_idx = len(elements)-1
            case 'h':
                if cur_type != Heading.ELEM_TYPE:
                    phrase = "changing to "+Heading.ELEM_TYPE+" mode."
                    print(phrase)
                    engine.say(phrase)
                    engine.runAndWait()
                    cur_type = Heading.ELEM_TYPE
                    cur_idx = 0 
                    elements = site.get_elements(Heading.ELEM_TYPE)
                else:
                    print("already in "+Heading.ELEM_TYPE+" mode.")
                    engine.say("already in "+Heading.ELEM_TYPE+" mode.")
                    engine.runAndWait()
            case 'l':
                if cur_type != Link.ELEM_TYPE:
                    print("changing to "+Link.ELEM_TYPE+" mode.")
                    engine.say("changing to "+Link.ELEM_TYPE+" mode.")
                    engine.runAndWait()
                    cur_type = Link.ELEM_TYPE
                    cur_idx = 0 
                    elements = site.get_elements(Link.ELEM_TYPE)
                else:
                    print("already in "+Link.ELEM_TYPE+" mode.")
                    engine.say("already in "+Link.ELEM_TYPE+" mode.")
                    engine.runAndWait()
            case 'i':
                if cur_type != Image.ELEM_TYPE:
                    print("changing to "+Image.ELEM_TYPE+" mode.")
                    engine.say("changing to "+Image.ELEM_TYPE+" mode.")
                    engine.runAndWait()
                    cur_type = Image.ELEM_TYPE
                    cur_idx = 0 
                    elements = site.get_elements(Image.ELEM_TYPE)
                else:
                    print("already in "+Image.ELEM_TYPE+" mode.")
                    engine.say("already in "+Image.ELEM_TYPE+" mode.")
                    engine.runAndWait()
            case 'a':
                if cur_type != "ALL":
                    cur_type = "ALL"
                    cur_idx = 0
                    site.sort_by("PAGE_ORDER")
                    elements = site.elements
            case '?':
                print(help)
            case 'p':
                print("All elements")
                site.sort_by("PAGE_ORDER")
                print(site)
                if cur_type != "ALL":
                    site.sort_by("TYPE")
                engine.say("printed all elements.")
                engine.runAndWait()

                print("in "+cur_type+" mode. At element")
                engine.say("in "+cur_type+" mode. At element")
                engine.runAndWait()

            case 'q':
                return
            case _:
                print("unidentified input. try again.")
                engine.say("unidentified input. try again.")
                engine.runAndWait()
                print(help)
        if len(elements) == 0:
            phrase = "No elements"
            if cur_type != "ALL":
                phrase = "No "+cur_type + " elements."
            print(phrase)
            engine.say(phrase)
            engine.runAndWait()
        else:
            element = elements[cur_idx] 

            print(element.get_spoken_str())
            engine.say(element.get_spoken_str())
            engine.runAndWait()



if __name__=="__main__":
    site_file = "./test_html/headings_only.html"
    access = AccessHTML(site_file)
    screen_reader = screen_reader(access, site_file)