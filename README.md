# password_manager
Password manager which genrates random password to stores them in txt file. and using tkinter to a nice UI experience


--UI setup
* Using Tkinter design a window, add padding
* create canvas and place the image on canvas and pack
* create labels,entries and buttons and place it using grid coordinates
* three entries and labels - website, email, password
* two buttons - ADD and generate password


--saving password to a txt file
* get entries of website,email,pwd using .get()
* length of 3 entries are checked and if its len() is 0, show a pop up telling user to fill all the entries
* popup created using messagebox.showerror() 
* store it in txt file, using with open("data.txt","a") and write function  
* delete entries of website, paswword in UI
* add this save function as command to ADD button

-- Generate password
* using the same code from password generator repository
* add the generated password to password entry and add the command to generate pwd button
