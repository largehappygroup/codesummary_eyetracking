public class LoginTest {
    public void testLogin() {
        SessionManager manager = new SimpleSessionManager();
        String sessionId = manager.createSession( null, null );		
        Session session = manager.getSession( sessionId );
        manager.login( session, "user", "password" );
		
        assertEquals( "user", session.getUserId() );
        assertEquals( "password", session.getUserPassword() );
        assertTrue( session.isLoggedIn() );
    }
}