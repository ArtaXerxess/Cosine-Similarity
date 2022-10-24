import  tkinter  as  tk
from  tkinter  import  ttk
import cos_dis_sim

class  App(tk.Tk):
        def  __init__(self):
            super().__init__()
            #  configure  the  root  window
            self.title('Cosine Similarity and Cosine Distance')
            self.geometry('400x500')
            # self.minsize(300,50)
    
            # sentence 1
            self.sentence1  =  ttk.Label(self,  text='Sentence 1:')
            self.sentence1.pack(pady=5)
            self.sentence1_entry = ttk.Entry(self,width=60)
            self.sentence1_entry.pack(pady=5)

            # sentence 2
            self.sentence2 = ttk.Label(self,text="Sentence 2:")
            self.sentence2.pack(pady=5)
            self.sentence2_entry = ttk.Entry(self,width=60)
            self.sentence2_entry.pack(pady=5)

            # Get Similarity
            self.get_sim_butn = ttk.Button(master=self,text='Get Similarity',command=self.get_similarity)
            self.get_sim_butn.pack(pady=5)
            self.results_label = ttk.Label(master=self,text='Results will appear here...')
            self.results_label.pack(pady=5)

            # Copy results
            self.copy_button = ttk.Button(master=self,text='Copy Results',command=self.copy_cmd)
            self.copy_button.pack(pady=5)

        
        # Get Similarity button command
        def get_similarity(self):
            self.juice = cos_dis_sim.engine(sentence1=self.sentence1_entry.get(),sentence2=self.sentence2_entry.get())
            self.results_label['text']=self.juice.output()

        # Copy results button command
        def copy_cmd(self):
            self.clipboard_clear()
            self.clipboard_append(string=self.juice.output())

        
if __name__=="__main__":
    App().mainloop()