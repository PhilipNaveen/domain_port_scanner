'''DOMAIN PORT SCANNER'''

#imports
import socket
import sys 

#class_[COLORAMA]
class COLORAMA:
    a = '\033[91m'
    b = '\033[92m'
    c = '\033[93m'
    d = '\033[94m'
    
#def_[banner1]
def banner1():
    print(COLORAMA.c + '''
         _,.-------.,_
     ,;~'             '~;,
   ,;                     ;,
  ;                         ;
 ,'                         ',
,;                           ;,
; ;      .           .      ; ;
| ;   ______       ______   ; |
|  `/~"     ~" . "~     "~|'  |
|  ~  ,-~~~^~, | ,~^~~~-,  ~  |
 |   |        }:{        |   |
 |   l       / | \       !   |
 .~  (__,.--" .^. "--.,__)  ~.
 |     ---;' / | \ `;---     |
  \__.       \/^\/       .__/
   V| \                 / |V
    | |T~\___!___!___/~T| |
    | |`IIII_I_I_I_IIII'| |
    |  \,III I I I III,/  |
     \   `~~~~~~~~~~'    /
       \   .       .   /     
         \.    ^    ./
           ^~~~^~~~^
    ''')

#def_[banner2]
def banner2():
    print(COLORAMA.a + '''
██████╗  ██████╗ ██████╗ ████████╗    
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝    
██████╔╝██║   ██║██████╔╝   ██║       
██╔═══╝ ██║   ██║██╔══██╗   ██║       
██║     ╚██████╔╝██║  ██║   ██║       
╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝       
                                      
███████╗ ██████╗ █████╗ ███╗   ██╗    
██╔════╝██╔════╝██╔══██╗████╗  ██║    
███████╗██║     ███████║██╔██╗ ██║    
╚════██║██║     ██╔══██║██║╚██╗██║    
███████║╚██████╗██║  ██║██║ ╚████║    
╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝    
                                      
    ''')
    
#class_[port_scanner]
class port_scanner:
    
    #init_[self//optional_parameters//objects_for_inheritance]
    def __init__(self):
        self.domain = str(input('\nenter domain name: '))
        self.domain_IP = socket.gethostbyname(self.domain)
        self.port_amount = None
        
    #def_[settings]_[self//optional_parameters//objects_for_inheritance]
    def settings(self):
        self.port_amount = None
        self.port_depth_settings = str(input('enter depth of scan [1==1000//2==500//3==250//4==???]: '))
        
        #try_block
        try:    
            #ifs_elifs_else
            if self.port_depth_settings ==int(1):
                self.port_amount =int(1000)
            elif self.port_depth_settings ==int(2):
                self.port_amount =int(5000)
            elif self.port_depth_settings ==int(3):
                self.port_amount =int(250)
            elif self.port_depth_settings ==int(4):
                print('custom amount of ports.....')
                self.port_amount =int(input('enter custom amount of ports: '))
                print('depth of port scan: {} ports'.format(str(self.port_amount)))
            else:
                print('incorrect input? --> count==retry')
        #exception
        except Exception as ERROR:
            pass
        
    #def_[scan]_[self//optional_parameters]
    def scan(self,port_amount=None,domain=None,IP=None):
        #SET_[counter==0]
        self.counter =int(0)
        
        try:    
            #redefine_params
            port_amount =self.port_amount
            domain=self.domain
            IP=self.domain_IP
            
            #for_loop
            for port in range(1,int(port_amount)):
                SOCK =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                RESULTS =SOCK.connect_ex((IP,port))
                
                if RESULTS ==0:
                    print(COLORAMA.c + 'port' + COLORAMA.a + ' {}'.format(port) + COLORAMA.c + ' open')
                    self.counter +=int(1)
                elif RESULTS !=0:
                    print(COLORAMA.c + 'port' + COLORAMA.a + ' {}'.format(port) + COLORAMA.c + ' closed')
                else:
                    pass
        #Exception
        except Exception as SOCKET_ERROR:
            pass 
     
    #def_[result_counter]
    def result_counter(self,counter=None,domain=None,IP=None):
        domain =self.domain
        IP =self.domain_IP
        counter =int(self.counter)
        print(COLORAMA.c + 'there are ' + COLORAMA.a + '{} '.format(str(counter)) + COLORAMA.c + 'open ports in ' + COLORAMA.a + '\ndomain: {} : IP {}'.format(domain,IP))

if __name__ == '__main__':
    banner1()
    banner2()
    
    PS = port_scanner()
    PS.settings()
    PS.scan()
    PS.result_counter()
            
        
    


