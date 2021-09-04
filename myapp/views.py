from django.shortcuts import render
from .models import *
from .forms import Messages
import json
# Create your views here.
import spacy
from spacy.matcher import Matcher
from spacy.util import filter_spans

from django.core.files.storage import FileSystemStorage
import time

def index(request):
    form = Messages()
    return render(request, 'index.html', {'form': form, 'button': 'show'})


import json 
import xmltodict
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import re
from bs4 import BeautifulSoup
from xml.dom import minidom



def submit(request):
    import json
    # check if the request is POST means it is from the input form
    if request.method=="POST":
        data=Messages(request.POST)
        time.sleep(2)
        if 1:
            options = webdriver.FirefoxOptions()
            options.headless = True
            # gz_data = minidom.parse(request.FILES['document'])  
            # gz_data = gz_data.toprettyxml()
            # gz_data = '<mxfile host="app.diagrams.net" modified="2021-03-30T18:07:44.134Z" agent="5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36" etag="656GnPVzddndN2rW8mCB" version="14.5.1" type="device"><diagram id="C5RBs43oDa-KdzZeNtuy" name="Page-1">7VhtU+IwEP41fOSGtqD40YJ6L56jp6f3NbShzZlme2kQ8dffpk1oSxWK6DneOMMwzZPNJtnn2WQnHW+U3J9IksbfIaS84/bC+4437rju0O3jvwYWBdD3vAKIJAsLyCmBS/ZADdgz6IyFNKsZKgCuWFoHAxCCBqqGESlhXjebAq/PmpKINoDLgPAmesNCFdtt7Zf4Z8qi2M7s7B0UPQmxxmYnWUxCmFcg76jjjSSAKr6S+xHlOnY2LjdfFjf89Hbv5OtF9of89L9dnV13C2fH2wxZbkFSoZ7t+uF2evz5uv/7V3p+fDHvnRxOvnbNkN4d4TMTr5TKDITZsVrYMGZzlnAisOVPQahL04NB8AlnkcDvAFdHJQJ3VCqGDByaDgUpokHMeHhKFjDTe8gUCW5ty49Bsgd0Szh2OQhgt1RGTO5ezeJSj0S4h6ikGdqc28A4S+iUZMrYBMA5STM2yResTRIiIyZ8UAoS6whmIqShaS2ZzhtKwu1SO3p8SzoMbToa9L4iRkPPCYWEKrlAE9O7VJpJNce256VwnT2DxVXRekOTMCZZoqXv5XQ/MLmIiDAI5Xzeynz9lvMhI7XpCEfiBVHU12HMqjLEj8pWSygX5xZCdRpCPSMJbcgUI60qkuR0qp4UZJaSgInoNLcZ90vkh9mphgDHTnkuhpiFIRW5WBRRpNCTVkgKTKg8FAMffxiwUe/ToDPABY2w7ZRt/GlzqUYgUFeE5QKiKNY51YJ9RFpr03aztBZ1xrZltiqkGqXb8uc1+DuM/j/61hwjsUq4+XwtkgfuG5Pcb5DcYJiz/A4x0XAePV830J8gkdqd5ftKy2HcdRqa8Jqa8B7hn5MJ5eeQMcVA+5eF7You3ipz94ftSF1zA+zEqbPfIJU8krlP1Ae9j/rg5eqDQW/4vPoA0efUB4PBO6oPDhoyHeOEiMAU/3wmccUf102bRH8/RYXbrCo+LpydaW1bRrzWjWPlso5VKsJD/TiALUjzNNtwJtdTBYcfM24FQcOI2guL8gnMj0rAzwHssKLY+nzPYCYDurkkwBstom2Y1Mttc13oU6R6fPfNgiTlRLG7+vvImpvhXMuydOsNV26FA7fuotiwGVV9kFhxNOhvcFREZLOj7oojb8UPTKcZrbl4qVvHbRZHlvVSq3nFUUn/DafNxNQdxTHhYzET5eIdAQesnsYCyiqrKIAct/1xYJPLPLeZZXWWTw/tq5HujnKyqvxnXA134Moe0e+VrJdJ/e5+/UDZnTpslg+ohXn5Cu0d/QU=</diagram></mxfile>'
            strr = ""
            gz_data = minidom.parse(request.FILES['document'])
            xz_data = gz_data
            gz_data = gz_data.toprettyxml()
            driver = webdriver.Firefox(executable_path=r'/home/abdul/Documents/Django-and-Spacy-for-NLP-master-main/geckodriver', options=options)
            #driver = webdriver.Firefox(executable_path=r'/home/abdul/Documents/Django-and-Spacy-for-NLP-master-main/geckodriver')
            url = 'https://jgraph.github.io/drawio-tools/tools/convert.html'
            driver.get(url)
            inputElement = driver.find_element_by_id('textarea')
            inputElement.send_keys(str(gz_data))
            driver.find_element_by_xpath('/html/body/form/button[5]').click()
            textbox = driver.find_element_by_id('textarea')
            strr = textbox.get_attribute('value')
            #strr = gz_data
            print(strr)
            soup = BeautifulSoup(strr, 'html.parser')

            links = []
            # for x in soup.find_all('mxcell', value=True):
            # # print(x['id']+'\t'+x['value'])
            #   links.append(x)
            classess = []
            iis = []
            arrows = []
            for link in soup.find_all(style=re.compile("swimlane")):
                classess.append(link['value'])
                print("THIS IS: "+  str(link['id']))
                iis.append(link['id'])

            asocs = []
            for link in soup.find_all(style=re.compile("resizable")):
                asocs.append(link['id'])

            fromm = []
            to = []

            for link in soup.find_all(style=re.compile("endArrow")):
                print("arrow"+link['id'])
                arrows.append(link['id'])
                to.append(link['target'])



            all_attribs = []
            global not_all_attribs
            not_all_attribs = []
            brits = []
            the_functions = []
            for i in range(0, len(iis)):
                for child in soup.find_all(style=re.compile("eastwest")):
                    if child['parent'] == iis[i]:
                        all_attribs.append(child['value'])

            for i in range(1, len(iis)):
                for child in soup.find_all(style=re.compile("eastwest")):
                    if child['parent'] == iis[i]:
                        print('gross'+iis[i]+' '+child['value'])
                        brits.append(child['value'])

            from_asoc = []
            to_asoc = []
            for i in range(0, len(to)):
                for child in soup.find_all(style=re.compile("swimlane")):
                    from_asoc.append(classess[0])
                    if child['id'] == to[i]:
                        to_asoc.append(child['value'])
            final_val_asoc = list(zip(from_asoc, to_asoc))
            print(json.dumps(final_val_asoc))

            for child in soup.find_all(style=re.compile("text")):
                if child['parent'] == iis[0]:
                    print('brass'+iis[i]+' '+child['value'])
                    the_functions.append(child['value'])
            global clean_functions
            clean_functions = []
            clean = ""
            for w in the_functions:
                for character in w:
                    if character.isalnum():
                        clean += character
                clean_functions.append(clean.lower())
                clean = ""
            final_asociations = []
            asociations1 = []
            final_1_asociations = []
            asociations2 = []
            a_count = 0
            for i in range(0, len(arrows)):
                for child in soup.find_all(style=re.compile("resizable=0")):
                    if child['parent'] == arrows[i]:
                        if a_count%2==0:
                            asociations2.append(child['value'])
                        else:
                            asociations1.append(child['value'])
                    a_count = a_count+1
                a_count=0
            print(str(len(asociations1))+" "+str(len(asociations2)))
            final_1_asociations = list(zip(asociations1, asociations2))
            final_asociations = list(zip(final_val_asoc, final_1_asociations))
            import json
            



            print(json.dumps(clean_functions))
            all_attribs = list(set(all_attribs))
            #ot_all_attribs = list(set(not_all_attribs))
            for i in brits:
                if i not in not_all_attribs:
                    not_all_attribs.append(i)
            all_attribs.remove('')
            not_all_attribs.remove('')

            print('not_all_attribs: '+str(not_all_attribs))

            print('atribbs:' + str(all_attribs))
            # reading the xml file input
            # xmldoc = minidom.parse(request.FILES['document'])
            xmldoc = xz_data
            # reading all the object tags in the XML
            itemlist = xmldoc.getElementsByTagName('object')
            finallist = []
            # finding all the class names
            for s in itemlist:
                finallist.append(s.getAttribute("label"))
                # print(s.getAttribute("value"))
            
            # finding all the attributes from the XML diagram
            itemlist = xmldoc.getElementsByTagName('mxCell')
            allValues = []
            for s in itemlist:
                allValues.append(s.getAttribute("value"))
            
            # removing the Function from the class names
            itemlist = xmldoc.getElementsByTagName('object')


            functions = []
            for s in itemlist:
                if s.getAttribute("property")=='func' or s.getAttribute("Property")=='func':
                    functions.append(s.getAttribute("label"))
            for s in finallist:
                if s in functions:
                    finallist.remove(s)
            for s in finallist:
                if s in functions:
                    finallist.remove(s)
            for s in finallist:
                if s in functions:
                    finallist.remove(s)
                
                    
            # print(finallist)
            # classess.append('height')
            finallist = classess
            associations=[]
            attributes = []
            # filtering the associations (example like 1,1) and attributes from all the MxCell tag in the XML diagram
            for el in allValues:
                try:
                    associations.append(int(el))
                except ValueError:
                    if el != '':
                        if '\n' in el:
                            el = el.replace('\n', ',')
                        if '-' in el:
                            el = el.replace('-', '')
                        
                        attributes.append(el)
            if '*' in allValues:
                associations.append('*')
            
            # Code for Nouns extraction using Spacy
            nlp = spacy.load('en_core_web_sm')
            A_np = []
            doc = nlp(request.POST.get('sentence'))
            nouns = []
            for np in doc.noun_chunks:
                    nouns.extend([token.text for token in np])

            #new work
            finale = []
            new_sentence = str(doc)
            seperated = new_sentence.split(" and ")
            for senn in seperated:
                finale.append(senn.split(" or "))

            

            #new work
        #   Code for Nouns extraction using Spacy
            
            nlp2 = spacy.load('en_core_web_sm') 

            sentence = request.POST.get('sentence')
            pattern = [{'POS': 'VERB', 'OP': '?'},
                       {'POS': 'ADV', 'OP': '*'},
                       {'POS': 'AUX', 'OP': '*'},
                       {'POS': 'VERB', 'OP': '+'}]


            # instantiate a Matcher instance
            matcher = Matcher(nlp2.vocab)
            matcher.add("Verb phrase", [pattern])

            doc = nlp2(sentence) 
            # call the matcher to find matches 
            matches = matcher(doc)
            spans = [doc[start:end] for _, start, end in matches]
            
            listofwords = sentence.split()
            model = Customized._meta.get_field('value')
            customized_sentence = sentence
            
            # replacing single words in the input sentence for SBVR sentence
            for word in listofwords:
                try:
                    obj = Customized.objects.get(value=word)
                    field_value = getattr(obj, 'key')
                    customized_sentence = sentence.replace(word,field_value)
                    # print(field_value)
                except:
                    pass
            

            condition=''
            pointer = 0
            value=''
            # replacing phrases (example: more than) in the input sentence for SBVR sentence
            for i,k in zip(listofwords[0::2], listofwords[1::2]):
                
                try:
                    phrase = str(i+' '+k)
                    obj = Customized.objects.get(value=phrase)
                    field_value = getattr(obj, 'key')
                    customized_sentence = customized_sentence.replace(phrase,field_value)
                except:
                    pass
                # print(i+k)
            
            finallist = [x.lower() for x in finallist]
            common1 = list(set(finallist).intersection(spans))
            common2 = list(set(finallist).intersection(nouns))
            common = len(common1)+len(common2)
            notmatch=[]
            finallist = [each_string.lower() for each_string in finallist]

            for s in finallist:
                if s in sentence.lower():
                    pass
                else:
                    notmatch.append(s)
            
            sentence_check='hello'
            if len(notmatch)<1 and (len(nouns)>=1 and len(spans)>=1):
                process='on'
                flag='show'
                sentence_check='on'
            elif len(nouns)<1 or len(spans)<1:
                process='off'
                flag='dont'
                sentence_check='off'
            else:
                process = 'off'
                flag='dont'

            # Removing Articles from Nouns
            # if 'The' in nouns:
            #     nouns.remove('The')
            # if 'a' in nouns:
            #     nouns.remove('a')
            # if 'an' in nouns:
            #     nouns.remove('an')
            # if 'A' in nouns:
            #     nouns.remove('A')
            # if 'An' in nouns:
            #     nouns.remove('An')

            for el in nouns:
                try:
                    if el.isdigit():
                        nouns.remove(el)
                except:
                    pass

            for i in range(0, len(attributes)):
                attributes[i] = attributes[i].lower()
            for x in attributes:
                if attributes.count(x) > 1:
                    attributes.remove(x)
            finallist = classess
            # replacing the SBVR sentence according to the phrases in the admin panel / database 
            return render(request,'index.html',{'sentence':request.POST.get('sentence') ,'pos':zip(nouns,spans),'nouns':nouns, 'verbs': spans,'value':value,'condition':condition, 'flag':flag,'button':"Convert To SBVR", 'process': process,'sentence_check': sentence_check,'classnames':finallist,'associations':final_asociations,'notmatch':notmatch,'customized_sentence':customized_sentence,'attributes':all_attribs,'attribs':not_all_attribs})
        # 'button':'It is necessary '+str(customized_sentence)
        else:
            data=Messages()
            respond='Your Message has been sent successfully!'
            return render(request,'index.html',{'response':response})
    respond='Send Message'
    context = {
        'response' : response
        }
    return render(request, 'index.html', context)

def sbvr(request):
    response = 'testing'
    # sleep time
    time.sleep(3)
    # takes the sentence input from the GET request
    sentence = request.GET.get('sentence')
    # spilt the sentence words in a list
    listofwords = sentence.split()
    # find the value in the CUstomized model from the database
    model = Customized._meta.get_field('value')
    # initially the SBVR customized sentence is same as the input sentence
    customized_sentence = sentence
    
    # replacing the SBVR sentence according to the keywords in the admin panel / database
    for word in listofwords:
        try:
            obj = Customized.objects.get(value=word)
            field_value = getattr(obj, 'key')
            customized_sentence = sentence.replace(word,field_value)
            # print(field_value)
        except:
            pass

    # replacing the SBVR sentence according to the phrases in the admin panel / database 
    for i,k in zip(listofwords[0::2], listofwords[1::2]):
        
        try:
            phrase = str(i+' '+k)
            # print(phrase)
            obj = Customized.objects.get(value=phrase)
            field_value = getattr(obj, 'key')
            # print(field_value)
            customized_sentence = customized_sentence.replace(phrase,field_value)
        except:
            pass
    print(customized_sentence)
    print(sentence)
    atribabes = not_all_attribs
    print('atribabes: '+str(atribabes))
    # rendering the output with all the values passed as context
    return render(request,'index.html',{'sentence':sentence ,'button':"Generate OCL", 'customized_sentence':request.GET.get('customized_sentence'),'condition':request.GET.get('condition'),'value':request.GET.get('value'),'classnames': request.GET.get('classnames'),'atr': request.GET.get('attribs')})
       
import ast
def ocl(request):
    # sleep time
    time.sleep(3)
    condition=''
    value=''

    # picks the sentence from the GET request
    listofwords = request.GET.get('sentence')
    listofwords = listofwords.split()

    finale = []
    atr = not_all_attribs
    print(type(atr))
    new_sentence = request.GET.get('sentence')
    seperated = new_sentence.split(" and ")

    for senn in seperated:
        finale.append(senn.split(" or "))

    
    #finale[1][0] = "Person "+finale[1][0]

    print(str(finale))
    a_func = []
    print("WORDS: "+str(listofwords))
    for i in range(0, len(listofwords)):
        if(listofwords[i] == "to"):
            a_func.append(listofwords[i+1])

    import json
    print("a_func: "+json.dumps(a_func))



    # finalizing the condition and value of invariant depending on the conditional input in the SBVR sentence
    check='no'
    for word in listofwords:
        try:
            if str(word) == 'greater than':
                condition='>'
                value=k
                check='yes'
                # print(str(i+' '+k))
            elif str(word) == 'atleast':
                condition='>='
                value=k
                check='yes'
                # print(str(i+' '+k))
            elif str(word) == 'less than':
                condition='<'
                value=k
                check='yes'
                # print(str(i+' '+k))
            elif str(word) == 'atmost':
                condition='<='
                value=k
                check='yes'
                # print(str(i+' '+k))
            elif str(word) == 'exactly':
                condition='='
                value=k
                check='yes'
                # print(str(i+' '+k))
            elif str(word) == 'morethan one':
                condition='>'
                value=k
                check='yes'
                # print(str(i+' '+k))

        except:
            pass
            

    for i,k in zip(listofwords[0::2], listofwords[1::2]):
        try:
            if str(i+' '+k) == 'greater than' or str(i+' '+k) == 'more than':
                condition='>'
                value=k
                print(str(i+' '+k))
            elif str(i) == 'atleast':
                condition='>='
                value=i
                print(str(i+' '+k))
            elif str(i+' '+k) == 'less than':
                condition='<'
                value=k
                print(str(i+' '+k))
            elif str(i) == 'atmost':
                condition='<='
                value=i
                print(str(i+' '+k))
            elif str(i) == 'exactly':
                condition='='
                value=i
                print(str(i+' '+k))
            elif str(i+' '+k) == 'more than':
                condition='>'
                value=str(i+' '+k)
                check='yes'
                print(str(i+' '+k))
            
        except:
            pass
        vals = []
        iinvariant = []
        setart = 1
        celas = request.GET.get('classnames')
        for jj in range(0, len(finale)):
            listmist = str(finale[jj]).split()
            for i,k in zip(listmist[0::2], listmist[1::2]):
                try:
                    if str(i+' '+k) == 'greater than' or str(i+' '+k) == 'more than':
                        condition='>'
                        value=k
                        print(str(i+' '+k))
                    elif str(i) == 'atleast':
                        condition='>='
                        # print("BARA BARA: "+str(listmist))

                        value=i
                        print(str(i))
                    elif str(i+' '+k) == 'less than':
                        condition='<'
                        value=k
                        print(str(i+' '+k))
                    elif str(i) == 'atmost':
                        condition='<='
                        value=i
                        print(str(i+' '+k))
                    elif str(i) == 'exactly':
                        condition='='
                        value=i
                        print(str(i+' '+k))
                    # elif str(i+' '+k) == 'more than':
                    #     condition='>1'
                    #     value=str(i+' '+k)
                    #     check='yes'
                    #     print(str(i+' '+k))

                    
                except:
                    pass
            iinvariant.append(condition)
            print('val'+str(value))
            vals.append(listmist[listmist.index(value) + 1])
            for one in range(1, len(celas)):
                if celas[one] in finale[jj]:
                    hexxo = celas[one]

    print(str(atr))
    sixx = request.GET.get('classnames')
    seven = sixx.strip("'")
    clasas = seven.strip('][').split(', ')
    res = sixx.strip('][').split(', ')
    print("seven:"+json.dumps(seven))
    res.pop(0)
    let_alone = []
    if len(a_func)==len(clasas)-1 and a_func[0] in clean_functions:
        jigsaw = zip(res, iinvariant , vals, a_func)
        gauge = 0
        value= listofwords[listofwords.index(value) + 1]
    else:
        for i in range(0, len(clasas)-1):
            let_alone.append(clasas[0])
        jigsaw = zip(res, iinvariant , vals, let_alone)
        gauge=1
        value= listofwords[listofwords.index(value) + 1]
    print('value '+ str(value))
    print('invariant' + str(iinvariant))
    print('func' + str(a_func))
    print('condition '+ str(condition))

    # rendering the output with all the values passed as context
    return render(request,'index.html',{'sentence': request.GET.get('sentence') ,'button':"Try A New Sentence?", 'customized_sentence': request.GET.get('customized_sentence'),'condition':iinvariant,'value':vals,'classnames': ast.literal_eval(request.GET.get('classnames')), 'gauge': gauge, 'jigsaw': jigsaw, 'ranger': range(2)})
  