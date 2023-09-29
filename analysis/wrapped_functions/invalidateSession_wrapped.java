public class SessionManager {
    public void invalidateSession(String uid, String sid) {
        cat.debug("==> invalidateSession( " + String.valueOf(uid) + ", " + String.valueOf(sid) + ")");

        synchronized (lock) {
            uid2sid.remove(uid);
            sid2ssc.remove(sid);
            sid2ttl.remove(sid);
        }
        cat.debug("<== invalidateSession()");
    }
}