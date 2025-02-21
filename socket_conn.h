// socket_conn.h
#ifndef SOCKET_CONN_H
#define SOCKET_CONN_H

#include <stdio.h>
#include <stdlib.h>

#include <sys/types.h>
#include <sys/socket.h>

#include <netinet/in.h>

static inline int socket_connection(){
    
    int capturer_socket;
    if((capturer_socket = socket(AF_INET,SOCK_STREAM , 0)) == -1 ){
        perror("can not created a socket");
    }

    

    return 0;
}

#endif