public class DbArgs {
    public void addDbArgs( List<String> args ) {
        args.add( currentConnection.driverClass );
        args.add( currentConnection.url );
        args.add( currentConnection.user );
        args.add( currentConnection.password );

        if ( currentConnection.jar1.trim().length() > 0 ) {
            args.add( "-jdbcjar" );
            args.add( currentConnection.jar1.trim() );
        }
        if ( currentConnection.jar2.trim().length() > 0 ) {
            args.add( "-jdbcjar2" );
            args.add( currentConnection.jar2.trim() );
        }
    }
}