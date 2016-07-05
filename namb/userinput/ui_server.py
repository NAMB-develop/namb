import socket

html="""<html>
<head>
<script type="text/javascript">
var d = {38:"<Up>",37:"<Left>",39:"<Right>",40:"<Down>",13:"<Return>",8:"<BackSpace>"};
function req(content){
var x = new XMLHttpRequest();
x.open("POST","input",true);
x.send(content);
}
function key(e){
req(d[e.keyCode]);
}
document.addEventListener("keydown", key, false);
</script>
</head>
<button type="button" onclick='req("<Up>");'>Up</button>
<button type="button" onclick='req("<Down>");'>Down</button>
<button type="button" onclick='req("<Left>");'>Left</button>
<button type="button" onclick='req("<Right>");'>Right</button>
<button type="button" onclick='req("<Return>");'>Enter</button>
<button type="button" onclick='req("<BackSpace>");'>Back</button>
<input oninput='req(this.value)' type="input"></input>
</html>
"""
CRLF="\r\n\r\n"
CRLF_I="\r\n"



def send_html(conn):
    reply="HTTP/1.1 200 OK%s"%CRLF_I
    reply=reply+"Content-type: text/html%s"%CRLF
    reply=reply+CRLF
    reply=reply+html+CRLF
    conn.send(reply)
    conn.close()
    

def process_get(conn, data):
    lines=data.split(CRLF_I)
    #print(lines)
    if lines[0]:
        path=lines[0].split(" ")[1]

        if path=="/input":

            data=lines[-1]
            if data:
                if data[0]=="<" and data[-1]==">":
                    print("Button pressed: %s" % data)
                    import namb.userinput.keys
                    import namb.userinput.keyboard
                    namb.userinput.queue(namb.userinput.keyboard._DICT[data])
                else:
                    print("Text data: %s" % data)
            else:
                print("No data received.")
            
            reply="HTTP/1.1 200 OK%s"%CRLF
            conn.send(reply)
            conn.close()
        else:
            send_html(conn)
        
def run():
    def do():
        server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('127.0.0.1',8000))
        server.listen(1)
        while True:
            conn, addr = server.accept()
            data=conn.recv(1024)
            process_get(conn, data)        
    
    import threading
    t=threading.Thread(None, do)
    t.daemon=True
    t.start()


