public class CollaborateCollection {
    public List<String> getCollaborateCollection(String userID) throws AccessException {
        logger.debug("entering getCollaborateCollection()");
        String query = "SELECT collection.PID PID, collection.TITLE TITLE,"
                + " collectionrole.ROLE ROLE FROM collectionrole, collection WHERE "
                + " collectionrole.USERID = '" + userID + "'"
                + " AND collectionrole.COLLECTIONPID = collection.PID"
                + " AND collection.ROOT = '1'";
        List<String> list = buildResult(query);
        return list;
    }

    // Build result method
    private List<String> buildResult(String query) {
        // implementation code
    }

    // Logger
    private static final Logger logger = Logger.getLogger(CollaborateCollection.class);
}