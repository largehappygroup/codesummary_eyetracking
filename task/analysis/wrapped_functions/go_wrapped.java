public class ChatClient {
    public void go( String theUserName ) {
        try {
            new ChatUI(( MessageInputReceiver ) this, theUserName );
            // shake hands
            writer.println( theUserName );
            writer.flush();
            // OK means init with server went well

            if ( reader.readLine().equals( "OK" )) {
                initialized = true;
                readChat();
            } else {
                bailOut( new IOException( "handshake failed" ));
            }
        } catch ( IOException ioe ) {
            bailOut( ioe );
        } catch ( Exception e ) {
            bailOut( e );
        }
    }
}