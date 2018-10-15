"""
This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.
The Intent Schema, Custom Slots, and Sample Utterances for this skill, as well
as testing instructions are located at http://amzn.to/1LzFrj6
For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG
"""
def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest" :
        return onLaunch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest" :
        return onIntent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest" :
        return onSessionEnd(event['request'], event['session'])

def onLaunch(launchRequest, session):
    return welcomeuser()

def onIntent(intentRequest, session):
             
    intent = intentRequest['intent']
    intentName = intentRequest['intent']['name']
    if intentName == "DCFactIntent":
        return DCFactIntent(intent, session)
    elif intentName == "AMAZON.HelpIntent":
        return welcomeuser()
    elif intentName == "AMAZON.CancelIntent" or intentName == "AMAZON.StopIntent":
        return handleSessionEndRequest()
    else:
        raise ValueError("Invalid intent")

def onSessionEnd(sessionEndedRequest, session):
    print("on_session_ended requestId=" + sessionEndedRequest['requestId'] + ", sessionId=" + session['sessionId'])

def welcomeuser():
    sessionAttributes = {}
    cardTitle = " Hello"
    speechOutput =  "Hello , Welcome to DC Comics Facts! " \
                    "You can know interesting facts about the world of DC Comics by saying Tell me about d. c. facts"
    repromptText =  "You can know interesting facts about the world of DC Comics by saying Tell me about d. c. facts"
    shouldEndSession = False
    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def DCFactIntent(intent, session):
    import random
    index = random.randint(0,len(facts)-1)
    cardTitle = "Hello"
    sessionAttributes = {}
    speechOutput = facts[index] 
    repromptText = "You can know interesting facts about the world of DC Comics by saying Tell me about d. c. facts"
    shouldEndSession = True                   
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def handleSessionEndRequest():
    cardTitle = "Session Ended"
    speechOutput = "Thank you for using DC Comics Facts Alexa Skills Kit. " \
                    "Have a great time! "
    shouldEndSession = True
    return buildResponse({}, buildSpeechletResponse(cardTitle, speechOutput, None, shouldEndSession))

def buildSpeechletResponse(title, output, repromptTxt, endSession):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
            },
            
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
            },
            
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': repromptTxt
                }
            },
        'shouldEndSession': endSession
    }


def buildResponse(sessionAttr , speechlet):
    return {
        'version': '1.0',
        'sessionAttributes': sessionAttr,
        'response': speechlet
    }



facts = [ 
            "Although Superman remains the most well known superhero in the world, Batman holds the title for most appearances, which currently stands at around 6250.",
            "Comic Sans MS, the one font that is hated all over the internet, was based on the lettering used in the 'The Dark Knight Returns' and 'Watchmen' graphic novels.",
            "In 2000, a project was started to create a DC-multiverse crossover movie: \"Batman versus Superman\". It was, sadly, abandoned in 2002, but a poster did make a cameo as a joke in the apocalyptic movie \"I Am Legend\". It has since been restarted, with the movie coming out in 2015, starring Henry Cavill as Superman and Ben Affleck as Batman.",
            "Aquaman's arch-enemy, the Black Manta, only became a supervillain because Aquaman didn't succed in rescuing him after he was captured by pirates.",
            "The Green Lantern and Wonder Woman were supposed to become a love-couple, but that was scratched in the 70's when DC received a letter by a fan that suggested the same idea. Due to legal reasons, this prohibited DC Comics from moving forward with the idea.",
            "DC created a superhero called Dog Welder. Pretty straightforward name, because his superpower was to weld dead dogs to people's faces.",
            "Earth-23 is a planet in the DC Multiverse that is almost solely inhabited by black versions of DC characters. Black Superman was based on Barack Obama, whereas for instance Wonder Woman was based on Beyoncé Knowles.",
            "The Flash gave his superpowers to himself. During the \"Crisis on Infinite Earths\" crossover comic, he ran so fast that he turned into pure energy, traveled back in time and hit himself as the very bolt of lightning that gave him his superpowers in the first place.",
            "Adam Glass, writer for DC Comics and co-creator of the 'Suicide Squad'series, received death threats after a picture of a newly designed, barely clothed version of Harley Quinn debuted in his series.",
            "The Hemo Goblin was a supervillain created to help a white-supremacists eliminate people of non-white ethnicity by spreading AIDS. He infected members of the New Guardians with AIDS before being killed off.",
            "George Clooney was once giving an interview when the conversation shifted to the topic of his alleged homosexuality. When asked if he'd ever play a gay character in a film, he said he already did when he had played Batman (Batman and Robin, 1997).",
            "Hawkeye is the only character that is a member of the Justice Legue as well as the Avengers.",
            "The Joker once served as the Iranian ambassador to the United Nations.",
            "Kevin Smith, director and actor famous for his role as Silent Bob, wrote an entire 'Batman' comic mini-series called 'The Widening Gyre' while high on marijuana.",
            "Lex Luthor refuses to believe Superman and Clark Kent are the same person. Even after computer analysis that confirms the two are the same person, he still believes that nobody with Superman's powers would hide from the world to live a normal life.",
            "There's a company that makes actual Rorschach Masks. The mask have special ink in the fabric that reacts to the heat of the breath of the person who wears it.",
            "The original Superman stories depicted him as a bald megalomaniac.",
            "In 1997 Marvel and DC made a crossover comic special called \"Batman/Captain America\". In this comic The Joker steals an atomic bomb after being hired by Red Skull. When he find out that the Red Skull is a Nazi, he attacks him while proclaiming \"I may be a criminal lunatic, but I'm an American criminal lunatic\".",
            "Superman Lives was a movie intended to be produced in the 90's. Quite possibly the worst nightmare of many comic book fans, it featured Nicholas Cage as Superman. It was put on hold and later abandoned in 1998.",
            "Bruce Wayne has an IQ that outranges Albert Einstein's. Einstein's IQ was estimated to be around 160-180. Wayne's has been stated to be about 192.",
            "DC created a supervillain called Snowflame. As the name sortof suggests, he gets his superpowers from the drug cocaine, becoming more powerful the more he used.",
            "In 2006, nearly half a century after comic books were declared as a cultural threat, a stamp was released to commemorate on how DC's super heroes had been and still are a significant part of American Culture. It also recognizes comic books as a true art form.",
            "Superman's sign, the big diamond-shaped S on his chest, does not only stands for Superman. It is also a Kryptonian glyph that is used as the family seal for the House of El. Translated it means \"Hope\".",
            "The Joker was originally supposed to die in his second appearance, he was saved however by editor Whitney Ellsworth who saw the potential of the character to grow.",
            "In a quite impressive display of his powers, the Flash once saved a group of people from a burning apartment, taught himself how to build such a complex, and build the group of people a new place to live, all within a matter of minutes.",
            "The Bleed is a sub-reality in the DC-multiverse. It functions as a separition between parallel universes.",
            "Thomas Wayne (Batman's Father) got Wayne Enterprises rejuvenated with Kryptonian Tech. In the crossover comic Superman/Batman #50, his brain was sucked to Krypton via a Kryptonian probe, so that Jor-El (Superman's father) could establish whether Earth was good enough for his son. Thomas Wayne used the technology in the probe he was exposed to.",
            "Students at the University of Victoria have the possibility to take a course called \"The Science of Batman\". In this course students examine human potential, where they use Batman as a metaphor for the ultimate in human conditioning.",
            "DC once created a superhero called Vibe. He was a breakdancer that danced for justice. He used his powers as a dancer to create sound waves. DC quickly found out it was a bit lame as a character, and killed him off after a few episodes.",
            "Creator of Watchmen Alan Moore was going to use original, classic DC characters such as blue Beetle and the Question. When DC learned that he was going to kill of some of them, he was pressed to adjust them into original characters like Rorschach and Nite Owl."
        ]
