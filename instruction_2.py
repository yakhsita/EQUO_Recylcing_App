#Instruction 
def instructions(): 
    message ='''
    Dear User,

`        Thank you for choosing e-Recyclers Recycling Software.
        INSTRUCTIONS FOR USING THE APP
        1. Enter the name of device that is to be recycled.
        2. Enter the mineral(s) present in your device from among the following minerals.\n\t1.Aluminium\n\t2.Gold\n\t3.Silver\n\t4.Cadmium\n\t5.Lead\n\t6.Antimony\n\t7.Nickle\n\t8.Mercury\n\t9.Others - Mention it's name and price per gram
        3. After entering each item, click on ADD MINERAL
        4. Once your are done with entering all the required detals, Click on Generate Bill

        NOTE : Click on OK to continue.

\    Thanks & Regards,
    Team e-Recyclers '''
    messagebox.showinfo("INSTRUCTIONS TO USE THE APPLICATION",message)

    
def intro():
    textarea.delete(1.0,END)
    textarea.insert(END,"\t\t  e-Recycler's India Pvt. Ltd")
    textarea.insert(END,"\n\t\tMG Road, Bangalore-560001")
    textarea.insert(END,f"\n-------------------------------------------------------------------------------------------")
    textarea.insert(END,f"\n\t            INSTRUCTIONS TO USE THE APP")
    textarea.insert(END,f"\n-------------------------------------------------------------------------------------------")
    textarea.insert(END,f"\n1. Enter the name of device that is to be recycled.\n2. ")
    textarea.insert(END,f"\n3. After entering each item, click on ADD MINERAL")
    textarea.insert(END,f"\n4. Once your are done with entering all the required detals, \n     Click on GENERATE BILL")
    textarea.insert(END,f"\n-------------------------------------------------------------------------------------------")
    textarea.insert(END,"\n Built by : Nishant V H and Priyanshu Singh")
    textarea.insert(END,f"\n-------------------------------------------------------------------------------------------\n")
    textarea.configure(font='arial 11')
