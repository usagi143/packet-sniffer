import customtkinter as ctk
import ctypes

# class App_sniffer(ctk.CTk):
#     def __init__(self):
#         super().__init__()
#         self.geometry=("1200x900")
#         self.packet_raw = "hola mundo"

#         label = ctk.CTkLabel(self, text=self.packet_raw, fg_color="blue", text_color="black")
#         label.place(relx=0.4, rely=0.4)
    
#     def recv_packet(self):
#         recieve_packet = ctypes.

#         self.packet_raw = 



# sniffer_app = App_sniffer()
# sniffer_app.mainloop()

clibrary = ctypes.CDLL("./lib/sniffer.so")

clibrary.capture_packet.argtypes = [ctypes.POINTER(ctypes.c_ubyte)]

clibrary.capture_packet.restype = ctypes.c_int

buffer = (ctypes.c_ubyte * 65536)()

packet_size = clibrary.capture_packet(buffer)
