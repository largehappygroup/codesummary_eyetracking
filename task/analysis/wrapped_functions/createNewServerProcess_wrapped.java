public class Server {
    protected void createNewServerProcess( Socket socket ){
        logger.info( "Received connection on port " + getPort() + " from [" + socket.getInetAddress() + ":" + socket.getPort() + "]." );

        Thread t = new Thread( getNewServerProcess( socket ));
        t.start();
        getServerProcesses().add( t );
        new Thread( new Monitor( t )).start();
    }
}