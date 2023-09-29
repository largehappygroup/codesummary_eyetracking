public class SocketServer {
    
    public void listen() throws IOException {
        logMessage( "Server started at " + this.getHostname() + ":" + this.getPort() );
        while ( true ) {
            Socket socket = serverSocket.accept();
            logMessage( socket.getInetAddress().getCanonicalHostName() + "has made a connection !" );
            logMessage( "Creating new listener" );
            ListenThread task = new ListenThread( socket, this );
            logMessage( "Adding new totemcontrolcomhandler" );
            addHandlers( task );
            Thread listener = new Thread( task );
            logMessage( "Starting new thread" );
            listener.run();
        }
    }
    
    public void logMessage(String message) {
        // implementation
    }
    
    public String getHostname() {
        // implementation
    }
    
    public int getPort() {
        // implementation
    }
    
    public void addHandlers(ListenThread task) {
        // implementation
    }
    
    class ListenThread implements Runnable {
        
        private Socket socket;
        private SocketServer server;
        
        ListenThread(Socket socket, SocketServer server) {
            this.socket = socket;
            this.server = server;
        }
        
        @Override
        public void run() {
            try {
                // implementation
            } catch (IOException e) {
                // handle exception
            }
        }
    }
}