import torch
import pandas
import re
from transformers import AutoTokenizer, AutoModelWithLMHead
# def remove_non_ascii(input_string):
#     return ''.join(char if ord(char) < 128 else '' for char in input_string)

# def remove_extra_spaces(text):
#     cleaned_text = re.sub(r'\s+', ' ', text)
#     cleaned_text = cleaned_text.strip()
#     return cleaned_text

# def keep_alphabets_and_specific_chars(input_string):
#     # Remove consecutive dots and allow only single dot
#     cleaned_string = re.sub(r'[^a-zA-Z\s.,()\[\]]+|(\.(?!\.))', lambda x: '.' if x.group(1) else '', input_string)
#     return cleaned_string

# def remove_duplicates(input_list):
#     seen = set()
#     result = []
#     for item in input_list:
#         if item not in seen:
#             result.append(item)
#             seen.add(item)
#     return result

def transform_to_para1(text):
    # Split the text into segments based on numbered points
    segments = text.split('\n')

    # Initialize a result string
    result = ""

    # Iterate through each segment
    for segment in segments:
        # Skip empty segments
        if segment.strip() == "":
            continue

        # Identify numbered points and transform into a unified paragraph
        if segment[0].isdigit():
            # Extract the content after the number and add to the result
            content = segment.split('.', 1)[-1].strip()
            result += content + " "
        else:
            # Add non-numbered content to the result
            result += segment.strip() + " "

    return result.strip()


tokenizer = AutoTokenizer.from_pretrained('t5-base')
model = AutoModelWithLMHead.from_pretrained('t5-base', return_dict=True)
# # # print("done")
# text = ("In May, Churchill was still generally unpopular with many Conservatives and probably most of the Labour Party. Chamberlain "
#             "remained Conservative Party leader until October when ill health forced his resignation. By that time, Churchill had won the "
#             "doubters over and his succession as party leader was a formality."
#             " "
#             "He began his premiership by forming a five-man war cabinet which included Chamberlain as Lord President of the Council, "
#             "Labour leader Clement Attlee as Lord Privy Seal (later as Deputy Prime Minister), Halifax as Foreign Secretary and Labour's "
#             "Arthur Greenwood as a minister without portfolio. In practice, these five were augmented by the service chiefs and ministers "
#             "who attended the majority of meetings. The cabinet changed in size and membership as the war progressed, one of the key "
#             "appointments being the leading trades unionist Ernest Bevin as Minister of Labour and National Service. In response to "
#             "previous criticisms that there had been no clear single minister in charge of the prosecution of the war, Churchill created "
#             "and took the additional position of Minister of Defence, making him the most powerful wartime Prime Minister in British "
#             "history. He drafted outside experts into government to fulfil vital functions, especially on the Home Front. These included "
#             "personal friends like Lord Beaverbrook and Frederick Lindemann, who became the government's scientific advisor."
#             " "
#             "At the end of May, with the British Expeditionary Force in retreat to Dunkirk and the Fall of France seemingly imminent, "
#             "Halifax proposed that the government should explore the possibility of a negotiated peace settlement using the still-neutral "
#             "Mussolini as an intermediary. There were several high-level meetings from 26 to 28 May, including two with the French "
#             "premier Paul Reynaud. Churchill's resolve was to fight on, even if France capitulated, but his position remained precarious "
#             "until Chamberlain resolved to support him. Churchill had the full support of the two Labour members but knew he could not "
#             "survive as Prime Minister if both Chamberlain and Halifax were against him. In the end, by gaining the support of his outer "
#             "cabinet, Churchill outmanoeuvred Halifax and won Chamberlain over. Churchill believed that the only option was to fight on "
#             "and his use of rhetoric hardened public opinion against a peaceful resolution and prepared the British people for a long war "
#             "– Jenkins says Churchill's speeches were 'an inspiration for the nation, and a catharsis for Churchill himself'."
#             " "
#             "His first speech as Prime Minister, delivered to the Commons on 13 May was the 'blood, toil, tears and sweat' speech. It was "
#             "little more than a short statement but, Jenkins says, 'it included phrases which have reverberated down the decades'.")
# print(text.type)\
# text = ' William Stephen Vs. State of Tamil Nadu and Anr.[Criminal Appeal No. 607/2024][Criminal Appeal No. 608/2024]Abhay S. Oka, J.Facts1. These two Appeals have been preferred by the accused nos.2 and 1 respectively against the impugned judgment dated 27th July, 2016 passed by the High Court of Judicature at Madras, whereby their conviction and sentence have been confirmed. The appellants-accused have been convicted for the offence punishable under Section 364A read with Section 34 of the Indian Penal Code, 1860 (for short, "IPC"). Both of them have been sentenced to undergo life imprisonment.2. With a view to appreciate the controversy, a brief reference to the factual aspects will be necessary. PW-1 and PW-3 are respectively the father and the mother of PW-2 (the child who is the victim of the offence). The age of the child-PW-2 at the relevant time was eight years. The child/PW-2 was taking education in third standard. After returning from the school, the child-PW-2 used to visit the house of PW-5, who was running tuition classes. The child-PW-2 used to return around 07:30 p.m.3. On 20th October, 2010, the child-PW-2 did not return from the tuition class at usual hour. The case of the prosecution is that after the tuition class was over, while the child-PW-2 was walking back towards his home, a Maruti Car came there. Two persons (appellants-accused) came out and told the child-PW-2 that his father was going to purchase a car from them and, therefore, he should accompany them. Accordingly, the child-PW-2 got into the car and was kidnapped by the appellants-accused.4. The case of the prosecution is that on 20th October, 2010, from a particular cell phone number, there was a call received by PW-3 of a male person who informed her that he has kidnapped the child. He demanded ransom of Rs.5 lakhs for releasing the child. The PW-1 lodged a complaint on the same date in the night with the Police. PW-14 (who was running a shop in the locality) informed the PW-1 and PW-3 that he saw the child being taken in a Maruti Swift grey colour car.Accordingly, a First Information Report under Section 364A of IPC was registered. PW-19 is the Investigating Officer. As per the information received, PW-19 went to Pallikonda toll gate, Vellore District on 21st October, 2010. Around 12:00 noon, the car in question came towards the toll gate which was intercepted. In the car, the appellants-accused along with the child were found. PW-19 arrested the accused and rescued the child.5. The prosecution evidence, as can be seen from both the judgments, was in the form of the call records and the evidence of PW-1 to PW-3 and PW-19, the Investigating Officer. As far as the call records are concerned, we find that the entire evidence of the prosecution has been discarded by the High Court for want of a certificate as required under Section 65B of the Indian Evidence Act, 1872 (for short, "the Evidence Act").Submissions6. The learned senior counsel appearing for both the appellants have taken us through the evidence of the prosecution witnesses. Their submission is that there is absolutely no evidence regarding the demand of ransom or any threat being administered by the appellants-accused to kill the child or to put him to some harm.Therefore, the necessary ingredients of Section 364A of IPC have not been proved. By inviting our attention to the evidence of the child, who is PW-2, and, in particular, his cross-examination by the learned counsel representing the accused no.2, the learned senior counsel contended that the victim child was tutored by his father-PW-1 and, therefore, his testimony cannot be considered.7. The learned senior counsel appearing for the State submitted that this was a case where there was a reasonable apprehension in the mind of the PW-1 and PW-3 that the accused, who had kidnapped their son, may put their son to death or cause hurt to him. He would, therefore, submit that on the basis of the evidence of PW-1 and PW-3, the ingredients of Section 364A of IPC have been proved by the prosecution.Our View8. We have carefully considered the submissions. Firstly, we may refer to Section 361 of IPC which defines 'kidnapping from lawful guardianship'. It provides that whoever takes or entices any minor male child under sixteen years of age, out of the keeping of the lawful guardian of such minor, without the consent of such guardian, is said to kidnap such minor or person from lawful guardianship. In this case, there is no dispute about the lawful guardianship of PW-1 and PW-3. The kidnapping from lawful guardianship is made punishable under Section 363 of IPC and the maximum punishment is imprisonment of either description which may extend to seven years.9. Now, we turn to Section 364A of IPC which reads thus:"364a. Kidnapping for Ransom, Etc.-Whoever kidnaps or abducts any person or keeps a person in detention after such kidnapping or abduction, and threatens to cause death or hurt to such person, or by his conduct gives rise to a reasonable apprehension that such person may be put to death or hurt, or causes hurt or death to such person in order to compel the Government or any foreign State or international inter-governmental organisation or any other person to do or abstain from doing any act or to pay a ransom, shall be punishable with death, or imprisonment for life, and shall also be liable to fine."10. The first ingredient of Section 364A is that there should be a kidnapping or abduction of any person or a person should be kept in detention after such kidnapping or abduction. If the said act is coupled with a threat to cause death or hurt to such person, an offence under Section 364A is attracted. If the first act of kidnapping or abduction of a person or keeping him in detention after such kidnapping is coupled with such conduct of the person kidnapping which gives rise to a reasonable apprehension that the kidnapped or abducted person may be put to death or hurt, still Section 364A will be attracted. In the light of this legal position, now we refer to the evidence of the child-PW-2.11. We have carefully perused the evidence of the child-PW-2, who is the victim of the offence. At the relevant time, the age of the child was eight years. In the examination-in-chief, he has given vivid account of what exactly transpired at the time of the incident. He stated thus:"I had been getting back home around 07.00 'O' Clock at night, after attending the tuition, as usual. A Swift Car, in grey shade, bearing Reg.No.TN 05 V 7290, gave a halt by my side. There were two persons on board. They summoned me, stating that my father is going to buy a car. They took me on board. They sought the phone number of my father. I gave them my father's phone number 98840 49011.They asked my mother's number. I gave them my mother's phone number 98402 58273. Subsequently, I fell asleep in the car. When I got up in the morning, I found the car in a check post. The police got them napped. The persons who took me in the car as such are the accused who are present before this Court. The car is marked as M.O.1. The police questioned me. I have recounted the turn of events."12. We have carefully perused the cross-examination. On the main incident, his version has not been shaken in the cross-examination. It is true that in response to the questions put to him in the cross-examination by the Advocate appearing for the accused no.2, the child-PW-2 deposed that his father-PW-1 taught him the particulars which need to be reproduced in the Court and that he has recounted the particulars taught by his father before the Court.13. We find from the cross-examination of the child-PW-2 that there is hardly any challenge to the main incident. In fact, a suggestion was given to him that the men who had taken him in the car are the ones who were acquaintance with him and his father. This is the defence as reflected from the cross-examination.14. It is not brought on record by the accused that there was a prior enmity or animosity between the parents of the victim child and the accused. There was no reason for the father of the victim to falsely implicate the appellants and tutor the child to depose against them. Therefore, the case sought to be made out that the child was tutored by his father was not rightly accepted by the Courts below. Therefore, it can be said that the 'kidnapping' within the meaning of Section 361 of IPC was established by the prosecution. Hence, the appellants are guilty of the offence punishable under Section 363 of IPC.15. The learned senior counsel appearing for the appellants were at pains to point out inconsistent versions of PW-1 and PW-3 about who received the phone call demanding ransom. However, this issue need not detain us. The details of the phone call records were produced by the Police. It is an admitted position that the Police could not trace the name of the person who was holding the cell phone number stated by both, the PW-1 and PW-3, in their examination-in-chief. Their version is that they received the call demanding ransom from the said number.The record relating to the call details has been discarded by the High Court as there was no certification under Section 65B of the Evidence Act. The call records could have been the best possible evidence for the prosecution to prove the threats allegedly administered by the accused and the demand of ransom. Even taking the evidence of PW-1 and PW-3 as correct, all that is proved is that they received a phone call from someone for demanding ransom and the person threatened to kill their son in case ransom is not paid.However, the prosecution is not able to connect the alleged demand and the threat with both the accused. Therefore, the ingredients of Section 364A of IPC were not proved by the prosecution inasmuch as the prosecution failed to lead cogent evidence to establish the second part of Section 364A about the threats given by the accused to cause death or hurt to such person.In a given case, if the threats given to the parents or the close relatives of the kidnapped person by the accused are established, then a case can be made out that there was a reasonable apprehension that the person kidnapped may be put to death or hurt may be caused to him. However, in this case, the demand and threat by the accused have not been established by the prosecution.16. Therefore, the only conclusion is that the conviction of the appellants for the offence punishable under Section 364A of IPC will have to be set aside. However, there will be a conviction for the lesser offence of kidnapping defined by Section 361 of IPC, which is punishable under Section 363 of IPC.It is not in dispute that the appellants have undergone actual incarceration for a period of more than eight years. The maximum sentence for the offences punishable under Section 363 of IPC extends to seven years with fine. The appellants have undergone more than the maximum sentence prescribed.17. Before we part with the judgment, we must note here that the PW-19, the Investigating Officer, was not aware of the procedure to be followed for obtaining a certificate under Section 65B of the Evidence Act. He cannot be blamed as a proper training was not imparted to him. The State Government must ensure that the Police Officers are imparted proper training on this aspect.18. Therefore, the Appeals are partly allowed and the conviction and sentence of the appellants for the offence punishable under Section 364A of IPC is hereby quashed and set aside and it is held that the appellants are guilty of the offence punishable under Section 363 of IPC.As the appellants are in custody and as they have undergone maximum sentence for the offence punishable under Section 363 of IPC, we direct that they shall be forthwith set at liberty......................J. (Abhay S.Oka).....................J. (Ujjal Bhuyan)New Delhi;February 21, 2024. '
df= pandas.read_csv("C:/Users/devan/Desktop/work/law_websites/indian_kanoon/data.csv")
text=df['data'][0]
# print(text)
print("------------------------------")
# text=keep_alphabets_and_specific_chars(remove_extra_spaces(remove_non_ascii(text)))
text=transform_to_para1(text)
print(text)
print("------------------------------")
inputs = tokenizer.encode("summarize: " + text,return_tensors='pt',max_length=3000,truncation=True)
summary_ids = model.generate(inputs, max_length=1000, min_length=500, length_penalty=5, num_beams=2)
summary = tokenizer.decode(summary_ids[0])
print(summary)