

from __future__ import print_function
from nltk.chat.util import Chat, reflections
from news import caller


joke_list = []

pairs = (
  (r'(.*)(([Tt]ell)|([Ss]ay))(.*)([Jj]okes?)(.*)',
  ( 'Doctor: I am sorry but you suffer from a terminal illness and have only 10 to live. Patient: What do you mean, 10? 10 what? Months?Weeks? Doctor: Nine ',
    'Anton, do you think I am a bad mother? My name is Paul.',
    'My wife suffers from a drinking problem. Oh, is she an alcoholic? No, I am, but she is the one who suffers')),

  (r'(.*)(([Tt]ell)|([Ss]ay))(.*)((thought)s?|(quote)s?)(.*)',
  ( 'Somewhere, someone else is happy with less than you have.',
    'Knowing others is wisdom, knowing yourself is enlightment.',
    'Life is really simple but we insist on making it complicated.',
    'Only the wisest and stupidest of men never change.')),
  
   (r'why should i join svnit\?',
   ( "Because I am made by students studying over there :P",
     "It is 2nd best NIT in India." )),  
  
  (r'(.*)(([Tt]ell)|([Ss]ay)|(what))(.*)(news)(.*)',
  ( caller("http://feeds.bbci.co.uk/news/rss.xml",1),
    "You can also ask like news about science and environment etc",
    caller("http://feeds.bbci.co.uk/news/rss.xml",2))),

  (r'(news about science|environment)',
  ( caller("http://feeds.bbci.co.uk/news/science_and_environment/rss.xml",1),
    caller("http://feeds.bbci.co.uk/news/science_and_environment/rss.xml",2))),
  
  (r'(news about technology)',
  ( caller("http://feeds.bbci.co.uk/news/technology/rss.xml",1),
    caller("http://feeds.bbci.co.uk/news/technology/rss.xml",2))),

  (r'(news about (entertainment)|(arts?))',
  ( caller("http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml",1),
    caller("http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml",2))),

  (r'(news about business)',
  ( caller("http://feeds.bbci.co.uk/news/business/rss.xml",1),
    caller("http://feeds.bbci.co.uk/news/business/rss.xml",2))),
  
  (r'(news about health)',
  ( caller("http://feeds.bbci.co.uk/news/health/rss.xml",1),
    caller("http://feeds.bbci.co.uk/news/health/rss.xml",2))),

  (r'(news about education)',
  ( caller("http://feeds.bbci.co.uk/news/education/rss.xml",1),
    caller("http://feeds.bbci.co.uk/news/education/rss.xml",2))),

  (r'((.*)((you)(help)|(assist)|(service))(.*))|(I have doubts|query)',
  ( "I can tell you about SVNIT and I can tell you jokes.",
    "Try me!",
    "I can give you latest news and brigthen you with quirky thoughts.")),


  (r'(.*)(([Tt]ell)|([Ss]ay))?(.*)((Computer Engineering Department)|(Computer Department))(.*)',
  ( 'The Computer Engineering Department building is situated besides the Central Computer Center building.The students can pursue B.Tech,M.Tech and Ph.D. programs in Computer Engineering here.',
    'The mission of the Computer Engineering Department is to provide educational programs that would encourage students to read critically, reason analytically, communicate persuasively, apply professionally and prepare them to excel in the field of computing.',)),

  (r'(.*)(([Tt]ell)|([Ss]ay))?(.*)((Chemical Engineering Department)|(Chemical Department))(.*)',
  ( 'The Chemical Engineering Department building is situated opposite to the Computer Engineering Department building.The students can pursue B.Tech,M.Tech and Ph.D. programs in Chemical Engineering here ',
    'The mission of the Chemical Engineering department is to be one of the top engineering departments with excellent research work in the fields related to Chemical Engineering and offering technical know how to the stake holders ',)),

(r'(.*)(([Tt]ell)|([Ss]ay))?(.*)((Electronics Engineering Department)|(Electronics Department))(.*)',
  ( 'The Electronics Engineering Department building is situated opposite to the Computer Engineering Department building.The students can pursue B.Tech,M.Tech and Ph.D. programs in Electronics Engineering here. ',
    'The mission of the Electronics Engineering Department is to contribute to society and industry through excellence in education, research, innovations and ethics by stakeholders. ',)),

(r'(.*)(([Tt]ell)|([Ss]ay))?(.*)((Electrical Engineering Department)|(Electrical Department))(.*)',
  ( 'The Electrical Engineering Department building is situated opposite to the Administrative building.The students can pursue B.Tech,M.Tech and Ph.D. programs in Electrical Engineering here. ',
    'The mission of the Electrical Engineering Department is To be a global centre of excellence in technical education and innovation producing competent professionals with integrity. ',)),

(r'(.*)(([Tt]ell)|([Ss]ay))?(.*)((Mechanical Engineering Department)|(Mechanical Department))(.*)',
  ( 'The Mechanical Engineering Department building is situated besides the New CRC building.The students can pursue B.Tech,M.Tech and Ph.D. programs in Mechanical Engineering here. ',
    'The mission of the Mechanical Engineering Department is to provide educational programs that would encourage students to read critically, reason analytically, communicate persuasively, apply professionally ',)),

(r'(.*)(([Tt]ell)|([Ss]ay))?(.*)((Civil Engineering Department)|(Civil Department))(.*)',
  ( 'The Civil Engineering Department building is situated besides the New CRC building.The students can pursue B.Tech,M.Tech and Ph.D. programs in Mechanical Engineering here ',
    'The mission of the Civil Engineering Department is To provide excellent education producing technically competent, globally employable civil engineers who will be leaders in the chosen field and to undertake research in conventional and advanced technologies fulfilling the needs and challenges of modern society. ',)),
  
(r'(.*)(([Tt]ell)|([Ss]ay))?(.*)((MSC Department)|(MSC))(.*)',
  ( 'Students can pursue M.Sc. In Physics/Chemistry/Mathematics.It is an five year integrated course ',
    'The department also offers Ph.D. programs and basic research activities are carried out in the various emerging areas. ',)),

(r'(.*)(([Tt]ell)|([Ss]ay))(.*)((SVNIT\b)|(NIT Surat))(.*)',
  ( 'The National Institute of Technology, Surat, formally known as Sardar Vallabhbhai National Institute of Technology or SVNIT, is an engineering institute of higher education established by the Parliament of India in 1961.',
    'To be a globally accepted centre of excellence in technical education catalyzing absorption, innovation, diffusion and transfer of high technologies resulting in enhanced quality for all the stake holders ',)),

(r'(.*)(([Tt]ell)|([Ss]ay))?(.*)((MTB)|(Mother Teresa Bhavan)|(Girls Hostel))(.*)',
  ( 'Only girls hostel in college with capacity of 865 inmates.',
    'Food you find here is more delicious than other hostels.')),

(r'(.*)(([Tt]ell)|([Ss]ay))?(.*)((SVB)|(Swami VIvekanada Bhavan))(.*)',
  ( 'Boys hostel for final year and third year students.',
    'It is the biggest hostel in institute.')),

(r'(.*)(([Tt]ell)|([Ss]ay))?(.*)((Narmad Bhavan))(.*)',
  ( 'It is a guest house in campus for visitors outside of the college.It is behind Mother Teresa Bhavan.',
    'It has 2 floors and AC and Non AC double bed rooms. Terrifs are subsidised by institute.')),

(r'(.*)(([Tt]ell)|([Ss]ay))?(.*)((Raman Bhavan))(.*)',
  ( 'It is a hostel for PHD students with their family.',
    'It is in front of swami vivekanand bhavan.')),
    
(r'(.*)(([Tt]ell)|([Ss]ay))?(.*)((Nehru Bhavan))(.*)',
  ( 'It is a hostel for M.Sc. students. It has 3 floors.',
    'Festival of Janmashtmi is celebrated here every year.')),

(r'(.*)(([Tt]ell)|([Ss]ay))?(.*)((Gajjar Bhavan))(.*)',
  ( 'It is a hostel for 1st year B. tech students with double occuopancy. It has 5 wings.',
    'It is in right far corner of the college. It is very far from academic buildings.')),

(r'(.*)(([Tt]ell)|([Ss]ay))?(.*)((Bhabha Bhavan))(.*)',
  ( 'It is a hostel for 3rd year and 2nd year B. tech students with double occuopancy. It has 8 floors. ',
    'It is one of the most beuatiful building of the college.')),

(r'(.*)(([Tt]ell)|([Ss]ay))?(.*)((Sarabhai Bhavan))(.*)',
  ( 'It is a hostel for M. tech students. It is a small old building near girls hostel.',
    'Festival of Shivratri is celebrated here every year.')),

(r'(.*)(([Tt]ell)|([Ss]ay))?(.*)((New CRC))(.*)',
  ( 'It is newly built class room complex with 8 floors. It has classrooms ,drawing halls and seminar hall. All the first year students attend classes in this building. It is beside mechanical department.',
    'It is newly built class room complex with 8 floors. It has classrooms ,drawing halls and seminar hall. All the first year students attend classes in this building. It is beside mechanical department.')),

 (r'(.*)(([Tt]ell)|([Ss]ay))?(.*)((Old CRC))(.*)',
  ( 'It is old classroom complex with 2 floors. It is in front of civil department. Civil engineering students attend some classes there.',
    'It is old classroom complex with 2 floors. It is in front of civil department. Civil engineering students attend some classes there.')),

 (r'(.*)(([Tt]ell)|([Ss]ay))?(.*)((SAC Ground))(.*)',
  ( 'It is student activity center where there is indoor as well as outdoor games facilities are provided for example basketball and tennis courts, badminton courts,chess,caroms. There is also a Gym there.',
    'It is student activity center where there is indoor as well as outdoor games facilities are provided for example basketball and tennis courts, badminton courts,chess,caroms. There is also a Gym there.')),

 (r'(.*)(([Tt]ell)|([Ss]ay))?(.*)((Canteen))(.*)',
  ( 'It is located in front of New CRC. A wide variety of dishes from south indian to chinese food as well as some fast food varieties are available here. During lunch time meals are available at nominal rates.',
    'It is located in front of New CRC. A wide variety of dishes from south indian to chinese food as well as some fast food varieties are available here. During lunch time meals are available at nominal rates.')),

 (r'(.*)(([Tt]ell)|([Ss]ay))?(.*)((CCC)|(Central Computer Center))(.*)',
  ( 'Central Computer Center primarily caters to the Internet Access requirements throughout the institute as wellas Campus-wide network connectivity throughout the campus. It has many computer labs too. It is in between Computer Engineering Department and Applied Mathematics and Huminities Department.',
    'Central Computer Center primarily caters to the Internet Access requirements throughout the institute as wellas Campus-wide network connectivity throughout the campus. It has many computer labs too. It is in between Computer Engineering Department and Applied Mathematics and Huminities Department.')),

 (r'(.*)(([Tt]ell)|([Ss]ay))?(.*)((TNP)|(Training and Placement))(.*)',
  ( 'TNP office is in CADLAB. Training and Placement Office arrange and coordinates placements of all final year students. It also try to arrange internship for pre final year students.',
    'TNP office is in CADLAB. Training and Placement Office arrange and coordinates placements of all final year students. It also try to arrange internship for pre final year students.')),

 (r'(.*)(([Tt]ell)|([Ss]ay))?(.*)((Staff Quarter))(.*)',
  ( 'Faculties of institute reside inside staff quarter. Two buildings with 3 BHK apartments are built recently for quarter.',
    'Faculties of institute reside inside staff quarter. Two buildings with 3 BHK apartments are built recently for quarter.')),

 (r'(.*)(([Tt]ell)|([Ss]ay))?(.*)((SBI))(.*)',
  ( 'Institute has one bank and 2 ATMS near main gate. SBI is regaular branch in campus for students and employees of institute.',
    'Institute has one bank and 2 ATMS near main gate. SBI is regaular branch in campus for students and employees of institute.')),

 (r'(.*)(([Tt]ell)|([Ss]ay))?(.*)((Admin))(.*)',
  ( 'It is administrative centre that manages students records, fee collection, course registration ,scholarship etc.',
    'It is administrative centre that manages students records, fee collection, course registration ,scholarship etc.')),

 (r'(.*)(([Tt]ell)|([Ss]ay))?(.*)((Library))(.*)',
  ( 'It is one amongst major technological libraries in area of science, engineering and technological libraries in the area of science, engineering and technology. It has a rich collection of resources in electronic media available locally on the Institute Intranet and accessible on the Web.',
    'It is one amongst major technological libraries in area of science, engineering and technological libraries in the area of science, engineering and technology. It has a rich collection of resources in electronic media available locally on the Institute Intranet and accessible on the Web.')),

 (r'(.*)(([Tt]ell)|([Ss]ay))?(.*)((Dispensary))(.*)',
  ( 'It is a full-fledged OPD unit managed by one full time Recidential doctor, six Hon. visiting Medical Consultants namely physician, Gynaecologist, Paediatrician, Radiologist etc. Timings: On Working days:- Morning :8:30 am to 1:00 pm, Evening: 4:00 pm to 7:30 pm',
    'It is a full-fledged OPD unit managed by one full time Recidential doctor, six Hon. visiting Medical Consultants namely physician, Gynaecologist, Paediatrician, Radiologist etc. Timings: On Working days:- Morning :8:30 am to 1:00 pm, Evening: 4:00 pm to 7:30 pm')),
 

  (r'(How are you)',
  ( "How do you suppose?",
    "Perhaps you can answer your own question.",
    "I am fine. Thankyou. Enough about me. You say what else is new?")),

  (r'thats (good|bad|interesting|new|unique)',
  ( "I feel same too!",
    "What? It completely feels opposite.")),
    
 (r'quit|bye|goodbye',
  ( "Thank you for talking with me.",
    "Good-bye.",
    "Adios.",
    "Have a good day!")),


  (r'Hello|Hi|Hola|Hey',
  ( "Hello... I am Gini.",
    "Oh good, somebody else to talk to. Joy.",
    "Hello? How original...",
    "I suppose I should say hello now."
    "Hi there... how are you today?",
    "Hey how can I help you?")),

 

  (r'(.*) friend (.*)',
  ( "Good to know.",
    "Thanks for sharing.")),

  (r'Yes',
  ( "You seem quite sure.",
    "OK.")),

  (r'(.*) computer(.*)',
  ( "Are you really talking about me?",
    "Does it seem strange to talk to a computer?",
    "How do computers make you feel?",
    "Do you feel threatened by computers?")),
 
  

  (r'(.*)\?',
  ( "I suppose I dont have enough information about that.",
    "Please consider whether you can answer your own question.",
    "It is confidential dear.")),

 
  (r'(.*)',
  ( "Please tell me more.",
    "Let's change focus a bit... Ask me something else.",
    "Can you be specific?",
    "Very interesting."))
)

gini_chatbot = Chat(pairs, reflections)

def gini_chat():
    print("--------------------------------------------------------------------")
    print("Talk to the program by typing in plain English, using normal upper-")
    print('and lower-case letters and punctuation.  Enter "quit" when done.')
    print('='*72)
    print("Hello. My name is GINI. How can I help you?")

    gini_chatbot.converse()

def demo():
    gini_chat()

if __name__ == "__main__":
    demo()
