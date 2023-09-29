public class ConnectionClass {
    public void connectionErrorOccurred(ConnectionEvent event) {
        logger.warn("Received Connection Error event from a conection in pool " + info.getName());

        if (info.isRemoveOnExceptions()) {
            checkIn(event.getSource(), true);
            logger.warn("removeOnExceptions == true, closed connection");
        }
    }
}