import customtkinter as ctk
import ctypes

# class App_sniffer(ctk.CTk):
#     def __init__(self):
#         super().__init__()
#         self.geometry("900x500")
#         self.overrideredirect(True)
#         self.attributes("-topmost", True)

#         self.option = 1
        
#         self.start_main()
#         self.start_submenu()


#     def start_main(self):
#         self.main = Main_principal(self, 1, width=630, height=470)
#         self.main.place(x=240, y=10)


#     ###submenu options
#     def start_submenu(self):
#         self.submenu = ctk.CTkFrame(self, width=200, height=400)
#         self.submenu.place(x=10, y=50)

#         self.sniffer_button = ctk.CTkButton(self.submenu, command=lambda:self.change_submenu(1), text="sniffer")
#         self.sniffer_button.place(relx=0.11, rely=0.10)

#         self.proxy_button = ctk.CTkButton(self.submenu, command=lambda:self.change_submenu(2),text="proxy")
#         self.proxy_button.place(relx = 0.11, rely= 0.20)

#     def change_submenu(self, option):
#         self.main.destroy()
        
#         self.main = Main_principal(self, option, width=630, height=470)
#         self.main.place(x=240, y=10)

        

# class Main_principal(ctk.CTkFrame):
#     def __init__(self, master, option, **kwargs):
#         super().__init__(master, **kwargs)
        
#         if option == 1:
#             self.sniffer_show()

#         if option == 2:
#             self.proxy_show()

#     def sniffer_show(self):
#         self.sniffer_label = ctk.CTkLabel(self, text="sniffer")
#         self.sniffer_label.place(relx=0.5, rely=0.5)

#     def proxy_show(self):
#         self.proxy_label = ctk.CTkLabel(self, text="under contruction")
#         self.proxy_label.place(relx=0.5, rely=0.5)

    


# if __name__ == "__main__":
#     sniffer_app = App_sniffer()
#     sniffer_app.mainloop()

continua = 1
while continua == 1:
    clibrary = ctypes.CDLL("./lib/sniffer.so")

    clibrary.capture_packet.argtypes = [ctypes.POINTER(ctypes.c_ubyte)]

    clibrary.capture_packet.restype = ctypes.c_int

    buffer = (ctypes.c_ubyte * 65536)()

    packet_size = clibrary.capture_packet(buffer)

    bytes_per_line = 16
    line = []

    for i, x in enumerate(buffer):
        if x != 0:  
            line.append(f"{x:02X}") 

            if len(line) == bytes_per_line:
                print(" ".join(line))
                line = []  

    if line:
        print(" ".join(line))

    continua =  int(input("continua:"))