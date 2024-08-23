#Trial Jai Shri Ram



from tkinter import *
root = Tk()

#Heading
centerAlignleft = Label(root,text="         ")
centerAlignleft.grid(row=0,column=1)
pageHeader = Label(root,text='Sample Request Form')
pageHeader.grid(row=0,column=2)
centerAlignright = Label(root,text="                  ")
centerAlignright.grid(row=0,column=6)


def SampleRequestInfo():
    # Create and place all Entry widgets
    requester_tag = Label(root,text='Requester Name ',fg="Blue")
    requester_tag.grid(row=3,column=0) 
    requester = Entry(root)
    requester.grid (row = 3,column=1)
    
    requester_email_tag = Label(root,text='Requester Email ',fg="Blue")
    requester_email_tag.grid(row=4,column=0)
    requester_email = Entry(root)
    requester_email.grid (row = 4,column=1)
    
    requester_num_tag = Label(root,text='Requester Phone Number ',fg="Blue")
    requester_num_tag.grid(row=5,column=0)
    requester_num = Entry(root)
    requester_num.grid (row = 5,column=1)
    
    university_tag = Label(root,text='University Name ',fg="Blue")
    university_tag.grid(row=6,column=0)
    university = Entry(root)
    university.grid (row = 6,column=1)
    
    sampleType_tag = Label(root,text='Plasma/Serum/GLP-1 ',fg="Blue")
    sampleType_tag.grid(row=7,column=0)
    sampleType = Entry(root)
    sampleType.grid (row = 7,column=1)
    
    panel_tag = Label(root,text='Panel Requested ',fg="Blue")
    panel_tag.grid(row=8,column=0)
    panel = Entry (root)
    panel.grid (row = 8,column=1)
    
    num_samples_tag = Label(root,text='Number of Participants  ',fg="Blue")
    num_samples_tag.grid(row=9,column=0)
    num_samples = Entry(root)
    num_samples.grid(row=9,column=1)
    
    arrangement_tag = Label(root,text='Single/Duplicate ',fg="Blue")
    arrangement_tag.grid(row=10,column=0)
    arrangement= Entry(root)
    arrangement.grid(row=10,column=1)
    
    volume_tag = Label(root,text='Volume per participant (microlitres)  ',fg="Blue")
    volume_tag.grid(row=11,column=0)
    volume = Entry(root)
    volume.grid(row=11,column=1)
    

    
    def submit():
        final_text = (f"{requester.get()} from {university.get()} requires {num_samples.get()} samples of "
                      f"{sampleType.get()} with a total volume of {volume.get()} arranged as {arrangement.get()} "
                      f"to run on {panel.get()}")
        final.config(text=final_text)

    submit_button = Button(root, text="Submit", command=submit)
    submit_button.grid(row=12, column=0)

# Create and place the initial button to start sample request
myButton = Button(root, text="Start Sample Request", state='active', command=SampleRequestInfo, fg="Blue")
myButton.grid(row=2, column=0)

# Create a label to display the final message
final = Label(root, text="")
final.grid(row=13, column=0)

root.mainloop()
