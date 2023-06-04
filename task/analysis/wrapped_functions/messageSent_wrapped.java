public class MyClass {

    public void messageSent( MessageEvent e ) {
        String str = e.getMessage();

        if ( str.endsWith( DIR_ADDED )) {
            str = str.substring( DIRECTORY.length(), str.indexOf( DIR_ADDED )).trim();
            createCvsFiles( str );
        }
        super.messageSent( e );
    }

}