public class EmailTest {
    public void testGetEmail() {
        System.out.println( "getEmail" );

        String expResult = "";
        String result = instance.getEmail();
        assertEquals( expResult, result );

        // TODO review the generated test code and remove the default call to fail.
        //  fail( "The test case is a prototype." );
    }
}