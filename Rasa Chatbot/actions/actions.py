# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, EventType, FollowupAction
from rasa_sdk.types import DomainDict
import base64
import io
from PIL import Image
from rasa_sdk.events import UserUttered

class CustomAction(Action):
    def name(self) -> Text:
        return "custom_action"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Get the previous intent
        prev_intent = tracker.get_intent_of_latest_message(skip_fallback_intent=True)

        # Do something with the previous intent
        if prev_intent == "explain":
            print("explain")
            dispatcher.utter_message("okay, what do you feel?")
        else:
            dispatcher.utter_message("okay, now i am gonna  ask you some question and want you to answer it.")
            dispatcher.utter_message("in which part of your body do you feel pain?")
        return []
    

class PreviousIntentsAction(Action):
    def name(self):
        return "action_previous_intents"
    
    def run(self, dispatcher, tracker, domain):
        # Get all the events from the tracker
        events = tracker.events
        prev_intent = tracker.get_intent_of_latest_message(skip_fallback_intent=True)

        # Loop through the events and extract the user intents
        if prev_intent == "placeOfPain_Head":
            dispatcher.utter_message("Do you feel seizures ?")
        elif prev_intent == "placeOfPain_breast":
            dispatcher.utter_message("do you notice any lumps in breast or underarm?")
        elif prev_intent == "placeOfPain_Lung":
            dispatcher.utter_message("Have you occurred coughing blood before?")
        elif prev_intent == "placeOfPain_Kidney":
            dispatcher.utter_message("do you see/notice/have blood in your urine?")
        elif prev_intent == "placeOfPain_oral":
            dispatcher.utter_message("are you suffering from long term ulcers in your mouth?")
        elif prev_intent == "placeOfPain":
            dispatcher.utter_message("i am terribly sorry by this part is out of my knowlegde. Could explain more to me how do you feel ")
        

        return []


class Action_yes_no_brain(Action):
    def name(self) -> Text:
        return "Action_yes_no_brain"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Get the previous intent

        prev_intent = tracker.get_intent_of_latest_message(skip_fallback_intent=True)

        # Do something with the previous intent
        latest_user_message = None
        for event in reversed(tracker.events):
            if event.get('event') == 'user':
                latest_user_message = event.get('text')
                break
        
        latest_bot_message = None
        for event in reversed(tracker.events):
            if event.get('event') == 'bot':
                latest_bot_message = event.get('text')
                break


        ################################ Brain

        if latest_bot_message == "Do you feel seizures ?":
            if prev_intent == "affirm":
                return [SlotSet("seizures_symptoms", "seizures")]
            
            elif prev_intent == "deny":
                return [SlotSet("seizures_symptoms", "NO ,seizures")]
            else:
                return[]
            
        if latest_bot_message == "Do you persistently feel sick (nausea), being sick (vomiting) and drowsiness ?":
            if prev_intent == "affirm":
                return [SlotSet("vomit_symptoms", "vomit")]
            
            elif prev_intent == "deny":
                return [SlotSet("vomit_symptoms", "NO ,vomit")]
            else:
                return[]
        
        if latest_bot_message == "Do you feel mental or behavioral changes, such as memory problems or changes in personality ?":
            if prev_intent == "affirm":
                return [SlotSet("mental_symtoms", "mental")]
            
            elif prev_intent == "deny":
                return [SlotSet("mental_symtoms", "NO ,mental")]
            else:
                return[]
            
        if latest_bot_message == "Do you have vision or speech problems ?":
            if prev_intent == "affirm":
                return [SlotSet("vision_speech_symtoms", "vision")]
            
            elif prev_intent == "deny":
                return [SlotSet("vision_speech_symtoms", "NO ,vision")]
            else:
                return[]
            
        if latest_bot_message == "Do you have headache ?":
            if prev_intent == "affirm":
                return [SlotSet("headache_symptoms", "headache")]
            
            elif prev_intent == "deny":
                return [SlotSet("headache_symptoms", "NO ,headache")]
            else:
                return[]
        

class Action_yes_no_breast(Action):
    def name(self) -> Text:
        return "Action_yes_no_breast"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Get the previous intent

        prev_intent = tracker.get_intent_of_latest_message(skip_fallback_intent=True)

        # Do something with the previous intent
        latest_user_message = None
        for event in reversed(tracker.events):
            if event.get('event') == 'user':
                latest_user_message = event.get('text')
                break
        
        latest_bot_message = None
        for event in reversed(tracker.events):
            if event.get('event') == 'bot':
                latest_bot_message = event.get('text')
                break

        dispatcher.utter_message(latest_bot_message)
        dispatcher.utter_message(latest_user_message)

        ################################ Breast

        if latest_bot_message == "Do you have Thickening or swelling of part of the breast?":
            if prev_intent == "affirm":
                return [SlotSet("thick_or_swell", "Thickening and swelling of part of the breast")]
            
            elif prev_intent == "deny":
                return [SlotSet("thick_or_swell", "NO ,Thickening and swelling of part of the breast")]
            else:
                return[]
            
        if latest_bot_message == "Do you have Nipple retraction?":
            if prev_intent == "affirm":
                return [SlotSet("Nipple_retraction", "Nipple retraction")]
            
            elif prev_intent == "deny":
                return [SlotSet("Nipple_retraction", "NO ,Nipple retraction")]
            else:
                return[]
        if latest_bot_message == "Do you have Sunken nipple?":
            if prev_intent == "affirm":
                return [SlotSet("Sunken_nipple", "Sunken nipple")]
            
            elif prev_intent == "deny":
                return [SlotSet("Sunken_nipple", "NO ,Sunken nipple")]
            else:
                return[]
            
        if latest_bot_message == "Do you have Dimpling of the breast skin?":
            if prev_intent == "affirm":
                return [SlotSet("Dimpling", "Dimpling of the breast skin")]
            
            elif prev_intent == "deny":
                return [SlotSet("Dimpling", "NO ,Dimpling of the breast skin")]
            else:
                return[]
        if latest_bot_message == "Do you notice any Growing veins on the breast?":
            if prev_intent == "affirm":
                return [SlotSet("Growing_veins", "Growing veins on the breast")]
            
            elif prev_intent == "deny":
                return [SlotSet("Growing_veins", "NO ,Growing veins on the breast")]
            else:
                return[]
            
        if latest_bot_message == "Do you feel breast pain?":
            if prev_intent == "affirm":
                return [SlotSet("breast_pain", "Pain in the breast")]
            
            elif prev_intent == "deny":
                return [SlotSet("breast_pain", "NO ,Pain in the breast")]
            else:
                return[]
        if latest_bot_message == "Do you have any alteration in size, shape or appearance of a breast?":
            if prev_intent == "affirm":
                return [SlotSet("alternation_in_appearance", "alteration in appearance of a breast")]
            
            elif prev_intent == "deny":
                return [SlotSet("alternation_in_appearance", "NO ,alteration in appearance of a breast")]
            else:
                return[]
            
        if latest_bot_message == "Do you have swollen lymph nodes under the arm or near the collar bone?":
            if prev_intent == "affirm":
                return [SlotSet("swollen_lumph_nodes", "Swollen lymph nodes near the collar bone or under the arm")]
            
            elif prev_intent == "deny":
                return [SlotSet("swollen_lumph_nodes", "NO ,Swollen lymph nodes near the collar bone or under the arm")]
            else:
                return[]
        if latest_bot_message == "Do you have Redness or flaky skin in the nipple area or the breast?":
            if prev_intent == "affirm":
                return [SlotSet("Redness_skin", "Redness skin in the breast or in nipple area")]
            
            elif prev_intent == "deny":
                return [SlotSet("Redness_skin", "NO ,Redness skin in the breast or in nipple area")]
            else:
                return[]
        if latest_bot_message == "Do you have Irritation or dimpling of breast skin?":
            if prev_intent == "affirm":
                return [SlotSet("irritaion_dimpling", "irritation of breast skin")]
            
            elif prev_intent == "deny":
                return [SlotSet("irritaion_dimpling", "NO ,irritation of breast skin")]
            else:
                return[]
            
        if latest_bot_message == "Do you have abnormal nipple discharge?":
            if prev_intent == "affirm":
                return [SlotSet("nipple_discharge", "abnormal nipple discharge")]
            
            elif prev_intent == "deny":
                return [SlotSet("nipple_discharge", "NO ,abnormal nipple discharge")]
            else:
                return[]
        if latest_bot_message == "do you notice any lumps in breast or underarm?":
            if prev_intent == "affirm":
                return [SlotSet("breast_lump", "New lump in the breast or underarm")]
            
            elif prev_intent == "deny":
                return [SlotSet("breast_lump", "NO ,New lump in the breast and underarm")]
            else:
                return[]
            
        if latest_bot_message == "do you notice any crusting in breast skin or area surrounding nipple?":
            if prev_intent == "affirm":
                return [SlotSet("breast_skin", "Peeling, scaling, crusting or flaking of the pigmented area of skin surrounding the nipple or breast skin")]
            
            elif prev_intent == "deny":
                return [SlotSet("breast_skin", "NO ,Peeling, scaling, crusting or flaking of the pigmented area of skin surrounding the nipple or breast skin")]
            else:
                return[]
        #return []

            

class Action_yes_no_kidney(Action):
    def name(self) -> Text:
        return "Action_yes_no_kidney"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Get the previous intent

        prev_intent = tracker.get_intent_of_latest_message(skip_fallback_intent=True)

        # Do something with the previous intent
        latest_user_message = None
        for event in reversed(tracker.events):
            if event.get('event') == 'user':
                latest_user_message = event.get('text')
                break
        
        latest_bot_message = None
        for event in reversed(tracker.events):
            if event.get('event') == 'bot':
                latest_bot_message = event.get('text')
                break

        dispatcher.utter_message(latest_bot_message)
        dispatcher.utter_message(latest_user_message)

    ############################################################# Kidney
        if latest_bot_message == "do you see/notice/have blood in your urine?":
            if prev_intent == "affirm":
                return [SlotSet("urine_blood", "Blood in your urine")]
            
            elif prev_intent == "deny":
                return [SlotSet("urine_blood", "NO ,Blood in your urine")]
            else:
                return[]
            
        if latest_bot_message == "do you have fever?":
            if prev_intent == "affirm":
                return [SlotSet("kidney_fever", "Fever")]
            
            elif prev_intent == "deny":
                return [SlotSet("kidney_fever", "NO ,Fever")]
            else:
                return[]
        if latest_bot_message == "do you feel tired?":
            if prev_intent == "affirm":
                return [SlotSet("kidney_tiredness", "Tiredness")]
            
            elif prev_intent == "deny":
                return [SlotSet("kidney_tiredness", "NO ,Tiredness")]
            else:
                return[]
            
        if latest_bot_message == "do you have a loss of appetite?":
            if prev_intent == "affirm":
                return [SlotSet("kidney_appetite_loss", "Loss of appetite")]
            
            elif prev_intent == "deny":
                return [SlotSet("kidney_appetite_loss", "NO ,Loss of appetite")]
            else:
                return[]
        if latest_bot_message == "do have high temperature?":
            if prev_intent == "affirm":
                return [SlotSet("Kidney_high_temp", "high temperature")]
            
            elif prev_intent == "deny":
                return [SlotSet("Kidney_high_temp", "NO ,high temperature")]
            else:
                return[]
            
        if latest_bot_message == "do you have fatigue?":
            if prev_intent == "affirm":
                return [SlotSet("Kidney_fatigue", "Fatigue")]
            
            elif prev_intent == "deny":
                return [SlotSet("Kidney_fatigue", "NO ,Fatigue")]
            else:
                return[]
        if latest_bot_message == "do you feel pain in bone?":
            if prev_intent == "affirm":
                return [SlotSet("Kidney_bone_pain", "bone pain")]
            
            elif prev_intent == "deny":
                return [SlotSet("Kidney_bone_pain", "NO ,bone pain")]
            else:
                return[]
            
        if latest_bot_message == "do you have anemia?":
            if prev_intent == "affirm":
                return [SlotSet("Kidney_anemia", "Anemia")]
            
            elif prev_intent == "deny":
                return [SlotSet("Kidney_anemia", "NO ,Anemia")]
            else:
                return[]
        if latest_bot_message == "do you have swelling in testicle?":
            if prev_intent == "affirm":
                return [SlotSet("testicle_swelling", "Testicle swelling")]
            
            elif prev_intent == "deny":
                return [SlotSet("testicle_swelling", "NO ,Testicle swelling")]
            else:
                return[]
        if latest_bot_message == "do have high blood pressure?":
            if prev_intent == "affirm":
                return [SlotSet("Kidney_blood_pressure", "persistent high blood pressure")]
            
            elif prev_intent == "deny":
                return [SlotSet("Kidney_blood_pressure", "NO ,persistent high blood pressure")]
            else:
                return[]
            
        if latest_bot_message == "do you feel swelling of legs or ankels?":
            if prev_intent == "affirm":
                return [SlotSet("leg_swelling", "Swelling of the legs or ankles")]
            
            elif prev_intent == "deny":
                return [SlotSet("leg_swelling", "NO ,Swelling of the legs or ankles")]
            else:
                return[]
        if latest_bot_message == "do you recently experinced unexplained weight loss?":
            if prev_intent == "affirm":
                return [SlotSet("kidney_weight_loss", "Unexplained weight loss")]
            
            elif prev_intent == "deny":
                return [SlotSet("kidney_weight_loss", "NO ,Unexplained weight loss")]
            else:
                return[]
            
        if latest_bot_message == "does your pee look darker than usual or reddish in colour?":
            if prev_intent == "affirm":
                return [SlotSet("dark_pee", "pee is darker than usual or reddish in colour")]
            
            elif prev_intent == "deny":
                return [SlotSet("dark_pee", "NO ,pee is darker than usual or reddish in colour")]
            else:
                return[]
        if latest_bot_message == "do have swelling of the veins in the testicles?":
            if prev_intent == "affirm":
                return [SlotSet("testicles_viens", "swelling of the veins in the testicles")]
            
            elif prev_intent == "deny":
                return [SlotSet("testicles_viens", "NO ,swelling of the veins in the testicles")]
            else:
                return[]
            
        if latest_bot_message == "do you have swollen glands in your neck?":
            if prev_intent == "affirm":
                return [SlotSet("swollen_glands", "swollen glands in the neck")]
            
            elif prev_intent == "deny":
                return [SlotSet("swollen_glands", "NO ,swollen glands in the neck")]
            else:
                return[]
        if latest_bot_message == "do you notice any lumps in your lower back or side?":
            if prev_intent == "affirm":
                return [SlotSet("back_lump", "A mass or lump in the side or back")]
            
            elif prev_intent == "deny":
                return [SlotSet("back_lump", "NO , mass or lump in the side or back")]
            else:
                return[]
            

class Action_yes_no_Lung(Action):
    def name(self) -> Text:
        return "Action_yes_no_Lung"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Get the previous intent

        prev_intent = tracker.get_intent_of_latest_message(skip_fallback_intent=True)

        # Do something with the previous intent
        latest_user_message = None
        for event in reversed(tracker.events):
            if event.get('event') == 'user':
                latest_user_message = event.get('text')
                break
        
        latest_bot_message = None
        for event in reversed(tracker.events):
            if event.get('event') == 'bot':
                latest_bot_message = event.get('text')
                break

        dispatcher.utter_message(latest_bot_message)
        dispatcher.utter_message(latest_user_message)

        ################################ Brain

        if latest_bot_message == "do you have a persistent cough?":
            if prev_intent == "affirm":
                return [SlotSet("coughing", "coughing")]
            
            elif prev_intent == "deny":
                return [SlotSet("coughing", "NO ,coughing")]
            else:
                return[]
            
        if latest_bot_message == "do you have pain in your chest?":
            if prev_intent == "affirm":
                return [SlotSet("chest_pain", "chest pain")]
            
            elif prev_intent == "deny":
                return [SlotSet("chest_pain", "NO ,chest pain")]
            else:
                return[]
        
        if latest_bot_message == "do you have pain in your bones?":
            if prev_intent == "affirm":
                return [SlotSet("lung_bone_pain", "Bone Pain")]
            
            elif prev_intent == "deny":
                return [SlotSet("lung_bone_pain", "NO ,Bone Pain")]
            else:
                return[]
            
        if latest_bot_message == "have you experienced any persistent shortness of breath?":
            if prev_intent == "affirm":
                return [SlotSet("shortness_breath", "Shortness of breath")]
            
            elif prev_intent == "deny":
                return [SlotSet("shortness_breath", "NO ,Shortness of breath")]
            else:
                return[]
            
        if latest_bot_message == "Have you noticed any changes in your voice?":
            if prev_intent == "affirm":
                return [SlotSet("wheezing", "wheezing")]
            
            elif prev_intent == "deny":
                return [SlotSet("wheezing", "NO ,wheezing")]
            else:
                return[]
        
        if latest_bot_message == "Have you occurred coughing blood before?":
            if prev_intent == "affirm":
                return [SlotSet("coughing_blood", "coughing up blood")]
            
            elif prev_intent == "deny":
                return [SlotSet("coughing_blood", "NO ,coughing up blood")]
            else:
                return[]
            
        if latest_bot_message == "do you feel tired most of the time?":
            if prev_intent == "affirm":
                return [SlotSet("feel_tired", "feel tired")]
            
            elif prev_intent == "deny":
                return [SlotSet("feel_tired", "NO ,feel tired")]
            else:
                return[]
        if latest_bot_message == "Do you have unexplained weight loss?":
            if prev_intent == "affirm":
                return [SlotSet("lung_weight_loss", "Weight Loss")]
            
            elif prev_intent == "deny":
                return [SlotSet("lung_weight_loss", "NO ,Weight Loss")]
            else:
                return[]
            
        if latest_bot_message == "do you have high temperature?":
            if prev_intent == "affirm":
                return [SlotSet("lung_high_temp", "high temperature")]
            
            elif prev_intent == "deny":
                return [SlotSet("lung_high_temp", "NO ,high temperature")]
            else:
                return[]
        if latest_bot_message == "do you have any ache in your muscles?":
            if prev_intent == "affirm":
                return [SlotSet("muscle_ache", "muscles ache")]
            
            elif prev_intent == "deny":
                return [SlotSet("muscle_ache", "NO ,muscles ache")]
            else:
                return[]
            
        if latest_bot_message == "do you have any ache in your head?":
            if prev_intent == "affirm":
                return [SlotSet("ache", "headache")]
            
            elif prev_intent == "deny":
                return [SlotSet("ache", "NO ,headache")]
            else:
                return[]
        if latest_bot_message == "have you noticed any changes in yor fingers shape?":
            if prev_intent == "affirm":
                return [SlotSet("change_appearance", "Changes in the appearance of fingers shapes")]
            
            elif prev_intent == "deny":
                return [SlotSet("change_appearance", "NO ,Changes in the appearance of fingers shapes")]
            else:
                return[]
            
        if latest_bot_message == "are you suffering from diffcuilty swallowing?":
            if prev_intent == "affirm":
                return [SlotSet("swallowing", "difficulty swallowing")]
            
            elif prev_intent == "deny":
                return [SlotSet("swallowing", "NO ,difficulty swallowing")]
            else:
                return[]
        if latest_bot_message == "have you noticed swelling of your face or neck?":
            if prev_intent == "affirm":
                return [SlotSet("swelling_face_neck", "Swelling of Face or Neck")]
            
            elif prev_intent == "deny":
                return [SlotSet("swelling_face_neck", "NO ,Swelling of Face or Neck")]
            else:
                return[]
        if latest_bot_message == "have you noticed yellowing of your skin or eyes?":
            if prev_intent == "affirm":
                return [SlotSet("yellow_skin", "Yellowing of skin or eyes")]
            
            elif prev_intent == "deny":
                return [SlotSet("yellow_skin", "NO ,Yellowing of skin or eyes")]
            else:
                return[]
            
        if latest_bot_message == "are you suffering from any weakness of your arm or leg?":
            if prev_intent == "affirm":
                return [SlotSet("weakness_arm_leg", "weakness of an arm or leg")]
            
            elif prev_intent == "deny":
                return [SlotSet("weakness_arm_leg", "NO ,weakness of an arm or leg")]
            else:
                return[]
        if latest_bot_message == "are you suffering from dizziness?":
            if prev_intent == "affirm":
                return [SlotSet("dizziness", "Dizziness")]
            
            elif prev_intent == "deny":
                return [SlotSet("dizziness", "NO ,Dizziness")]
            else:
                return[]
            
        if latest_bot_message == "do you have mouth dryness?":
            if prev_intent == "affirm":
                return [SlotSet("mouth_dryness", "Dry Mouth")]
            
            elif prev_intent == "deny":
                return [SlotSet("mouth_dryness", "NO ,Dry Mouth")]
            else:
                return[]
        #return []

        if latest_bot_message == "Have you noticed any unexplained loss of appetite?":
            if prev_intent == "affirm":
                return [SlotSet("lung_loss_appetite", "Loss Of Appetite")]
            
            elif prev_intent == "deny":
                return [SlotSet("lung_loss_appetite", "NO ,Loss Of Appetite")]
            else:
                return[]
            
        if latest_bot_message == "do you feel any inflammation in your chest or any swelling?":
            if prev_intent == "affirm":
                return [SlotSet("pneumonia", "pneumonia")]
            
            elif prev_intent == "deny":
                return [SlotSet("pneumonia", "NO ,pneumonia")]
            else:
                return[]
        if latest_bot_message == "do you notice yellowing of your skin?":
            if prev_intent == "affirm":
                return [SlotSet("yellow_skin", "Yellowing of skin")]
            
            elif prev_intent == "deny":
                return [SlotSet("yellow_skin", "NO ,Yellowing of skin")]
            else:
                return[]
            
        if latest_bot_message == "do you notice yellowing of your eyes?":
            if prev_intent == "affirm":
                return [SlotSet("yellow_eyes", "Yellowing of eyes")]
            
            elif prev_intent == "deny":
                return [SlotSet("yellow_eyes", "NO ,Yellowing of eyes")]
            else:
                return[]
        if latest_bot_message == "do you feel weakness or numbness of your arm or leg?":
            if prev_intent == "affirm":
                return [SlotSet("arm_leg_numbness", "numbness of an arm or leg")]
            
            elif prev_intent == "deny":
                return [SlotSet("arm_leg_numbness", "NO ,numbness of an arm or leg")]
            else:
                return[]
            
        


class Action_yes_no_oral(Action):
    def name(self) -> Text:
        return "Action_yes_no_oral"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Get the previous intent

        prev_intent = tracker.get_intent_of_latest_message(skip_fallback_intent=True)

        # Do something with the previous intent
        latest_user_message = None
        for event in reversed(tracker.events):
            if event.get('event') == 'user':
                latest_user_message = event.get('text')
                break
        
        latest_bot_message = None
        for event in reversed(tracker.events):
            if event.get('event') == 'bot':
                latest_bot_message = event.get('text')
                break

        dispatcher.utter_message(latest_bot_message)
        dispatcher.utter_message(latest_user_message)

        ################################ Brain

        if latest_bot_message == "does your teeth fall or do you loose teeth?":
            if prev_intent == "affirm":
                return [SlotSet("loose_teeth", "Loose teeth")]
            
            elif prev_intent == "deny":
                return [SlotSet("loose_teeth", "NO ,Loose teeth")]
            else:
                return[]
            
        if latest_bot_message == "do you have pain in your ear?":
            if prev_intent == "affirm":
                return [SlotSet("ear_pain", "ear pain")]
            
            elif prev_intent == "deny":
                return [SlotSet("ear_pain", "NO ,ear pain")]
            else:
                return[]
        
        if latest_bot_message == "do you have pain in your mouth?":
            if prev_intent == "affirm":
                return [SlotSet("mouth_pain", "mouth pain")]
            
            elif prev_intent == "deny":
                return [SlotSet("mouth_pain", "NO ,mouth pain")]
            else:
                return[]
            
        if latest_bot_message == "do you have a lip or mouth sore that doesn't heal?":
            if prev_intent == "affirm":
                return [SlotSet("lip_or_sore", "A lip or Mouth sore that doesn't heal")]
            
            elif prev_intent == "deny":
                return [SlotSet("lip_or_sore", "NO ,A lip or Mouth sore that doesn't heal")]
            else:
                return[]
            
        if latest_bot_message == "do you have a growth or lump inside your mouth?":
            if prev_intent == "affirm":
                return [SlotSet("growth_or_lump", "A lump or growth inside the mouth")]
            
            elif prev_intent == "deny":
                return [SlotSet("growth_or_lump", "NO ,A lump or growth inside the mouth")]
            else:
                return[]
        
        ################################ Breast

        if latest_bot_message == "do you have dysphagia?":
            if prev_intent == "affirm":
                return [SlotSet("dysphagia", "dysphagia")]
            
            elif prev_intent == "deny":
                return [SlotSet("dysphagia", "NO ,dysphagia")]
            else:
                return[]
            
        if latest_bot_message == "do you have bleeding or numbness in the mouth?":
            if prev_intent == "affirm":
                return [SlotSet("mouth_bleeding_or_numbness", "bleeding or numbness in the mouth")]
            
            elif prev_intent == "deny":
                return [SlotSet("mouth_bleeding_or_numbness", "NO ,bleeding or numbness in the mouth")]
            else:
                return[]
        if latest_bot_message == "do you have a tooth socket that does not heal after a tooth is removed?":
            if prev_intent == "affirm":
                return [SlotSet("tooth_socket", "a tooth socket that does not heal after a tooth is removed")]
            
            elif prev_intent == "deny":
                return [SlotSet("tooth_socket", "NO ,a tooth socket that does not heal after a tooth is removed")]
            else:
                return[]
            
        if latest_bot_message == "do you have Leukoplakia?":
            if prev_intent == "affirm":
                return [SlotSet("Leukoplakia", "Leukoplakia")]
            
            elif prev_intent == "deny":
                return [SlotSet("Leukoplakia", "NO ,Leukoplakia")]
            else:
                return[]
        if latest_bot_message == "do you have Erythroplakia?":
            if prev_intent == "affirm":
                return [SlotSet("Erythroplakia", "Erythroplakia")]
            
            elif prev_intent == "deny":
                return [SlotSet("Erythroplakia", "NO ,Erythroplakia")]
            else:
                return[]
            
        if latest_bot_message == "do you feel like having Chronic bad breath?":
            if prev_intent == "affirm":
                return [SlotSet("bad_breath", "Chronic bad breath")]
            
            elif prev_intent == "deny":
                return [SlotSet("bad_breath", "NO ,Chronic bad breath")]
            else:
                return[]
        if latest_bot_message == "do you feel stiffness in your mouth?":
            if prev_intent == "affirm":
                return [SlotSet("stifness", "stiffness")]
            
            elif prev_intent == "deny":
                return [SlotSet("stifness", "NO ,stiffness")]
            else:
                return[]
            
        if latest_bot_message == "do you feel difficulty in moving your tongue?":
            if prev_intent == "affirm":
                return [SlotSet("tongue_movement", "Difficulty in tongue movement")]
            
            elif prev_intent == "deny":
                return [SlotSet("tongue_movement", "NO ,Difficulty in tongue movement")]
            else:
                return[]
        if latest_bot_message == "do you have an eroded areas on the lips, gums, cheek, or other areas inside the mouth?":
            if prev_intent == "affirm":
                return [SlotSet("erode_areas", "eroded areas on the lips, gums, cheek, or other areas inside the mouth")]
            
            elif prev_intent == "deny":
                return [SlotSet("erode_areas", "NO ,eroded areas on the lips, gums, cheek, or other areas inside the mouth")]
            else:
                return[]
            
        if latest_bot_message == "do you have a white or reddish patch on the inside of your mouth ?":
            if prev_intent == "affirm":
                return [SlotSet("red_white_patches", "red or white patches on the inside of your mouth")]
            
            elif prev_intent == "deny":
                return [SlotSet("red_white_patches", "NO ,red or white patches on the inside of your mouth")]
            else:
                return[]
        if latest_bot_message == "do have difficulty moving your jaw ?":
            if prev_intent == "affirm":
                return [SlotSet("jaw_movement", "difficulty moving the jaw")]
            
            elif prev_intent == "deny":
                return [SlotSet("jaw_movement", "NO ,difficulty moving the jaw")]
            else:
                return[]
            
        if latest_bot_message == "are you suffering from long term ulcers in your mouth?":
            if prev_intent == "affirm":
                return [SlotSet("mouth_ulcers", "sore mouth ulcers that do not heal within several weeks")]
            
            elif prev_intent == "deny":
                return [SlotSet("mouth_ulcers", "NO ,sore mouth ulcers that do not heal within several weeks")]
            else:
                return[]
        #return []

    ############################################################# Kidney
        if latest_bot_message == "have you noticed unexplained weight loss?":
            if prev_intent == "affirm":
                return [SlotSet("mouth_weight_loss", "unintentional weight loss")]
            
            elif prev_intent == "deny":
                return [SlotSet("mouth_weight_loss", "NO ,unintentional weight loss")]
            else:
                return[]
            
        if latest_bot_message == "have you noticed any bleeding from your mouth?":
            if prev_intent == "affirm":
                return [SlotSet("mouth_bleeding", "bleeding in the mouth")]
            
            elif prev_intent == "deny":
                return [SlotSet("mouth_bleeding", "NO ,bleeding in the mouth")]
            else:
                return[]
        if latest_bot_message == "are you suffering from difficulty of chewing or swallowing?":
            if prev_intent == "affirm":
                return [SlotSet("diff_swallowing", "Difficulty swallowing or chewing")]
            
            elif prev_intent == "deny":
                return [SlotSet("diff_swallowing", "NO ,Difficulty swallowing or chewing")]
            else:
                return[]
            
        if latest_bot_message == "are you suffering from difficulty of speaking?":
            if prev_intent == "affirm":
                return [SlotSet("diff_speaking", "Difficulty speaking")]
            
            elif prev_intent == "deny":
                return [SlotSet("diff_speaking", "NO ,Difficulty speaking")]
            else:
                return[]
        if latest_bot_message == "have you noticed any change in your voice?":
            if prev_intent == "affirm":
                return [SlotSet("voice_change", "change in voice")]
            
            elif prev_intent == "deny":
                return [SlotSet("voice_change", "NO ,change in voice")]
            else:
                return[]
            
        if latest_bot_message == "do you have a white or reddish patch lining of your mouth?":
            if prev_intent == "affirm":
                return [SlotSet("red_white_patches_lining", "red or white patches on the lining of your mouth")]
            
            elif prev_intent == "deny":
                return [SlotSet("red_white_patches_lining", "NO ,red or white patches on the lining of your mouth")]
            else:
                return[]
            

class Im_Fine_action(Action):
    def name(self) -> Text:
        return "Im_Fine_action"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Get the previous intent

        prev_intent = tracker.get_intent_of_latest_message(skip_fallback_intent=True)

        # Do something with the previous intent
        latest_user_message = None
        for event in reversed(tracker.events):
            if event.get('event') == 'user':
                latest_user_message = event.get('text')
                break
        
        latest_bot_message = None
        for event in reversed(tracker.events):
            if event.get('event') == 'bot':
                latest_bot_message = event.get('text')
                break

        dispatcher.utter_message("Thank you for asking. As an AI-powered chatbot, I don't have feelings like humans do, but I'm always ready and available to assist you, lets go back to our topic.")
        if latest_bot_message == "Hi, I am Estshara Chatbot. How can I help you?":
            dispatcher.utter_message("How can i help you?")
        else:
            dispatcher.utter_message(latest_bot_message)

class CustomAction(Action):
    def name(self) -> Text:
        return "xrayAnswer"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Get the previous intent
        latest_user_message = None
        for event in reversed(tracker.events):
            if event.get('event') == 'user':
                latest_user_message = event.get('text')
                break
        
        latest_bot_message = None
        for event in reversed(tracker.events):
            if event.get('event') == 'bot':
                latest_bot_message = event.get('text')
                break


        prev_intent = tracker.get_intent_of_latest_message(skip_fallback_intent=True)

        # Do something with the previous intent
        if latest_bot_message == "It seems that you have some problems. Do you have an MRI image or X-ray image on your brain?" and prev_intent == "affirm":
            dispatcher.utter_message("Please upload the image here to pass it to our model to check if there is brain disease or not, as it will help the doctor in further stages.")
        else:
            dispatcher.utter_message("Having the image will help the doctors to be more accurate about the disease")
            
        return []

class ActionAskImage(Action):
    def name(self) -> Text:
        return "action_ask_image"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict
    ) -> List[Dict[Text, Any]]:

        message = "Please upload an image."
        dispatcher.utter_message(text=message)

        return []
    


class ActionHandleImage(Action):
    def name(self) -> Text:
        return "action_handle_image"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict
    ) -> List[Dict[Text, Any]]:

        message = tracker.latest_message
        image_data = message.get("image")[0]["data"]
        image_bytes = base64.b64decode(image_data)

        image = Image.open(io.BytesIO(image_bytes))

        # Save the image to the slot
        tracker.slots["image"] = image

        return []
    


    
'''
class ActionSaveConversation(Action):

    def name(self) -> Text:
        return "action_save_conversation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        x=tracker.latest_message['intent']['confidence']
        print(x)
        return []
    

class nn(Action):
    def name(self) -> Text:
        return "nn"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        # tell the user they are being passed to a customer service agent


        # assume there's a function to call customer service
        # pass the tracker so that the agent has a record of the conversation between the user
        # and the bot for context
        latest_message = tracker.current_state()['latest_message']
        intent_ranking = latest_message.get("intent_ranking")
        bu = ["symptomsForBrainCancer","symptomsForBreastCancer","symptomsForLungCancer"]
        c=0
        if not intent_ranking:
            return None
        for i in range(3):
            if intent_ranking[i]['name'] in bu:
                c=c+1
            print(intent_ranking[i]['name'])
            print(intent_ranking[i]['confidence'])
        print(c)
        # pause the tracker so that the bot stops responding to user input
        return []
'''