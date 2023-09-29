public class Email_DBImplTest {
    public void testGetEvtIDs() {
        System.out.println( "getEvtIDs" );
        Email_DBImpl instance = new Email_DBImpl();     
        String[] expResult = null;
        String[] result = instance.getEvtIDs();
        assertEquals( expResult, result );
            
        // TODO review the generated test code and remove the default call to fail.
        fail( "The test case is a prototype." );
    }
}