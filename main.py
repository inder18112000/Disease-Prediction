# Welcome to hackathone code
# Here we trying to build an small application on Disease symptoms tracker and also display method to cure it
from tkinter import *
from tkinter.messagebox import showerror, showinfo

import pandas

import connection
import otp
from datetime import datetime


class login:
    def gen_otp(self):
        self.str10=otp.send(self.txt3.get())
    def press(self):
        if str(self.str10) == str(self.txt4.get()):
            conn = connection.Connect()
            cr = conn.cursor()
            q1 = 'insert into disease_symtoms (name,age,gender,email,time) values("{}","{}","{}","{}","{}")'.format(
                str(self.txt1.get()), str(self.txt2.get()), str(self.r.get()), self.txt3.get(), str(datetime.now().strftime("%H:%M:%S")))

            cr.execute(q1)
            conn.commit()
            showinfo("Welcome", "Welcome to disease predictor...")
            
            self.root.destroy()
            disease_prediction()
        elif str(self.txt4.get()) == "":
            showerror("Error", "Please enter otp...")
        else:
            showerror("Error", "Please enter correct otp !")
    def __init__(self):

        # THIS IS OUR MAIN WINDOW/LOGIN SCREEN
        self.root = Tk()
        self.root.state("zoomed")

        self.root.geometry("1550x766")
        self.root.title("DISEASE PREDICTOR")
        self.photo = PhotoImage(file = "logo.png")
        self.root.iconphoto(False, self.photo)
        self.open = PhotoImage(file = "front_login.png")
        self.front_label1 = Label(self.root, image = self.open)
        self.front_label1.place(x = 0, y = 0)


        self.bf1 = Frame(self.root, padx = 20, pady = 20, bg = "white", height = 40, width = 60)
        self.bf1.place(x = 150, y =50)

        Label(self.bf1, text = "Enter User's Detail", font = ('Cambria',24, 'bold')).grid(row = 0, column = 0,columnspan=4, padx = 5, pady = 10)

        Label(self.bf1, text = 'NAME', font = ('Cambria', 14, 'bold')).grid(row = 1, column = 0, padx = 5, pady = 10)

        self.txt1 = Entry(self.bf1, font = ('Cambria', 14, 'bold'), width = 40)
        self.txt1.grid(row = 1, column = 1,columnspan=3, pady = 10)
        Label(self.bf1, text = 'AGE', font = ('Cambria', 14, 'bold')).grid(row = 2, column = 0, padx = 5, pady = 10)
        self.txt2 = Entry(self.bf1, font = ('Cambria', 14, 'bold'), width = 40)
        self.txt2.grid(row = 2, column = 1,columnspan=3, pady = 10)

        Label(self.bf1, text = 'GENDER', font = ('Cambria', 14, 'bold')).grid(row = 3, column = 0, padx = 5,
                                                                                 pady = 10)
        self.r = StringVar()
        self.r.set(NONE)
        Radiobutton(self.bf1, text = "Male", font = ('arial', 14, 'bold'),
                    variable = self.r,
                    value = "Male").grid(row = 3, column = 1, padx = 5,
                                                                                      pady = 1)
        Radiobutton(self.bf1, text = "Female", font = ('arial', 14, 'bold'), variable = self.r,
                    value = "Female").grid(row = 3, column = 2, padx = 5,
                                                    pady = 1)
        Radiobutton(self.bf1, text = "Others", font = ('arial', 14, 'bold'), variable = self.r,
                    value = "Others").grid(row = 3, column = 3, padx = 5,
                                                                pady = 1)




        Label(self.bf1, text = 'E-mail', font = ('Cambria', 14, 'bold')).grid(row = 4, column = 0, padx = 5, pady = 10)

        self.txt3 = Entry(self.bf1, font = ('Cambria', 14, 'bold'), width = 40)
        self.txt3.grid(row = 4, column = 1, columnspan = 3, pady = 10)

        # self.log_butt = Button(self.bf1, text = 'Login', font = ('arial', 16, 'bold'), bg="#4267B2", fg="white",width = 20)
        # self.log_butt.grid(row=3, column=0, columnspan=2, pady=25)
        # Button(self.bf1, text = 'Forgot Password', font = ('arial', 16, 'bold'), relief=FLAT, bg = "orange", fg = "white", width = 20).grid(row = 4, column = 0, columnspan = 2)

        Button(self.bf1, text = 'Generate OTP', borderwidth = 2
        , font = ('Cambria', 14, 'bold'), bg = "orange", fg = "white", width = 20,command=self.gen_otp).grid(row = 5, column = 0, columnspan = 4, pady = 10)

        Label(self.bf1, text = 'ENTER OTP', font = ('Cambria', 16, 'bold'),width=20).grid(row = 6, column = 0,columnspan=2, padx = 5, pady = 10)
        self.txt4 = Entry(self.bf1, font = ('Cambria', 16, 'bold'), width = 20)
        self.txt4.grid(row = 6, column = 2, columnspan = 2, pady = 10)



        Button(self.bf1, text = 'Verify', borderwidth = 2
               , font = ('Cambria', 14, 'bold'), bg = "green", fg = "white", width = 20,command=self.press).grid(row = 7, column = 0,
                                                                                              columnspan = 4, pady = 10)

        self.root.mainloop()
        print(self.r.get())
class disease_prediction:
    def get_input(self):
        self.my_list2.configure(state = NORMAL)
        flag = 0
        if self.my_entry.get() != "":
            if self.count <= 8:
                for j in self.slist:
                    if j == self.my_entry.get():
                        flag = 1
                        break
                if flag == 0:
                    self.my_list2.insert(END, str(self.count) + ". " + self.my_entry.get())
                    self.slist.append(self.my_entry.get())
                    self.my_entry.delete(0, END)
                    self.count += 1
                    self.my_list2.configure(state = DISABLED)
                else:
                    showerror("Already Exit!", "Symptom is already selected")
                    self.my_list2.configure(state = DISABLED)
            else:

                showerror("Out of limit!", "LIMIT OUT OF BOUND:\nPlease select any 8 symptoms")
                self.my_list2.configure(state = DISABLED)
        else:
            showerror("Empty", "Please select any option !")
            self.my_list2.configure(state = DISABLED)

    def update(self, data):
        # clear the list
        self.my_list.delete(0, END)
        # Add t to listbox

        for item in data:
            self.my_list.insert(END, item.capitalize())

    def update1(self, data):
        # clear the list
        self.disease_list.delete(0, END)
        # Add t to listbox

        for item in data:
            self.disease_list.insert(END, item.capitalize())

    def refresh(self):
        self.count = 1
        self.my_list2.configure(state = NORMAL)
        self.my_list2.delete(0, END)
        self.disease_list.configure(state = NORMAL)
        self.disease_list.delete(0, END)
        self.T.config(state = NORMAL)
        self.my_entry3.delete(0, 'end')
        self.T1.config(state = NORMAL)
        self.T.delete(1.0, END)
        self.T1.delete(1.0, END)
        self.T1.config(state = DISABLED)
        self.T.config(state = DISABLED)
        self.my_list2.configure(state = DISABLED)
        self.slist = []

    def fillout(self, e):

        # delete whatever is in the entry box
        self.my_entry.delete(0, END)
        self.my_entry.insert(0, self.my_list.get(ACTIVE))

    def fillout1(self, e):

        # delete whatever is in the entry box
        self.my_entry3.delete(0, END)
        self.my_entry3.insert(0, self.disease_list.get(ACTIVE))

    # function to check vs listbox
    def check(self, e):
        # grab what was type
        typed = self.my_entry.get()
        if typed == "":

            data = self.t
        else:
            data = []
            for item in self.t:
                if typed.lower() in item.lower():
                    data.append(item.capitalize())

        # update our listbox with the selected items
        self.update(data)

    def check1(self, e):
        # grab what was type
        typed = self.my_entry3.get()
        if typed == "":

            data = self.dlist
        else:
            data = []
            for item in self.dlist:
                if typed.lower() in item.lower():
                    data.append(item.capitalize())

        # update our listbox with the selected items
        self.update1(data)

    def precure(self):
        if self.my_entry3.get() != "":
            for i in range(len(self.main_list)):
                if self.main_list[i][0] == self.my_entry3.get().lower():
                    self.T.config(state = NORMAL)
                    self.T.tag_configure("", justify = CENTER)
                    self.T.delete(1.0, END)
                    self.T.insert(INSERT, self.main_list[i][1])
                    self.T1.config(state = NORMAL)
                    self.T1.delete(1.0, END)
                    self.T1.insert(INSERT, self.main_list[i][2])
                    self.T1.config(state = DISABLED)
                    self.T.config(state = DISABLED)
                    print("bye")
                    break
        else:
            showerror("Error","You have not selected any disease.")

    def predict(self):
        te = self.slist[0].lower()
        self.filter = self.df[te] == 1
        for i in self.slist:
            temp = i.lower()
            self.filter1 = self.df[temp] == 1
            self.df = self.df.where(self.filter1 & self.filter).dropna()
            self.dlist = self.df["prognosis"].tolist()
        print(self.dlist)
        if len(self.dlist) == 0:
            showinfo("Information", "Disease with these symptoms doesnot exist in this machine.")
        else:
            self.update1(self.dlist)

    def __init__(self):

        self.rootd = Tk()
        self.rootd.geometry("1550x766")
        self.rootd.title("DISEASE PREDICTOR")
        self.photo = PhotoImage(file = "logo.png")
        self.rootd.iconphoto(False, self.photo)
        self.rootd.state("zoomed")
        self.open = PhotoImage(file = "front_login.png")
        self.front_label1 = Label(self.rootd, image = self.open)



        self.count = 1
        self.slist = []

        self.rootd.config(bg = "#f6deb4")
        # create labelframe
        self.hframe = Frame(self.rootd)
        self.hframe.place(x=750,y=40,anchor=CENTER)
        self.hlabel = Label(self.hframe, text = "DISEASE PREDICTOR", width=60,font = ('Cambria', 30, 'bold'), bg = "blue",
                            fg = "white")
        self.hlabel.pack(fill="x")

        self.intro_frame = Frame(self.rootd,bg="grey")
        self.intro_frame.place(x = 470, y = 500)
        self.intro_Label= Label(self.intro_frame, text = "\"EVERY HUMAN\nBEING IS THE\nAUTHOR OF HIS\nOWN HEALTH OR\nDISEASE.\"", font = ('Cambria', 26, 'bold'),
                            bg = "grey",
                            fg = "white")
        self.intro_Label.pack(padx=50,pady=10)
        self.intro_Label1 = Label(self.intro_frame,
                                 text ="-Gautam Budha",
                                 font = ('Brush Script MT', 20, 'bold'),
                                 bg = "grey",
                                 fg = "white")
        self.intro_Label1.pack(padx=50,pady=5)

        self.button_frame = LabelFrame(self.rootd, text = "SYMPTOMS", font = ('Comic Sans MS', 14, 'bold'), bg = "white",
                                       fg = "black")
        self.button_frame.place(x=50,y=90)

        self.button_frame1 = LabelFrame(self.rootd, text = "DISEASES", font = ('Comic Sans MS', 14, 'bold'), bg = "white",
                                        fg = "black")
        self.button_frame1.place(x=470,y=90)

        self.prec_label = LabelFrame(self.rootd, text = "PRECAUTIONS & CURES", font = ('Comic Sans MS', 14, 'bold'), bg = "white",
                                        fg = "black")
        self.prec_label.place(x = 890, y = 90)

        self.prec = Label(self.prec_label, text = "PRECAUTIONS", font = ('Cambria', 16, 'bold'),width=15,bg="orange",fg="white")
        self.prec.pack(padx=20,pady=15,anchor=W)

        self.T = Text(self.prec_label, font = ('Cambria', 13), height = 12, width = 60,bg="skyblue",fg="black")
        self.T.pack(padx=20,pady=15)
        self.T.config(state = DISABLED)

        self.cure = Label(self.prec_label, text = "CURES", font = ('Cambria', 16, 'bold'),width=15,bg="orange",fg="white")
        self.cure.pack(padx=20,pady=15,anchor=W)

        self.T1 = Text(self.prec_label, font = ('Cambria', 13), height = 12, width = 60,bg="skyblue",fg="black")
        self.T1.pack(padx=20,pady=15)
        self.T1.config(state = DISABLED)


        self.symptomlabel = LabelFrame(self.rootd, text = "SYMPTOMS SELECTED", font = ('Comic Sans MS', 14, 'bold'),)
        self.symptomlabel.place(x=50, y=500)

        # working with button_frame_1

        self.label2 = Label(self.button_frame1, text = "Select Disease:", font = ('Comic Sans MS', 12, 'bold'))
        self.label2.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.my_entry3 = Entry(self.button_frame1, font = ('Comic Sans MS', 12, 'bold'))
        self.my_entry3.grid(row = 0, column = 1, padx = 10, pady = 10)

        self.disease_list = Listbox(self.button_frame1, width = 40, height = 10, bg = "skyblue",
                                    font = ('Cambria', 12, "bold"))
        self.disease_list.grid(row = 1, column = 0, columnspan = 2, padx = 10, pady = 10)

        self.dselect = Button(self.button_frame1, text = "PRECAUTIONS & CURES", width = 30, font = ('Cambria', 14,'bold'),
                                    bg = "green", fg = "white", command = self.precure)
        self.dselect.grid(row = 2, columnspan = 2, padx = 10, pady = 20)

        # This is our mainframe i.e. button_frame
        self.label1 = Label(self.button_frame, text = "Enter Symptoms:", font = ('Comic Sans MS', 12, 'bold'))
        self.label1.grid(row = 0, column = 0, padx = 10, pady = 10)

        self.my_entry = Entry(self.button_frame, font = ('Comic Sans MS', 12, 'bold'))
        self.my_entry.grid(row = 0, column = 1, padx = 10, pady = 10)

        self.my_list = Listbox(self.button_frame, width = 40, height = 10, bg = "skyblue",
                               font = ('Cambria', 12, "bold"))
        self.my_list.grid(row = 1, columnspan = 2, padx = 10, pady = 10)

        self.select_button = Button(self.button_frame, text = "Select", width = 10, font = ('Cambria', 14, 'bold'),
                                    bg = "red", fg = "white", command = self.get_input)
        self.select_button.grid(row = 2, column=0, padx = 10, pady = 20)

        self.refresh_button = Button(self.button_frame, text = "Refresh", width = 10, font = ('Cambria', 14, 'bold'),
                                     bg = "red", fg = "white", command = self.refresh)
        self.refresh_button.grid(row = 2, column=1, padx = 10, pady = 10)


        self.predict_button = Button(self.symptomlabel, text = "Predict Disease", width = 20,
                                     font = ('Cambria', 14, 'bold'),
                                     bg = "red", fg = "white", command = self.predict)
        self.predict_button.grid(row = 4, columnspan = 2, padx = 10, pady = 15)

        self.my_list2 = Listbox(self.symptomlabel, width = 40, height = 8, bg = "skyblue",
                                font = ('Cambria', 12, "bold"))
        self.my_list2.grid(row = 3, columnspan = 2, padx = 10, pady = 10)

        self.df = pandas.read_csv("prediction.csv")

        self.t = self.df.head().drop(columns = ['prognosis'])
        self.update(self.t)

        self.disease = self.df["prognosis"]

        self.main_list = [["fungal infection","Keep your skin clean and dry, particularly the folds of your skin.Wash your hands often, especially after touching animals or other people.Avoid using other people's towels and other personal care products.Wear shoes in locker rooms, community showers, and swimming pools.","Antifungal medications work to treat fungal infections. They can either kill fungi directly or prevent them from growing and thriving. Antifungal drugs are available as OTC treatments or prescription medications, and come in a variety of forms, including creams or ointments."],
                          ["allergy","Avoid your allergens.Take your medicines as prescribed. If you are at risk for anaphylaxis, keep your epinephrine auto-injectors with you at all times.Keep a diary.Wear a medical alert bracelet (or necklace). Know what to do during an allergic reaction. ","There is currently no cure for allergies. However, there are OTC and prescription medications that may relieve symptoms. Avoiding allergy triggers or reducing contact with them can help prevent allergic reactions. Over time, immunotherapy may reduce the severity of allergic reactions."],
                          ["gerd","Obesity is the leading cause of GERD.Avoid foods known to cause reflux. If you're at risk for GERD, avoid to Eat smaller meals. Don't lie down after eating. Elevate your bed. Review your medications. Quit smoking. ","Although common, the disease often is unrecognized – its symptoms misunderstood. This is unfortunate because GERD is generally a treatable disease, though serious complications can result if it is not treated properly. Heartburn is the most frequent – but not the only symptom of GERD."],
                          ["chronic cholestasis"," Salt diet that emphasizes fruits, vegetables and whole grains. Limit the amount of animal fats and use good fats in moderation. Lose extra pounds and maintain a healthy weight.Quit smoking.","Lose extra pounds. Losing weight can help lower cholesterol.Eat a heart-healthy diet. Focus on plant-based foods, including fruits, vegetablesand whole grains."],
                          ["drug reaction","Carefully read and follow all directions on the medicine bottle and box. Take the minimum effective dose. Call your doctor if you think you are having a problem with your medicine. Do not take a medicine if you have had an allergic reaction to it in the past."," If the rash occurs, the medication should be stopped as soon as possible. The rash may persist for several days to weeks after you discontinue the medication, then it fades. Usually, the rash disappears from the top of the body first and the legs and feetThey may take a few hours to a few days to disappear. If the exposure to the allergen continues, such as during a spring pollen season, allergic reactions may last for longer periods such as a few weeks to months. Even with adequate treatment, some allergic reactions may take two to four weeks to go away."],
                          ["peptic ulcer disease","Avoid tobacco products. Avoid alcohol. Use caution with aspirin and/or NSAIDs.Don't ignore your ulcer symptoms.Protect yoursel rom infections by washing hands regularly and consuming foods that have been cooked thoroughly.","PPIs work by reducing the amount of acid your stomach produces, preventing further damage to the ulcer as it heals naturally. They're usually prescribed for 4 to 8 weeks. Omeprazole, pantoprazole and lansoprazole are the PPIs most commonly used to treat stomach ulcers."],
                          ["aids","Use new gloves for every patient. Wear protective eye wear, masks or face shields (with safety glasses or goggles) during procedures likely to generate droplets of blood or body fluids. In general, protective eye wear, masks and clothing are not needed for routine care of AIDS virus-infected persons.","Although there is no cure for acquired immunodeficiency syndrome (AIDS), medications have been highly effective in fighting HIV and its complications. Drug treatments help reduce the HIV virus in your body, keep your immune system as healthy as possible and decrease the complications you may develop."],
                          ["diabetes","Make healthy eating and physical activity part of your daily routine. Maintain a healthy weight. Monitor your blood sugar, and follow your doctor's instructions for managing your blood sugar level. Take your medications as directed by your doctor."," No cure for diabetes currently exists, but the disease can go into remission. When diabetes goes into remission, it means that the body does not show any signs of diabetes, although the disease is technically still present."],
                          ["gastroenteritis","Contact precautions includes wearing gloves and a plastic apron or impervious gown when having contact with the patient or the patient's environment, especially when attending to patient toileting and hygiene. Protective eyewear and mask must be worn when there is the potential of vomit or faecal splashing","In most cases, people with viral gastroenteritis get better on their own without medical treatment. You can treat viral gastroenteritis by replacing lost fluids and electrolytes to prevent dehydration. In some cases, over-the-counter medicines may help relieve your symptoms."],
                          ["bronchial asthma"," If you have asthma, you need to do what you can to cut your exposure to asthma triggers. That starts by knowing what causes you to cough, wheeze and grasp for breath. While there’s no cure, there are steps you can take to keep your asthma in control and prevent an attack."," Quick-relief inhalers (bronchodilators) quickly open swollen airways that are limiting breathing. In some cases, allergy medications are necessary. Long-term asthma control medications, generally taken daily, are the cornerstone of asthma treatment"],
                          ["hypertension","Eat a Healthy Diet. Choose healthy meal and snack options to help you avoid high blood pressure and its complications.Keep Yourself at a Healthy Weight. Be Physically Active. Do Not Smoke.","Lose extra pounds and watch your waistline. Blood pressure often increases as weight increases. Exercise regularly. Eat a healthy diet.Reduce sodium in your diet. Limit the amount of alcohol you drink. "],
                          ["migraine","If you get these headaches often or have severe ones, avoid the things that you know set them off, called triggers, like specific foods, smells, and alcohol. For example,You might be able to keep migraines away with a couple other tactics, too. Use preventive medications or devices. Make lifestyle changes","Rest in a Quiet, Dark Room. Many people with migraine report sensitivity to light and sound, which can make headaches worse.Apply a Warm or Cold Compress to Your Head or Neck.Hydrate Aggressively."],
                          ["cervical spondylosis"," Stay physically active.Use good posture.Prevent neck injuries by always using the right equipment and the right form when exercising or playing sports.","Nonsteroidal anti-inflammatory drugs. While some types of NSAIDs are available over the counter, you may need prescription-strength versions to relieve the pain and inflammation associated with cervical spondylosis."],
                          ["paralysis (brain hemorrhage)","Quit smoking.Lose weight.Eat a balanced diet low in sodium and saturated and trans fat.Moderate alcohol intake (no more than two small drinks per day)Exercise regularly to stay physically fit.","There isn't a cure for permanent paralysis. The spinal cord can't heal itself. Temporary paralysis like Bell's palsy often goes away over time without treatment. Physical, occupational and speech therapy can accommodate paralysis and provide exercises, adaptive and assistive devices to improve function."],
                          ["jaundice","Drink at least eight glasses of fluids per day. Consider adding milk thistle to your routine. Opt for fruits like papaya and mango, which are rich in digestive enzymes.Eat at least 2 1/2 cups of veggies and 2 cups of fruit per day.","However, infants with extremely high bilirubin levels will require treatment with either a blood transfusion or phototherapy. In these cases, treatment is vital as jaundice in newborns can lead to kernicterus, a very rare type of permanent brain damage."],
                          ["malaria","Bite prevention – avoid mosquito bites by using insect repellent, covering your arms and legs, and using a mosquito net. Check whether you need to take malaria prevention tablets – if you do, make sure you take the right antimalarial tablets at the right dose, and finish the course.","Malaria can be cured with prescription drugs. The type of drugs and length of treatment depend on the type of malaria, where the person was infected, their age, whether they are pregnant, and how sick they are at the start of treatment."],
                          ["chicken pox","The best way to prevent chickenpox is to get the chickenpox vaccine. Everyone—including children, adolescents, and adults—should get two doses of chickenpox vaccine if they have never had chickenpox or were never vaccinated. Chickenpox vaccine is very safe and effective at preventing the disease","There is no cure for chickenpox, but it generally resolves within a week or two without treatment. A doctor may prescribe medication or give advice on how to reduce symptoms of itchiness and discomfort, and also on how to prevent transmission of the infection."],
                          ["dengue","Apply mosquito repellent, ideally one containing DEET. Wear long-sleeves and long pants to cover your arms and legs.Use mosquito nets while sleeping.","There is no specific treatment for dengue fever. Fever reducers and pain killers can be taken to control the symptoms of muscle aches and pains, and fever. The best options to treat these symptoms are acetaminophen or paracetamol."],
                          ["typhoid","Receiving a typhoid fever vaccination. Avoiding food that is raw or undercooked.Drinking only bottled water or water that has been boiled.","Yes, typhoid is dangerous, but curable. Typhoid fever is treated with antibiotics that kill the Salmonella bacteria. Prior to the use of antibiotics, the fatality rate was 20%. Death occurred from overwhelming infection, pneumonia, intestinal bleeding, or intestinal perforation."],
                          ["hepatitis a","To reduce your risk of spreading or catching the hepatitis A virus: Always wash your hands thoroughly after using the restroom and when you come in contact with an infected person's blood, stools, or other bodily fluid. Avoid unclean food and water","There's currently no cure for hepatitis A, but it normally gets better on its own within a couple of months. You can usually look after yourself at home. But it's still a good idea to see your GP for a blood test if you think you could have hepatitis A, as more serious conditions can have similar symptoms."],
                          ["hepatitis b","There appears to be no transmission of Hepatitis B via tears, sweat, urine, and stool or droplet nuclei (airborne). Hepatitis B is not spread by casual contact.","Most adults with hepatitis B recover fully, even if their signs and symptoms are severe. Infants and children are more likely to develop a chronic (long-lasting) hepatitis B infection. A vaccine can prevent hepatitis B, but there's no cure if you have the condition."],
                          ["hepatitis c","Never share needles. Avoid direct exposure to blood or blood products. Don't share personal care items.","Today's treatments are all oral and can be completed in as few as 8–24 weeks. Additionally, many of today's treatments have high cure rates of 95% or higher. A patient is considered cured if the hepatitis C virus is not detectable in their blood months after treatment has ended."],
                          ["hepatitis d","Hepatitis D can only occur if the person has hepatitis B. Hepatitis D virus (HDV) and hepatitis B virus (HBV) may infect a person at the same time or HDV infection may occur in persons with chronic HBV infection. Others risk groups include: Injection drug users.","There's currently no cure or vaccine for hepatitis D, but it can be prevented in people who aren't already infected with hepatitis B. Treatment may also help prevent liver failure when the condition is detected early."],
                          ["hepatitis e","Prevention of hepatitis E relies primarily on good sanitation and the availability of clean drinking water. Travelers to developing countries can reduce their risk for infection by not drinking unpurified water. Boiling and chlorination of water will inactivate HEV.","Hepatitis E usually resolves on its own without treatment. There is no specific antiviral therapy for acute hepatitis E. Physicians should offer supportive therapy.Hepatitis E is contagious from one week before symptoms start to four weeks afterward. Some people have no symptoms or signs and do not know they are contagious with the infection. Hepatitis E is diagnosed by blood and stool (feces) tests."],
                          ["alcoholic hepatitis","The only certain way to prevent alcoholic hepatitis is to avoid all alcohol. Protect yourself from hepatitis C. Hepatitis C is an infectious liver disease caused by a virus. Untreated, it can lead to cirrhosis","Treatment involves hydration, nutritional care and stopping alcohol use. Steroid drugs can help reduce liver inflammation."],
                          ["tuberculosis","Take all of your medicines as they're prescribed, until your doctor takes you off them.Keep all your doctor appointments.Always cover your mouth with a tissue when you cough or sneeze. ","Tuberculosis (TB) is a bacterial infection that most commonly affects the lungs. It can be completely cured with the right treatment whch typically consists of medication in a pill form containing a mix of antibiotics. Tuberculosis (TB) is a bacterial infection that most commonly affects the lungs."],
                          ["common cold","Wash your hands often with soap and water. Wash them for 20 seconds, and help young children do the same.Avoid touching your eyes, nose, and mouth with unwashed hands. Viruses that cause colds can enter your body this way and make you sick.","There is no way to get rid of a cold fast. A cold will usually go away on its own without treatment. However, a person may experience uncomfortable symptoms while they recover. People can take steps to aid recovery, such as getting plenty of rest.Nothing can cure a cold, but there are some remedies that might help ease your symptoms and keep you from feeling so miserable."],
                          ["pneumonia","Pneumonia can be prevented by immunization, adequate nutrition, and by addressing environmental factors. Pneumonia caused by bacteria can be treated with antibiotics, but only one third of children with pneumonia receive the antibiotics they need.","Mild pneumonia can usually be treated at home with rest, antibiotics (if it's likely be caused by a bacterial infection) and by drinking plenty of fluids. More severe cases may need hospital treatment."],
                          ["dimorphic hemmorhoids(piles)","Eat high-fibre foods.Drink plenty of fluids.Consider using fibre supplements.Avoid straining when on the toilet.Go to the toilet as soon as you feel the urge.","Eat high-fiber foods. Eat more fruits, vegetables and whole grains.Use topical treatments. Apply an over-the-counter hemorrhoid cream or suppository containing hydrocortisone, or use pads containing witch hazel or a numbing agent.Soak regularly in a warm bath or sitz bath. Take oral pain relievers."],
                          ["heart attack","To prevent your risk of a heart attack: Stop smoking and minimize your exposure to secondhand smoke. Get your high blood cholesterol and high blood pressure under control by modifying your diet, losing weight, taking medication, or doing a combination of these things. Stay physically active daily.","Aspirin. The 911 operator might tell you to take aspirin, or emergency medical personnel might give you aspirin immediately. Thrombolytics. Antiplatelet agents. Other blood-thinning medications.Pain relievers.Nitroglycerin. "],
                          ["varicose veins","Refined Carbohydrates. Refined carbohydrates or simple carbohydrates should be avoided as much as possible. Added Sugar.Alcohol.Canned Foods","Endothermal ablation. This is a procedure where heat is used to seal the affected veins.Ambulatory phlebectomy.Sclerotherapy. Ligation and stripping. "],
                          ["hypothyroidism","Studies suggest that phytoestrogens in soybeans and soy-rich foods may inhibit the activity of an enzyme that makes thyroid hormones. Iodine-rich foods.Iron and calcium supplements.","It is possible to cure hypothyroidism permanently for many of those suffering from Hashimoto's, which causes 90% of hypothyroidism cases. In order to reverse hypothyroidism, we look at the symptoms and root causes of Hashimoto's disease: Hormone imbalance."],
                          ["hyperthyroidism","An overactive or enlarged thyroid gland may produce more thyroid hormone. Your thyroid is a butterfly-shaped gland at the front of your neck. It produces thyroid hormones called T3 and T4.Avoid other foods high in iodine ","There is a permanent treatment for hyperthyroidism. Removing your thyroid through surgery will cure hyperthyroidism. However, once the thyroid is removed, you will need to take thyroid hormone replacement medications for the rest of your life"],
                          ["hypoglycemia","Monitor your blood sugar.Don't skip or delay meals or snacks.Measure medication carefully, and take it on time. Adjust your medication or eat additional snacks if you increase your physical activity.","When someone has symptoms of reactive hypoglycemia, the immediate treatment involves consuming a small amount of a sugary food or beverage, such as half a cup of fruit juice. Following a healthful diet may help prevent the sugar spikes in the bloodstream that lead to sugar dips and symptoms of hypoglycemia"],
                          ["osteoarthritis","If fear of joint pain after exercise keeps you from exercising, try using heat and cold on painful joints or take pain relievers. Doing so may make it easier to exercise and stay active. The safest exercises are those that place the least body weight on the joints, such as bicycling, swimming, and other water exercise.","There's no cure for osteoarthritis, but the condition does not necessarily get any worse over time. There are a number of treatments to help relieve the symptoms. The main treatments for the symptoms of osteoarthritis including  lifestyle measures such as maintaining a healthy weight and exercising regularly."],
                          ["arthritis","Stay at a healthy weight. Extra pounds put pressure on weight-bearing joints like hips and knees.Control your blood sugar. ","Although there's no cure for arthritis, treatments have improved greatly in recent years and, for many types of arthritis, particularly inflammatory arthritis, there's a clear benefit in starting treatment at an early stage. It may be difficult to say what has caused your arthritis."],
                          ["(vertigo)paroymsal positional vertigo"," Avoid driving.Avoid working at heights.Wear shoes with low heels and non-slip soles.Keep your shoes tied.","Benign paroxysmal positional vertigo may go away on its own within a few weeks or months. But, to help relieve BPPV sooner, your doctor, audiologist or physical therapist may treat you with a series of movements known as the canalith repositioning procedure."],
                          ["acne","Properly wash your face. To help prevent pimples, it's important to remove excess oil, dirt, and sweat daily. Know your skin type. Anyone can get pimples, no matter their skin type. Moisturize skin.","Although acne cannot be cured, it can be controlled with treatment. If you develop mild acne, it's a good idea to speak to a pharmacist for advice. Several creams, lotions and gels for treating spots are available to buy from pharmacies."],
                          ["urinary tract infection","Drink plenty of liquids, especially water. Drink cranberry juice.Wipe from front to back. Empty your bladder soon after intercourse","You will need to treat a urinary tract infection. Antibiotics are medicines that kill bacteria and fight an infection. Antibiotics are typically used to treat urinary tract infections. Your healthcare provider will pick a drug that best treats the particular bacteria that's causing your infection"],
                          ["psoriasis","Can prevent and manage psoriasis flares using certain remedies, treatments, and lifestyle methods. These include avoiding cold, dry environments, moisturizing regularly, and eating an anti-inflammatory diet.","Although there is no cure, there are more effective treatments for psoriasis today than ever before. Treating psoriasis can help improve symptoms as well as lower the risk of developing other health conditions such as psoriatic arthritis, heart disease, obesity, diabetes and depression."],
                          ["impetigo","To prevent the spread of impetigo and of other infections, take the following precautions: Wash your hands with soap and water often (no matter whom you touch) and use alcohol hand rubs. Do not share personal items, such as towels, clothes, or hair combs. The germs that cause impetigo can live on these objects","mpetigo is treated with prescription mupirocin antibiotic ointment or cream applied directly to the sores two to three times a day for five to 10 days. Before applying the medicine, soak the area in warm water or apply a wet cloth compress for a few minutes."]
                          ]
        # print(self.disease)

        # create a binding on listbox onclick
        self.my_list.bind("<<ListboxSelect>>", self.fillout)
        self.disease_list.bind("<<ListboxSelect>>", self.fillout1)

        self.my_entry3.bind("<KeyRelease>", self.check1)

        self.my_entry.bind("<KeyRelease>", self.check)

        self.rootd.mainloop()
        print(self.slist)


login()