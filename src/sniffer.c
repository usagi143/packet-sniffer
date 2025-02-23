#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#include <sys/types.h>
#include <sys/socket.h>
#include <linux/if_ether.h>

#include <netinet/in.h>


#define BUFFER_SIZE 65536

void print_hex(unsigned char *buffer, int length) {
    printf("📡 Datos en HEX:\n");
    for (int i = 0; i < length; i++) {
        printf("%02X ", buffer[i]);
        if ((i + 1) % 16 == 0) printf("\n");
    }
    printf("\n");
}

int capture_packet(unsigned char *buffer){
    
    int capturer_socket, packet_socket;

    if((capturer_socket = socket(AF_PACKET,SOCK_RAW , htons(ETH_P_ALL))) == -1 ){
        perror("Error while creating a socket"); 
        return 1;
    }

    while(1){
        ssize_t packet_recieved =  recvfrom(capturer_socket,buffer ,BUFFER_SIZE, 0, NULL, NULL);
        if(packet_recieved < 0){
            perror("Error al recibir paquete");
            close(packet_socket);
            return 1;
        }

        close(capturer_socket);
        return packet_recieved;
    }

    return 0;
}
